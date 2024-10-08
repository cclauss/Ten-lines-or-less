#!/usr/bin/env python3

import bs4
import requests

ignore = ["python/cpython"]

fmt = """  echo ; echo -n "{i} flake8 testing of {long} on " ; python -V
  - git clone --depth=50 --branch=master https://github.com/{long} ~/{short}
  - cd ~/{short}
  # stop the build if there are Python syntax errors or undefined names
  - flake8 . --count --exit-zero --select=E9,F63,F7,F82 --statistics
  # exit-zero treats all errors as warnings.  The GitHub editor is 127 chars wide
  - flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
"""

url = "https://github.com/trending?l=Python"
soup = bs4.BeautifulSoup(requests.get(url).content, "lxml")  # or 'html5lib'
# 'python / cpython'
repos = soup.find("ol", class_="repo-list").find_all("a", href=True)
# 'python/cpython'
repos = (r.text.strip().replace(" ", "") for r in repos if "/" in r.text)
# {'i', 7, 'long': 'python/cpython', 'short': 'cpython'}
repos = (
    {"i": i + 1, "long": repo, "short": repo.split("/")[-1]}
    for i, repo in enumerate(repos)
)
print("=" * 50)
print("\n".join(fmt.format(**repo) for repo in repos if repo not in ignore))
