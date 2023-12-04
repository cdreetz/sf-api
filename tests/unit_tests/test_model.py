
import unittest
from pydantic import ValidationError
from app.models.prediction_models import SingleDataModel, PredictionResult, ResponseModel  

class TestModels(unittest.TestCase):

    def test_single_data_model_valid_input(self):
        # Test with valid data
        data = {f"x{i}": 1.0 for i in range(100)}
        for col in ['x5', 'x12', 'x31', 'x63', 'x81', 'x82']:
            data[col] = 'string_value'

        model = SingleDataModel(**data)
        self.assertEqual(model.model_dump(), data)

    def test_single_data_model_invalid_input(self):
        # Test with invalid data
        data = {f"x{i}": 1.0 for i in range(100)}
        data['x5'] = 5  # Invalid, should be a string

        with self.assertRaises(ValidationError):
            SingleDataModel(**data)

    def test_prediction_result(self):
        # Test with valid data
        data = {'predicted_class': 1, 'probability': 0.75, 'variables': {'var1': 1.0}}
        model = PredictionResult(**data)
        self.assertEqual(model.dict(), data)

        # Test with invalid data
        data = {'predicted_class': 'one', 'probability': 1.1}  # Invalid types and values
        with self.assertRaises(ValidationError):
            PredictionResult(**data)

    def test_response_model(self):
        # Test with valid data
        prediction = {'predicted_class': 0, 'probability': 0.85, 'variables': {'var1': 1.0}}
        data = {'results': [prediction]}
        model = ResponseModel(**data)
        self.assertEqual(model.dict(), data)

        # Test with invalid data
        data = {'results': 'not_a_list'}  # Invalid, should be a list
        with self.assertRaises(ValidationError):
            ResponseModel(**data)

if __name__ == '__main__':
    unittest.main()
