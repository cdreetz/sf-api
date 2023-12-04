# config settings
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    model_path: str = r"pickles/tempmodel.pkl"
    #imputer_path: str = "path/to/imputer.pkl"
    scaler_path: str = r"pickles/tempscaler.pkl"
    model_variables_path: str = r"pickles/tempmodel_variables.pkl"

    class Config:
        env_file = ".env"
        protected_namespaces = ('settings_',)

settings = Settings()
