#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd
import streamlit as st
from PIL import Image
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
st.set_page_config(page_title='Predictor', page_icon='🖥️', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
digital_class = pd.read_csv(r"data/digital_class.csv")

# -- img
image3 = Image.open(r'img/Predictor.png')
st.image(image3)
# -- img

st.sidebar.title('MENÚ 🛒')
option = st.sidebar.radio('',('Pycaret, Extreme Gradient Boosting', 'Gradient Boosting Classifier', 'Red Neuronal'))

if option=='Pycaret, Extreme Gradient Boosting':
    # --pycaret
    if st.button('Redirección 👈'):
        link = 'https://electronicsmodels.streamlit.app/Pycaret_Extreme_Gradient_Boosting'
        st.markdown(f'<a href="{link}">Predictor Extreme Gradient Boosting (Pycaret)</a>', unsafe_allow_html=True)
    else:
        st.write('📝 Estimando ... ')
    # --pycaret


elif option=='Gradient Boosting Classifier':
# --GBC
    if st.button('Redirección 👈'):
        link = 'https://electronicsmodels.streamlit.app/Gradient_Boostring_Classifier'
        st.markdown(f'<a href="{link}">Predictor Gradient Boosting Classifier</a>', unsafe_allow_html=True)
    else:
        st.write('📝 Estimando ... ')
# --GBC


elif option=='Red Neuronal':
# --NN
    if st.button('Redirección 👈'):
        link = 'https://electronicsmodels.streamlit.app/Red_Neuronal'
        st.markdown(f'<a href="{link}">Predictor Neural Network</a>', unsafe_allow_html=True)
    else:
        st.write('📝 Estimando ... ')
# --NN



#--------------------------------------SIDEBAR-------------------------------------#
st.sidebar.markdown("""---""")
image1 = Image.open(r'img/logo.png')
st.sidebar.image(image1)
#--------------------------------------SIDEBAR-------------------------------------#