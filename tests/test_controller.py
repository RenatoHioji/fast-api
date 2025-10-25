from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_get_all_students_success():
    response = client.get("/students")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_student_by_id_success():
    response = client.get("/students/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_get_student_by_id_not_found():
    response = client.get("/students/999")
    assert response.status_code == 404


def test_create_student_success():
    response = client.post(
        "/students",
        json={
            "name": "Leticia Sayuri Okamoto Imasato",
            "email": "lesyimasato@fatec.sp.gov.br",
        },
    )
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Leticia Sayuri Okamoto Imasato"


def test_create_student_invalid_email():
    response = client.post(
        "/students",
        json={"name": "incorrect", "email": "incorrect"},
    )
    assert response.status_code == 422
