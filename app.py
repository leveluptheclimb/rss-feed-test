from flask import Flask, send_from_directory, Response
import os

app = Flask(__name__)

# Serve feed.xml at root
@app.route("/")
def serve_root_feed():
    if os.path.exists("feed.xml"):
        return send_from_directory(".", "feed.xml", mimetype="application/rss+xml")
    return Response("feed.xml not found", status=404)

@app.route("/<path:filename>")
def serve_any_xml(filename):
    """Serve any .xml file in the same folder as app.py, regardless of working dir."""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, filename)
    if filename.endswith(".xml") and os.path.exists(file_path):
        return send_from_directory(base_dir, filename, mimetype="application/rss+xml")
    return Response("File not found", status=404)
    
@app.route("/whereami")
def whereami():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    files = os.listdir(base_dir)
    return f"Current directory: {base_dir}<br>Files: {', '.join(files)}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 10000)))
