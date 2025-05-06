import streamlit as st
import joblib

# Load the trained model
model = joblib.load('place.pkl')  

def main():
   st.markdown(
    """
    <style>
    .centered-image {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="centered-image"><img src="placement_predict.png" width="300"></div>', unsafe_allow_html=True)
    st.title("Welcome to Placement Predictor")
    st.subheader("Prem Mohan - CGPA and Predicted LPA")
    # User input for CGPA
    cgpa = st.slider("Choose your CGPA", min_value=0.0, max_value=10.0, step=0.1)
    st.write("Entered CGPA:", cgpa)

    # Predict button
    if st.button("Predict"):
        result = model.predict([[cgpa]])[0]  # input should be a 2D list
        try:
            # Ensure result is a numeric type before formatting
            result = float(result)  # Convert to float if necessary
            st.success(f"Your predicted package would be: {result:.2f} LPA")  # 2 decimal places
        except ValueError:
            st.error("Prediction result is not valid. Please check the model or input data.")

# Run the app
if __name__ == '__main__':
    main()
