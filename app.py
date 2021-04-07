import streamlit as st
import joblib
import pandas as pd
from PIL import Image
from config import CONFIG

# @st.cache(allow_output_mutation=True)

# Add streamlit title, add descriptions and load an attractive iamge
st.title("Diabetes Prediction App")
st.write("""The data for the following example is originally from the National Institute of Diabetes and Digestive 
and Kidney Diseases and contains information on females at least 21 years old of Pima Indian heritage.
This is a sample application and cannot be used as a substitute for real medical device""")
image = Image.open(CONFIG.imgs / "diabetes.jpg")
st.image(image, use_column_width=True)
st.write("""Please fill in the details of the person under consideration in the left
sidebar and click on the button below!""")

def inference(row, scaler, model, fea_cols):
    df = pd.DataFrame([row], columns=feat_cols)
    X = scaler.transform(df)
    features = pd.DataFrame(X, columns=feat_cols)
    if (model.predict(features)==0):
        return "This is a healthy person!"
    else:
        return "This person has high chances of having diabetes!"

age = st.sidebar.number_input("Age in Years", 1, 150, 25, 1)
pregnancies = st.sidebar.number_input("Number of pregnancies", 0, 20, 0, 1)
glucose = st.sidebar.slider("Glucose Level", 0, 200, 25, 1)
skinthickness = st.sidebar.slider("Skin Thickness", 0, 99, 20, 1)
bloodpressure = st.sidebar.slider("Blood Pressure", 0, 122, 69, 1)
insulin = st.sidebar.slider("Insulin", 0, 846, 79, 1)
bmi = st.sidebar.slider("BMI", 0.0, 67.1, 31.4, 0.1)
dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.000, 2.420, 0.471, 0.001)

row = [pregnancies, glucose, bloodpressure, skinthickness, insulin, bmi, dpf, age]

@st.cache(allow_output_mutation=True)
def load(scaler_path, model_path):
    sc = joblib.load(scaler_path)
    model = joblib.load(model_path)
    return sc, model
if (st.button("Find Health Status")):
    feat_cols = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age']
    sc, model = load(str(CONFIG.models / "scaler.joblib"), str(CONFIG.models / "model.joblib"))
    result = inference(row, sc, model, feat_cols)
    st.write(result)


if __name__ == "__main__":
    pass