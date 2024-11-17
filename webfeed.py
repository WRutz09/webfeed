import feedparser
#feed_url="http://feeds.bbci.co.uk/news/rss.xml"
#feed_url="https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
#feed_url="https://rss.nytimes.com/services/xml/rss/nyt/Technology.xml"
feed_url="http://feeds.feedburner.com/TechCrunch/"
def fetch_feed(url):
    feed=feedparser.parse(url)
    if feed.bozo==1:
        print("Failed to fetch feed.")
        return
    print(f"Feed Title:{feed.feed.title}\n")
    print("Latest Entries:")
    for entry in feed.entries[:5]:
        print(f"\nTitle:{entry.title}")
        print(f"Link:{entry.link}")
        print(f"Published:{entry.published}")
        print(f"Summary:{entry.summary}\n")

if _name_=="__main__":
    fetch_feed(feed_url)
