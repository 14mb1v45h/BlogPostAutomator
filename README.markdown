# BlogPostAutomator

A Python-based automation tool to generate and publish cybersecurity news posts to a Google Blogger site (e.g., https://cyberbivash.blogspot.com/). This project leverages the Blogger API to fetch the latest cybersecurity updates from RSS feeds and automatically creates blog posts with summaries and links to original sources.

## Overview

- **Purpose**: Automates the process of posting cybersecurity news, analysis, and updates to boost blog traffic and support monetization efforts (e.g., Google AdSense, affiliate marketing).
- **Technology**: Built with Python, using `google-api-python-client`, `google-auth-oauthlib`, `feedparser`, and `requests`.
- **Target Audience**: Bloggers, cybersecurity enthusiasts, and developers interested in content automation.

## Features

- Fetches the latest cybersecurity news from RSS feeds (e.g., The Hacker News).
- Generates HTML-formatted blog posts with titles, summaries, and source links.
- Publishes posts directly to a specified Blogger blog via the Blogger API.
- Supports scheduling for regular updates (e.g., via Task Scheduler or cron).

## Prerequisites

- Python 3.6 or higher.
- Required libraries:
  - `google-api-python-client`
  - `google-auth-oauthlib`
  - `feedparser`
  - `requests`
- Google Cloud Project with Blogger API enabled and OAuth 2.0 credentials (`client_secrets.json`).
- Blogger account with admin access to the target blog.

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/BlogPostAutomator.git
   cd BlogPostAutomator
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
   (Create `requirements.txt` with: `google-api-python-client google-auth-oauthlib feedparser requests`.)

3. Set up Google Cloud:
   - Create a project in [Google Cloud Console](https://console.cloud.google.com/).
   - Enable the Blogger API.
   - Create OAuth 2.0 Credentials (Desktop app) and download `client_secrets.json`.
   - Place `client_secrets.json` in the project directory.

4. Obtain your Blog ID:
   - Log in to Blogger, go to Settings > Basic, and copy the Blog ID.

## Configuration

- Update `automate_blog_posts.py` with your details:
  - Replace `YOUR_BLOG_ID_HERE` with your Blogger Blog ID.
  - Adjust `RSS_FEEDS` list to include desired news sources (e.g., `https://feeds.feedburner.com/TheHackersNews`).
- Ensure the script has write permissions for the `posted_titles.txt` file (if using duplicate checking).

## Usage

1. Run the script:
   ```
   python automate_blog_posts.py
   ```
   - The script will open a browser for OAuth authentication (first run only).
   - It fetches the latest news, generates a post, and publishes it to your blog.

2. Schedule automation:
   - **Windows**: Use Task Scheduler to run the script daily (e.g., 1:00 PM IST).
     - Action: `python.exe`
     - Arguments: `path\to\automate_blog_posts.py`
   - **Linux/Mac**: Use cron (e.g., `0 7 * * * python /path/to/automate_blog_posts.py` for 1:00 PM IST).

3. Verify posts on your blog (e.g., https://cyberbivash.blogspot.com/).

## Enhancing the Project

- **Add Analysis**: Modify the `generate_post_content` function to include custom insights or use an API for dynamic content.
- **Duplicate Prevention**: The script includes basic duplicate checking with `posted_titles.txt`—expand as needed.
- **Multiple Feeds**: Add more RSS feeds to `RSS_FEEDS` and remove the `break` to process all.
- **Monetization**: Integrate affiliate links or AdSense optimization logic.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes and commit (`git commit -m "Description of changes"`).
4. Push to the branch (`git push origin feature-branch`).
5. Open a Pull Request with details of your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

- **Author**: CyberDudeBivash (iambivash.bn@gmail.com)
- **Blog**: [https://cyberbivash.blogspot.com/](https://cyberbivash.blogspot.com/)
- For issues or suggestions, open an issue on GitHub or reach out via email.

## Acknowledgments

- Inspired by the need to automate cybersecurity content for https://cyberbivash.blogspot.com/.
- Thanks to The Hacker News and other RSS providers for news feeds.
- Built with guidance from the xAI community and Google API documentation.