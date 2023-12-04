# training models log regression
from sklearn.linear_model import LogisticRegression
import logging

def train_model(X_train, y_train):
    """
    Train the logistic regression model.

    Args:
        X_train (DataFrame): Training feature set.
        y_train (Series): Training target.

    Returns:
        model: Trained model.
    """
    try:
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        return model
    except Exception as e:
        logging.error(f"Error occurred during model training: {e}")
        return None