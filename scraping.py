import requests
from bs4 import BeautifulSoup

# Website URL
url = "https://example.com"

# Send request to website
response = requests.get(url, timeout=10)

# Check response
if response.status_code == 200:

    # Read HTML content
    soup = BeautifulSoup(response.text, "html.parser")

    # Print website title
    print("Website Title:", soup.title.string)

    # Find all links
    links = soup.find_all("a")

    print("\nLinks found on website:\n")

    for link in links:
        text = link.get_text(strip=True)
        href = link.get("href")

        print("Text:", text)
        print("Link:", href)
        print("-------------------")

else:
    print("Failed to access website")
    print("Status Code:", response.status_code)