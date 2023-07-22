#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly_express as px
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss
from statsmodels.tsa.arima.model import ARIMA
import streamlit as st
from PIL import Image
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
st.set_page_config(page_title='Visitas a Productos', page_icon='🖥️', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

digital = pd.read_csv(r"data/digital_limpio.csv")

# -- img
col1,col2,col3 = st.columns(3)
with col2:
    image2 = Image.open(r'img/Visitas.png')
    st.image(image2)
# -- img


st.sidebar.title('MENÚ 🛒')
option = st.sidebar.radio('',('Serie Temporal', 'Forecasting'))
if option=='Serie Temporal':
# -- serie temporal
    st.title('Estudio de las visitas mensuales a productos')
    precios_medios_diarios=digital.groupby('nuevas_fechas')['Precio medio'].mean().reset_index()
    precios_medios_diarios['nuevas_fechas']=pd.to_datetime(precios_medios_diarios['nuevas_fechas'])
    precios_medios_diarios.set_index('nuevas_fechas', inplace=True)
    precios_medios_diarios=precios_medios_diarios.resample('M').mean()
    precios_medios_diarios = precios_medios_diarios.fillna(precios_medios_diarios.mean(skipna=True))

    tab1, tab2, tab3=st.tabs(['Observación de los datos', 'Estacionariedad', 'Modelo ARIMA'])
    with tab1:
        fig=px.area(precios_medios_diarios, y="Precio medio",title = "Precio medio de los artículos visitados mensualmente",
            color_discrete_sequence=['#715AFF'],
            height=550, width=750)
        fig.update_layout(
            yaxis_title="Precio medio",
            xaxis_title="Fechas"
        )
        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)
    with tab2:
        st.subheader('Evaluación de la estacionariedad de la serie temporal')

        st.markdown("""##### Diferenciación de orden cero""")
        # Creamos gráfico
        f = plt.figure(figsize=(16, 4), dpi=80)
        # Preparamos primer componente
        ax1 = f.add_subplot(131)
        ax1.set_title('Serie original')
        ax1.plot(precios_medios_diarios.values)
        # Preparamos segundo componente
        ax2 = f.add_subplot(132)
        plot_acf(precios_medios_diarios.values, ax=ax2)
        # Preparamos tercer componente
        ax3 = f.add_subplot(133)
        plot_pacf(precios_medios_diarios.values, ax=ax3)
        col1,col2,col3=st.columns(3)
        with col2:
            st.pyplot()
            st.markdown("""##### Test Dickey-Fuller aumentada (ADF)
    * Hipótesis nula: Tiene raíz unitaria (serie no estacionaria).
    * Hipótesis alternativa: No tiene raíz unitaria (serie estacionaria).
        """)
            ADF_test1 = adfuller(precios_medios_diarios)
            if ADF_test1[1]<0.05:
                st.write(f"El p-valor obtenido la diferenciación de orden cero es de {ADF_test1[1]}")
                st.write('Se rechaza la hipótesis nula.')
            else:
                st.write(f"El p-valor obtenido la diferenciación de orden cero es de {ADF_test1[1]}")
                st.write('No se puede rechazar la hipóteisis nula.')
            
            st.markdown("""##### Test Kwiatkowski–Phillips–Schmidt–Shin (KPSS)
    * Hipótesis nula: No tiene raíz unitaria (serie estacionaria).
    * Hipótesis alternativa: Tiene raíz unitaria (serie no estacionaria).
        """)
            stat, p, lags, crit = kpss(precios_medios_diarios)
            if p<0.05:
                st.write(f"El p-valor obtenido la diferenciación de orden cero es de {p}")
                st.write('Se rechaza la hipótesis nula.')
            else:
                st.write(f"El p-valor obtenido la diferenciación de orden cero es de {p}")
                st.write('No se puede rechazar la hipóteisis nula.')
            
            st.markdown("""##### Conclusión
Hay discrepancia entre los dos tests realizados, por lo que la serie es de diferenciación estacionaria.
                         """)
            
        st.markdown("""##### Diferenciación de orden uno""")
        # Creamos gráfico
        f = plt.figure(figsize=(16, 4), dpi=80)
        # Preparamos primer componente
        ax1 = f.add_subplot(131)
        ax1.set_title('Serie original')
        ax1.plot(precios_medios_diarios.diff().values)
        # Preparamos segundo componente
        ax2 = f.add_subplot(132)
        plot_acf(precios_medios_diarios.diff().values, ax=ax2)
        # Preparamos tercer componente
        ax3 = f.add_subplot(133)
        plot_pacf(precios_medios_diarios.diff().values, ax=ax3)
        col1,col2,col3=st.columns(3)
        with col2:
            st.pyplot()
            st.markdown("""##### Test Dickey-Fuller aumentada (ADF)
    * Hipótesis nula: Tiene raíz unitaria (serie no estacionaria).
    * Hipótesis alternativa: No tiene raíz unitaria (serie estacionaria).
        """)
            ADF_test2 = adfuller(precios_medios_diarios.diff().dropna())
            if ADF_test2[1]<0.05:
                st.write(f"El p-valor obtenido la diferenciación de orden uno es de {ADF_test2[1]}")
                st.write('Se rechaza la hipótesis nula.')
            else:
                st.write(f"El p-valor obtenido la diferenciación de orden cuno es de {ADF_test2[1]}")
                st.write('No se puede rechazar la hipóteisis nula.')
            
            st.markdown("""##### Test Kwiatkowski–Phillips–Schmidt–Shin (KPSS)
    * Hipótesis nula: No tiene raíz unitaria (serie estacionaria).
    * Hipótesis alternativa: Tiene raíz unitaria (serie no estacionaria).
        """)
            stat, p, lags, crit = kpss(precios_medios_diarios.diff().dropna())
            if p<0.05:
                st.write(f"El p-valor obtenido la diferenciación de orden uno es de {p}")
                st.write('Se rechaza la hipótesis nula.')
            else:
                st.write(f"El p-valor obtenido la diferenciación de orden uno es de {p}")
                st.write('No se puede rechazar la hipóteisis nula.')
            
            st.markdown("""##### Conclusión
Se obtiene una serie temporal estacionaria para la diferenciación de orden uno.
                         """)
            
    
    with tab3:
        col1,col2,col3=st.columns(3)
        with col2:
            st.write('Best ARIMA(1,0,0) RMSE=191.729')
            model = ARIMA(precios_medios_diarios.values, order=(1,0,0))
            model_fit = model.fit()
            st.write(model_fit.summary())

            model_fit.plot_diagnostics()
            plt.tight_layout()
            st.pyplot()

# -- serie temporal


elif option=='Forecasting':
# -- neural prophet
    st.title('Neural Prophet para la predicción de valores futuros')

    st.subheader('Evaluación del error')
    col1,col2,col3 = st.columns(3)
    with col2:
        image2 = Image.open(r'img/error.png')
        st.image(image2, width=1000)
    
    st.subheader('Predicción de valores')

    data = {
    'ds': ['2014-08-31', '2014-09-30', '2014-10-31', '2014-11-30', '2014-12-31'],
    'y': [215.895000, 369.155556, 20.990000, 349.582337, 349.582337],
    'yhat1': [236.833466, 265.042206, 210.788132, 309.188049, 322.032959],
    'trend': [264.913940, 274.684326, 284.780426, 293.556183, 299.154114],
    'season_yearly': [-28.080475, -9.642130, -73.992302, 15.631866, 22.878849],
    'residual1': [-20.938466, 104.11335, -189.798132, 40.394287, 27.549378]
}

    df = pd.DataFrame(data)

    

    col1,col2,col3 = st.columns(3)
    with col2:
        st.write(df)
        image2 = Image.open(r'img/output.png')
        st.image(image2, width=1100)
# -- neural prophet



#--------------------------------------SIDEBAR-------------------------------------#
st.sidebar.markdown("""---""")
image1 = Image.open(r'img/logo.png')
st.sidebar.image(image1)
#--------------------------------------SIDEBAR-------------------------------------#
