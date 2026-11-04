# RSS feeds

A public, hand-maintained list of the blogs I read. `feeds.opml` is the
canonical file; the table below mirrors it for humans.

**Subscribe to everything at once** — point a reader that accepts an OPML URL at:

```
https://raw.githubusercontent.com/OscarPindaro/feeds/main/feeds.opml
```

Readers that only take a file can download that URL and import it.

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
| [Sublucid Geometry](https://zalo.github.io/) | <https://zalo.github.io/feed.xml> |
| [Doors to the Unknown](https://doorstotheunknown.substack.com/) | <https://doorstotheunknown.substack.com/feed> |

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
