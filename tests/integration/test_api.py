from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Prueba: Crear una pregunta
def test_create_question():
    response = client.post("/questions/", json={
        "description": "What is 2 + 2?",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "4"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["description"] == "What is 2 + 2?"
    assert data["correct_answer"] == "4"
    assert "id" in data  # La respuesta debería incluir un ID

# Prueba: Obtener todas las preguntas
def test_get_all_questions():
    response = client.get("/questions/")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

# Prueba: Obtener una pregunta específica (usamos ID 1 como ejemplo)
def test_get_question_by_id():
    # Creamos una nueva pregunta primero
    post_response = client.post("/questions/", json={
        "description": "What is the capital of Peru?",
        "options": ["Lima", "Cusco", "Arequipa", "Trujillo"],
        "correct_answer": "Lima"
    })
    question_id = post_response.json()["id"]

    # Ahora la buscamos
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200
    assert response.json()["description"] == "What is the capital of Peru?"

# Prueba: Actualizar una pregunta
def test_update_question():
    # Crear primero
    post_response = client.post("/questions/", json={
        "description": "Test question",
        "options": ["A", "B", "C", "D"],
        "correct_answer": "A"
    })
    question_id = post_response.json()["id"]

    # Actualizar
    update_response = client.put(f"/questions/{question_id}", json={
        "description": "Updated question",
        "options": ["X", "Y", "Z", "W"],
        "correct_answer": "Z"
    })
    assert update_response.status_code == 200
    assert update_response.json()["description"] == "Updated question"

# Prueba: Eliminar una pregunta
def test_delete_question():
    # Crear primero
    post_response = client.post("/questions/", json={
        "description": "To be deleted",
        "options": ["1", "2", "3", "4"],
        "correct_answer": "1"
    })
    question_id = post_response.json()["id"]

    # Eliminar
    delete_response = client.delete(f"/questions/{question_id}")
    assert delete_response.status_code == 204

    # Verificar que ya no existe
    get_response = client.get(f"/questions/{question_id}")
    assert get_response.status_code == 404
