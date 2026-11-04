# RSS feeds

A public list of RSS feeds, in two files:

| File | Size | For |
| --- | --- | --- |
| [`feeds.opml`](feeds.opml) | 9 feeds | Me. Hand-picked, one folder per interest. |
| [`feeds-llm.opml`](feeds-llm.opml) | 179 feeds, 13 categories | Agents and LLMs that ingest broadly. |

```
https://raw.githubusercontent.com/OscarPindaro/feeds/main/feeds.opml
https://raw.githubusercontent.com/OscarPindaro/feeds/main/feeds-llm.opml
```

Readers that only take a file can download those URLs and import them.

**Inoreader** can subscribe to that URL directly (Preferences → Import, Export,
Backup → OPML subscriptions). It re-checks the file every 24 hours on free
accounts, hourly on Pro, and adds or removes feeds automatically. Feeder,
Feedly, NetNewsWire and Reeder only import files, so they need a re-import after
each change.

## Feeds

| Feed | RSS |
| --- | --- |
| [&lt;antirez&gt;](https://antirez.com/) | <https://antirez.com/rss> |
| [Ed Zitron's Where's Your Ed At](https://www.wheresyoured.at/) | <https://www.wheresyoured.at/rss/> |
| [Sean Goedecke](https://www.seangoedecke.com/) | <https://www.seangoedecke.com/rss.xml> |
| [Karri Saarinen](https://karrisaarinen.com/) | <https://karrisaarinen.com/rss.xml> |
| [Hugging Face Blog](https://huggingface.co/blog) | <https://huggingface.co/blog/feed.xml> |
| [Ludicity](https://ludic.mataroa.blog/) | <https://ludic.mataroa.blog/rss/> |
| [Computer, Enhance!](https://www.computerenhance.com/) (Casey Muratori) | <https://www.computerenhance.com/feed> |
| [Sublucid Geometry](https://zalo.github.io/) | <https://zalo.github.io/feed.xml> |
| [Doors to the Unknown](https://doorstotheunknown.substack.com/) | <https://doorstotheunknown.substack.com/feed> |

## feeds-llm.opml

The wide file, for a model that wants a lot of sources rather than a good
reading list. It contains the curated feeds plus:

- **AI & ML** (19) — lab blogs and researchers: OpenAI, DeepMind, Google
  Research, Hugging Face, BAIR, Distill, Latent Space, Import AI, Simon Willison,
  Karpathy, arXiv cs.LG, and others.
- **Systems programming** (10) — Dan Luu, Julia Evans, fasterthanli.me, Russ
  Cox, Andrew Gallant, matklad, Daniel Lemire, Travis Downs, Brendan Gregg,
  Michael Stapelberg.
- **GPU programming** (4) — Thonk From First Principles, Colfax Research,
  Modular, Simon Boehm.
- **Tech, Programming, Web Development, Cyber security, Science, Business &
  Economy, Startups, UI/UX** — 157 feeds taken from
  [awesome-rss-feeds](https://github.com/plenaryapp/awesome-rss-feeds) (CC0).

Every URL was fetched and kept only if it returned HTTP 200 with at least one
`<item>`/`<entry>`; 28 candidates from the upstream list were dead and are
dropped. Nothing regenerates it automatically — when it drifts, re-run the
check.

## Adding a feed

1. Find the feed URL (usually `<site>/rss`, `/feed`, `/feed.xml` or `/atom.xml`;
   check the page source for `application/rss+xml`).
2. Confirm it returns XML: `curl -sI <url> | grep -i content-type`.
3. Add an `<outline type="rss" …>` line to `feeds.opml` and a row to the table.
4. Commit and push. Raw GitHub URLs refresh within a few minutes.

## Notes

- **Tom Aarsen** (Sentence Transformers maintainer) has no personal feed:
  [tomaarsen.com](https://www.tomaarsen.com/) is a static portfolio with no RSS.
  He publishes through the Hugging Face blog, which exposes only the global feed
  (<https://huggingface.co/blog/feed.xml>) — `?author=` is ignored — so the HF
  entry above is a firehose covering every author, not just him.
