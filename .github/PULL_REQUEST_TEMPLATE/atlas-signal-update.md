## Source Signal(s)

- Signal ID/title:
- Source name:
- Source URL:
- Source date:
- Date checked:

## Target Atlas Page(s)

- Existing page update:
- New page candidate:
- Related pages:

## Files Changed

-

## Evidence Summary

- Concrete facts:
- Product/components:
- Operational implication:

## Why This Belongs Here

-

## Quality Gates Passed

- [ ] Source URL and date present
- [ ] Source body opened
- [ ] At least two concrete facts present
- [ ] Existing target page exists or new-page rationale is present
- [ ] Duplicate-page check passed
- [ ] Generic commentary check passed
- [ ] Private-path/public-safety check passed

## Validation Commands

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -m pytest tests
python3 scripts/generate_atlas_artifacts.py --check
python3 scripts/check_public_repo.py
bundle exec jekyll build
python3 scripts/check_links.py _site
python3 scripts/check_seo.py _site
```

## Safety Note

- [ ] No private drafts, local paths, secrets, raw dumps, or runtime logs
- [ ] No direct push to `main`
- [ ] No unreviewed page creation
- [ ] No automatic publishing beyond the reviewed GitHub Pages merge flow
