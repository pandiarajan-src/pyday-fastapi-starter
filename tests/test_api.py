# This test file tests all the requirements in main.py

import random

# Generate test client
from fastapi.testclient import TestClient
from api.main import app

client = TestClient(app)


def test_generate_name():
    response = client.get("/generate_name")
    assert response.status_code == 200
    assert response.json()["name"] in ["Minnie", "Margaret", "Myrtle", "Noa", "Nadia"]


def test_generate_name_max_length():
    random.seed(0)
    response = client.get("/generate_name?max_length=5")
    assert response.status_code == 200
    assert response.json()["name"] in ["Nadia"]


def test_geneate_name_starts_with():
    random.seed(0)
    response = client.get("/generate_name?starts_with=N")
    assert response.status_code == 200
    assert response.json()["name"] in ["Noa", "Nadia"]


def test_generate_name_starts_with_max_length():
    random.seed(0)
    response = client.get("/generate_name?max_length=3&starts_with=N")
    assert response.status_code == 200
    assert response.json()["name"] in ["Noa"]


def test_generate_name_capture_max_length_zero_and_starts_with_noexist_exception():
    random.seed(0)
    response = client.get("/generate_name?max_lenght=0&starts_with=P")
    assert response.status_code == 404


def test_generate_name_capture_max_length_zero_exception():
    random.seed(0)
    response = client.get("/generate_name?max_lenght=0")
    assert response.status_code == 200
