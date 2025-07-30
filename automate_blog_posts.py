import google.oauth2.credentials
import google_auth_oauthlib.flow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import feedparser
import datetime

# Blogger API Setup
SCOPES = ['https://www.googleapis.com/auth/blogger']
CLIENT_SECRETS_FILE = 'client_secrets.json'  # Your downloaded file
BLOG_ID = ''  # e.g., '1234567890123456789'

# RSS Feed for Cybersecurity News (add more if needed)
RSS_FEEDS = [
    'https://feeds.feedburner.com/TheHackersNews',
    # Add others: 'https://krebsonsecurity.com/feed/',
]

def authenticate_blogger():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES)
    credentials = flow.run_local_server(port=0)
    return build('blogger', 'v3', credentials=credentials)

def fetch_latest_news(feed_url):
    feed = feedparser.parse(feed_url)
    if not feed.entries:
        return None
    latest_entry = feed.entries[0]  # Get the most recent
    return {
        'title': latest_entry.title,
        'summary': latest_entry.summary[:300] + '...' if 'summary' in latest_entry else 'No summary available.',
        'link': latest_entry.link,
        'published': latest_entry.published if 'published' in latest_entry else datetime.datetime.now().isoformat()
    }

def generate_post_content(news):
    # Simple post generation: Add your analysis or keep it basic
    content = f"""
    <h2>{news['title']}</h2>
    <p><strong>Published on:</strong> {news['published']}</p>
    <p>{news['summary']}</p>
    <p>For full details, read the original article <a href="{news['link']}">here</a>.</p>
    <p><strong>My Analysis:</strong> [Add your tech insights here, e.g., implications for users or mitigation tips]. As a cybersecurity enthusiast, I recommend...</p>
    <p>Stay safe online! #Cybersecurity #TechNews</p>
    """
    return content

def post_to_blogger(service, title, content):
    body = {
        'kind': 'blogger#post',
        'title': title,
        'content': content
    }
    try:
        posts = service.posts()
        insert = posts.insert(blogId=BLOG_ID, body=body, isDraft=False).execute()  # Set isDraft=True to save as draft
        print(f"Post created: {insert.get('url')}")
    except HttpError as error:
        print(f"An error occurred: {error}")

# Main Automation Flow
if __name__ == '__main__':
    service = authenticate_blogger()
    
    for feed in RSS_FEEDS:
        news = fetch_latest_news(feed)
        if news:
            post_title = f"Cybersecurity Update: {news['title']} ({datetime.date.today()})"  # SEO-friendly title
            post_content = generate_post_content(news)
            post_to_blogger(service, post_title, post_content)
            break  # Post only one per run to avoid spamming; remove to post multiple
        
import os
posted_titles_file = 'posted_titles.txt'

def is_posted(title):
    if os.path.exists(posted_titles_file):
        with open(posted_titles_file, 'r') as f:
            return title in f.read()
    return False

def mark_as_posted(title):
    with open(posted_titles_file, 'a') as f:
        f.write(title + '\n')

# In the main loop, add:
if news and not is_posted(news['title']):
    post_title = f"Cybersecurity Update: {news['title']} ({datetime.date.today()})"
    post_content = generate_post_content(news)
    post_to_blogger(service, post_title, post_content)
    mark_as_posted(news['title'])