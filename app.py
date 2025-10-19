from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def rss_feed():
    # List of article dictionaries — add or edit these any time
    articles = [
        {
            "title": "Office Relocatio99999999999999999999n - Canary Wharf",
            "link": "https://commercialobserver.co.uk/canary-relocation",
            "description": "New 25,000 sq ft HQ lease agreed at 20 Canada Square.",
            "pubDate": datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        },
        {
            "title": "Fit-Out Completed - Soho HQ",
            "link": "https://propertynews.london/soho-fitout",
            "description": "Creative agency completes 15,000 sq ft refurbishment on Wardour Street.",
            "pubDate": datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        },
        {
            "title": "New Letting - South Bank",
            "link": "https://realestateweek.co.uk/southbank-lease",
            "description": "Tech startup secures 10,000 sq ft lease at 2 More London Place.",
            "pubDate": datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')
        }
    ]

    # Build RSS XML dynamically
    items_xml = ""
    for a in articles:
        items_xml += f"""
        <item>
          <title>{a['title']}</title>
          <link>{a['link']}</link>
          <description>{a['description']}</description>
          <pubDate>{a['pubDate']}</pubDate>
        </item>"""

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
    <rss version="2.0">
      <channel>
        <title>SkyLearn Live Feed</title>
        <link>https://skylearn.io</link>
        <description>Dynamically served feed for SkyLearn testing</description>
        {items_xml}
      </channel>
    </rss>"""

    return Response(rss, mimetype="application/rss+xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
