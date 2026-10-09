#!/usr/bin/env python3
"""person-search.py - quick public-web lookup for a name using Google's
Programmable Search (Custom Search JSON API).

Setup (free tier: 100 searches/day):
  1. Create a search engine at https://programmablesearchengine.google.com (search the whole web)
  2. Get an API key at https://developers.google.com/custom-search/v1/introduction
  3. export GOOGLE_API_KEY=...  and  export GOOGLE_CSE_ID=...   (e.g. in ~/.bash_aliases.local)

Usage:  person-search.py "Full Name" [extra words, e.g. a city]
Saves a JSON report next to where you run it. Needs: pip3 install requests beautifulsoup4
Use responsibly: public information only, and respect people's privacy.
"""
import json
import os
import re
import sys

import requests
from bs4 import BeautifulSoup

API = "https://www.googleapis.com/customsearch/v1"
HEADERS = {"User-Agent": "Mozilla/5.0 (person-search.py)"}


class BiographyBot:
    def __init__(self, name, extra=""):
        self.name = name
        self.query = f'"{name}" {extra}'.strip()
        self.data = {"name": name, "query": self.query, "results": []}
        self.errors = []

    def search(self):
        key, cx = os.environ.get("GOOGLE_API_KEY"), os.environ.get("GOOGLE_CSE_ID")
        if not key or not cx:
            sys.exit("Set GOOGLE_API_KEY and GOOGLE_CSE_ID first (see the top of this script).")
        r = requests.get(API, params={"q": self.query, "key": key, "cx": cx, "num": 10}, timeout=15)
        if r.status_code != 200:
            sys.exit(f"Search failed: HTTP {r.status_code} - {r.text[:200]}")
        return r.json().get("items", [])

    def scrape(self, url):
        """Pull the page title and description (works on most sites)."""
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            r.raise_for_status()
        except requests.RequestException as e:
            self.errors.append((url, str(e)[:120]))
            return {}
        soup = BeautifulSoup(r.text, "html.parser")
        desc = soup.find("meta", attrs={"name": "description"}) or soup.find("meta", attrs={"property": "og:description"})
        return {"page_title": soup.title.get_text(strip=True) if soup.title else "",
                "description": (desc.get("content", "") if desc else "").strip()}

    def generate_biography(self):
        for item in self.search():
            entry = {"title": item.get("title"), "link": item.get("link"), "snippet": item.get("snippet")}
            entry.update(self.scrape(item["link"]))
            self.data["results"].append(entry)
        self.data["errors"] = [f"{u} - {e}" for u, e in self.errors]
        return self.data


def main():
    if len(sys.argv) > 1:
        name, extra = sys.argv[1], " ".join(sys.argv[2:])
    else:
        name, extra = input("Enter the name: ").strip(), ""
    if not name:
        sys.exit("No name given.")
    report = BiographyBot(name, extra).generate_biography()
    out = re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower() + "-report.json"
    with open(out, "w") as f:
        json.dump(report, f, indent=2)
    for r in report["results"]:
        print(f"- {r['title']}\n  {r['link']}\n  {r.get('description') or r.get('snippet') or ''}\n")
    print(f"{len(report['results'])} results saved to {out}")


if __name__ == "__main__":
    main()
