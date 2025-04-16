import requests

import os
API_URL = os.getenv("API_URL", "http://api:8000")  # Asegúrate que main.py esté corriendo

class Question:
    def __init__(self, id, description, options):
        self.id = id
        self.description = description
        self.options = options

class Quiz:
    def __init__(self, player):
        self.player = player
        self.questions = []
        self.current_question_index = 0
        self.correct_answers = 0
        self.incorrect_answers = 0

    def add_question(self, question):
        self.questions.append(question)

    def get_next_question(self):
        if self.current_question_index < len(self.questions):
            question = self.questions[self.current_question_index]
            self.current_question_index += 1
            return question
        return None

    def enviar_respuesta(self, question_id, selected_answer):
        payload = {
            "player": self.player,
            "question_id": question_id,
            "answer": selected_answer
        }
        try:
            response = requests.post(f"{API_URL}/submit", json=payload)
            result = response.json()
            return result["correct"], result["message"]
        except Exception as e:
            print("Error al enviar respuesta:", e)
            return False, "No se pudo verificar la respuesta."

def cargar_preguntas_por_nivel(nivel):
    preguntas = []
    niveles_api = {
        "1": "facil",
        "2": "intermedio",
        "3": "dificil"
    }

    try:
        response = requests.get(f"{API_URL}/questions/{niveles_api[nivel]}")
        response.raise_for_status()
        data = response.json()

        for item in data:
            preguntas.append(Question(item["id"], item["description"], item["options"]))
    except Exception as e:
        print("Error al cargar preguntas desde la API:", e)

    return preguntas

def run_quiz():
    print("=== Bienvenido al Quiz de Tecnología ===")
    player = input("Ingresa tu nombre: ").strip()

    print("Selecciona el nivel:")
    print("1. Redes (Fácil)")
    print("2. Ciberseguridad (Intermedio)")
    print("3. Computación Cuántica (Difícil)")

    while True:
        nivel = input("Nivel (1/2/3): ").strip()
        if nivel in ["1", "2", "3"]:
            break
        print("Nivel inválido. Intenta otra vez.")

    quiz = Quiz(player)
    preguntas_nivel = cargar_preguntas_por_nivel(nivel)

    for pregunta in preguntas_nivel:
        quiz.add_question(pregunta)

    total_questions = len(quiz.questions)

    for _ in range(total_questions):
        question = quiz.get_next_question()
        print(f"\n{question.description}")
        for idx, option in enumerate(question.options):
            print(f"{idx + 1}. {option}")

        while True:
            answer = input("Tu respuesta: ").strip()
            if not answer.isdigit():
                print("Entrada inválida. Ingresa un número.")
                continue
            selected_index = int(answer) - 1
            if selected_index < 0 or selected_index >= len(question.options):
                print("Opción fuera de rango. Intenta otra vez.")
                continue
            selected_option = question.options[selected_index]
            break

        correcto, mensaje = quiz.enviar_respuesta(question.id, selected_option)
        print(mensaje)

        if correcto:
            quiz.correct_answers += 1
        else:
            quiz.incorrect_answers += 1

    print("\n=== Resultados ===")
    print(f"Jugador: {quiz.player}")
    print(f"Correctas: {quiz.correct_answers}")
    print(f"Incorrectas: {quiz.incorrect_answers}")
    print(f"Puntaje final: {quiz.correct_answers}/{total_questions}")


if __name__ == "__main__":
    run_quiz()


