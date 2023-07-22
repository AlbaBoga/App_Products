#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
from scipy.stats import shapiro
from scipy.stats import mannwhitneyu
import random
import streamlit as st
from PIL import Image
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
st.set_page_config(page_title='Análisis de Productos', page_icon='🖥️', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

digital = pd.read_csv(r"data/digital_limpio.csv")

# -- img
col1,col2,col3 = st.columns(3)
with col2:
    image2 = Image.open(r'img/Analisis.png')
    st.image(image2)
# -- img

st.sidebar.title('MENÚ 🛒')
option = st.sidebar.radio('',('Precios medios', 'Disponibilidad', 'Estado', 'Rebajas', 'Envíos','Tiendas'))

if option=='Precios medios':
    # -- distribución precios
    st.title('Distribución de precios medios por visitas')
    digital['nuevas_fechas']=pd.to_datetime(digital['nuevas_fechas'],format='mixed')
    digital['año']=digital['nuevas_fechas'].dt.year

    option1 = st.sidebar.radio('Selecciona:', ('Distribución Anual','Distribución'))
    if option1 == 'Distribución':
        st.subheader('Evaluación de los datos')
        fig=px.histogram(x=digital['Precio medio'], color_discrete_sequence=['#715AFF'])
        fig.update_layout(height=600, width=600, title_text="Distribución de precios medios para todos los años", 
                        xaxis=dict(title="Precio medio"), yaxis=dict(title="Número de artículos visitados"))
        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)
        st.subheader('Análisis de hipótesis')
        st.markdown("""
En la distribución de precios medios se observa que hay un mayor número de visitas para los rangos de precios que van hasta los 200 dólares y que el precio medio máximo del artículos visitados es de 6500 dólares. El número de visitas decrece considerablemente conforme el precio de los artículos aumenta, por tanto, la hipótesis que se presenta es que la distribución de precios medios no estaría normalmente distribuida debido a la variación en el número de visitas en función de los diferentes rangos de precios.

Para la confirmación de dicha hipóteisis, se procede a utilizar el ``test de Shapiro-Wilk``.
* ``Hipótesis nula``: La distribución de visitas en función de los precios medios sigue una distribución Gaussiana, es decir, el mayor número de visitas se centra en un rango medio de precios.
* ``Hipótesis alternativa``: El rango de precios medios de artículos visitados no sigue una distribución Gaussiana, indicando que los diferentes clientes pueden tener ciertas preferencias dependiendo de los rangos de precios presentados.
                    """)
        shapiro_test = shapiro(digital['Precio medio'])
        if shapiro_test[1]<0.05:
            st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test[1]}")
            st.write('Se rechaza la hipótesis nula.')
        else:
            st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test[1]}")
            st.write('No se puede rechazar la hipóteisis nula.')

    elif option1 == 'Distribución Anual':
        col1,col2,col3=st.columns(3)
        with col2:
            year = st.slider('Selecciona el año:', min_value=2014, max_value=2018)
        
        precios_año = digital[digital['año']==year]['Precio medio']
        
        fig=px.histogram(x=precios_año, color_discrete_sequence=['#715AFF'])
        fig.update_layout(height=600, width=600, title_text="Distribución de precios medios por años", 
                        xaxis=dict(title="Precio medio"), yaxis=dict(title="Número de artículos visitados"))
        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    # -- distribución precios


elif option=='Disponibilidad':
    # -- distribución disponibilidad
    st.title('Distribución de precios medios por disponibilidad y categorías')

    st.subheader('Evaluación de los datos')
    distribution1=digital.groupby(['Categoria Principal','Disponibilidad'])['Precio medio'].value_counts().sort_values(ascending=False).reset_index()
    fig = px.strip(distribution1, x='Categoria Principal', y="Precio medio", color='Disponibilidad',
                color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

    fig.update_layout(
        title='Distribución de categorías por disponibilidad',
        xaxis=dict(title='Categorías'),
        yaxis=dict(title='Precio medio de los artículos'),
        height=650, width=650
    )

    col1,col2,col3=st.columns(3)
    with col2:
        st.plotly_chart(fig)

    st.subheader('Análisis de hipótesis')
    st.markdown("""
Se busca determinar si la distribución de precios para aquellos artículos disponibles y los que sólo están disponibles por encargo es la misma o no.

Para la confirmación de dicha hipóteisis, primero se estudia la distribución de los dos grupos mediante el ``test de Shapiro-Wilk``, lo que nos permitirá saber si siguen una distribución normal para utilizar un test paramétrico, o no, en cuyo caso se haría uso de tests no paramétricos.
* ``Hipótesis nula``: Siguen una distribución Gaussiana.
* ``Hipótesis alternativa``: No siguen una distribución Gaussiana.
                    """)
    st.markdown("""##### Grupo A: Artículos disponibles""")

    # Se obtienen las dos muestras.
    group_A = digital.loc[digital['Disponibilidad'].isin(['In Stock']),'Precio medio']
    group_B = digital.loc[digital['Disponibilidad'].isin(['Special Order']),'Precio medio']

    shapiro_test_A = shapiro(group_A)
    if shapiro_test_A[1]<0.05:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.markdown("""##### Grupo B: Artículos por encargo""")

    shapiro_test_B = shapiro(group_B)
    if shapiro_test_B[1]<0.05:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.markdown("""##### A/B testing""")
    st.markdown("""
Dado que se ha rechazado la hipóteisis nula en el test de Shapiro-Wilk para los dos casos, se va a proceder a estudiar la hipótesis establecida para ambos grupos mediante el ``test U de Mann-Whitney``, que es el test no paramétrico más común.
* ``Hipótesis nula``: Ambos grupos siguen la misma distribución, por lo que las categorías no son determinantes en el precio medio de artículos visitados.
* ``Hipótesis alternativa``: Ambos grupos no siguen la misma distribución, por lo que hay una diferencia significativa entre los rangos de precios visitados por los clientes para cada categoría.
""")
    MW_test = mannwhitneyu(group_A, group_B)
    if MW_test.pvalue<0.05:
        st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
        st.write('No se puede rechazar la hipóteisis nula.')
    
    st.write(f'🌐 La mediana del precio de los artículos disponibles: {group_A.median()} USD')
    st.write(f'🌐 La mediana del precio de los artículos disponibles por encargo: {group_B.median()} USD')

    # -- distribución disponibilidad


elif option=='Estado':
    # -- distribucion estado
    st.title('Distribución de precios medios por estado y categorías')

    st.subheader('Evaluación de los datos')
    distribution2=digital.groupby(['Categoria Principal','Estado'])['Precio medio'].value_counts().sort_values(ascending=False).reset_index()
    fig = px.strip(distribution2, x='Categoria Principal', y="Precio medio", color='Estado',
                color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

    fig.update_layout(
        title='Distribución de categorías por estado',
        xaxis=dict(title='Categorías'),
        yaxis=dict(title='Precio medio de los artículos'),
        height=650, width=650
    )

    col1,col2,col3=st.columns(3)
    with col2:
        st.plotly_chart(fig)

    st.subheader('Análisis de hipótesis')
    st.markdown("""
Se quiere averiguar si los clientes buscan los mismos rangos de precios en artículos nuevos y usados o no.

Para la confirmación de dicha hipóteisis, primero se estudia la distribución de los dos grupos mediante el ``test de Shapiro-Wilk``, lo que nos permitirá saber si siguen una distribución normal para utilizar un test paramétrico, o no, en cuyo caso se haría uso de tests no paramétricos.
* ``Hipótesis nula``: Siguen una distribución Gaussiana.
* ``Hipótesis alternativa``: No siguen una distribución Gaussiana.
                    """)
    st.markdown("""##### Grupo A: Artículos nuevos""")

    # Se obtienen las dos muestras.
    group_A = digital.loc[digital['Estado'].isin(['New']),'Precio medio']
    group_B = digital.loc[digital['Estado'].isin(['Used']),'Precio medio']

    shapiro_test_A = shapiro(group_A)
    if shapiro_test_A[1]<0.05:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.markdown("""##### Grupo B: Artículos usados""")

    shapiro_test_B = shapiro(group_B)
    if shapiro_test_B[1]<0.05:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.markdown("""##### A/B testing""")
    st.markdown("""
Dado que se ha rechazado la hipóteisis nula en el test de Shapiro-Wilk, se va a proceder a estudiar la hipótesis establecida para ambos grupos mediante el ``test U de Mann-Whitney``, que es el test no paramétrico más común.
* ``Hipótesis nula``: Ambos grupos siguen la misma distribución, por lo que las categorías no son determinantes en el precio medio de artículos visitados.
* ``Hipótesis alternativa``: Ambos grupos no siguen la misma distribución, por lo que hay una diferencia significativa entre los rangos de precios visitados por los clientes para cada categoría.
""")
    MW_test = mannwhitneyu(group_A, group_B)
    if MW_test.pvalue<0.05:
        st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.write(f'🌐 La mediana del precio de los artículos nuevos: {group_A.median()} USD')
    st.write(f'🌐 La mediana del precio de los artículos usados: {group_B.median()} USD')
    # -- distribucion estado


elif option=='Rebajas':
    # -- distribución rebajas
    st.title('Distribución de precios medios por artículos en rebajas y categorías')

    st.subheader('Evaluación de los datos')
    distribution3=digital.groupby(['Categoria Principal','prices.isSale'])['Precio medio'].value_counts().sort_values(ascending=False).reset_index()
    distribution3['prices.isSale']=distribution3['prices.isSale'].map({0:'No está en rebajas', 1:'Está en rebajas'})
    fig = px.strip(distribution3, x='Categoria Principal', y="Precio medio", color='prices.isSale', labels={'prices.isSale':'Rebajas'},
                color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

    fig.update_layout(
        title='Distribución de categorías por artículos en rebajas',
        xaxis=dict(title='Categorías'),
        yaxis=dict(title='Precio medio de los artículos'),
        height=650, width=650
    )

    col1,col2,col3=st.columns(3)
    with col2:
        st.plotly_chart(fig)

    st.subheader('Análisis de hipótesis')
    st.markdown("""
Se pretende saber si los clientes buscan el mismo rango de precios para artículos rebajados y artículos sin descuento.

Para la confirmación de dicha hipóteisis, primero se estudia la distribución de los dos grupos mediante el ``test de Shapiro-Wilk``, lo que nos permitirá saber si siguen una distribución normal para utilizar un test paramétrico, o no, en cuyo caso se haría uso de tests no paramétricos.
* ``Hipótesis nula``: Siguen una distribución Gaussiana.
* ``Hipótesis alternativa``: No siguen una distribución Gaussiana.
                    """)
    st.markdown("""##### Grupo A: Artículos no rebajados""")

    # Se obtienen las dos muestras.
    group_A = digital.loc[digital['prices.isSale'].isin([0]),'Precio medio']
    group_B = digital.loc[digital['prices.isSale'].isin([1]),'Precio medio']

    shapiro_test_A = shapiro(group_A)
    if shapiro_test_A[1]<0.05:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.markdown("""##### Grupo B: Artículos rebajados""")

    shapiro_test_B = shapiro(group_B)
    if shapiro_test_B[1]<0.05:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.markdown("""##### A/B testing""")
    st.markdown("""
Dado que se ha rechazado la hipóteisis nula en el test de Shapiro-Wilk, se va a proceder a estudiar la hipótesis establecida para ambos grupos mediante el ``test U de Mann-Whitney``, que es el test no paramétrico más común.
* ``Hipótesis nula``: Ambos grupos siguen la misma distribución, por lo que las categorías no son determinantes en el precio medio de artículos visitados.
* ``Hipótesis alternativa``: Ambos grupos no siguen la misma distribución, por lo que hay una diferencia significativa entre los rangos de precios visitados por los clientes para cada categoría.
""")
    MW_test = mannwhitneyu(group_A, group_B)
    if MW_test.pvalue<0.05:
        st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
        st.write('No se puede rechazar la hipóteisis nula.')
    
    st.write(f'🌐 La mediana del precio de los artículos sin descuento: {group_A.median()} USD')
    st.write(f'🌐 La mediana del precio de los artículos rebajados: {group_B.median()} USD')
    # -- distribución rebajas


elif option=='Envíos':
    # -- distribución envíos
    st.title('Distribución de precios medios por envío y categorías')

    st.subheader('Evaluación de los datos')
    distribution4=digital.groupby(['Categoria Principal','Envios'])['Precio medio'].value_counts().sort_values(ascending=False).reset_index()
    fig = px.strip(distribution4, x='Categoria Principal', y="Precio medio", color='Envios',
                color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

    fig.update_layout(
        title='Distribución de categorías por tipo de envíos',
        xaxis=dict(title='Categorías'),
        yaxis=dict(title='Número de artículos'),
        height=650, width=650
    )

    col1,col2,col3=st.columns(3)
    with col2:
        st.plotly_chart(fig)

    st.subheader('Análisis de hipótesis')
    st.markdown("""
Se quiere averiguar si los clientes buscan el mismo rango de precio para envios estándar gratuitos y envíos con un mínimo de compra.

Para la confirmación de dicha hipóteisis, primero se estudia la distribución de los dos grupos mediante el ``test de Shapiro-Wilk``, lo que nos permitirá saber si siguen una distribución normal para utilizar un test paramétrico, o no, en cuyo caso se haría uso de tests no paramétricos.
* ``Hipótesis nula``: Siguen una distribución Gaussiana.
* ``Hipótesis alternativa``: No siguen una distribución Gaussiana.
                    """)
    st.markdown("""##### Grupo A: Envío gratis estándar""")

    # Se obtienen las dos muestras.
    group_A = digital.loc[digital['Envios'].isin(['Free Standard Shipping']),'Precio medio']
    group_B = digital.loc[digital['Envios'].isin(['Minimum Order Free Shipping']),'Precio medio']

    shapiro_test_A = shapiro(group_A)
    if shapiro_test_A[1]<0.05:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.markdown("""##### Grupo B: Envío con pedido mínimo""")

    shapiro_test_B = shapiro(group_B)
    if shapiro_test_B[1]<0.05:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.markdown("""##### A/B testing""")
    st.markdown("""
Dado que se ha rechazado la hipóteisis nula en el test de Shapiro-Wilk, se va a proceder a estudiar la hipótesis establecida para ambos grupos mediante el ``test U de Mann-Whitney``, que es el test no paramétrico más común.
* ``Hipótesis nula``: Ambos grupos siguen la misma distribución, por lo que las categorías no son determinantes en el precio medio de artículos visitados.
* ``Hipótesis alternativa``: Ambos grupos no siguen la misma distribución, por lo que hay una diferencia significativa entre los rangos de precios visitados por los clientes para cada categoría.
""")
    MW_test = mannwhitneyu(group_A, group_B)
    if MW_test.pvalue<0.05:
        st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
        st.write('Se rechaza la hipótesis nula.')
    else:
        st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
        st.write('No se puede rechazar la hipóteisis nula.')

    st.write(f'🌐 La mediana del precio de los artículos con envío gratis estándar: {group_A.median()} USD')
    st.write(f'🌐 La mediana del precio de los artículos con envío gratis a partir de un mínimo de compra: {group_B.median()} USD')
    # -- distribución envíos

elif option=='Tiendas':
    # -- tiendas
    st.title('Distribución de precios medios por visitas a tiendas')

    st.subheader('Evaluación de los datos')
    tab1,tab2,tab3,tab4,tab5 = st.tabs(['Distribución','Bestbuy','Walmart','Bhphotovideo','Ebay'])
    with tab1:
        tiendas=digital.groupby(['Tienda Precio', 'nuevas_fechas'])['Precio medio'].mean().reset_index()
        fig = px.violin(tiendas,
    x='Tienda Precio',
    y='Precio medio',
    color='Tienda Precio',
    box=True,
    points='all',
    color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'],
    height=550, width=650)
        fig.update_layout(xaxis=dict(tickfont=dict(size=17, color="darkblue", family="Arial")))
        
        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)
        
        st.subheader('Análisis de hipótesis')
        st.markdown("""
Se quiere averiguar si los clientes buscan el mismo rango de precios en las tiendas más visitadas, que serían Walmart y Bestbuy.    

Para la confirmación de dicha hipóteisis, primero se estudia la distribución de los dos grupos mediante el ``test de Shapiro-Wilk``, lo que nos permitirá saber si siguen una distribución normal para utilizar un test paramétrico, o no, en cuyo caso se haría uso de tests no paramétricos.
* ``Hipótesis nula``: Siguen una distribución Gaussiana.
* ``Hipótesis alternativa``: No siguen una distribución Gaussiana.
                        """)
        st.markdown("""##### Grupo A: Walmart""")

        # Se obtienen las dos muestras.
        group_A = digital.loc[digital['Tienda Precio'].isin(['walmart']),'Precio medio']
        group_B = digital.loc[digital['Tienda Precio'].isin(['bestbuy']),'Precio medio']

        shapiro_test_A = shapiro(group_A)
        if shapiro_test_A[1]<0.05:
            st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
            st.write('Se rechaza la hipótesis nula.')
        else:
            st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_A[1]}")
            st.write('No se puede rechazar la hipóteisis nula.')

        st.markdown("""##### Grupo B: Bestbuy""")

        shapiro_test_B = shapiro(group_B)
        if shapiro_test_B[1]<0.05:
            st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
            st.write('Se rechaza la hipótesis nula.')
        else:
            st.write(f"El p-valor obtenido en el test de Shapiro-Wilk es de {shapiro_test_B[1]}")
            st.write('No se puede rechazar la hipóteisis nula.')

        st.markdown("""##### A/B testing""")
        st.markdown("""
    Dado que se ha rechazado la hipóteisis nula en el test de Shapiro-Wilk, se va a proceder a estudiar la hipótesis establecida para ambos grupos mediante el ``test U de Mann-Whitney``, que es el test no paramétrico más común.
    * ``Hipótesis nula``: Ambos grupos siguen la misma distribución, por lo que las categorías no son determinantes en el precio medio de artículos visitados.
    * ``Hipótesis alternativa``: Ambos grupos no siguen la misma distribución, por lo que hay una diferencia significativa entre los rangos de precios visitados por los clientes para cada categoría.
    """)
        MW_test = mannwhitneyu(group_A, group_B)
        if MW_test.pvalue<0.05:
            st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
            st.write('Se rechaza la hipótesis nula.')
        else:
            st.write(f"El p-valor obtenido en el test de Mann-Whitney es de {MW_test.pvalue}")
            st.write('No se puede rechazar la hipóteisis nula.')
        
        st.write(f'🌐 La mediana del precio de los artículos vistos en Walmart: {group_A.median()} USD')
        st.write(f'🌐 La mediana del precio de los artículos vistos en Bestbuy: {group_B.median()} USD')
    
    with tab2:
        bestbuy=digital[digital['Tienda Precio']=='bestbuy'].groupby('nuevas_fechas')['Precio medio'].mean().reset_index()
        fig=px.area(bestbuy, y="Precio medio",title = "Precio medio de los artículos visitados en Bestbuy",
            color_discrete_sequence=['#715AFF'],
            height=550, width=750)
        fig.update_layout(
                yaxis_title="Precio medio",
                xaxis_title="Datos"
        )
        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)
    
    with tab3:
        walmart=digital[digital['Tienda Precio']=='walmart'].groupby('nuevas_fechas')['Precio medio'].mean().reset_index()
        fig=px.area(walmart, y="Precio medio",title = "Precio medio de los artículos visitados en Walmart",
            color_discrete_sequence=['#715AFF'],
            height=550, width=750)
        fig.update_layout(
            yaxis_title="Precio medio",
            xaxis_title="Datos"
        )
        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab4:
        bhphotovideo=digital[digital['Tienda Precio']=='bhphotovideo'].groupby('nuevas_fechas')['Precio medio'].mean().reset_index()
        fig=px.area(bhphotovideo, y="Precio medio",title = "Precio medio de los artículos visitados en Bhphotovideo",
            color_discrete_sequence=['#715AFF'],
            height=550, width=750)
        fig.update_layout(
            yaxis_title="Precio medio",
            xaxis_title="Datos"
        )
        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)
    
    with tab5:
        ebay=digital[digital['Tienda Precio']=='ebay'].groupby('nuevas_fechas')['Precio medio'].mean().reset_index()
        fig=px.area(ebay, y="Precio medio",title = "Precio medio de los artículos visitados en Ebay",
            color_discrete_sequence=['#715AFF'],
            height=550, width=750)
        fig.update_layout(
            yaxis_title="Precio medio",
            xaxis_title="Datos"
        )
        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    # -- tiendas



#--------------------------------------SIDEBAR-------------------------------------#
st.sidebar.markdown("""---""")
image1 = Image.open(r'img/logo.png')
st.sidebar.image(image1)
#--------------------------------------SIDEBAR-------------------------------------#