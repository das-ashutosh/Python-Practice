from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

websites = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.wikipedia.org"
]

print("=== Website Link Checker ===")

for website in websites:
    request = Request(
        website,
        headers={"User-Agent": "PythonLinkChecker/1.0"}
    )

    try:
        with urlopen(request, timeout=10) as response:
            print(f"✅ {website} - Status: {response.status}")

    except HTTPError as error:
        print(f"⚠️ {website} - HTTP Error: {error.code}")

    except (URLError, TimeoutError, ValueError) as error:
        print(f"❌ {website} - Connection failed: {error}")

print("\nLink checking complete!")
