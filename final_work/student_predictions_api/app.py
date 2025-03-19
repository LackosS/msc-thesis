from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import joblib
import numpy as np
import os
from typing import List
from sklearn.svm import SVR

app = FastAPI()

STACKED_SVM_MODEL_PATH = "stacked_svm.pkl"

if os.path.exists(STACKED_SVM_MODEL_PATH):
    model_svm_six = joblib.load(STACKED_SVM_MODEL_PATH)
else:
    raise Exception(f"SVM model file '{STACKED_SVM_MODEL_PATH}' not found.")

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
    group: int
    day: int
    start_hour: int
    first_zh: float
    second_zh: float
    third_zh: float
    fourth_zh: float
    fifth_zh: float
    sixth_zh: float
    assignment: float

class StudentsList(BaseModel):
    students: List[StudentData]

class PredictionResponse(BaseModel):
    svm_stacked_prediction: float
    svm_stacked_classification_performance_tiered: str
    svm_stacked_classification_subject_based: str
    svm_stacked_classification_buffer_zone: str

class PredictionsListResponse(BaseModel):
    predictions: List[PredictionResponse]

@app.post("/predict", response_model=PredictionsListResponse)
def predict_grades(input_data: StudentsList):
    try:
        results = []

        for student in input_data.students:
            input_array = np.array([
                student.group, student.day, student.start_hour,
                student.first_zh, student.second_zh, student.third_zh,
                student.fourth_zh, student.fifth_zh, student.sixth_zh,
                student.assignment
            ]).reshape(1, -1)

            svm_prediction = np.round(model_svm_six.predict(input_array)[0], 2)
            svm_classification_performance_tiered = classify_grade_performance(svm_prediction)
            svm_classification_subject_based = classify_grade_subject(svm_prediction)
            svm_classification_buffer_zone = classify_grade_buffer(svm_prediction)

            results.append(PredictionResponse(
                svm_stacked_prediction=svm_prediction,
                svm_stacked_classification_performance_tiered=svm_classification_performance_tiered,
                svm_stacked_classification_subject_based = svm_classification_subject_based,
                svm_stacked_classification_buffer_zone = svm_classification_buffer_zone,
            ))

        return PredictionsListResponse(predictions=results)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def home():
    return {"message": "API is running"}