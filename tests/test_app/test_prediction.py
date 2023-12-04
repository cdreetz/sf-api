# tests test app test prediction
import requests
import time
import pandas as pd
import numpy as np
from config.settings import settings

model = settings.model_path
scaler = settings.scaler_path
model_variables = settings.model_variables_path

# URL of your FastAPI application
API_URL = "http://34.135.31.176:1313/predict"

def make_single_call(row):
    """
    Make a single API call with one row of data.
    """
    # Directly send the row as JSON
    req = row.to_dict()
    print(req)
    response = requests.post(API_URL, json=row.to_dict())
    return response.json()

def make_batch_call(data):
    """
    Make a batch API call with multiple rows of data.
    """
    # Send the data as a list of dictionaries
    batch_data = data.to_dict(orient='records')
    response = requests.post(API_URL, json=batch_data)
    return response.json()



def format_data_for_json(data):
    """
    Format the data to be JSON compliant.
    """
    # Convert infinity and NaN values
    data = data.replace([np.inf, -np.inf], np.nan)

    # Fill NaN values with a default number, e.g., 0 or an appropriate value for your context
    data = data.fillna(0)
    string_columns = ['x5', 'x12', 'x31', 'x63', 'x81', 'x82']


    # Ensure all floats are rounded to a fixed number of decimal places
    if isinstance(data, pd.DataFrame):
        for col in data.select_dtypes(include=['float64', 'float32']):
            data[col] = data[col].apply(lambda x: round(x, 4))
        for col in string_columns:
            data[col] = data[col]. replace(0, '')
    elif isinstance(data, pd.Series):
        if data.dtype in ['float64', 'float32']:
            data = data.apply(lambda x: round(x, 4))
        if data.name in string_columns:
            data = data.replace(0, '')

    return data


def main():
    # Load data from CSV
    df = pd.read_csv("exercise_26_test.csv")

    # Test single API call with the first row of the DataFrame
    start_time = time.time()
    single_call_result = make_single_call(format_data_for_json(df.iloc[0]))
    end_time = time.time()
    print("Single Call Result:", single_call_result)
    print("Single Call Time:", end_time - start_time)

    # Test batch API call with the first 10 rows of the DataFrame
    start_time = time.time()
    batch_call_result = make_batch_call(format_data_for_json(df.head(10)))
    end_time = time.time()
    print("Batch Call Result:", batch_call_result)
    print("Batch Call Time:", end_time - start_time)

    # Test scalability by gradually increasing the batch size
    for i in range(100, len(df), 100):  # Adjust the range as needed
        start_time = time.time()
        batch_call_result = make_batch_call(format_data_for_json(df.head(i)))
        end_time = time.time()
        print(f"Batch Call Time for {i} rows:", end_time - start_time)

if __name__ == "__main__":
    main()