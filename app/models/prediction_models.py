# prediction models 
from pydantic import BaseModel, create_model
from typing import Union, List, Any


# List of columns that are of type string
string_columns = ['x5', 'x12', 'x31', 'x63', 'x81', 'x82']

# Dynamically create the model with string and float fields
fields = {f"x{i}": (float, ...) for i in range(100) if f"x{i}" not in string_columns}
for col in string_columns:
    fields[col] = (str, ...)
    
# Assuming the definition of string_columns and fields here
SingleDataModel = create_model('SingleDataModel', **fields)

class DataModel(BaseModel):
    __root__: Union[SingleDataModel, List[SingleDataModel]]

class PredictionResult(BaseModel):
    predicted_class: int
    probability: float
    variables: Any


class ResponseModel(BaseModel):
    results: List[PredictionResult]

