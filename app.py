from flask import Flask, Response
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def rss_feed():
    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
    <rss version="2.0">
      <channel>
        <title>SkyLearn Live Feed</title>
        <link>https://skylearn.io</link>
        <description>Dynamically served feed for SkyLearn testing</description>
        <item>
          <title>Render Deployment Test</title>
          <link>https://skylearn.io/test-article</link>
          <description>This confirms live dynamic updates via Render.</description>
          <pubDate>{datetime.utcnow().strftime('%a, %d %b %Y %H:%M:%S GMT')}</pubDate>
        </item>
      </channel>
    </rss>"""
    return Response(rss, mimetype="application/rss+xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
