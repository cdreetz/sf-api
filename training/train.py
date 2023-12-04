# main training script
from data_processing.loader import load_data
from data_processing.cleaner import clean_and_format_data
from data_processing.preprocessing import preprocess_data, split_data
from models.logistic_regression import train_model
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
import joblib
import logging

def main():
    try:
        # Load data
        train_data = load_data('path/to/training/data.csv')
        test_data = load_data('path/to/test/data.csv')

        # Clean and format data
        train_data = clean_and_format_data(train_data)
        test_data = clean_and_format_data(test_data)

        # Split data into training and validation sets
        X_train, X_val, y_train, y_val = split_data(train_data, 'target_column')

        # Preprocess training data
        imputer = SimpleImputer(strategy='mean')
        scaler = StandardScaler()
        X_train_processed = preprocess_data(X_train, imputer, scaler, is_training=True)

        # Train the model
        model = train_model(X_train_processed, y_train)

        # Save the model
        joblib.dump(model, 'model.pkl')
    except Exception as e:
        logging.error(f"Error in the main training pipeline: {e}")

if __name__ == "__main__":
    main()
