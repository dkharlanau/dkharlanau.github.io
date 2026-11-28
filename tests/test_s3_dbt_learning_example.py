"""Self-contained regression for the SQL published in the S3/dbt learning pages.

Run: python3 -m unittest discover -s tests -p 'test_s3_dbt_learning_example.py' -v
SQLite tests SQL semantics only, not an actual Athena/dbt deployment.
"""
import csv
import html
import io
import re
import sqlite3
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "atlas/concepts/s3-dbt-analytics-explained.md"
SKILL = ROOT / "skill-hub/dama-dmbok/s3-dbt-analytics-working-skill.md"


def get_sql(filename):
    body = ATLAS.read_text(encoding="utf-8")
    pattern = (r'<strong>models/' + re.escape(filename)
               + r'</strong>[\s\S]*?<pre><code class="language-sql">([\s\S]*?)</code></pre>')
    match = re.search(pattern, body)
    if match is None:
        raise AssertionError("Missing SQL code block: " + filename)
    return html.unescape(match.group(1)).strip()


def sample_events():
    body = SKILL.read_text(encoding="utf-8")
    match = re.search(r'<pre><code>(order_id,status,updated_at,amount,event_seq\n[\s\S]*?)</code></pre>', body)
    if match is None:
        raise AssertionError("Missing CSV sample")
    return list(csv.DictReader(io.StringIO(html.unescape(match.group(1)))))


class S3DbtAnalyticsExampleTest(unittest.TestCase):
    def setUp(self):
        self.db = sqlite3.connect(":memory:")
        self.addCleanup(self.db.close)
        self.db.execute(
            "CREATE TABLE orders_events (order_id INTEGER, status TEXT, "
            "updated_at TEXT, amount INTEGER, event_seq INTEGER)"
        )
        self.db.executemany(
            "INSERT INTO orders_events VALUES (:order_id,:status,:updated_at,:amount,:event_seq)",
            sample_events(),
        )
        latest = get_sql("int_latest_order.sql")
        self.assertIn("order by updated_at desc, event_seq desc", latest.lower())
        self.assertIn("{{ source('erp', 'orders_events') }}", latest)
        self.db.execute(
            "CREATE VIEW int_latest_order AS " +
            latest.replace("{{ source('erp', 'orders_events') }}", "orders_events")
        )
        metric = get_sql("fct_shipped_order_value.sql")
        self.assertIn("{{ ref('int_latest_order') }}", metric)
        self.metric_sql = metric.replace(
            "{{ ref('int_latest_order') }}", "int_latest_order"
        )

    def metric(self):
        return self.db.execute(self.metric_sql).fetchone()

    def test_five_events_three_orders_170(self):
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM orders_events").fetchone()[0], 5)
        self.assertEqual(self.db.execute("SELECT COUNT(*) FROM int_latest_order").fetchone()[0], 3)
        self.assertEqual(self.metric(), (2, 170))

    def test_naive_events_would_sum_to_220(self):
        self.assertEqual(
            self.db.execute("SELECT SUM(amount) FROM orders_events WHERE status='shipped'").fetchone()[0],
            220,
        )

    def test_late_correction_changes_total_to_50(self):
        self.db.execute(
            "INSERT INTO orders_events VALUES (101, 'cancelled', '2026-11-22 08:00:00', 120, 3)"
        )
        self.assertEqual(self.metric(), (1, 50))

    def test_same_timestamp_uses_event_sequence(self):
        self.db.execute(
            "INSERT INTO orders_events VALUES (103, 'cancelled', '2026-11-21 08:00:00', 50, 3)"
        )
        self.assertEqual(self.metric(), (1, 120))

    def test_no_shipped_orders_return_zero_not_null(self):
        self.db.execute("DELETE FROM orders_events")
        self.db.execute(
            "INSERT INTO orders_events VALUES (102, 'cancelled', '2026-11-20 08:10:00', 80, 1)"
        )
        self.assertEqual(self.metric(), (0, 0))

    def test_both_pages_remain_noindex(self):
        for page in (ATLAS, SKILL):
            frontmatter = page.read_text(encoding="utf-8").split("---", 2)[1]
            for expected in (
                "status: needs_verification",
                "verified: false",
                "robots: noindex,follow",
                "sitemap: false",
            ):
                self.assertIn(expected, frontmatter)


if __name__ == "__main__":
    unittest.main()
