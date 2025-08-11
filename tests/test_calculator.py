from fastapi.testclient import TestClient
from calculator import app

client = TestClient(app)

def test_addition():
    """
    Testing Addition.
    """
    response = client.post("/calculate/add", json={"x": 5, "y": 3})
    assert response.status_code == 200
    assert "Using the operation (add)" in response.json()["message"]

def test_subtraction():
    """
    Testing Subtraction.
    """    
    response = client.post("/calculate/subtract", json={"x": 10, "y": 4})
    assert response.status_code == 200
    assert "Using the operation (subtract)" in response.json()["message"]

def test_multiply():
    """
    Testing Multiplication.
    """
    response = client.post("/calculate/multiply", json={"x": 10, "y": 4})
    assert response.status_code == 200
    assert "Using the operation (multiply)" in response.json()["message"]

def test_divide():
    """
    Testing Division.
    """
    response = client.post("/calculate/divide", json={"x": 12, "y": 4})
    assert response.status_code == 200
    assert "Using the operation (divide)" in response.json()["message"]

def test_divide_by_zero(): 
    """
    Testing Divide by zero.
    """
    response = client.post("/calculate/divide", json={"x": 10, "y": 0})
    assert response.status_code == 400

def test_exponent():
    """
    Testing Exponent.
    """
    response = client.post("/calculate/exponent", json={"x": 10, "y": 4})
    assert response.status_code == 200
    assert "Using the operation (exponent)" in response.json()["message"]

def test_modulus():
    """
    Testing Modulus.
    """
    response = client.post("/calculate/modulus", json={"x": 10, "y": 4})
    assert response.status_code == 200
    assert "Using the operation (modulus)" in response.json()["message"]

def test_invalid_operation():
    """
    Testing Invalid Operation.
    """
    response = client.post("/calculate/invalidop", json={"x": 1, "y": 2})
    assert response.status_code == 400
    assert "error" in response.json()
