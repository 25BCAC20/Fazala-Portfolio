from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from db_config import get_db_connection
import os

app = Flask(__name__, static_folder="../frontend", static_url_path="")
CORS(app)

# Serve index.html at root
@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

# Serve any other static files (CSS, JS)
@app.route("/<path:path>")
def serve_static_files(path):
    return send_from_directory(app.static_folder, path)

# Contact form API
@app.route("/contact", methods=["POST", "OPTIONS"])
def contact():
    try:
        data = request.get_json()
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO contact_messages (name, email, message) VALUES (?, ?, ?)",
            (data["name"], data["email"], data["message"])
        )
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Message saved to database successfully!"})
    except Exception as e:
        print("Error:", e)
        return jsonify({"message": "Error saving message!"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

