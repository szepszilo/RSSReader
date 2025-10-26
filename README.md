# RSSReader

A tiny CLI that **downloads** an RSS/Atom feed (with an explicit *User-Agent* and a 10s timeout), **parses** it using [`feedparser`](https://pypi.org/project/feedparser/), and prints each entry’s **title**, **link**, **published date**, and **summary**.  
Includes friendly **error handling** for HTTP, network, timeout, and parse issues.

---

## Features
- Fetch via `urllib.request` with custom **User-Agent** and **timeout**.
- Check **HTTP status** (non-200 → clear error).
- Detect parsing problems via **`feedparser`’s `bozo` flag**.
- Safe field fallbacks:
  - `title` → `"(no title)"`
  - `published` → try `published`, then `updated`, else `"(no date)"`
  - `summary` → try `summary`, then `description`, else `""`
- Human-readable error messages.

---

## Requirements
- **Python 3.8+**
- **feedparser**

`requirements.txt` example: