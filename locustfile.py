from locust import HttpUser, task, between
import random

NIVELES = ["facil", "intermedio", "dificil"]
RESPUESTAS_FALSAS = ["Incorrecta", "Random", "Otra", "Error"]

class TriviaUser(HttpUser):
    wait_time = between(1, 3) 

    @task
    def jugar_trivia(self):
        # Obtener preguntas de un nivel aleatorio
        nivel = random.choice(NIVELES)
        response = self.client.get(f"/questions/{nivel}")

        if response.status_code == 200 and response.json():
            preguntas = response.json()
            pregunta = random.choice(preguntas)  

            # Simular enviar una respuesta 
            payload = {
                "player": "LocustBot",
                "question_id": pregunta["id"],
                "answer": random.choice(RESPUESTAS_FALSAS)
            }

            self.client.post("/submit", json=payload)
