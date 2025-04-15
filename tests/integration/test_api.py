from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_questions_by_level():
    response = client.get("/questions/facil")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    assert "description" in data[0]

def test_submit_correct_answer():
    response = client.post("/submit", json={
        "player": "Tester",
        "question_id": 1,
        "answer": "Router"
    })
    assert response.status_code == 200
    result = response.json()
    assert result["correct"] is True
    assert "¡Correcto!" in result["message"]
