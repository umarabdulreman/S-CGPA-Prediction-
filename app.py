import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load the saved models
models = {
    'Linear Regression': joblib.load('Linear_Regression_model.joblib'),
    'Ridge Regression': joblib.load('Ridge_Regression_model.joblib'),
    'Lasso Regression': joblib.load('Lasso_Regression_model.joblib'),
    'Decision Tree': joblib.load('Decision_Tree_model.joblib'),
    'Random Forest': joblib.load('Random_Forest_model.joblib'),
    'Support Vector Regression': joblib.load('Support_Vector_Regression_model.joblib')
}

# Function to provide performance comments based on GPA
def get_performance_comment(gpa):
    if 3.51 <= gpa <= 4.00:
        return 'Extraordinary Performance'
    elif 3.00 <= gpa < 3.51:
        return 'Very Good Performance'
    elif 2.51 <= gpa < 3.00:
        return 'Good Performance'
    elif 2.00 <= gpa < 2.51:
        return 'Satisfactory Performance'
    elif 1.00 <= gpa < 2.00:
        return 'Poor Performance'
    elif 0.00 <= gpa < 1.00:
        return 'Very Poor Performance'
    else:
        return 'Invalid GPA'

# Streamlit app
st.title('SGPA and CGPA Predictor')

model_names = list(models.keys())
selected_model = st.selectbox('Select a model for prediction:', model_names)

st.sidebar.title('Enter Input Data:')

# Input fields for the required data
input_matric_percentage = st.sidebar.number_input('Matric Percentage:', min_value=0.0, max_value=100.0, step=0.1)
input_intermediate_percentage = st.sidebar.number_input('Intermediate Percentage:', min_value=0.0, max_value=100.0, step=0.1)
input_sgpa_1st_sem = st.sidebar.number_input('SGPA in BS First Semester:', min_value=0.0, max_value=4.0, step=0.01)
input_sgpa_2nd_sem = st.sidebar.number_input('SGPA in BS Second Semester:', min_value=0.0, max_value=4.0, step=0.01)
input_sgpa_3rd_sem = st.sidebar.number_input('SGPA in BS Third Semester:', min_value=0.0, max_value=4.0, step=0.01)
input_sgpa_4th_sem = st.sidebar.number_input('SGPA in BS Fourth Semester:', min_value=0.0, max_value=4.0, step=0.01)

# Button to predict
if st.sidebar.button('Predict'):
    model = models[selected_model]
    
    # Creating a DataFrame for the input data
    input_data = pd.DataFrame(
        [[input_matric_percentage, input_intermediate_percentage, input_sgpa_1st_sem, 
          input_sgpa_2nd_sem, input_sgpa_3rd_sem, input_sgpa_4th_sem]], 
        columns=["Matric percentage", "Intermediate percentage", 
                 "SGPA in BS First semester", "SGPA in BS Second semester", 
                 "SGPA in BS Third semester", "SGPA in BS Fourth semester"]
    )

    # Make predictions for 5th semester SGPA
    sgpa_prediction_5th_sem = model.predict(input_data)[0]

    # Calculate CGPA for 5th semester
    sgpa_1st_to_4th = [input_sgpa_1st_sem, input_sgpa_2nd_sem, input_sgpa_3rd_sem, input_sgpa_4th_sem]
    total_semesters = 5  # Including 5th semester
    cgpa_5th_sem = (sum(sgpa_1st_to_4th) + sgpa_prediction_5th_sem) / total_semesters

    # Display results
    sgpa_comment = get_performance_comment(sgpa_prediction_5th_sem)
    st.subheader('Predicted Results for 5th Semester:')
    st.write(f'SGPA of 5th Semester: {sgpa_prediction_5th_sem:.2f} - {sgpa_comment}')
    st.write(f'CGPA after 5th Semester: {cgpa_5th_sem:.2f}')

