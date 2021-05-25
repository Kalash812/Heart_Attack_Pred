import streamlit as st
from sklearn.preprocessing import StandardScaler
import pickle

pickle_in = open("model.pkl" , "rb")
classifier = pickle.load(pickle_in)

sc_X = StandardScaler()

def pred(a = [[]]):
    a = sc_X.fit_transform(a)
    y_pred = classifier.predict(a)
    return(y_pred)
    

def main():

    st.title("Heart Attack Prediction")
    html_temp = """
    <div style = "background-colo:tomato;padding:10px">
    <h2 style = "color:white;text-align:center;">Streamlit Heart Attack Predictor ML App </h2>
    </div>
    """
    st.markdown(html_temp , unsafe_allow_html=True)
    
    age = st.text_input("Age" ,  key="1")
    sex = st.text_input("Gender" ,  key="2")
    cp = st.text_input("Cp" ,  key="3")
    trtbps = st.text_input("trtbps" ,  key="4")
    chol = st.text_input("chol" ,  key="5")
    
    if st.button("Predict"):
        result = pred([[age , sex , cp , trtbps , chol]])
        st.success("The Output is {}".format(result))    

if __name__ == '__main__':
    main()
