# entry point for FastAPI app
from fastapi import FastAPI
import uvicorn
from app.routes.prediction import router as prediction_router
from app.routes.heartbeat import heartbeat

app = FastAPI()

# Include the router for prediction
app.include_router(prediction_router)
app.include_router(heartbeat)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=1313)


