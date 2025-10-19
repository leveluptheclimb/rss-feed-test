from flask import Flask, Response

app = Flask(__name__)

@app.route("/")
def serve_feed():
    with open("feed.xml", "r", encoding="utf-8") as f:
        rss_content = f.read()
    return Response(rss_content, mimetype="application/rss+xml")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
