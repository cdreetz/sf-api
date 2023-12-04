# model loader service
import joblib
import logging
from config.settings import settings

def load_model():
    try:
        model_path = settings.model_path
        print(f"model path = {model_path}")
        return joblib.load(model_path)
    except Exception as e:
        logging.error(f"Error loading model from {model_path}: {e}")
        return None

def load_imputer():
    try:
        imputer_path = settings.imputer_path
        return joblib.load(imputer_path)
    except Exception as e:
        logging.error(f"Error loading imputer from {imputer_path}: {e}")
        return None
