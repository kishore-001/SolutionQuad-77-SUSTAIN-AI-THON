from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load model and scaler at the global level (not inside the endpoint function)
model = joblib.load('./Model/random_forest_model.pkl')  # Assuming you've saved your model
scaler = joblib.load('./Model/scaler.pkl')  # Assuming you've saved your scaler

# Create a Pydantic model for request validation
class PredictRequest(BaseModel):
    temperature: float
    humidity: float
    ph: float

# Define the router
router = APIRouter()

@router.post("/predict")
def predict(request: PredictRequest):
        # Get input features from the request
        features = np.array([request.temperature, request.humidity, request.ph]).reshape(1, -1)

        # Scale the input features
        scaled_features = scaler.transform(features)

        # Predict the crop using the trained model
        prediction = model.predict(scaled_features)

        # Return the prediction result
        return {"crop": prediction[0]}

