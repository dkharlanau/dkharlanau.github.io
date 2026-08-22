from scripts.check_structured_data import validate_item


CANONICAL = "https://dkharlanau.github.io/atlas/diagnostics/example/"


def breadcrumb(*urls: str) -> dict:
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {
                "@type": "ListItem",
                "position": index,
                "name": f"Level {index}",
                "item": url,
            }
            for index, url in enumerate(urls, start=1)
        ],
    }


def validate(value: dict, canonical_url: str = CANONICAL) -> list[str]:
    errors: list[str] = []
    validate_item(value, errors, "fixture", canonical_url)
    return errors


def test_valid_breadcrumb_chain_passes():
    value = breadcrumb(
        "https://dkharlanau.github.io/",
        "https://dkharlanau.github.io/knowledge/",
        "https://dkharlanau.github.io/atlas/",
        "https://dkharlanau.github.io/atlas/diagnostics/",
        CANONICAL,
    )

    assert validate(value) == []


def test_breadcrumb_validator_rejects_duplicate_urls():
    value = breadcrumb(
        "https://dkharlanau.github.io/",
        "https://dkharlanau.github.io/atlas/diagnostics/",
        "https://dkharlanau.github.io/atlas/diagnostics/",
        CANONICAL,
    )

    assert any("duplicate item URLs" in error for error in validate(value))


def test_breadcrumb_validator_rejects_double_slash_paths():
    value = breadcrumb(
        "https://dkharlanau.github.io/",
        "https://dkharlanau.github.io/atlas//diagnostics/",
        CANONICAL,
    )

    assert any("double-slash path" in error for error in validate(value))


def test_breadcrumb_validator_requires_canonical_terminal_url():
    value = breadcrumb(
        "https://dkharlanau.github.io/",
        "https://dkharlanau.github.io/atlas/diagnostics/",
    )

    assert any("canonical is" in error for error in validate(value))


def test_breadcrumb_validator_requires_contiguous_positions():
    value = breadcrumb(
        "https://dkharlanau.github.io/",
        "https://dkharlanau.github.io/atlas/diagnostics/",
        CANONICAL,
    )
    value["itemListElement"][-1]["position"] = 4

    assert any("positions must be contiguous" in error for error in validate(value))
