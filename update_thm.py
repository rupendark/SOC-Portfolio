import re
import requests
from bs4 import BeautifulSoup

USERNAME = "Rupendar"

README = "README.md"


def fetch_profile():

    url = f"https://tryhackme.com/p/{USERNAME}"

    html = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0"
        }
    ).text

    soup = BeautifulSoup(html, "html.parser")

    text = soup.get_text(" ", strip=True)

    def extract(pattern, default="N/A"):
        match = re.search(pattern, text)
        return match.group(1) if match else default

    stats = {
        "rank": extract(r"Rank\s*(\d+)"),
        "rooms": extract(r"Rooms Completed\s*(\d+)"),
        "streak": extract(r"Streak\s*(\d+)"),
        "badges": extract(r"Badges\s*(\d+)")
    }

    return stats


def replace(content, tag, value):

    pattern = rf"(<!--{tag}-->).*?(<!--/{tag}-->)"

    return re.sub(
        pattern,
        rf"\1{value}\2",
        content,
        flags=re.DOTALL,
    )


def main():

    stats = fetch_profile()

    with open(README, "r", encoding="utf-8") as f:
        readme = f.read()

    readme = replace(readme, "THM_RANK", stats["rank"])
    readme = replace(readme, "THM_ROOMS", stats["rooms"])
    readme = replace(readme, "THM_STREAK", stats["streak"])
    readme = replace(readme, "THM_BADGES", stats["badges"])

    with open(README, "w", encoding="utf-8") as f:
        f.write(readme)

    print(stats)


if __name__ == "__main__":
    main()
