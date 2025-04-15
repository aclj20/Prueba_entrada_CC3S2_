from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Preguntas por nivel
questions = [
    # Nivel 1: Redes
    {
        "id": 1,
        "description": "¿Qué dispositivo enruta paquetes entre redes?",
        "options": ["Switch", "Router", "Hub", "Bridge"],
        "correct_answer": "Router",
        "nivel": "facil"
    },
    {
        "id": 2,
        "description": "¿Qué significa IP?",
        "options": ["Internet Protocol", "Internal Path", "Interconnect Port", "Input Protocol"],
        "correct_answer": "Internet Protocol",
        "nivel": "facil"
    },
    # Nivel 2: Ciberseguridad
    {
        "id": 3,
        "description": "¿Qué es un firewall?",
        "options": ["Un virus", "Una red privada", "Un sistema de defensa", "Un protocolo"],
        "correct_answer": "Un sistema de defensa",
        "nivel": "intermedio"
    },
    {
        "id": 4,
        "description": "¿Qué es un ransomware?",
        "options": ["Un antivirus", "Un tipo de ataque que cifra datos", "Un exploit de red", "Un router modificado"],
        "correct_answer": "Un tipo de ataque que cifra datos",
        "nivel": "intermedio"
    },
    # Nivel 3: Computación cuántica
    {
        "id": 5,
        "description": "¿Qué es un qubit?",
        "options": ["Unidad clásica", "Unidad cuántica", "Transistor", "Circuito lógico"],
        "correct_answer": "Unidad cuántica",
        "nivel": "dificil"
    },
    {
        "id": 6,
        "description": "¿Qué permite la superposición?",
        "options": ["Medir bits", "Procesar datos", "Estar en varios estados", "Conectar routers"],
        "correct_answer": "Estar en varios estados",
        "nivel": "dificil"
    }
]

# Modelo para recibir respuestas del jugador
class AnswerSubmission(BaseModel):
    player: str
    question_id: int
    answer: str

# Obtener preguntas por nivel
@app.get("/questions/{nivel}")
def get_questions_by_level(nivel: str):
    nivel = nivel.lower()
    return [
        {
            "id": q["id"],
            "description": q["description"],
            "options": q["options"]
        }
        for q in questions if q["nivel"] == nivel
    ]

# Evaluar la respuesta del jugador
@app.post("/submit")
def submit_answer(data: AnswerSubmission):
    question = next((q for q in questions if q["id"] == data.question_id), None)
    if not question:
        return {"message": "Pregunta no encontrada", "correct": False}

    is_correct = data.answer.strip().lower() == question["correct_answer"].strip().lower()

    return {
        "player": data.player,
        "correct": is_correct,
        "message": "¡Correcto!" if is_correct else f"Incorrecto. La respuesta correcta era: {question['correct_answer']}"
    }