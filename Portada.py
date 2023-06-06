import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64


file1_ = open("./Im1.png", "rb")


#Portada
contents1 = file1_.read()
data_url1 = base64.b64encode(contents1).decode("utf-8")
file1_.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url1}" alt="Escudo_Unam">',
    unsafe_allow_html=True,
)


st.title('''UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO\n

            ''',)

st.header('FACULTAD DE ESTUDIOS SUPERIORES ACATLÁN')


st.title('TALLER ALGEBRA LINEAL')

file2 = open("./Fig2.gif", "rb")
contents2 = file2.read()
data_url2 = base64.b64encode(contents2).decode("utf-8")
file2.close()

st.markdown(
    f'<img src="data:image/gif;base64,{data_url2}" alt="Escudo_Unam">',
    unsafe_allow_html=True,
)

st.subheader('Profesor: RIcardo Guzman Fuentes')

r'''
## Organizadores:

### Alexia Fernadez Castañeda

### Oscar David Davila Dominguez

'''



'''
## ÍNDICE

1. Introducción al Álgebra Lineal
   - Definición y conceptos básicos
   - Historia del Álgebra Lineal

2. Vectores en el Espacio
   - Vectores en 2D
   - Vectores en 3D
   - Operaciones con vectores

3. Sistemas de Ecuaciones Lineales
   - Matrices y su representación
   - Solución de sistemas de ecuaciones
   - Eliminación de Gauss-Jordan

4. Espacios Vectoriales
   - Definición de espacio vectorial
   - Propiedades y ejemplos de espacios vectoriales
   - Subespacios vectoriales

5. Transformaciones Lineales
   - Definición y propiedades de las transformaciones lineales
   - Matrices de transformación
   - Aplicaciones prácticas de las transformaciones lineales

6. Diagonalización de Matrices
   - Vectores propios y valores propios
   - Diagonalización de matrices
   - Aplicaciones de la diagonalización

7. Espacios Vectoriales Ortogonales
   - Producto escalar y propiedades
   - Espacios vectoriales ortogonales
   - Proyecciones y mínimos cuadrados

8. Determinantes
   - Definición y propiedades de los determinantes
   - Cálculo de determinantes
   - Aplicaciones de los determinantes

9. Espacios Vectoriales con Producto Interno
   - Espacios vectoriales con producto interno
   - Ortogonalidad y ortonormalidad
   - Bases ortogonales y ortonormales

10. Valores y Vectores Propios
    - Valores y vectores propios
    - Diagonalización de matrices simétricas
    - Aplicaciones de los valores y vectores propios


12. Apéndices
    - A. Álgebra Matricial
    - B. Transforaciones Lineales
    - C. Teoremas y demostraciones
    - D. Campos


'''
