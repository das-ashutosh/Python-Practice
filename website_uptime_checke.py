from urllib.request import urlopen
from urllib.error import URLError, HTTPError
from time import perf_counter

url = input("Enter website URL: ").strip()

if not url.startswith(("http://", "https://")):
    url = "https://" + url

print("\nChecking website...")

start = perf_counter()

try:
    with urlopen(url, timeout=10) as response:
        elapsed = perf_counter() - start

        print("Website:", url)
        print("Status code:", response.status)
        print(f"Response time: {elapsed:.2f} seconds")
        print("Result: Website responded successfully!")

except HTTPError as error:
    print("HTTP error:", error.code)
    print("The website returned an error response.")

except (URLError, TimeoutError, ValueError) as error:
    print("Could not reach the website.")
    print("Reason:", error)
