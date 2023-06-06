
import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp



r'''
## Solución de Sistemas de Ecuaciones Lineales y Métodos de Resolución

El estudio de los sistemas de ecuaciones lineales es fundamental en el ámbito del álgebra lineal. Estos sistemas se componen de un conjunto de ecuaciones lineales, donde se busca encontrar los valores de las incógnitas que satisfacen todas las ecuaciones simultáneamente. En este artículo, exploraremos algunos métodos comunes para resolver sistemas de ecuaciones lineales y proporcionaremos ejemplos ilustrativos.

### Definición de un sistema de ecuaciones lineales

Un sistema de ecuaciones lineales se representa de la siguiente manera:

$$
\begin{align*}
a_{11}x_1 + a_{12}x_2 + \ldots + a_{1n}x_n &= b_1 \\
a_{21}x_1 + a_{22}x_2 + \ldots + a_{2n}x_n &= b_2 \\
\vdots \\
a_{m1}x_1 + a_{m2}x_2 + \ldots + a_{mn}x_n &= b_m \\
\end{align*}
$$

Donde $x_1, x_2, \ldots, x_n$ son las incógnitas del sistema, $a_{ij}$ son los coeficientes de las variables y $b_i$ son los términos constantes.

### Resolución de sistemas de ecuaciones lineales

Existen varios métodos para resolver sistemas de ecuaciones lineales. A continuación, presentaremos algunos de los métodos más utilizados.



El método de eliminación gaussiana, también conocido como el método de eliminación de Gauss-Jordan, es un método directo para resolver sistemas de ecuaciones lineales. El objetivo es transformar el sistema original en uno equivalente que sea más fácil de resolver. El proceso consta de tres pasos principales:


### Método de Gauss

El método de Gauss, también conocido como eliminación gaussiana, es un método sistemático para resolver sistemas de ecuaciones lineales. Consiste en aplicar una serie de operaciones elementales de fila para triangularizar el sistema y luego obtener las soluciones mediante sustitución hacia atrás.

El proceso del método de Gauss se puede describir en los siguientes pasos:

1. **Escalonamiento**: El objetivo es convertir el sistema de ecuaciones en una forma escalonada o triangular superior, donde los coeficientes por debajo de la diagonal principal son cero. Para lograrlo, se aplican las siguientes operaciones elementales de fila:

   - Intercambio de filas: Se intercambian dos filas para ordenar las ecuaciones o para evitar divisiones por cero.
   - Multiplicación de una fila por un escalar no nulo: Se multiplica una fila por un número distinto de cero para obtener un coeficiente deseado.
   - Combinación lineal de filas: Se suma o resta un múltiplo de una fila a otra fila para eliminar los coeficientes.

2. **Sustitución hacia atrás**: Una vez que el sistema está en forma escalonada, se resuelve comenzando desde la última ecuación y sustituyendo los valores conocidos hacia atrás. Se obtienen los valores de las incógnitas restantes.

3. **Comprobación**: Se verifica si las soluciones encontradas satisfacen todas las ecuaciones del sistema original.

Veamos un ejemplo para ilustrar el método de eliminación gaussiana. Consideremos el siguiente sistema de ecuaciones lineales:

$$
\begin{align*}
2x + 3y - z &= 7 \\
4x - y + 2z &= 4 \\
x - 2y + 3z &= 9 \\
\end{align*}
$$

Aplicando el método de eliminación gaussiana, obtenemos:

Paso 1: Eliminación hacia adelante
$$
\begin{align*}
2x + 3y - z &= 7 \\
0x - 7y + 4z &= -10 \\
0x - 0y + \frac{37}{7}z &= \frac{20}{7} \\
\end{align*}
$$

Paso 2: Sustitución hacia atrás
$$
\begin{align*}
x &= \frac{10}{37} \\
y &= \frac{4}{37} \\
z &= \frac{20}{37} \\
\end{align*}
$$

Paso 3: Comprobación
Sustituyendo los valores encontrados en las ecuaciones originales, verificamos que se cumplan.





El método de Gauss es ampliamente utilizado debido a su eficiencia y simplicidad. Sin embargo, puede haber casos en los que el método no sea adecuado, como cuando la matriz de coeficientes es singular o si el sistema tiene múltiples soluciones.

### Regla de Cramer

La regla de Cramer es un método alternativo para resolver sistemas de ecuaciones lineales utilizando determinantes. Este método se basa en la teoría de matrices y se utiliza para encontrar las soluciones únicas del sistema.

La regla de Cramer establece que si tenemos un sistema de ecuaciones lineales $AX = B$, donde $A$ es la matriz de coeficientes, $X$ es el vector de incógnitas y $B$ es el vector de términos constantes, entonces la solución para la incógnita $x_i$ se calcula mediante la siguiente fórmula:

$$
x_i = \frac{{\det(A_i)}}{{\det(A)}}
$$

donde $A_i$ se obtiene reemplazando la columna $i$ de $A$ por el vector $B$, y $\det(A)$ es el determinante de la matriz de coeficientes $A$.

Es importante destacar que la regla de Cramer solo es aplicable cuando la matriz de coeficientes $A$ es invertible, es decir, cuando su determinante $\det(A)$ es diferente de cero. Además, este método puede resultar computacionalmente costoso en sistemas grandes debido a la necesidad de calcular determinantes.

La regla de Cramer proporciona una forma elegante de resolver sistemas de ecuaciones lineales, especialmente cuando se busca una solución única. Sin embargo, en la práctica, se prefieren otros métodos más eficientes, como la eliminación gaussiana, cuando se trata de sistemas grandes o cuando se necesitan soluciones aproximadas.


#### Método de la matriz inversa

Otro método común para resolver sistemas de ecuaciones lineales es el método de la matriz inversa. En este método, se utiliza la propiedad de la matriz inversa para obtener la solución del sistema. El proceso consta de los siguientes pasos:

1. Se escribe el sistema de ecuaciones en forma matricial: $AX = B$, donde $A$ es la matriz de coeficientes, $X$ es el vector de incógnitas y $B$ es el vector de términos constantes.

2. Se calcula la matriz inversa de $A$, si existe. Si la matriz inversa no existe, significa que el sistema no tiene solución única.

3. Se multiplica la matriz inversa por el vector de términos constantes: $X = A^{-1}B$, obteniendo así la solución del sistema.

Veamos un ejemplo para ilustrar el método de la matriz inversa. Consideremos el siguiente sistema de ecuaciones lineales:

$$
\begin{align*}
2x + 3y &= 5 \\
4x - y &= 1 \\
\end{align*}
$$

Escribiendo el sistema en forma matricial, tenemos:

$$
\begin{bmatrix}
2 & 3 \\
4 & -1 \\
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
\end{bmatrix}
=
\begin{bmatrix}
5 \\
1 \\
\end{bmatrix}
$$

Calculando la matriz inversa de $A = \begin{bmatrix}2 & 3 \\ 4 & -1\end{bmatrix}$, obtenemos $A^{-1} = \begin{bmatrix}0.1667 & 0.5 \\ 0.3333 & -0.3333\end{bmatrix}$.

Multiplicando $A^{-1}$ por el vector $B = \begin{bmatrix}5 \\ 1\end{bmatrix}$, obtenemos:

$$
\begin{bmatrix}
x \\
y \\
\end{bmatrix}
=
\begin{bmatrix}
0.1667 & 0.5 \\
0.3333 & -0.3333 \\
\end{bmatrix}
\begin{bmatrix}
5 \\
1 \\
\end{bmatrix}
=
\begin{bmatrix}
1.5 \\
0.6667 \\
\end{bmatrix}
$$

Por lo tanto, la solución del sistema de ecuaciones lineales es $x = 1.5$ y $y = 0.6667$.


'''
