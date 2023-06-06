import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp


st.title('Campos')



r'''

Un campo es una estructura algebraica que cumple ciertos axiomas y propiedades. En este resumen, exploraremos la definición axiomática de un campo y proporcionaremos ejemplos de campos finitos e infinitos.

### Definición Axiomática

Un campo se define como un conjunto no vacío $F$ junto con dos operaciones binarias, suma $(+)$ y multiplicación $(\cdot)$, que cumplen los siguientes axiomas:

1. **Propiedad de cerradura**: Para todo $a, b \in F$, tanto la suma como la multiplicación de $a$ y $b$ están definidas y pertenecen al campo $F$. En otras palabras, $a + b$ y $a \cdot b$ son elementos de $F$.

2. **Propiedad conmutativa**: Para todo $a, b \in F$, la suma y la multiplicación son operaciones conmutativas. Esto significa que $a + b = b + a$ y $a \cdot b = b \cdot a$.

3. **Propiedad asociativa**: Para todo $a, b, c \in F$, la suma y la multiplicación son operaciones asociativas. Es decir, $(a + b) + c = a + (b + c)$ y $(a \cdot b) \cdot c = a \cdot (b \cdot c)$.

4. **Elemento neutro**: Existen dos elementos distintos en $F$ que actúan como elementos neutros para la suma y la multiplicación, denotados como $0$ y $1$ respectivamente. Para todo $a \in F$, se cumple $a + 0 = a$ y $a \cdot 1 = a$.

5. **Elemento opuesto**: Para todo $a \in F$, existe un elemento en $F$, denotado como $-a$, tal que $a + (-a) = 0$.

6. **Elemento inverso**: Para todo $a \in F$ distinto de $0$, existe un elemento en $F$, denotado como $a^{-1}$ o $\frac{1}{a}$, tal que $a \cdot a^{-1} = 1$.

7. **Propiedad distributiva**: Para todo $a, b, c \in F$, la multiplicación se distribuye sobre la suma. Esto significa que $a \cdot (b + c) = (a \cdot b) + (a \cdot c)$.

Cuando un conjunto $F$ y las operaciones de suma y multiplicación cumplen estos axiomas, se dice que $F$ es un campo.

### Ejemplos de Campos

1. **Campo de los números reales**: El conjunto de los números reales $\mathbb{R}$ junto con las operaciones usuales de suma y multiplicación es un campo. Los números reales cumplen todos los axiomas de un campo.

2. **Campo de los números complejos**: El conjunto de los números complejos $\mathbb{C}$ con las operaciones usuales de suma y multiplicación forma un campo. Los números complejos también satisfacen todos los axiomas de un campo.

3. **Campo finito**: Un campo finito es un campo con un número finito de elementos.

Un ejemplo de campo finito es el campo de Galois $\mathbb{GF}(p)$, donde $p$ es un número primo. En este campo, los elementos son congruencias de enteros módulo $p$, y las operaciones de suma y multiplicación se definen de manera similar a la aritmética modular.

4. **Campo de los números racionales**: El conjunto de los números racionales $\mathbb{Q}$ con las operaciones usuales de suma y multiplicación también forma un campo. Los números racionales cumplen todos los axiomas de un campo.

Estos son solo algunos ejemplos de campos, tanto finitos como infinitos. Los campos son objetos fundamentales en matemáticas y encuentran aplicaciones en diversas áreas, como la teoría de números, la criptografía y la geometría algebraica.

'''
