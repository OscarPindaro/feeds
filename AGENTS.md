# Agent notes

A public list of RSS feeds. Two files, two audiences:

- `feeds.opml` — the curated list Oscar actually reads. `README.md` mirrors it
  in a table. Both must be updated together.
- `feeds-llm.opml` — a wide list for agents and LLMs. Curated feeds plus a
  large set of tech/programming/science feeds. No README mirror; the file is
  the artifact.

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
4. Add the same entry to `feeds-llm.opml` if it fits that file's breadth.
5. Commit and push.

## Keeping feeds-llm.opml honest

```bash
python3 refresh.py --dry-run   # report only
python3 refresh.py             # drop feeds that no longer serve a feed
```

- A feed counts as alive only if it returns HTTP 200 *and* the body contains
  `<item>` or `<entry>`. `200 text/html` is usually a soft 404.
- `refresh.py` retries each URL three times and refuses to rewrite when more
  than 20% fail, because a single failed fetch is usually rate limiting rather
  than a dead feed. Do not lower those guards to "clean up faster" — a 24-way
  concurrent run falsely killed `github.blog` and `martinfowler.com`.
- `refresh.py` rewrites the file through `ElementTree`, so expect a formatting
  diff. That is fine; the XML is equivalent.

## Rules

- The repo is public. Never commit tokens, cookies or private feed URLs.
- `feeds.opml` stays curated: one blog per entry, no aggregators.
- `feeds-llm.opml` favours breadth; a firehose belongs there, not in the
  curated file.
