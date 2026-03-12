import streamlit as st
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("AI Disease Prediction System")

st.write("Select Symptoms (0 = No, 1 = Yes)")

# Symptom inputs
fever = st.selectbox("Fever", [0,1])
headache = st.selectbox("Headache", [0,1])
cough = st.selectbox("Cough", [0,1])
vomiting = st.selectbox("Vomiting", [0,1])
fatigue = st.selectbox("Fatigue", [0,1])

# Doctor recommendation
doctor_map = {
    "Typhoid": "Infectious Disease Specialist",
    "Common Cold": "General Physician",
    "Migraine": "Neurologist",
    "Allergy": "Allergist",
    "Fungal infection": "Dermatologist",
    "GERD": "Gastroenterologist",
    "Diabetes": "Endocrinologist",
    "Hypertension": "Cardiologist"
}

# Precautions
precautions_map = {
    "Typhoid": "Drink clean water, maintain hygiene, take antibiotics prescribed by doctor",
    "Common Cold": "Drink warm fluids and take proper rest",
    "Migraine": "Rest in a quiet dark room and avoid stress",
    "Allergy": "Avoid allergens and take antihistamines",
    "Fungal infection": "Keep skin dry and maintain good hygiene",
    "GERD": "Avoid spicy food and eat small meals",
    "Diabetes": "Maintain healthy diet and monitor sugar levels",
    "Hypertension": "Reduce salt intake and exercise regularly"
}

# Prediction
if st.button("Predict Disease"):

    input_data = [fever, headache, cough, vomiting, fatigue]

    prediction = model.predict([input_data])

    disease = prediction[0]

    doctor = doctor_map.get(disease, "General Physician")

    precaution = precautions_map.get(disease, "Consult doctor for proper advice")

    st.success("Predicted Disease: " + disease)
    st.write("👨‍⚕️ Consultant Doctor:", doctor)
    st.write("⚠️ Precautions:", precaution)