# LibraryBot

LibraryBot

A lightweight, student-friendly virtual library assistant that answers common questions about hours, borrowing, study rooms, printing, Wi-Fi, databases, events, and general support.

GitHub: https://github.com/revanthreddy24/LibraryBot

✨ Features

Clear, concise answers in simple language

Built-in details for Sampleville Library hours and services

Graceful fallback to website/staff when unsure

Fast API: uses gpt-4o-mini with curated system prompt

Easy to run locally (Flask) or in Docker

📦 Tech Stack

Python 3.10+

Flask (API)

OpenAI API (gpt-4o-mini)


🧱 Suggested Project Structure
LibraryBot/
├─ app.py
├─ requirements.txt
├─ .env.example
├─ README.md
└─ docker/
   ├─ Dockerfile
   └─ gunicorn.conf.py


requirements.txt

flask
python-dotenv
openai>=1.0.0



✅ Usage Tips

Keep temperature low-ish (0.4–0.7) for factual, consistent answers.

If you add more local policies, append them to the system prompt.

For real libraries, replace Sampleville info with current hours, loan limits, and contacts.
