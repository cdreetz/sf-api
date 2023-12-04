# data preperation service
import pandas as pd
import joblib
import logging
from training.data_processing.cleaner import clean_and_format_data
from training.data_processing.preprocessing import create_dummy_variables, preprocess_data
from config.settings import settings

scaler_path = settings.scaler_path
model_variables_path = settings.model_variables_path

def prepare_data(input_data, scaler_path=scaler_path, model_variables_path=model_variables_path):
    """
    Prepare the data for prediction.

    Args:
        input_data (Union[SingleDataModel, List[SingleDataModel]]): The input data received from the API call.
        scaler_path (str): Path to the scaler pickle file.
        model_variables_path (str): Path to the model variables pickle file.

    Returns:
        DataFrame: Preprocessed data ready for prediction.
    """
    try:
        # Convert input data to DataFrame
        if isinstance(input_data, list):
            df = pd.DataFrame([item.dict() for item in input_data])
        else:
            df = pd.DataFrame([input_data.dict()])

        # Clean and format data
        try:
            df_cleaned = clean_and_format_data(df)
        except Exception as e:
            logging.error(f"Error during cleaning and formatting data: {e}")
            return pd.DataFrame()

        # Load the scaler
        try:
            scaler_path = settings.scaler_path
            scaler = joblib.load(scaler_path)
        except Exception as e:
            logging.error(f"Error loading scaler from {scaler_path}: {e}")
            return pd.DataFrame()

        # Load model variables
        try:
            model_variables_path = settings.model_variables_path
            model_variables = joblib.load(model_variables_path)
        except Exception as e:
            logging.error(f"Error loading model variables from {model_variables_path}: {e}")
            return pd.DataFrame()

        # Apply scaling
        try:
            training_columns = scaler.feature_names_in_
            columns_to_scale = [col for col in training_columns if col in df_cleaned.columns]
            df_cleaned[columns_to_scale] = scaler.transform(df_cleaned[columns_to_scale])
        except Exception as e:
            logging.error(f"Error during scaling: {e}")
            return pd.DataFrame()

        # Create dummy variables
        try:
            categorical_columns = ['x5', 'x31', 'x81', 'x82']
            df_with_dummies = create_dummy_variables(df_cleaned, categorical_columns)
        except Exception as e:
            logging.error(f"Error during dummy variable creation: {e}")
            return pd.DataFrame()

        # Add missing dummy columns and select model variables
        try:
            for variable in model_variables:
                if variable not in df_with_dummies.columns:
                    df_with_dummies[variable] = 0
            df_final = df_with_dummies[model_variables]
        except Exception as e:
            logging.error(f"Error during final data preparation: {e}")
            return pd.DataFrame()

        return df_final
    except Exception as e:
        logging.error(f"General error in data preparation: {e}")
        return pd.DataFrame()




def add_missing_dummy_columns(df, model_columns):
    missing_cols = set(model_columns) - set(df.columns)
    for c in missing_cols:
        df[c] = 0
    return df[model_columns]
