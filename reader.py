from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import feedparser, socket

URL = input("Enter the RSS feed URL: ")

def feed(url):
    try:
        req = Request(url, headers={"User-Agent": "RSSReader/1.0"})
        with urlopen(req, timeout=10) as resp:
            status = getattr(resp, "status", 200)
            if status != 200:
                raise RuntimeError(f"HTTP error: {status}")
            data = resp.read()
        parsed = feedparser.parse(data)
        if getattr(parsed, "bozo", False):
            exc = getattr(parsed, "bozo_exception", None)
            raise RuntimeError(f"Feed parse error: {exc}")
        items = parsed.entries or []
        print("\n")

        for i in items:
            title = getattr(i, "title", "(nincs cím)")
            link = getattr(i, "link", "")
            published = getattr(i, "published", None) or getattr(i, "updated", None) or "(no date)"
            summary = getattr(i, "summary", None) or getattr(i, "description", None) or ""
            print(f"Title: {title}")
            print(f"Link: {link}")
            print(f"Published: {published}")
            print(f"Summary: {summary}\n")
    except HTTPError as e:
        print(f"Error: HTTP error ({e.code}) – {e.reason}. Query is not possible.")
    except URLError as e:
        print(f"Error: Network error – {e.reason}. Query is not possible.")
    except socket.timeout:
        print("Error: Timeout. Query is not possible.")
    except Exception as e:
        print(f"Error: {e}. Query is not possible.")
feed(URL)
