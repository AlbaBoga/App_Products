import streamlit as st
from PIL import Image

#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#
st.set_page_config(page_title='ELECTRONIC PRODUCTCS', page_icon='🖥️', layout='centered')
st.set_option('deprecation.showPyplotGlobalUse', False)
#----------------------------CONFIGURACIÓN DE PÁGINAS----------------------------#

#--------------------------------------TÍTULO-------------------------------------#

image2 = Image.open(r'img/ElectronicProducts.png')
st.image(image2)
st.title('Productos electrónicos e información sobre precios')
st.markdown(
            """

Se ha obtenido una lista con más de 7000 registros de visitas a productos electrónicos que proviene de la base de datos de ``Datafiniti``. Debido a que es una base de datos de productos de pago, sólo se ha podido obtener una muestra de la información, no consiguiendo el listado de productos total original. 

¿Qué es lo que encontramos en el listado? Los principales ``datos proporcionados`` son:
* ID del producto.
* Precio máximo que ha tenido el producto.
* Precio mínimo que ha tenido el producto.
* La disponibilidad en tienda del producto.
* La condición.
* La moneda que utilizan los precios mostrados.
* La fecha de visualización de los precios.
* El tipo de envío que proporciona la tienda.
* La tienda con el enlace a compra.
* Nombre de la tienda donde se han podido ver los precios.
* Fecha de inscripción y actualización del producto.
* La marca, fabricante y código de producto.
* Categorías principales del producto.
* Peso del producto.
* Web de donde se ha obtenido información sobre el producto.

¿Cuáles han sido las ``motivaciones principales`` para el uso de estos datos? La industria de los productos electrónicos es un mercado con un gran crecimiento en los últimos años. Estas herramientas se han convertido en indispensables en nuestro día a día, haciéndonos trabajar de una forma más eficiente. Es por estas razones que existe la necesidad de encontrar aquellos productos de interés al mejor precio, sin renunciar a marcas y tiendas de confianza. Así, en este análisis realizado a los productos electrónicos más visitados desde 2014 a 2018, se pretende descubrir:
* ¿Cuáles son los productos que más despiertan el interés de los usuarios?
* ¿Qué rangos de precios tienen los productos que visitan los clientes?
* ¿Qué categorías de productos son más populares?
* ¿Cuáles son las condiciones de disponibilidad, estado y envío que prefieren los clientes en base a su precio?
* Finalmente, ¿qué tiendas son las más populares y si existen diferentes rangos de precio preferidos para productos dentro de cada tienda?

¿Cuáles son los ``pasos`` que se han llevado a cabo para la realización de dicho análisis?
* Primero se ha hecho un análisis inicial de los datos y un preprocesamiento de los mismos, donde se han utilizado aquellas columnas de mayor interés, se han hecho categorías nuevas que agrupan de una forma más clara las ya existentes y se ha utilizado un modelo de clasificación para predecir los datos faltantes dentro de la columna envío, en base al resto de datos ya preprocesados.
* Seguidamente, se ha realizado un análisis de los datos presentados en el dataset y se han estudiado posibles teorías a las que se han llegado a partir de los mismos.
* Como tercer paso, se ha hecho un estudio de los precios medios de los artículos visitados mensualmente por los clientes para tratar de predecir el comportamiento de los precios medios de artículos en función de las visitas.
* Finalmente, se ha realizado un modelo de clasificación que permite predecir la tienda que más se ajusta a las necesidades del cliente, en función de ciertas características clave.

``Principales problemas encontrados`` a la hora de la realización del análisis:
* El dataset obtenido a partir de la página data.world es una muestra perteneciente a una base de datos mayor, por lo que el principal desafío a la hora de analizar los productos visitados, ha sido la información faltante, no permitiendo analizar de una forma más precisa los precios y tipos de productos visitados por los clientes, en cierto espacio de tiempo.
* La columna envío se ha considerado un dato de interés ya que permite analizar una de las caracteríscticas que tienen los productos más visitados por clientes, comprendiendo así sus preferencias a la hora de encontrar el producto perfecto. No obstante, dentro de la columna había más de un 40% de datos faltantes, lo cuál se ha intentado solventar a partir de un modelo de clasificación para facilitar el análisis de los productos visitados.
* Ya que sólo se tienen ciertos productos visitados en determinadas fechas, a la hora de realizar el análisis de los precios medios de los productos visitados en función de los meses, se han tenido que aproximar ciertos valores, lo cuál no proporcionaría una predicción muy exacta de como esos precios van a evolucionar en el futuro.
* Para poder realizar un modelo de clasificación en base a las necesidades de los clientes, se ha tenido que crear una nueva columna de categorías de productos, que permita al usuario determinar de una forma más concreta a qué categoría pertenece el producto que está buscando.
* Finalmente, tras la implementación del modelo de clasificación, no se ha podido obtener un accuracy alto en la preddicción debido a que serían necesarios más datos para poder determinar con exactitud aquellas tiendas que se adaptan a diferentes necesidades de los clientes.
      """  )

#--------------------------------------TÍTULO-------------------------------------#



#--------------------------------------SIDEBAR-------------------------------------#
image1 = Image.open(r'img/logo.png')
st.sidebar.image(image1)

#--------------------------------------SIDEBAR-------------------------------------#