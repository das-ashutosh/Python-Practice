from urllib.request import Request, urlopen
from html.parser import HTMLParser
from urllib.error import URLError, HTTPError


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.description = ""
        self.headings = []
        self.current_tag = None
        self.current_text = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)

        if tag == "title":
            self.current_tag = "title"
            self.current_text = []
        elif tag in ("h1", "h2", "h3"):
            self.current_tag = tag
            self.current_text = []
        elif tag == "meta" and attrs.get("name", "").lower() == "description":
            self.description = attrs.get("content", "")

    def handle_data(self, data):
        if self.current_tag:
            self.current_text.append(data.strip())

    def handle_endtag(self, tag):
        if tag == self.current_tag:
            text = " ".join(part for part in self.current_text if part)

            if tag == "title":
                self.title = text
            elif tag in ("h1", "h2", "h3") and text:
                self.headings.append(f"{tag.upper()}: {text}")

            self.current_tag = None
            self.current_text = []


url = input("Enter webpage URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

try:
    request = Request(
        url,
        headers={"User-Agent": "PythonMetadataExtractor/1.0"}
    )

    with urlopen(request, timeout=10) as response:
        html = response.read(2_000_000).decode("utf-8", errors="replace")

    parser = PageParser()
    parser.feed(html)

    print("\n=== Webpage Metadata ===")
    print("URL:", url)
    print("Title:", parser.title or "Not found")
    print("Description:", parser.description or "Not found")

    print("\nHeadings:")
    if parser.headings:
        for heading in parser.headings:
            print("-", heading)
    else:
        print("No headings found.")

except (HTTPError, URLError, TimeoutError, ValueError) as error:
    print("Could not fetch webpage:", error)
