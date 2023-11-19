import numpy as np
import pickle
import streamlit as st
from fpdf import FPDF
import base64

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
            # https://news.yale.edu/sites/default/files/styles/in_/public/adobestock_170883795_ynews-in-focus.jpeg?itok=pc0AYuha&c=6cbf340b08e67289e94a0b1beffa5aae
            # https://img.freepik.com/free-photo/breast-cancer-woman-white-t-shirt-with-satin-pink-ribbon-her-chest-symbol-breast-cancer-awareness_1150-18923.jpg?w=740&t=st=1668298279~exp=1668298879~hmac=3c8e78325ef03a8f964c31d1bc29e8f9b8cc40568f4b580960d5f404ddf9a7f4
            # https://img.freepik.com/free-photo/world-cancer-day-breast-cancer-awareness-ribbon-white-backg_1232-3613.jpg?w=740&t=st=1668298001~exp=1668298601~hmac=c9a3978f8e844867bcbc102e5876130c2bd713ab8d8a297b753f61d08b625347
            #  background-image: url("https://img.freepik.com/free-photo/breast-cancer-awareness-woman-pink-t-shirt-with-satin-pink-ribbon-her-chest-supporting-symbolbreast-cancer-awareness_1150-18882.jpg?w=740&t=st=1668297749~exp=1668298349~hmac=b6cc7579a2884a59e987e87d3b21257a518688f9daa33e1931afdb8475e74470");
            #  background-image: url("https://img.freepik.com/free-photo/world-cancer-day-breast-cancer-awareness-ribbon-white-backg_1232-3613.jpg?w=740&t=st=1668298001~exp=1668298601~hmac=c9a3978f8e844867bcbc102e5876130c2bd713ab8d8a297b753f61d08b625347");
             background-image: url("https://news.yale.edu/sites/default/files/styles/in_/public/adobestock_170883795_ynews-in-focus.jpeg?itok=pc0AYuha&c=6cbf340b08e67289e94a0b1beffa5aae");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url() 

st.markdown(
    """
    <style>
 
    input {
        font-size: 2rem !important;
    }
  
    </style>
    """,
    unsafe_allow_html=True,
)

# st.markdown(page_bg_img, unsafe_allow_html=True)

# loading the saved model
loaded_model = pickle.load(open(r'C:\Users\AbdulHamid\Desktop\BC\trained_model.sav', 'rb'))

# creating a function for Prediction

def cancer_prediction(input_data):

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        ss=st.success('Benign Tumor', icon="✅")
        return ss
    else:
        ee=st.warning('Malignant Tumor', icon="🚨")
        return ee

    # return prediction


def main():
    
    
    # giving a title
    # st.title('Web Application for Predicting Cancer')
   
    st.header('Web Application for Predicting Cancer')

    Age = st.text_input('1. Number of Age')
    FBS = st.text_input('2. Number of FBS')
    Urea = st.text_input('3. Number of Urea')
    ALB = st.text_input('4. Number of ALB')
    TCa = st.text_input('5. Number of TCa')
    GPT = st.text_input('6. Number of GPT')
    ALP = st.text_input('7. Number of ALP')
    CA15 = st.text_input('8. Number of CA15')
    CEA = st.text_input('9. Number of CEA')
    WBC = st.text_input('10. Number of WBC')
    RBC = st.text_input('11. Number of RBC')
    PLT = st.text_input('12. Number of PLT')
    ESR = st.text_input('13. Number of ESR')
    LDH = st.text_input('14. Number of LDH')

    
    
    # c=prediction
    # code for Prediction
    cancer = ''
    
    # creating a button for Prediction
    
    if st.button('Cancer Test Result'):
        cancer = cancer_prediction([Age, FBS, Urea, ALB, TCa, GPT, ALP, CA15,CEA,WBC,RBC,PLT,ESR,LDH])

      
    print(cancer)
    # r=st.write(cancer)  
    export_as_pdf = st.button("Export Report")

    def create_download_link(val, filename):
        b64 = base64.b64encode(val)  # val looks like b'...'
        return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'

    if export_as_pdf:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font('Arial', 'B', 16)
        pdf.cell(10)
        pdf.cell(20, 10, Age, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, FBS, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, Urea, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, TCa, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, GPT, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, ALP, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, CA15, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, CEA, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, WBC, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, RBC, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, PLT, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, ESR, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, LDH, 1, 1, 'C')
        pdf.cell(10)
        pdf.cell(20, 10, cancer, 1, 1, 'C')

        html = create_download_link(pdf.output(dest="S").encode("latin-1"), "test")

        st.markdown(html, unsafe_allow_html=True)
    
  
if __name__ == '__main__':
    main()