from fastapi import FastAPI
from pydantic import BaseModel

from backend.agent import query_engine
app = FastAPI(title="AI Database Assistant")


class Question(BaseModel):
    question: str


@app.get("/")
def home():
    return {"message": "AI Database Assistant Running 🚀"}


@app.post("/chat")
def chat(data: Question):
    q = data.question.lower()

    try:
        if "show all" in q:
            result = query_engine.query("SELECT * FROM employees")
            return {
                "question": data.question,
                "answer": str(result)
            }

        if "how many" in q:
            result = query_engine.query("SELECT COUNT(*) FROM employees")
            return {
                "question": data.question,
                "answer": f"Total employees: {result}"
            }

        if "highest salary" in q:
            result = query_engine.query("""
                SELECT name, salary 
                FROM employees 
                ORDER BY salary DESC 
                LIMIT 1
            """)
            return {
                "question": data.question,
                "answer": str(result)
            }

        return {
            "question": data.question,
            "answer": "Try: show all employees / how many employees"
        }

    except Exception as e:
        return {
            "question": data.question,
            "error": str(e)
        }