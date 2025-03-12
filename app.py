from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import os
import logging
from config import VIDEO_DIR, LOG_DIR
from downloader import download_video

# Initialize Flask
app = Flask(__name__)
CORS(app)  # Allow frontend to access API

# Logging setup
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "app.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

@app.route("/")
def home():
    return jsonify({"message": "YouTube Downloader API is running!"})

@app.route("/download", methods=["GET"])
def download():
    url = request.args.get("url")
    format_type = request.args.get("format", "video")  # Default to video

    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    logging.info(f"Downloading {format_type}: {url}")

    file_path, error = download_video(url, format=format_type)
    
    if error:
        logging.error(f"Download failed: {error}")
        return jsonify({"error": "Download failed", "details": error}), 500

    return send_file(file_path, as_attachment=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
