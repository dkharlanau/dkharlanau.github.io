# Design Adoption Brief: Martenweave Style → cv-ai

Рабочая проработка: что именно взять из дизайна `martenweave.github.io` и как применить к сайту cv-ai (dkharlanau.github.io), не ломая контент, SEO и систему верификации.

Источник стиля: `/Users/dzmitryikharlanau/Developments/martenweave.github.io` (`styles.css`, `home.css`, `index.html`).
Цель: `/Users/dzmitryikharlanau/Developments/cv-ai` (`assets/site.css`, `assets/main.css`, `_includes/sections/*`, `DESIGN-SYSTEM.md`).

---

## 1. Дизайн-ДНК Martenweave (что делает его узнаваемым)

| Приём | Реализация в martenweave |
|---|---|
| Ruled-grid («линованная» сетка) | Секции и карточки разделены 1px линиями (`--line`, `--lilac`); гриды с общими границами, без зазоров, без скруглений, без теней |
| Eyebrow / kicker | Моноширинный uppercase, amber `#d98d12`, letter-spacing 0.08–0.11em |
| Моно-слой метаданных | Trust-lines, индексы `01/02/03`, version lines — маленький monospace |
| Огромные заголовки | `clamp()` до 5.8rem, `letter-spacing: -0.045…-0.055em`, `max-width` в `ch`, `text-wrap: balance` |
| Hard offset shadow | `box-shadow: 14px 14px 0 #eee7db` на тёмных терминалах и скриншотах — эффект «вырезанной бумаги» |
| Рейлы процессов | `workflow-rail` / `process-rail`: горизонтальные шаги с соединительными линиями, стрелками-уголками, пульсирующей точкой |
| Proof strip | 3–4 колонки с жирным утверждением + пояснением, разделённые hairline |
| Тёмные терминалы | Блоки кода/вывода на глубоком акценте (`#321136`/`#291035`) с amber-подсветкой |
| Навигация | Анимированное подчёркивание `scaleX` при hover; fixed header с blur |
| A11y | Skip-link, `:focus-visible` amber outline 3px, `prefers-reduced-motion` |
| Радиусы | `--radius: 3px` — почти прямые углы |

## 2. Текущее состояние cv-ai

- Палитра: холодный нейтральный (`#f6f7f9` фон, `#111827` ink, акцент navy-charcoal `#152033`).
- Карточки: скругления 10–18px, мягкие тени — «app-like», не editorial.
- Уже есть: Inter + Source Serif 4, kicker-элементы, page-builder на `_includes/sections`, сильный `DESIGN-SYSTEM.md` с editorial B2B интентом.
- Проблема: структура (rounded cards + shadows) противоречит заявленному editorial-интенту; martenweave показывает, как тот же интент выглядит в зрелом виде.

## 3. Решение: гибрид

**Берём структурную грамматику martenweave, оставляем холодную палитру cv-ai как бренд.**

- Фон/ink/акцент cv-ai не меняем (navy-charcoal вместо aubergine).
- Вводим ОДИН тёплый акцент — amber `#d98d12` — только для kicker, индексов, focus-outline, маркеров. Amber + navy — рабочая пара, конфликта нет.
- Радиусы: 18/14/10px → 2–4px. Тени: убрать, оставить только offset paper shadow на тёмных блоках/скриншотах.
- Скруглённые карточки с тенями → hairline-гриды с общими границами.

## 4. Маппинг компонентов

| cv-ai секция / страница | Паттерн martenweave |
|---|---|
| `_includes/sections/hero.html` | `atlas-hero`: eyebrow + h1 max-14ch + mono trust-line + 2 кнопки (primary fill / secondary outline, radius 2px) |
| `credibility.html` | `proof-strip`: 3–4 колонки, hairline-разделители, жирное утверждение + мелкое пояснение |
| `analysis-problem.html` | `distinction` / `pillars`: грид с общими границами, крупный текст без карточек |
| `engagement-framework.html` | `workflow-rail`: нумерованные шаги, соединительная линия, mono-индексы |
| `explore-site.html` | `use-case-list` / `docs-grid`: bordered cell-грид, hover-заливка accent-soft |
| `faq.html` | `faq-list`: hairline top/bottom, вопросы без карточек |
| `contact.html` | `conversion-section`: сетка заголовок + текст + CTA в одну строку |
| Страницы datasets | `docs-card` грид с mono-kicker и hover-tint |
| Atlas-страницы | `doc-shell`: sticky sidebar 230px + контент max-790px, h2 с hairline top |
| Header/footer | underline-анимация ссылок, mono footer-line |

## 5. Чего НЕ делать

- Не копировать aubergine-палитру и фиолетовые оттенки — конфликт бренда cv-ai.
- Не переносить hero-анимацию дрейфа картинки и product-скриншоты — это product-сайт, cv-ai — персональный консалтинг.
- Не трогать контент, claims, frontmatter, verification-статусы, sitemap/llms-файлы.
- Не переписывать `main.css`/`material3.css` — новый слой токенов и компонентов поверх, `site.css` грузится последним.
- Не менять SEO/Schema/JSON-LD.

## 6. План внедрения (фазы)

1. **Токены**: новый блок `:root` в `site.css` (или `design-tokens.css` последним): radius 2–4px, amber accent, mono stack, line colors, offset-shadow токен.
2. **Глобальный хром**: header underline-анимация, focus-visible amber, footer mono-line.
3. **Главная**: hero → atlas-hero структура; credibility → proof-strip; engagement → workflow-rail; explore → bordered grid; faq → hairline list.
4. **Внутренние шаблоны**: тот же слой на about/services/atlas/datasets через общие классы.
5. **Atlas/doc shell**: sticky sidebar, hairline-заголовки, amber-заметки.
6. **Валидация** (обязательно, из AGENTS.md): `pytest tests`, `check_public_repo.py`, `jekyll build`, `check_links.py _site`, `check_seo.py _site`, `check_page_quality.py`.

## 7. Критерии приёмки

- Ни одного элемента с radius > 4px; теней нет, кроме offset paper shadow.
- Все списки/гриды карточек — hairline с общими границами.
- Kicker/индексы/метаданные — monospace amber.
- Mobile: гриды складываются в 1 колонку с hairline-разделителями (как в martenweave `@media 680/760px`).
- Весь validation-набор зелёный; `prefers-reduced-motion` соблюдён.
