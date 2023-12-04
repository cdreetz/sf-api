import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models.prediction_models import SingleDataModel
import unittest
import json

client = TestClient(app)

def test_predict():
    # Load test data
    with open('tests/test_json/test_data.json') as f:
        data = json.load(f)

    # Make request and get response
    response = client.post("/predict", json=data)

    # Check response status code
    assert response.status_code == 200

    # Check response data
    assert "results" in response.json()
    assert isinstance(response.json()["results"], list)

class TestPredictionAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_predict_valid_single_data(self):
        # Test with valid single data input
        with open('tests/test_json/test_data.json') as f:
            data = json.load(f)
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_predict_valid_multiple_data(self):
        # Test with valid multiple data input
        with open('tests/test_json/test_data.json') as f:
            data = json.load(f)
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_predict_invalid_data(self):
        # Test with invalid data
        data = {"x0": 1}
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 422)  # HTTP 422 for validation error

    def test_predict_empty_data(self):
        # Test with empty data
        data = {}
        response = self.client.post("/predict", json=data)
        self.assertEqual(response.status_code, 422)  # HTTP 422 for validation error

    # Additional tests can be added for other scenarios like server errors, etc.

if __name__ == '__main__':
    unittest.main()