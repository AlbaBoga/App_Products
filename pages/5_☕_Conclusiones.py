#--------------LIBRERÍAS--------------#
import streamlit as st
from PIL import Image
#--------------LIBRERÍAS--------------#

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
st.set_page_config(page_title='Conclusiones', page_icon='🖥️', layout='wide')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#




st.sidebar.title('MENÚ 🛒')
option = st.sidebar.radio('',('Resumen de los datos', 'Conclusiones'))

if option=='Resumen de los datos':
    st.markdown("""<iframe title="Report Section" width="1024" height="804" src="https://app.powerbi.com/view?r=eyJrIjoiZTcyMjM1NjktYTNkZi00N2Q2LWFhNjgtOGRkYjFkNTk2Y2YwIiwidCI6IjhhZWJkZGI2LTM0MTgtNDNhMS1hMjU1LWI5NjQxODZlY2M2NCIsImMiOjl9" frameborder="0" allowFullScreen="true"></iframe>""",unsafe_allow_html=True)

elif option=='Conclusiones':
    col1,col2,col3=st.columns(3)
    with col2:
        # -- img
        image3 = Image.open(r'img/Conclusiones.png')
        st.image(image3)
        # -- img
        st.markdown("""
        * Se han analizado ``7249 visitas`` a ``835 productos`` diferentes.
        * Más del ``50% de los artículos`` visitados por los clientes están dentro de las categorías de televisores, ordenadores y accesorios.
        * ``Casi el 50% de los artículos`` visitados tienen un tipo de envío estándar gratis.
        * ``Casi el 95% de los artículos`` visitados tiene disponibilidad inmediata.
        * ``En más del 95% de los casos``, los clientes buscan artículos nuevos.
        * ``En más de un 75% de los casos``, los clientes buscan artículos sin ningún tipo de descuento.
        * Las ``marcas más populares`` buscadas por clientes son: Samsung, Sony, Apple, Pioneer, Alpine y Corsair.
        * Las ``tiendas más visitadas`` son Bestbuy y Walmart.
        * Se ha determinado que la disponibilidad, el estado, el tipo de envío y los descuentos de los artículos podrían influir en los precios de los productos.
        * Se ha utilizado el ``modelo Neural Prophet`` para predecir futuras tendencias en los precios en base a las visitas mensuales y se ha concluido, a través de los resultados, que los precios de los artículos visitados podrían ir en crecimiento.
        * Se han implementado varios modelos de clasificación y se ha obtenido una ``precisión máxima del 79%`` a través del modelo Extreme Gradient Boosting.
        * Finalmente, serían necesarios más datos para que los modelos predictivos creados se ajustasen de una forma más adecuada.

        """)

#--------------------------------------SIDEBAR-------------------------------------#
st.sidebar.markdown("""---""")
image1 = Image.open(r'img/logo.png')
st.sidebar.image(image1)
st.sidebar.markdown("""Logo: ``Vecteezy.com``""")
st.sidebar.markdown("""Todas las imágenes de cabecera: ``canva.com``""")
#--------------------------------------SIDEBAR-------------------------------------#
