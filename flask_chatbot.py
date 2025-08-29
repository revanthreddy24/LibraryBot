
import os
from dotenv import load_dotenv
from flask import Flask, render_template_string, request, jsonify
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app = Flask(__name__)

HTML = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>OpenAI Chatbot</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; margin: 2rem auto; max-width: 800px; }
    .bubble { padding: .8rem 1rem; border-radius: 10px; margin: .5rem 0; }
    .user { background: #eef; }
    .assistant { background: #efe; }
  </style>
</head>
<body>
  <h1>LibraryBot</h1>
  <div id="chat"></div>
  <form id="form">
    <input id="msg" placeholder="Type your message" style="width:75%" />
    <button>Send</button>
  </form>
  <script>
    const chat = document.getElementById('chat');
    const form = document.getElementById('form');
    const msg = document.getElementById('msg');

    function addBubble(text, cls) {
      const div = document.createElement('div');
      div.className = 'bubble ' + cls;
      div.textContent = text;
      chat.appendChild(div);
      window.scrollTo(0, document.body.scrollHeight);
    }

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const text = msg.value.trim();
      if (!text) return;
      addBubble(text, 'user');
      msg.value = '';

      const res = await fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({ message: text })
      });
      const data = await res.json();
      addBubble(data.reply, 'assistant');
    });
  </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json.get('message', '')
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a helpful and friendly library assistant for Sampleville Library located at 123 College Ave Sampleville MA "
                    "Provide clear accurate and student friendly answers to questions about library hours Monday to Thursday 8 am to 10 pm "
                    "Friday 8 am to 6 pm Saturday 10 am to 6 pm Sunday 12 pm to 6 pm as well as borrowing and renewing books study room reservations "
                    "printing wifi computers databases events and general academic support "
                    "Always use simple language keep responses short practical and easy to understand "
                    "If you do not know the answer politely suggest checking the library website or contacting library staff for more help"
                )
            },
            {"role": "user", "content": message},
        ],
        temperature=0.1
    )
    reply = resp.choices[0].message.content
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
