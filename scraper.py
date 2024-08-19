import requests
from bs4 import BeautifulSoup

def fetch_article_content(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the title
        title = soup.find('h1').get_text() if soup.find('h1') else "No title found"

        # Extract all paragraphs
        paragraphs = soup.find_all('p')

        # Initialize variables to capture relevant content
        article_text = ""
        capture = False

        for paragraph in paragraphs:
            text = paragraph.get_text().strip()

            # Start capturing after the subscription notice
            if "your digital subscription" in text.lower():
                capture = True
                continue  # Skip the subscription notice itself

            # Stop capturing before the newsletter sign-up
            if "sign up to receive the courier's news alerts" in text.lower():
                break

            if capture:
                article_text += text + "\n"

        return title, article_text.strip()
    else:
        return None, f"Failed to retrieve the article. Status code: {response.status_code}"

# Example URLs from the site (replace with actual URLs)
urls = [
    "https://www.thecourier.com.au/story/8344520/student-computer-hackers-learn-skills-of-defence/",
    # Add more URLs here
]

for url in urls:
    title, content = fetch_article_content(url)
    print(f"Title: {title}\n")
    print(f"Content: {content}\n")
    print("="*80)
