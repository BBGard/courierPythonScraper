import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from bs4 import BeautifulSoup

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
    ]

    for paragraph in paragraphs:
        text = paragraph.get_text().strip()

        if "your digital subscription" in text.lower():
            capture = True
            continue

        if any(phrase in text.lower() for phrase in stop_phrases):
            break

        if capture:
            article_text += text + "\n\n"  # Add extra newline for paragraph spacing

    return title, article_text.strip()

def display_content():
    url = url_entry.get()
    title, content = fetch_article_content(url)

    if content:
        title_label.config(text=f"Title: {title}")
        text_area.delete(1.0, tk.END)
        formatted_content = format_content(content)
        text_area.insert(tk.INSERT, formatted_content)
    else:
        text_area.delete(1.0, tk.END)
        title_label.config(text="Title: ")

def format_content(content):
    """
    Formats the content by splitting into paragraphs and adding spacing.
    """
    paragraphs = content.split('\n\n')  # Split paragraphs based on double newlines
    formatted_content = '\n\n'.join(paragraphs)  # Join paragraphs with double newlines
    return formatted_content

# Create the main window
root = tk.Tk()
root.title("Courier Python Scraper")

# Set the window size and background color
root.geometry("800x600")  # Width x Height
root.configure(bg="#f5f5f5")

# Create URL input
url_label = tk.Label(root, text="Enter Article URL:", font=("Arial", 14, "bold"), bg="#f5f5f5")
url_label.pack(pady=10)

url_entry = tk.Entry(root, width=80, font=("Arial", 12))
url_entry.pack(pady=5)

# Create fetch button
fetch_button = tk.Button(root, text="Fetch Content", command=display_content, font=("Arial", 12, "bold"), bg="#007bff", fg="#ffffff", relief=tk.RAISED)
fetch_button.pack(pady=15)

# Create title display
title_label = tk.Label(root, text="Title: ", font=("Arial", 16, "bold"), bg="#f5f5f5")
title_label.pack(pady=10)

# Create text area to display content
text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=30, font=("Arial", 12), bg="#ffffff", fg="#000000", padx=10, pady=10)
text_area.pack(pady=10)

# Start the main loop
root.mainloop()
