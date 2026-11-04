# Agent notes

A public list of the RSS feeds Oscar reads. `feeds.opml` is the source of
truth; `README.md` mirrors it for humans. Both must be updated together.

## Environment

- This repo lives under `~/Personal`, which uses Oscar's **personal** GitHub
  account `OscarPindaro`. The globally active `gh` account is the Shop Circle
  one, so the folder is wrapped in direnv:

  ```bash
  # .envrc
  export GH_TOKEN="$(gh auth token --user OscarPindaro)"
  ```

  Run `direnv allow` after cloning or after editing `.envrc`.
- SSH for personal repos goes through the `github-wauhaus` host alias, which
  authenticates as `OscarPindaro`:

  ```bash
  git@github-wauhaus:OscarPindaro/feeds.git
  ```

  Plain `git@github.com:` authenticates as `OscarPindaroShopcircle` and will be
  refused.

## Adding or removing a feed

1. Find the feed URL. Try `/rss`, `/feed`, `/feed.xml`, `/atom.xml`, or read
   `application/rss+xml` out of the page `<head>`. The HTML page is not the feed.
2. Verify it is real XML with recent items:

   ```bash
   curl -sL --max-time 15 "$URL" | head -c 400
   ```

   A `200 text/html` response is usually a soft 404, not a feed.
3. Add an `<outline type="rss" …>` entry to `feeds.opml` and a row to the table
   in `README.md`. Keep the existing category groupings.
4. Commit and push.

## Rules

- The repo is public. Never commit tokens, cookies or private feed URLs.
- Do not add aggregator feeds that are not one blog: keep the list curated.
- No build step, no scripts. One OPML file and one README is the whole design.
