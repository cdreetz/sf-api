# prediction API endpoint
from fastapi import APIRouter, HTTPException
from app.models.prediction_models import SingleDataModel, ResponseModel, PredictionResult
from app.services.data_preparation import prepare_data
from app.services.model_loader import load_model
import logging
from typing import List, Union

router = APIRouter()
model = load_model()


@router.post("/predict", response_model=ResponseModel)
async def predict(data: Union[SingleDataModel, List[SingleDataModel]]):

    try:
        logging.info("Data received")
        if isinstance(data, SingleDataModel):
            data = [data]

        prepared_data = prepare_data(data)


        if prepared_data.empty:
            logging.error("Data preparation failed, empty DataFrame returned.")
            raise HTTPException(status_code=400, detail="Data preparation failed.")

        probabilities = model.predict(prepared_data)
        predictions = (probabilities >= 0.5).astype(int)

        response = ResponseModel(results=[
            PredictionResult(
                predicted_class=int(pred), 
                probability=float(prob), 
                variables=row)
            for prob, row, pred in zip(probabilities.values, prepared_data.to_dict('records'), predictions.values)
        ])
        return response

    except Exception as e:
        logging.error(f"Error during prediction: {e}")
        raise HTTPException(status_code=500, detail=str(e))
