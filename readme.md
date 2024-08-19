# Courier Python Scraper

## Overview

**Courier Python Scraper** is a simple Python-based desktop application that allows users to extract and display the content of articles from "The Courier" website. This project demonstrates how certain paywalls can be circumvented on some sites by extracting the content directly from the webpage's HTML.

### Features

- **User-Friendly Interface**: Input an article URL from "[The Courier](https://www.thecourier.com.au/)" and view the content directly in the application.
- **Title Extraction**: Automatically extracts and displays the title of the article.
- **Content Display**: Presents the main body of the article while skipping subscription notices and other irrelevant sections.

### Disclaimer

This program is intended solely for educational purposes and personal use. It showcases a technique for extracting content from webpages and should not be used to bypass paywalls in violation of terms of service or applicable laws. Always respect copyright and content ownership.

## Prerequisites

- Python 3.x installed on your machine.
- `pip` package installer.

## Installation Instructions

1. **Clone or Download the Repository**

   Clone the repository from GitHub or download it as a ZIP file and extract it to your desired directory.

   ```bash
   git clone https://github.com/BBGard/courierPythonScraper.git
   cd courier-python-scraper
   ```

2. **Install Required Python Libraries**

   The application requires two main libraries: `requests` and `beautifulsoup4`. You can install them using the following command:

   ```bash
   pip install -r requirements.txt
   ```

   If there is no `requirements.txt` file, install them directly:

   ```bash
   pip install requests beautifulsoup4
   ```

3. **Run the Application**

   After installing the required libraries, you can run the application using Python:

   ```bash
   python article_fetcher_gui.py
   ```

## Usage Instructions

1. Launch the program by running the script as shown in the installation steps.
2. Enter a valid article URL from "The Courier" website into the text box.
3. Click the "Fetch Content" button.
4. The article title and main content will be displayed in the application window.

## Limitations

- **Website-Specific**: This tool is designed to work specifically with articles from "The Courier" website. It may not function correctly with other websites.
- **Content Structure Dependency**: The script relies on the specific HTML structure of "The Courier" articles, including specific phrases to identify content sections. If the website changes its structure, the script may need adjustments.

## Future Enhancements

- **Support for Multiple Sites**: Expand functionality to support content extraction from other news websites.
- **Error Handling**: Improve error handling for various edge cases, such as incorrect URLs or network issues.
- **Save and Export**: Add the ability to save the extracted content as a text file or PDF.

## Conclusion

This project is a simple but effective demonstration of how web scraping can be used to extract content from specific websites. It's a personal project meant for learning and exploration, and users are encouraged to use it responsibly and ethically.

---

Feel free to contribute to the project by submitting issues or pull requests. Your feedback and ideas are welcome!
