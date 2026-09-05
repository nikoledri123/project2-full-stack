from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from FastAPI"}


def test_get_items():
    response = client.get("/items")
    assert response.status_code == 200
    assert response.json() == ["Docker", "FastAPI", "Python"]


def test_add_item():
    response = client.post("/items/Java")
    assert response.status_code == 200
    assert response.json()["message"] == "Java added"
    assert "Java" in response.json()["items"]