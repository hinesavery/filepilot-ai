from flask import Flask, render_template, jsonify
import os
import shutil
from ai_logic import suggest_folder
from datetime import datetime

app = Flask(__name__)

DOWNLOADS_PATH = "/mnt/chromeos/MyFiles/Downloads"
LOG_PATH = "log.txt"
undo_stack = []

def log(message):
    with open(LOG_PATH, "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/organize", methods=["POST"])
def organize():
    files = os.listdir(DOWNLOADS_PATH)
    moved = 0
    errors = 0

    for filename in files:
        full_path = os.path.join(DOWNLOADS_PATH, filename)

        # Skip folders, hidden, and temp files
        if not os.path.isfile(full_path) or filename.startswith(".") or filename.endswith(".crdownload"):
            continue

        try:
            folder_name = suggest_folder(filename)
            folder_path = os.path.join(DOWNLOADS_PATH, folder_name)
            os.makedirs(folder_path, exist_ok=True)

            new_path = os.path.join(folder_path, filename)

            # Skip if already moved
            if os.path.exists(new_path):
                log(f"⚠️ Skipped (already exists): {filename}")
                continue

            shutil.move(full_path, new_path)
            undo_stack.append((new_path, full_path))

            moved += 1
            log(f"✅ Moved: {filename} → {folder_name}/")
        except FileNotFoundError:
            log(f"❌ File not found (skipped): {filename}")
            errors += 1
        except Exception as e:
            log(f"❌ Error moving {filename}: {e}")
            errors += 1

    return jsonify({"moved": moved, "errors": errors})

@app.route("/undo", methods=["POST"])
def undo():
    undone = 0
    errors = 0

    while undo_stack:
        try:
            src, dest = undo_stack.pop()
            shutil.move(src, dest)
            undone += 1
            log(f"🔄 Restored: {os.path.basename(src)} → original location")
        except Exception as e:
            errors += 1
            log(f"❌ Undo error: {e}")

    return jsonify({"restored": undone, "errors": errors})

@app.route("/logs", methods=["GET"])
def logs():
    try:
        with open(LOG_PATH, "r") as f:
            content = f.read()
        return jsonify({"logs": content})
    except Exception as e:
        return jsonify({"logs": f"Error reading log: {e}"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
