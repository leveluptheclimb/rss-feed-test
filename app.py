from flask import Flask, send_from_directory, Response
import os

app = Flask(__name__)

# Serve feed.xml at root
@app.route("/")
def serve_root_feed():
    if os.path.exists("feed.xml"):
        return send_from_directory(".", "feed.xml", mimetype="application/rss+xml")
    return Response("feed.xml not found", status=404)

# Serve any other XML file by direct URL, e.g. /feedv2.xml
@app.route("/<path:filename>")
def serve_any_xml(filename):
    if filename.endswith(".xml") and os.path.exists(filename):
        return send_from_directory(".", filename, mimetype="application/rss+xml")
    return Response("File not found", status=404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
