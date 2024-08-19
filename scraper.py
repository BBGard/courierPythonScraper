import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup

# def fetch_article_content(url):
#     try:
#         response = requests.get(url)
#         response.raise_for_status()
#     except requests.exceptions.RequestException as e:
#         messagebox.showerror("Error", f"Failed to retrieve the article: {e}")
#         return None, None

#     soup = BeautifulSoup(response.text, 'html.parser')

#     title = soup.find('h1').get_text() if soup.find('h1') else "No title found"
#     paragraphs = soup.find_all('p')

#     article_text = ""
#     capture = False

#     for paragraph in paragraphs:
#         text = paragraph.get_text().strip()

#         if "your digital subscription" in text.lower():
#             capture = True
#             continue

#         if "sign up to receive the courier's news alerts" in text.lower():
#             break

#         if capture:
#             article_text += text + "\n"

#     return title, article_text.strip()
def fetch_article_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"Failed to retrieve the article: {e}")
        return None, None

    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1').get_text() if soup.find('h1') else "No title found"
    paragraphs = soup.find_all('p')

    article_text = ""
    capture = False
    stop_phrases = [
        "sign up to receive the courier's news alerts",
        "today's top stories curated by our news team",
        # "weekly",
        # "daily",
        # "advertisement",
    ]

    for paragraph in paragraphs:
        text = paragraph.get_text().strip()

        if "your digital subscription" in text.lower():
            capture = True
            continue

        if any(phrase in text.lower() for phrase in stop_phrases):
            break

        if capture:
            article_text += text + "\n"

    return title, article_text.strip()


def display_content():
    url = url_entry.get()
    title, content = fetch_article_content(url)

    if content:
        title_label.config(text=f"Title: {title}")
        text_area.delete(1.0, tk.END)
        text_area.insert(tk.INSERT, content)
    else:
        text_area.delete(1.0, tk.END)
        title_label.config(text="Title: ")

# Create the main window
root = tk.Tk()
root.title("Article Fetcher")

# Create URL input
url_label = tk.Label(root, text="Enter Article URL:")
url_label.pack(pady=5)

url_entry = tk.Entry(root, width=50)
url_entry.pack(pady=5)

# Create fetch button
fetch_button = tk.Button(root, text="Fetch Content", command=display_content)
fetch_button.pack(pady=10)

# Create title display
title_label = tk.Label(root, text="Title: ", font=("Arial", 12, "bold"))
title_label.pack(pady=5)

# Create text area to display content
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=60, height=20, font=("Arial", 10))
text_area.pack(pady=5)

# Start the main loop
root.mainloop()
