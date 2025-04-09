
# 📁 FilePilot AI

**FilePilot AI** is an AI-powered file organizing assistant built with **Flask**, **OpenAI**, and **Tailwind CSS**. It intelligently sorts files into folders based on their names using GPT, saving you time and keeping your system clean.

---

## 🚀 Features

- 🧠 AI-Powered File Sorting (uses GPT to name folders smartly)
- 💬 GPT folder suggestions logged and visible
- 🗃️ Auto-organize files from your Downloads folder
- 🔄 One-click Undo (restore files to original location)
- 🧾 Built-in activity log (`log.txt`)
- 🌐 Simple web interface (HTML + Tailwind CSS)
- 🔐 .env support for secure API key management

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-lightgrey?logo=flask)
![OpenAI](https://img.shields.io/badge/OpenAI-API-blueviolet?logo=openai)
![Tailwind CSS](https://img.shields.io/badge/TailwindCSS-2.0-38B2AC?logo=tailwindcss)

---

## 📸 Screenshot

*(optional: you can drop a screenshot of the app UI here)*

---

## ⚙️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/hinesavery/filepilot-ai.git
cd filepilot-ai

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Add your OpenAI API key to .env
echo "OPENAI_API_KEY=sk-..." > .env

# Run the app
./run.sh
```

Open in browser: [http://localhost:5001](http://localhost:5001)

---

## 📂 Folder Suggestions

FilePilot AI suggests folders like:

- `Documents/`
- `Screenshots/`
- `Photos/`
- `Code/`
- `Videos/`
- `Unsorted/` *(fallback if GPT fails)*

---

## 🤖 Powered by GPT

Using OpenAI's latest API for natural language understanding of filenames. If the quota is exceeded, it falls back gracefully.

---

## 💡 Inspiration

Created as a smart productivity tool to reduce digital clutter and show off some fullstack + AI integration skills. Made for portfolio use with love 💻❤️

---

## 👤 Author

**GitHub:** [@hinesavery](https://github.com/hinesavery)

---

## 📄 License

MIT License
