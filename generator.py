from urllib.parse import quote_plus
from textwrap import dedent
projects = [
    {
        "repo": "",
        "website": "https://data.cleanchemi.com",
        "rtd": "",
        "name": "Clean Chemistry Inc. Dashboard Website",
        "status": "🟠",
        "type": "Website",
    },
    {
        "repo": "",
        "website": "https://cleanchemi.com",
        "rtd": "",
        "name": "Clean Chemistry Inc. Informational Website",
        "status": "🟢",
        "type": "Website",
    },
    {
        "repo": "flabnatz/Game.WordGuess",
        "website": "",
        "rtd": "Game.WordGuess",
        "name": "Game.WordGuess",
        "status": "🔴",
        "type": "Game",
    },
    {
        "repo": "flabnatz/AlphaWebsite",
        "website": "",
        "rtd": "AlphaWebsite",
        "name": "AlphaWebsite",
        "status": "⚪️",
        "type": "Learning",
    }
]

headings = ["Name", "Status", "Type", "Links"]
rows = []
for p in projects:

    repo, website, rtd, name, status, type = p["repo"], p["website"], p["rtd"], p["name"], p["status"], p["type"]

    url_encoded = "" if not website else quote_plus(website)
    row_tds = [
        f"<td>{name}</td>",
        f"<td>{status}</td>",
        f"<td>{type}</td>",
        "<td>\n\n",
        "" if not p["rtd"] else f"\n[![{name}](https://img.shields.io/readthedocs/{rtd}?style=flat-square)](https://{rtd}.readthedocs.io)",
        "" if not p["website"] else f"\n[![{name}](https://img.shields.io/website?style=flat-square&url={url_encoded})]({website})",
        "" if not p["repo"] else f"\n[![GitHub Repo stars](https://img.shields.io/github/stars/{repo}?style=flat-square)](https://github.com/{repo})",
        "\n\n</td>"
    ]

    rows.append("".join(row_tds).format(**p))

heading_tds = "".join([f"<th>{name}</th>" for name in headings])
rows_tds = "".join([f"<tr>{name}</tr>\n" for name in rows])
html = f"""
<table>
 <tr>
  {heading_tds}
 </tr>
{rows_tds}
</table>
"""

print(dedent(html))
