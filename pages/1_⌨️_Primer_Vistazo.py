#--------------LIBRERÍAS--------------#
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st
from PIL import Image
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
st.set_page_config(page_title='Primer Vistazo', page_icon='🖥️', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

digital = pd.read_csv(r"data/digital_limpio.csv")

# -- img
col1,col2,col3 = st.columns(3)
with col2:
    image2 = Image.open(r'img/PrimerVistazo.png')
    st.image(image2)
# -- img

st.sidebar.title('MENÚ 🛒')
option = st.sidebar.radio('',('Datos a analizar', 'Número de productos', 'Proporción de artículos', 'Marcas más populares', 'Visitas a tiendas'))

if option=='Datos a analizar':
    # -- shape df
    st.title('Datos a analizar')
    st.write(digital.head())
    st.write('El número total de visitas realizadas a productos es de: ',digital.shape[0])
    st.write('El número de las diferentes categorías analizadas para cada producto: ',digital.shape[1])
    # -- shape df


elif option=='Número de productos':
    # -- unique products
    st.title('Número de productos')
    productos=digital.groupby(['id','name'])['id'].value_counts().reset_index()
    st.write(productos.head())
    st.write('El número de productos distintos visitados es de:', len(productos))
    # -- unique products


elif option=='Proporción de artículos':
    # -- proporción de artículos
    st.title('Proporción de artículos por categorías')
    tab1, tab2, tab3, tab4, tab5 = st.tabs(['Categorías Principales', 'Tipos de Envío','Disponibilidad de Artículos','Estado de Artículos','Artículos en Rebajas'])

    with tab1:
        categorias=digital.groupby('Categoria Principal')['Categoria Principal'].value_counts().sort_values(ascending=False).reset_index()
        categoria_1 = (categorias.loc[0,'count']*100)/categorias['count'].sum()
        categoria_2 = (categorias.loc[1,'count']*100)/categorias['count'].sum()
        categoria_3 = (categorias.loc[2,'count']*100)/categorias['count'].sum()
        categoria_4 = (categorias.loc[3,'count']*100)/categorias['count'].sum()
        categoria_5 = (categorias.loc[4,'count']*100)/categorias['count'].sum()
        categoria_6 = (categorias.loc[5,'count']*100)/categorias['count'].sum()

        fig = px.pie(labels=['TV and accesories','Computer and accesories', 'Audio and accesories','Wireless Tech','Electronics','Phones and accesories'], 
                    values=[categoria_1,categoria_2,categoria_3,categoria_4,categoria_5,categoria_6],
                    names=['TV and accesories','Computer and accesories', 'Audio and accesories','Wireless Tech','Electronics','Phones and accesories'],
                    color=['TV and accesories','Computer and accesories', 'Audio and accesories','Wireless Tech','Electronics','Phones and accesories'],
                    template='plotly_dark', color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

        fig.update_layout(
            title='Porcentaje de artículos visitados dentro de cada categoría',
            height=700)
        fig.update_traces(textfont={'size': 20})

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab2:
        tipo_envio=digital.groupby('Envios')['Envios'].value_counts().reset_index()
        envio1=tipo_envio.loc[0, 'count']/tipo_envio['count'].sum()
        envio2=tipo_envio.loc[1, 'count']/tipo_envio['count'].sum()
        envio3=tipo_envio.loc[2, 'count']/tipo_envio['count'].sum()
        envio4=tipo_envio.loc[3, 'count']/tipo_envio['count'].sum()

        fig = px.pie(labels=['Free Expedited Shipping','Free Standard Shipping', 'Minimum Order Free Shipping','Paid Shipping'], 
                    values=[envio1,envio2,envio3,envio4],
                    names=['Free Expedited Shipping','Free Standard Shipping', 'Minimum Order Free Shipping','Paid Shipping'],
                    color=['Free Expedited Shipping','Free Standard Shipping', 'Minimum Order Free Shipping','Paid Shipping'],
                    template='plotly_dark', color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

        fig.update_layout(
            title='Porcentaje de artículos visitados según el tipo de envío',
            height=700)
        fig.update_traces(textfont={'size': 20})

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab3:
        tipo_disp=digital.groupby('Disponibilidad')['Disponibilidad'].value_counts().reset_index()
        disp1=tipo_disp.loc[0, 'count']/tipo_disp['count'].sum()
        disp2=tipo_disp.loc[1, 'count']/tipo_disp['count'].sum()
        disp3=tipo_disp.loc[2, 'count']/tipo_disp['count'].sum()
        disp4=tipo_disp.loc[3, 'count']/tipo_disp['count'].sum()
        disp5=tipo_disp.loc[4, 'count']/tipo_disp['count'].sum()
        disp6=tipo_disp.loc[5, 'count']/tipo_disp['count'].sum()

        fig = px.pie(labels=['In Stock','Low Stock', 'More on the Way','Out of Stock','Retired','Special Order'], 
                    values=[disp1,disp2,disp3,disp4,disp5,disp6],
                    names=['In Stock','Low Stock', 'More on the Way','Out of Stock','Retired','Special Order'],
                    color=['In Stock','Low Stock', 'More on the Way','Out of Stock','Retired','Special Order'],
                    template='plotly_dark', color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

        fig.update_layout(
            title='Porcentaje de artículos visitados según la disponibilidad',
            height=700)
        fig.update_traces(textfont={'size': 13})

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab4:
        tipo_estado=digital.groupby('Estado')['Estado'].value_counts().reset_index()
        estado1=tipo_estado.loc[0, 'count']/tipo_estado['count'].sum()
        estado2=tipo_estado.loc[1, 'count']/tipo_estado['count'].sum()
        estado3=tipo_estado.loc[2, 'count']/tipo_estado['count'].sum()

        fig = px.pie(labels=['New','Refurbished', 'Used'], 
                    values=[estado1,estado2,estado3],
                    names=['New','Refurbished', 'Used'],
                    color=['New','Refurbished', 'Used'],
                    template='plotly_dark', color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

        fig.update_layout(
            title='Porcentaje de artículos visitados según el estado del artículo',
            height=700)
        fig.update_traces(textfont={'size': 20})

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab5:
        tipo_sale=digital.groupby('prices.isSale')['prices.isSale'].value_counts().reset_index()
        sale1=tipo_sale.loc[0, 'count']/tipo_sale['count'].sum()
        sale2=tipo_sale.loc[1, 'count']/tipo_sale['count'].sum()


        fig = px.pie(labels=['Sin descuento','Con descuento'], 
                    values=[sale1,sale2],
                    names=['Sin descuento','Con descuento'],
                    color=['Sin descuento','Con descuento'],
                    template='plotly_dark', color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])

        fig.update_layout(
            title='Porcentaje de artículos visitados según artículos en rebajas',
            height=700)
        fig.update_traces(textfont={'size': 20})

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)


    # -- proporción de artículos


elif option=='Marcas más populares':
    # -- marcas populares por categoría
    st.title('Marcas más populares entre categorías')
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(['Audio and accessories', 'TV and accessories', 'Wireless Tech', 'Computer and accessories', 'Phones and accessories', 'Electronics'])

    marcas=digital.groupby(['Categoria Principal', 'brand'])['brand'].value_counts().sort_values(ascending=False).reset_index()
    marcas_top5 = marcas.groupby('Categoria Principal').apply(lambda x: x.nlargest(5, 'count')).reset_index(drop=True)

    with tab2:
        marcas_tv=marcas_top5[marcas_top5['Categoria Principal']=='TV and accessories']
        fig = px.bar_polar(marcas_tv, r="count", theta="brand",
                        color="brand",color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'],
                        height=600, title='Marcas de televisores y accesorios más visitadas')
        
        fig.update_layout(polar=dict(angularaxis=dict(tickfont=dict(color="darkblue", size=14))))

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab4:
        marcas_computer=marcas_top5[marcas_top5['Categoria Principal']=='Computer and accessories']
        fig = px.bar_polar(marcas_computer, r="count", theta="brand",
                        color="brand",color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'],
                        height=600, title='Marcas de ordenadores y accesorios más visitadas')
        fig.update_layout(polar=dict(angularaxis=dict(tickfont=dict(color="darkblue", size=14))))

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab6:
        marcas_elec=marcas_top5[marcas_top5['Categoria Principal']=='Electronics']
        fig = px.bar_polar(marcas_elec, r="count", theta="brand",
                        color="brand",color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'],
                        height=600, title='Marcas de electrónica más visitadas')
        fig.update_layout(polar=dict(angularaxis=dict(tickfont=dict(color="darkblue", size=14))))

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab1:
        marcas_audio=marcas_top5[marcas_top5['Categoria Principal']=='Audio and accessories']
        fig = px.bar_polar(marcas_audio, r="count", theta="brand",
                        color="brand",color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'],
                        height=600, title='Marcas de audio y accesorios más visitadas')
        fig.update_layout(polar=dict(angularaxis=dict(tickfont=dict(color="darkblue", size=14))))

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab5:
        marcas_phone=marcas_top5[marcas_top5['Categoria Principal']=='Phones and accessories']
        fig = px.bar_polar(marcas_phone, r="count", theta="brand",
                        color="brand",color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'],
                        height=600, title='Marcas de teléfonos y accesorios más visitadas')
        fig.update_layout(polar=dict(angularaxis=dict(tickfont=dict(color="darkblue", size=14))))

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    with tab3:
        marcas_wireless=marcas_top5[marcas_top5['Categoria Principal']=='Wireless Tech']
        fig = px.bar_polar(marcas_wireless, r="count", theta="brand",
                        color="brand",color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'],
                        height=600, title='Marcas de electrónica inalámbrica más visitadas')
        fig.update_layout(polar=dict(angularaxis=dict(tickfont=dict(color="darkblue", size=14))))

        col1,col2,col3=st.columns(3)
        with col2:
            st.plotly_chart(fig)

    # -- marcas populares por categoría


elif option=='Visitas a tiendas':
    # -- tiendas más visitadas
    st.title('Visitas realizadas a tiendas')
    tiendas=digital.groupby(['Tienda Precio','Categoria Principal'])['Categoria Principal'].value_counts().reset_index()
    fig=px.bar(data_frame=tiendas,x='count', y='Tienda Precio', color='Categoria Principal',title = "Número de artículos visitados por tienda y cateogría", template= "plotly_dark",barmode='group', color_discrete_sequence=['#172D67','#715AFF','#22DDD2','#2E73EA','#8C15E9','#17072B'])
    fig.update_layout(
        xaxis_title="Número de visitas por categoría",
        yaxis_title="Tienda",
        yaxis=dict(tickfont=dict(size=17, color="darkblue", family="Arial")),
        height=800
    )
    col1,col2,col3=st.columns(3)
    with col2:
        st.plotly_chart(fig)

    # -- tiendas más visitadas



#--------------------------------------SIDEBAR-------------------------------------#
st.sidebar.markdown("""---""")
image1 = Image.open(r'img/logo.png')
st.sidebar.image(image1)
#--------------------------------------SIDEBAR-------------------------------------#