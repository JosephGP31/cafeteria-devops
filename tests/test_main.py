from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_leer_raiz():
    # 1. Haz una peticion GET a la ruta "/" usando client.get("/")
    response = # Completa aquí
    assert response.status_code == 200


def test_listar_productos():
    # 2. Haz una peticion GET a "/productos/" para comprobar la conexion con PostgreSQL
    response = # Completa aquí
    assert response.status_code == 200
    assert isinstance(response.json(), list)