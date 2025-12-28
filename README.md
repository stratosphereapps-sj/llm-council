# 🧠 LLM Council (Local Multi-Agent AI)

LLM Council is a **local, privacy-friendly AI discussion system** where multiple AI “agents” (Generator, Analyst, Critic, Summarizer) collaborate to think through a topic step by step.

It runs **entirely on your laptop** using **Ollama + Gemma models**, with a simple **Streamlit web interface**.

No cloud APIs. No data leaves your machine.

---

## ✨ What it does

Given a topic, the system:

1. Frames the problem clearly
2. Analyzes it logically
3. Critiques assumptions and gaps
4. Produces a balanced final conclusion

All intermediate responses are stored locally in a SQLite database.

---

## 🧩 Tech stack

* **Ollama** – runs the AI model locally
* **Gemma (4B recommended)** – the language model
* **Python** – orchestration logic
* **Streamlit** – web UI
* **SQLite** – local storage

---

## 🚀 Quick start

### 1️⃣ Install Ollama

Download and install from:
👉 [https://ollama.com](https://ollama.com)

After installation, open a terminal and run:

```bash
ollama pull gemma3:4b
```

(You can also use `gemma3:270m` for lower-end machines.)

---

### 2️⃣ Clone this repository

```bash
git clone https://github.com/<your-username>/llm-council.git
cd llm-council
```

---

### 3️⃣ Set up Python environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

### 4️⃣ Run the app

```bash
streamlit run app.py
```

Your browser will open automatically.
Enter a topic and click **Run Council**.

---

## 🖥️ Example topics

* *Should AI be used in school grading?*
* *Impact of AI on modern education*
* *Is a four-day work week viable in India?*

---

## 🧠 Agents in the council

| Agent      | Role                       |
| ---------- | -------------------------- |
| Generator  | Frames the problem clearly |
| Analyst    | Breaks it down logically   |
| Critic     | Challenges assumptions     |
| Summarizer | Produces final insight     |

---

## 📂 Project structure

```
app.py              # Streamlit UI
council_runner.py   # Agent orchestration
agents/             # Individual agent logic
ollama_client.py    # Ollama API wrapper
db/                 # SQLite database
```

---

## 🔒 Privacy & data

* Runs **fully offline**
* No external APIs
* All discussions stored locally in SQLite
* Safe for sensitive topics

---

## 🛠️ Requirements

* Python 3.10+
* Ollama installed and running
* ~6–8 GB RAM recommended for Gemma 4B

---

## 📌 Notes

* First run may be slower (model loading)
* Small models may produce shorter answers
* Designed for learning, research, and experimentation

---

## 📜 License

MIT License — free to use, modify, and share.
