from locust import HttpUser, task, between
import random

NIVELES = ["facil", "intermedio", "dificil"]
RESPUESTAS_FALSAS = ["Incorrecta", "Random", "Otra", "Error"]

class TriviaUser(HttpUser):
    wait_time = between(1, 3)  # Simula tiempo de espera entre acciones (1 a 3 segundos)

    @task
    def jugar_trivia(self):
        # 1. Obtener preguntas de un nivel aleatorio
        nivel = random.choice(NIVELES)
        response = self.client.get(f"/questions/{nivel}")

        if response.status_code == 200 and response.json():
            preguntas = response.json()
            pregunta = random.choice(preguntas)  # Elige una al azar

            # 2. Simula enviar una respuesta (incorrecta o al azar)
            payload = {
                "player": "LocustBot",
                "question_id": pregunta["id"],
                "answer": random.choice(RESPUESTAS_FALSAS)
            }

            self.client.post("/submit", json=payload)
