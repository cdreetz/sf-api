# training data processing cleaner
import pandas as pd
import logging


def clean_and_format_data(df):
    """
    Clean and format the data.

    Args:
        df (DataFrame): The DataFrame to clean.

    Returns:
        DataFrame: Cleaned and formatted DataFrame.
    """
    try:
        df_cleaned = df.copy()

        # Cleaning and formatting monetary fields (example: 'x12')
        if 'x12' in df_cleaned.columns:
            df_cleaned['x12'] = df_cleaned['x12'].str.replace('[\$\,]', '', regex=True)
            df_cleaned['x12'] = df_cleaned['x12'].str.replace('\(', '-', regex=True).str.replace('\)', '', regex=True)
            df_cleaned['x12'] = df_cleaned['x12'].astype(float)

        # Cleaning and formatting percentage fields (example: 'x63')
        if 'x63' in df_cleaned.columns:
            df_cleaned['x63'] = df_cleaned['x63'].str.replace('%', '').astype(float)

        return df_cleaned
    except Exception as e:
        logging.error(f"Error occured while cleaning data: {e}")
        return None
