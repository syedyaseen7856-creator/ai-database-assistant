🤖 AI Database Assistant

An intelligent Natural Language to SQL system that allows users to query a database using simple English. Built using FastAPI (backend) and Streamlit (frontend) with an AI-powered query engine.

🚀 Demo

User types natural language like:

Show all employees
How many employees are there?
Who has the highest salary?

System converts it into SQL → executes on database → returns results instantly.

🏗️ Architecture
User
  ↓
Streamlit Frontend (UI)
  ↓
FastAPI Backend (/chat API)
  ↓
AI Query Engine (SQL Generator / Logic)
  ↓
SQLite Database
  ↓
Response back to UI
✨ Features
🧠 Natural Language to SQL conversion
📊 Employee data querying
⚡ FastAPI backend (high performance API)
🎨 Streamlit interactive UI
🗄️ SQLite database integration
🔍 Smart query handling:
Show all employees
Count employees
Highest salary employee
🧰 Tech Stack
Python 🐍
FastAPI ⚡
Streamlit 🎨
SQLite 🗄️
Requests 🌐
Pydantic 📦
📁 Project Structure
AI Database Assistant/
│
├── backend/
│   ├── app.py            # FastAPI backend
│   ├── agent.py         # AI query engine logic
│   ├── db.py            # Database connection
│
├── app.py               # Streamlit frontend
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/syedyaseen7856-creator/ai-database-assistant.git
cd ai-database-assistant
2️⃣ Install dependencies
pip install fastapi uvicorn streamlit requests pydantic
3️⃣ Run FastAPI backend
uvicorn backend.app:app --reload

Backend runs at:

http://127.0.0.1:8000
4️⃣ Run Streamlit frontend
streamlit run app.py

Frontend runs at:

http://localhost:8501
📡 API Endpoint
POST /chat

Request:

{
  "question": "Show all employees"
}

Response:

{
  "question": "Show all employees",
  "answer": "[('John', 50000), ('Alice', 60000)]"
}
💡 Example Queries

Try these in the UI:

Show all employees
How many employees are there?
Who has the highest salary?
List all employee names
🎯 Future Improvements
🔥 ChatGPT-style UI
📊 Graphs & analytics (Plotly)
🧠 LLM-based SQL generation (OpenAI / HuggingFace)
🗂️ Multiple database support (MySQL, PostgreSQL)
🌐 Cloud deployment (Render / Streamlit Cloud)
👨‍💻 Author

sd yaseen

GitHub: https://github.com/syedyaseen7856-creator

⭐ Acknowledgements

Thanks to FastAPI and Streamlit communities for amazing tools that make rapid AI app development possible.