# Twitter Chat Visualizer

A web-based viewer for exploring your Twitter DM archive. It categorizes and displays messages and media in a clean, chat-like interface built with Svelte and Vite.

---

## ✨ Features

* Browse Twitter DMs by conversation
* Embedded support for images and videos
* Emoji reactions display
* Categorized media by sender
* Responsive layout with conversation list and chat view

---

## 🧰 Requirements

* [Node.js](https://nodejs.org) (v16+ recommended)
* Python 3 (for the media organizing script)
* A downloaded Twitter archive from [Twitter's data page](https://twitter.com/settings/download_your_data)

---

## ⚙️ Setup Instructions

### 1. Extract Your Twitter Archive

Unzip your Twitter archive and locate the folder with:

* `direct-messages.js`
* `direct_messages_media/`

### 2. Run the Media Categorizer

Copy the `categorize_media.py` script to the **root of your Twitter archive folder**, then run:

```bash
python categorize_media.py
```

This will:

* Parse `direct-messages.js`
* Move media from `direct_messages_media/` to `categorized_media/` organized by `senderId`

### 3. Copy Files Into Project

Move the generated files to the project:

```bash
# From the archive root
mv categorized_media/ /path/to/twitter-chat-visualizer/public/

# Extract the JSON from direct-messages.js (or manually remove the first part of the first line until the equal sign)
node /path/to/twitter-chat-visualizer/scripts/extract-json.cjs

# Then move the result:
mv direct-messages.json /path/to/twitter-chat-visualizer/public/
```

### 4. Install and Run the App

```bash
cd twitter-chat-visualizer
npm install
npm run dev
```

Visit: [http://localhost:5173](http://localhost:5173)

---

## 🚀 Tech Stack

* [Svelte](https://svelte.dev/)
* [Vite](https://vitejs.dev/)
* Python (for archive media organization)
