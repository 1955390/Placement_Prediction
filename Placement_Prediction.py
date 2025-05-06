import streamlit as st
import joblib

# Load the trained model
model = joblib.load('place.pkl')  

def main():
    st.title("Welcome to Placement Predictor")
    
    # User input for CGPA
    cgpa = st.slider("Choose your CGPA", min_value=0.0, max_value=10.0, step=0.1)
    st.write("Entered CGPA:", cgpa)

    # Predict button
    if st.button("Predict"):
        result = model.predict([[cgpa]])[0]  # input should be a 2D list
        st.success(f"Your predicted package would be: {result:.2f} LPA")  # 2 decimal places

# Run the app
if __name__ == '__main__':
    main()
