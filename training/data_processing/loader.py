# trainin data processing loader
import pandas as pd
import logging


def load_data(filepath):
    """
    Load data from a CSV file.

    Args:
        filepath (str): Path to the CSV file.

    Returns:
        DataFrame: Loaded data.
    """
    try:
        df = pd.read_csv(filepath)
        logging.info(f"Data loaded successfully from {filepath}")
        return df
    except Exception as e:
        logging.error(f"Error occurred while loading data from {filepath}: {e}")
        return None
