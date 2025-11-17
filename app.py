from flask import Flask, send_from_directory, Response
import os

# Force base directory to the deployed source root
BASE_DIR = "/opt/render/project/src"

app = Flask(__name__)

@app.route("/")
def serve_root_feed():
    """Serve feed.xml at root."""
    file_path = os.path.join(BASE_DIR, "feed.xml")
    if os.path.exists(file_path):
        return send_from_directory(BASE_DIR, "feed.xml", mimetype="application/rss+xml")
    return Response("feed.xml not found", status=404)

@app.route("/<path:filename>")
def serve_any_xml(filename):
    """Serve any .xml file from project root regardless of working dir."""
    file_path = os.path.join(BASE_DIR, filename)
    if filename.endswith(".xml") and os.path.exists(file_path):
        return send_from_directory(BASE_DIR, filename, mimetype="application/rss+xml")
    return Response("File not found", status=404)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
