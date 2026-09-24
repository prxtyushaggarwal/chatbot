# 🤖 Pratyush AI — Intelligent Gemini Chatbot

A high-performance, modern conversational AI assistant powered by **Google Gemini** (via the official `google-genai` SDK).

The Gemini API key is **permanently configured on the backend**, so users can chat immediately without entering any keys or configuring credentials in the browser!

---

## ✨ Features

- ⚡ **Real-Time Token Streaming**: Smooth, responsive word-by-word generation.
- 🔒 **Zero-Config Backend Key**: API key is handled securely on the backend server. No API prompts on the web interface.
- 🧠 **Latest Gemini Models**:
  - `gemini-2.5-flash` (Default — fast, highly intelligent, versatile)
  - `gemini-2.5-pro` (Deep reasoning & complex tasks)
  - `gemini-2.0-flash`
  - `gemini-1.5-flash` & `gemini-1.5-pro`
- 🎨 **Modern Dark Glassmorphism UI**: High-contrast, responsive slate-theme layout designed for desktop and mobile.
- 💻 **Syntax Highlighting & Code Copy**: Instant copy button for code snippets with language badges.
- 🎭 **AI Personas**: Easily switch between Senior Software Engineer, Data Scientist, Creative Brainstormer, or Custom system instructions.
- 📥 **Export Chat**: Download the entire conversation as clean Markdown at any time.

---

## 🚀 Quick Start

### 1. Installation

```bash
git clone https://github.com/prxtyushaggarwal/chatbot-assistant.git
cd chatbot-assistant
pip install -r requirements.txt
```

### 2. Run the App

#### Option A: Full-Stack Web Application (Recommended)
Run the FastAPI backend server:

```bash
python server.py
```
Open **`http://localhost:8000`** in your browser and start chatting immediately!

#### Option B: Streamlit Chatbot
Run the Streamlit application:

```bash
streamlit run app.py
```
Open **`http://localhost:8501`** in your browser.

---

## 📁 Project Structure

```
chatbot-assistant/
├── app.py              # Streamlit chatbot application
├── app2.py             # Streamlit execution alias
├── server.py           # FastAPI backend server with permanent Gemini key & SSE streaming
├── index.html          # Modern dark-mode web chat interface (no API key prompts)
├── requirements.txt    # Python dependencies
├── .env                # Backend environment configuration
└── README.md           # Documentation
```

---

## 🛠️ Tech Stack

- **AI SDK**: `google-genai` (Google GenAI Python SDK)
- **Frontend**: HTML5, CSS3, Vanilla JS, `marked.js`, `highlight.js`
- **Backend**: FastAPI, Uvicorn, Pydantic
- **Data App**: Streamlit
