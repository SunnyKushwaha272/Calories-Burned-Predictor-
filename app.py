import pickle
import streamlit as st
import numpy as np

# Loading the trained model
model_path = r"C:\Users\Rapid IT World\Desktop\New folder\Calories burned Predictor\calories.sav"
loaded_model = pickle.load(open(model_path, 'rb'))

#UI layout
st.set_page_config(page_title="Smart Calorie Burn Predictor", layout="centered")
st.title("🔥 Smart Calorie Burn Predictor")
st.markdown("Predict the number of calories burned based on your workout and physical features using a machine learning model.")

#Sidebar
st.sidebar.header("💡 About This App")
st.sidebar.markdown("""
This app uses a eXtreme  Gradient Boosting model to estimate calories burned during physical activity based on your:
- Age
- Height & Weight
- Duration & Heart Rate
- Body Temperature
""")

# --- Input Form ---
with st.form("calorie_form"):
    st.header("📥 Enter Your Details")

    col1, col2 = st.columns(2)

    with col1:
        gender = st.radio("Gender", ["Male", "Female"])
        age = st.slider("Age", 10, 80, 25)
        height = st.slider("Height (cm)", 100, 220, 170)
        weight = st.slider("Weight (kg)", 30, 120, 65)

    with col2:
        duration = st.slider("Duration (minutes)", 10, 180, 30)
        heart_rate = st.slider("Heart Rate (bpm)", 60, 200, 120)
        body_temp = st.slider("Body Temperature (°C)", 35.0, 40.0, 37.0)

    submit = st.form_submit_button("🚀 Predict Burned Calories")

    if submit:
        gender_value = 1 if gender == "Male" else 0
        input_data = np.array([[gender_value, age, height, weight, duration, heart_rate, body_temp]])
        prediction = loaded_model.predict(input_data)

        st.success(f"🔥 Estimated Calories Burned: **{prediction[0]:.2f} kcal**")
