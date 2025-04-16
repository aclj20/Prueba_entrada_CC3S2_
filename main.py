from sqlalchemy.orm import Session
from fastapi import Depends
from database import SessionLocal
from models import Question as DBQuestion
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import json  # ← necesario para decodificar opciones

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
# Modelo para recibir respuestas del jugador
class AnswerSubmission(BaseModel):
    player: str
    question_id: int
    answer: str

# Obtener preguntas por nivel
@app.get("/questions/{nivel}")
def get_questions_by_level(nivel: str, db: Session = Depends(get_db)):
    nivel = nivel.lower()
    results = db.query(DBQuestion).filter(DBQuestion.nivel == nivel).all()
    return [
        {
            "id": q.id,
            "description": q.description,
            "options": json.loads(q.options)  # ← aquí se decodifica el string JSON
        } for q in results
    ]

# Evaluar la respuesta del jugador
@app.post("/submit")
def submit_answer(data: AnswerSubmission, db: Session = Depends(get_db)):
    question = db.query(DBQuestion).filter(DBQuestion.id == data.question_id).first()

    if not question:
        return {"message": "Pregunta no encontrada", "correct": False}

    is_correct = data.answer.strip().lower() == question.correct_answer.strip().lower()

    return {
        "player": data.player,
        "correct": is_correct,
        "message": "¡Correcto!" if is_correct else f"Incorrecto. La respuesta correcta era: {question.correct_answer}"
    }
