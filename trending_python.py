#!/usr/bin/env python3

import bs4
import requests

url = "https://github.com/trending?l=Python"
soup = bs4.BeautifulSoup(requests.get(url).content, "lxml")  # or 'html5lib'
repos = soup.find("ol", class_="repo-list").find_all("a", href=True)
repos = (r.text.strip().replace(" ", "") for r in repos if "/" in r.text)
print("\n".join(repos))
