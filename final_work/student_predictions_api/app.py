from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os
from typing import List
import pandas as pd

app = FastAPI()

BAGGED_RF_MODEL_PATH = "bagged_rf.pkl"

if os.path.exists(BAGGED_RF_MODEL_PATH):
    model_bagged_rf_six = joblib.load(BAGGED_RF_MODEL_PATH)
else:
    raise Exception(f"Bagged RF model file '{BAGGED_RF_MODEL_PATH}' not found.")

def classify_grade_subject(score, max_score=50, interval=15):
    excellent_threshold = max_score * 0.85  # 42.5
    good_threshold = max_score * 0.7        # 35
    medium_threshold = max_score * 0.55     # 27.5
    sufficient_threshold = max_score * 0.4  # 20

    if score > excellent_threshold:
        return "EXCELLENT"
    elif good_threshold < score <= excellent_threshold:
        return "GOOD"
    elif medium_threshold < score <= good_threshold:
        return "MEDIUM"
    elif sufficient_threshold < score <= medium_threshold:
        return "SUFFICIENT"
    else:
        return "FAIL"

def classify_grade_performance(score, max_score=50):
    high_threshold = max_score * 0.6  # Top 60% and above
    medium_threshold = max_score * 0.4  # Middle 30-60%

    if score >= high_threshold:
        return "HIGH"
    elif score >= medium_threshold:
        return "MEDIUM"
    else:
        return "LOW"
    
def classify_grade_buffer(score, max_score=50, interval=15, buffer=0.06):
    # Define grade thresholds
    excellent_threshold = max_score * 0.85
    good_threshold = max_score * 0.7
    medium_threshold = max_score * 0.55
    sufficient_threshold = max_score * 0.4

    buffer_zone = max_score * buffer

    # Apply grading logic with buffer zones
    if score > excellent_threshold or (excellent_threshold - buffer_zone) <= score:
        return "EXCELLENT"
    elif good_threshold < score <= excellent_threshold or (good_threshold - buffer_zone) <= score < excellent_threshold:
        return "GOOD"
    elif medium_threshold < score <= good_threshold or (medium_threshold - buffer_zone) <= score < good_threshold:
        return "MEDIUM"
    elif sufficient_threshold < score <= medium_threshold or (sufficient_threshold - buffer_zone) <= score < medium_threshold:
        return "SUFFICIENT"
    else:
        return "FAIL"
    
class StudentData(BaseModel):
    Group: int
    First_Weekly_Exam: float
    Second_Weekly_Exam: float
    Third_Weekly_Exam: float
    Fourth_Weekly_Exam: float
    Fifth_Weekly_Exam: float
    Sixth_Weekly_Exam: float
    Assignment: float
    Day: int
    Start_Hour: int

class StudentsList(BaseModel):
    students: List[StudentData]

class PredictionResponse(BaseModel):
    bagged_rf_prediction: float
    bagged_rf_classification_performance_tiered: str
    bagged_rf_classification_subject_based: str
    bagged_rf_classification_buffer_zone: str

class PredictionsListResponse(BaseModel):
    predictions: List[PredictionResponse]

@app.post("/predict", response_model=PredictionsListResponse)
def predict_grades(input_data: StudentsList):
    try:
        results = []

        for student in input_data.students:
            input_df = pd.DataFrame([student.dict()])

            bagged_rf_prediction = np.round(model_bagged_rf_six.predict(input_df)[0], 2)
            bagged_rf_classification_performance_tiered = classify_grade_performance(bagged_rf_prediction)
            bagged_rf_classification_subject_based = classify_grade_subject(bagged_rf_prediction)
            bagged_rf_classification_buffer_zone = classify_grade_buffer(bagged_rf_prediction)

            results.append(PredictionResponse(
                bagged_rf_prediction=bagged_rf_prediction,
                bagged_rf_classification_performance_tiered=bagged_rf_classification_performance_tiered,
                bagged_rf_classification_subject_based = bagged_rf_classification_subject_based,
                bagged_rf_classification_buffer_zone = bagged_rf_classification_buffer_zone,
            ))

        return PredictionsListResponse(predictions=results)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "API is running"}