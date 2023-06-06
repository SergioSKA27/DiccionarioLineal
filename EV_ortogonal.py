import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64




r'''

# Espacios Vectoriales Ortogonales

En el álgebra lineal, los espacios vectoriales ortogonales juegan un papel fundamental en el estudio de la geometría y las propiedades de los vectores. Un espacio vectorial ortogonal es aquel en el que todos los vectores son perpendiculares entre sí. A continuación, exploraremos la definición y algunas propiedades de los espacios vectoriales ortogonales.

## Definición
Dado un espacio vectorial $V$ sobre un campo escalar $\mathbb{F}$, decimos que dos vectores $\mathbf{u}$ y $\mathbf{v}$ en $V$ son ortogonales si su producto interno es cero. El producto interno de dos vectores $\mathbf{u}$ y $\mathbf{v}$ se denota como $\langle \mathbf{u}, \mathbf{v} \rangle$ y se define como:

$$\langle \mathbf{u}, \mathbf{v} \rangle = \mathbf{u} \cdot \mathbf{v} = \sum_{i=1}^n u_i v_i$$

donde $n$ es la dimensión de los vectores y $u_i$ y $v_i$ son las componentes correspondientes de $\mathbf{u}$ y $\mathbf{v}$ respectivamente.

## Propiedades de los Espacios Vectoriales Ortogonales

- **Propiedad Reflexiva**: Un vector $\mathbf{u}$ es ortogonal a sí mismo, es decir, $\langle \mathbf{u}, \mathbf{u} \rangle = 0$ si y solo si $\mathbf{u} = \mathbf{0}$, donde $\mathbf{0}$ es el vector cero.

- **Propiedad Simétrica**: Si $\mathbf{u}$ es ortogonal a $\mathbf{v}$, entonces $\mathbf{v}$ es ortogonal a $\mathbf{u}$, es decir, $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$.

- **Propiedad Lineal**: Si $\mathbf{u}$ y $\mathbf{v}$ son ortogonales, y $a$ y $b$ son escalares, entonces $a\mathbf{u} + b\mathbf{v}$ también es ortogonal a ambos $\mathbf{u}$ y $\mathbf{v}$.

- **Propiedad de Combinación Lineal**: Si $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n$ son vectores ortogonales, y $a_1, a_2, \ldots, a_n$ son escalares, entonces la combinación lineal $a_1\mathbf{u}_1 + a_2\mathbf{u}_2 + \ldots + a_n\mathbf{u}_n$ también es ortogonal a todos los vectores $\mathbf{u}_i$.

## Ejemplo

Consideremos el espacio vectorial $\mathbb{R}^3$ con los vectores $\mathbf{u} = (1, 2, 3)$ y $\mathbf{v} = (4, -2, 1)$. Para determinar si estos vectores son ortogonales, calculamos su producto interno:

$$\langle \mathbf{u}, \mathbf{v} \rangle = (1)(4) + (2)(-2) + (3)(1) = 4 - 4 + 3 = 3$$

Como el producto interno es diferente de cero, concluimos que los vectores $\mathbf{u}$ y $\mathbf{v}$ no son ortogonales.

Los espacios vectoriales ortogonales son fundamentales en diversas áreas de las matemáticas y la física, especialmente en el estudio de la geometría euclidiana y en el análisis de sistemas de ecuaciones lineales. El concepto de ortogonalidad permite caracterizar la independencia y la relación entre vectores, y es fundamental en la construcción de bases ortogonales y la resolución de problemas de optimización.

'''




r'''

# Proyecciones y Mínimos Cuadrados

En el álgebra lineal, las proyecciones y los mínimos cuadrados son conceptos fundamentales que se utilizan para aproximar y resolver problemas en diversas áreas, como el análisis de datos, la estadística y la optimización. A continuación, exploraremos la idea de la proyección de un vector sobre un subespacio y su relación con el concepto de mínimos cuadrados.

## Proyección de un vector sobre un subespacio
Dado un vector $\mathbf{v}$ en un espacio vectorial $V$, la proyección de $\mathbf{v}$ sobre un subespacio $U$ de $V$ es el vector más cercano a $\mathbf{v}$ en $U$. Este vector proyectado se denota como $\text{proj}_U(\mathbf{v})$. La proyección de $\mathbf{v}$ sobre $U$ se obtiene sumando las componentes de $\mathbf{v}$ que son paralelas a los vectores de $U$.

La fórmula para calcular la proyección de $\mathbf{v}$ sobre $U$ se puede expresar de la siguiente manera:

$$\text{proj}_U(\mathbf{v}) = \frac{\langle \mathbf{v}, \mathbf{u}_1 \rangle}{\|\mathbf{u}_1\|^2}\mathbf{u}_1 + \frac{\langle \mathbf{v}, \mathbf{u}_2 \rangle}{\|\mathbf{u}_2\|^2}\mathbf{u}_2 + \ldots + \frac{\langle \mathbf{v}, \mathbf{u}_n \rangle}{\|\mathbf{u}_n\|^2}\mathbf{u}_n$$

donde $\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n$ son los vectores que forman una base de $U$ y $\langle \cdot, \cdot \rangle$ representa el producto interno.

## Mínimos Cuadrados
El método de mínimos cuadrados es una técnica utilizada para aproximar una relación lineal entre variables cuando existen errores o ruido en los datos. Dado un conjunto de datos $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$, se busca encontrar una línea (en el caso de una regresión lineal) o una función (en el caso de una regresión polinomial) que se ajuste mejor a los datos en el sentido de minimizar la suma de los cuadrados de las diferencias entre los valores predichos y los valores reales.

La solución del método de mínimos cuadrados se puede obtener utilizando proyecciones. Consideremos el caso de una regresión lineal, donde se busca ajustar una línea de la forma $y = mx + b$ a los datos. La proyección de los puntos $(x_1, y_1), (x_2, y_2), \ldots, (x_n, y_n)$ sobre la recta de ajuste proporciona los valores predichos $\hat{y}_1, \hat{y}_2, \ldots, \hat{y}_n$. Los coeficientes $m$ y $b$ se eligen de manera que la suma de los cuadrados de las diferencias

 entre los valores predichos y los valores reales sea mínima.

## Ejemplo
Supongamos que tenemos un conjunto de datos que representa el precio de algunas casas en función de su tamaño. Queremos ajustar una línea de regresión lineal a estos datos para predecir el precio de una casa dado su tamaño.

Los datos se pueden representar de la siguiente manera:

| Tamaño ($x$) | Precio ($y$) |
|--------------|--------------|
| 1500         | 200000       |
| 2000         | 250000       |
| 2500         | 300000       |
| 3000         | 350000       |
| 3500         | 400000       |



Para ajustar una línea de regresión lineal a estos datos, utilizamos el método de mínimos cuadrados. Aplicando la fórmula de proyección, obtenemos los coeficientes $m$ y $b$ de la línea de ajuste. Luego, podemos utilizar estos coeficientes para predecir el precio de una casa dada su tamaño.

Los resultados obtenidos podrían ser, por ejemplo, $m = 100$ y $b = 150000$, lo que significa que la línea de ajuste sería $y = 100x + 150000$. Utilizando esta ecuación, podemos predecir el precio de una casa de tamaño 2700 pies cuadrados, obteniendo un valor predicho de $y = 100(2700) + 150000 = 420000$.

La proyección y el método de mínimos cuadrados son herramientas poderosas en el análisis de datos y la modelización de relaciones lineales. Estas técnicas nos permiten encontrar una aproximación óptima y hacer predicciones basadas en los datos disponibles.
'''
