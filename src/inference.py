from joblib import load
import pandas as pd
import numpy as np
from config import CONFIG

scaler = load(str(CONFIG.models / "scaler.joblib"))
model = load(str(CONFIG.models / "model.joblib"))


pregnancies = 2
glucose = 13
bloodpressure = 30
skinthickness = 4
insulin = 5
bmi = 5
dpf = 0.55
age = 34

feat_cols = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI", "DiabetesPedigreeFunction", "Age"]
row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]
df = pd.DataFrame([row], columns=feat_cols)
X = scaler.transform(df)
features = pd.DataFrame(X, columns=feat_cols)
if (model.predict(features) == 0):
    print("This is a healthy person!")
else:
    print("This person has high chances of having diabetes")