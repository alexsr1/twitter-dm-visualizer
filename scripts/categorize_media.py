import json
import os
import shutil

# === Config ===
ARCHIVE_FILE = "direct-messages.js"  # Adjust to your filename
MEDIA_FOLDER = "direct_messages_media"
OUTPUT_FOLDER = "categorized_media"
MAX_FILES = 50

# === Load JSON safely ===
def load_json_from_js_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        # Remove "window.YTD.direct_messages.part0 = " from the beginning
        json_str = content.split("=", 1)[1].strip()
        return json.loads(json_str)

# === Main logic ===
def categorize_media():
    data = load_json_from_js_file(ARCHIVE_FILE)

    os.makedirs(OUTPUT_FOLDER, exist_ok=True)
    moved = 0

    for entry in data:
        conv = entry.get("dmConversation", {})
        messages = conv.get("messages", [])
        for message in messages:
            msg_create = message.get("messageCreate", {})
            sender_id = msg_create.get("senderId")
            msg_id = msg_create.get("id")
            media_urls = msg_create.get("mediaUrls", [])

            for media_url in media_urls:
                if msg_id and sender_id:
                    partial_filename = f"{msg_id}-"
                    matches = [
                        f for f in os.listdir(MEDIA_FOLDER)
                        if f.startswith(partial_filename)
                    ]
                    for match in matches:
                        src_path = os.path.join(MEDIA_FOLDER, match)
                        dest_dir = os.path.join(OUTPUT_FOLDER, sender_id)
                        os.makedirs(dest_dir, exist_ok=True)
                        dest_path = os.path.join(dest_dir, match)

                        shutil.move(src_path, dest_path)
                        print(f"Moved: {src_path} -> {dest_path}")

if __name__ == "__main__":
    categorize_media()
