# training data processing preprocessor
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import logging


def create_dummy_variables(df, columns):
    """
    Create dummy variables for specified categorical columns.

    Args:
        df (DataFrame): The DataFrame.
        columns (list): List of columns to create dummies for.

    Returns:
        DataFrame: DataFrame with dummy variables.
    """
    try:
        df_with_dummies = df.copy()
        for column in columns:
            if column in df_with_dummies.columns:
                dummies = pd.get_dummies(df_with_dummies[column], prefix=column, dummy_na=True)
                df_with_dummies = pd.concat([df_with_dummies, dummies], axis=1)
                df_with_dummies.drop(column, axis=1, inplace=True)
            else:
                logging.warning(f"Column '{column}' not found in DataFrame")

        return df_with_dummies
    except Exception as e:
        logging.error(f"Error occurred during creating dummy variables: {e}")
        return None

def preprocess_data(df, imputer, scaler, is_training=True):
    """
    Preprocess the data: impute missing values and standardize.

    Args:
        df (DataFrame): The DataFrame to preprocess.
        imputer (SimpleImputer): The imputer object.
        scaler (StandardScaler): The scaler object.
        is_training (bool): Flag to indicate if it's training data.

    Returns:
        DataFrame: Preprocessed DataFrame.
    """
    try:
        columns_for_imputation = [col for col in df.columns if col not in ['y', 'x5', 'x31', 'x81', 'x82']]
        df_imputed = df[columns_for_imputation]

        if is_training:
            df_imputed = pd.DataFrame(imputer.fit_transform(df_imputed), columns=df_imputed.columns)
            df_imputed = pd.DataFrame(scaler.fit_transform(df_imputed), columns=df_imputed.columns)
        else:
            df_imputed = pd.DataFrame(imputer.transform(df_imputed), columns=df_imputed.columns)
            df_imputed = pd.DataFrame(scaler.transform(df_imputed), columns=df_imputed.columns)

        return df_imputed
    except Exception as e:
        logging.error(f"Error occurred during data preprocessing: {e}")
        return None


def split_data(df, target_column, test_size=0.1, random_state=13):
    """
    Split the data into training and validation sets.

    Args:
        df (DataFrame): The DataFrame to split.
        target_column (str): The name of the target column.
        test_size (float): The proportion of the dataset to include in the test split.
        random_state (int): The seed used by the random number generator.

    Returns:
        tuple: Split DataFrames.
    """
    try:
        X = df.drop(columns=[target_column])
        y = df[target_column]
        X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=test_size, random_state=random_state)
        return X_train, X_val, y_train, y_val
    except Exception as e:
        logging.error(f"Error occurred during data splitting: {e}")
        return None, None, None, None




