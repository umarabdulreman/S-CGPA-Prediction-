
# Project Title: Prediction of Student GPA based on Various Factors

## Overview
This project aims to predict the GPA of students from the Institute of Space and Technology by analyzing various factors that might affect their academic performance. By utilizing a dataset collected from the students, we explore the relationship between students' GPA and several contributing factors, including matriculation percentage, FSC percentage, and GPA of the first four semesters, among others.

## Dataset Description
The dataset comprises responses from students of the Institute of Space and Technology, detailing various factors potentially impacting their studies. Key features include matriculation percentage, FSC percentage, GPA of the first four semesters (C and S GPA), along with other attributes collected through a survey. 

## Exploratory Data Analysis (EDA)
The EDA process involved analyzing the dataset to understand the factors contributing significantly to students' GPA. Through various visualization and statistical methods, we identified the most relevant features that have a correlation with the GPA, focusing primarily on matriculation percentage, FSC percentage, and GPA of the first four semesters.

## Preprocessing Steps
1. **Handling Missing Values:** Missing values were addressed using the Z-score method to ensure data integrity.
2. **Data Encoding:** Categorical data were encoded to transform into a machine-readable format.
3. **Data Standardization:** The data was standardized to bring all features to a similar scale, enhancing the performance of the machine learning models.

## Machine Learning Models
We applied five regression algorithms to predict the GPA based on the identified features:
- Lasso Regression
- Linear Regression
- Decision Tree
- Random Forest
- Ridge Regression
- Support Vector Regression

Each model was trained on the preprocessed dataset, and their performance was evaluated to determine the most effective model for GPA prediction.

## Model Training and Saving
After training, the models were saved in Joblib format for future predictions. This approach allows for the reuse of trained models without the need to retrain them, facilitating quick predictions.

## Streamlit Application
A Streamlit app was developed to deploy the trained models, enabling users to input the relevant data and receive GPA predictions. The app provides an intuitive interface for interacting with the models, making it accessible to users without a technical background.

### How to Use the Streamlit App
1. **Install Requirements:** Ensure you have Python and Streamlit installed on your system. 
2. **Run the App:** Navigate to the app's directory and run `streamlit run app.py` in your terminal.
3. **Input Data:** Enter the required information based on the factors identified in the dataset.
4. **Get Predictions:** Submit the data to receive a GPA prediction based on the selected machine learning model.

## Conclusion
This project demonstrates the capability of machine learning algorithms to predict student GPA by analyzing various academic and non-academic factors. The Streamlit app provides a practical tool for students and educators to estimate GPA outcomes and identify areas of improvement.
