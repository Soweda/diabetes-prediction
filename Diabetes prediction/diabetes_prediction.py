
import streamlit as st
import numpy as np
import pickle
import sklearn
from sklearn.preprocessing import StandardScaler 

loaded_model=pickle.load(open('C:/Users/sowed/OneDrive/Documents/machine learning/Diabetes prediction/trained_model.sav','rb'))
try:
    loaded_model = pickle.load(open('C:/Users/sowed/OneDrive/Documents/machine learning/Diabetes prediction/trained_model.sav', 'rb'))
    print("File loaded successfully.")
except FileNotFoundError:
    print("File not found. Please check the file path.")
except pickle.UnpicklingError:
    print("Error loading the file. It may not be a valid pickle file.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
    
def diabetes_prediction(input_data):
    
    #input_data = (5,166,72,19,175,25.8,0.587,51)
    
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)
    
    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    
    if (prediction[0] == 0):
      return 'The person is not diabetic'
    else:
      return 'The person is diabetic'

def main():
    
    
    st.title('Diabetes Prediction')
    
    #getting input
    pregnancies= st.text_input("Number of pregnancies ")
    glucose= st.text_input('Enter Glucose level')
    bp=st.text_input('Enter your Blood Pressure')
    skin_thick= st.text_input('Enter your Skin Thickness')
    insulin=st.text_input('Enter insulin level')
    bmi=st.text_input('Enter BMI value ')
    d_pedigree=st.text_input('EDiabetes Pedigree function value')
    age=st.text_input('Enter your age ')
        
    diagnosis=''
    
    if st.button('Diabetes Test Result'):
        diagnosis=diabetes_prediction([pregnancies,glucose,bp,skin_thick,insulin,bmi,d_pedigree,age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()