import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64



r'''
# Determinante

En el álgebra lineal, el determinante es una función que se aplica a una matriz cuadrada y proporciona información importante sobre las propiedades y el comportamiento de la matriz. El determinante es un concepto fundamental y tiene diversas aplicaciones en áreas como la resolución de sistemas de ecuaciones lineales, el cálculo de áreas y volúmenes, y el estudio de transformaciones lineales. A continuación, exploraremos la definición del determinante y algunas de sus propiedades clave.

## Definición del determinante
Dado una matriz cuadrada $A$, el determinante de $A$ se denota como $\det(A)$ o $|A|$. La definición del determinante depende del tamaño de la matriz. Para una matriz de tamaño 1x1, el determinante es simplemente el único elemento de la matriz. Para una matriz de tamaño 2x2, el determinante se calcula de la siguiente manera:

$$\det(A) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

Para una matriz de tamaño 3x3 o superior, el determinante se calcula utilizando la regla de Sarrus o mediante la expansión de cofactores.

## Propiedades de los determinantes
Los determinantes tienen varias propiedades que los hacen útiles y fáciles de calcular. A continuación, se presentan algunas de las propiedades más importantes:

1. El determinante de la matriz identidad es igual a 1: $\det(I) = 1$, donde $I$ es la matriz identidad.
2. El determinante de una matriz triangular (superior o inferior) es igual al producto de los elementos de la diagonal principal.
3. Si intercambiamos dos filas (o columnas) de una matriz, el determinante cambia de signo: $\det(-A) = -\det(A)$.
4. Si multiplicamos una fila (o columna) de una matriz por un escalar $k$, el determinante se multiplica por el mismo escalar: $\det(kA) = k^n \cdot \det(A)$, donde $n$ es el tamaño de la matriz.
5. Si dos filas (o columnas) de una matriz son iguales, el determinante de esa matriz es cero.
6. Si una fila (o columna) de una matriz consiste en ceros, el determinante de esa matriz es cero.
7. Si sumamos (o restamos) un múltiplo de una fila (o columna) a otra fila (o columna), el determinante no se ve afectado.
8. El determinante de una matriz multiplicada por su matriz inversa es igual a 1: $\det(A \cdot A^{-1}) = 1$, siempre y cuando la matriz inversa exista.

Estas propiedades son fundamentales para el cálculo de determinantes y facilitan la simplificación de cálculos complejos.

## Ejemplo
Consideremos la siguiente matriz 3x3:

$$A = \begin{pmatrix} 2 & 1 & 3 \\ 0 & -1 & 2 \\ 4 & 3 & 5 \end{pmatrix}$$

Para calcular el determinante de esta matriz, podemos utilizar la regla de Sarrus:

$$\det(A) = (2 \cdot -1 \cdot 5) + (1 \cdot 2 \cdot 4) + (3 \cdot 0 \cdot 3) - (3 \cdot -1 \cdot 4) - (2 \cdot 2 \cdot 5) - (1 \cdot 0 \cdot 3) = -35$$

Por lo tanto, el determinante de la matriz $A$ es igual a -35.



# Regla de Sarrus

La regla de Sarrus es un método utilizado para calcular el determinante de una matriz cuadrada de tamaño 3x3. Esta regla simplifica el cálculo del determinante al utilizar una serie de productos diagonales y sumas. A continuación, se presenta la regla de Sarrus y se proporciona un ejemplo para ilustrar su aplicación.

## Regla de Sarrus
Dado una matriz cuadrada 3x3:

$$A = \begin{pmatrix} a & b & c \\ d & e & f \\ g & h & i \end{pmatrix}$$

El determinante de esta matriz, denotado como $\det(A)$ o $|A|$, se puede calcular utilizando la regla de Sarrus de la siguiente manera:

$$\det(A) = (aei + bfg + cdh) - (ceg + afh + bdi)$$

En la fórmula anterior, los términos de la suma se obtienen multiplicando los elementos en las diagonales ascendentes y restando los productos de los elementos en las diagonales descendentes.

## Ejemplo
Consideremos la siguiente matriz 3x3:

$$A = \begin{pmatrix} 2 & 1 & 3 \\ 0 & -1 & 2 \\ 4 & 3 & 5 \end{pmatrix}$$

Aplicando la regla de Sarrus, podemos calcular el determinante de la matriz de la siguiente manera:

$$\det(A) = (2 \cdot -1 \cdot 5) + (1 \cdot 2 \cdot 4) + (3 \cdot 0 \cdot 3) - (3 \cdot -1 \cdot 4) - (2 \cdot 2 \cdot 5) - (1 \cdot 0 \cdot 3) = -35$$

Por lo tanto, el determinante de la matriz $A$ es igual a -35.

La regla de Sarrus es un método sencillo y práctico para calcular el determinante de matrices de tamaño 3x3. Aunque es específico para esta dimensión, existen métodos más generales para calcular determinantes de matrices de mayor tamaño. Sin embargo, la regla de Sarrus sigue siendo útil y se utiliza como base para comprender y aplicar métodos más complejos en el cálculo de determinantes.


# Expansión por Cofactores

La expansión por cofactores es un método utilizado para calcular el determinante de una matriz de cualquier tamaño. Este método se basa en descomponer el determinante en una suma de productos de elementos de la matriz multiplicados por sus cofactores correspondientes. A continuación, se presenta la expansión por cofactores y se proporciona un ejemplo para ilustrar su aplicación.

## Expansión por Cofactores
Dada una matriz cuadrada $A$ de tamaño $n \times n$, el determinante de $A$ se puede calcular mediante la expansión por cofactores de la siguiente manera:

$$\det(A) = \sum_{i=1}^{n} a_{ij} \cdot C_{ij}$$

En la fórmula anterior, $a_{ij}$ representa el elemento de la matriz $A$ en la fila $i$ y la columna $j$, y $C_{ij}$ es el cofactor correspondiente al elemento $a_{ij}$.

El cofactor $C_{ij}$ se define como el determinante de la submatriz que se obtiene al eliminar la fila $i$ y la columna $j$ de la matriz original $A$, multiplicado por $(-1)^{i+j}$ para tener en cuenta el patrón de signo alternante.

## Ejemplo
Consideremos la siguiente matriz 3x3:

$$A = \begin{pmatrix} 2 & 1 & 3 \\ 0 & -1 & 2 \\ 4 & 3 & 5 \end{pmatrix}$$

Podemos calcular el determinante de esta matriz utilizando la expansión por cofactores. Primero, seleccionamos una fila o una columna de la matriz y calculamos los cofactores correspondientes. Por ejemplo, seleccionemos la primera fila:

$$\det(A) = 2 \cdot C_{11} + 1 \cdot C_{12} + 3 \cdot C_{13}$$

Calculamos los cofactores correspondientes utilizando la definición anterior. Por ejemplo, el cofactor $C_{11}$ se calcula tomando el determinante de la submatriz que se obtiene al eliminar la primera fila y la primera columna de la matriz $A$:

$$C_{11} = \begin{vmatrix} -1 & 2 \\ 3 & 5 \end{vmatrix} = (-1 \cdot 5) - (2 \cdot 3) = -11$$

De manera similar, calculamos los cofactores $C_{12}$ y $C_{13}$ correspondientes. Luego, reemplazamos estos valores en la fórmula de la expansión por cofactores para obtener el determinante de la matriz $A$.

$$\det(A) = 2 \cdot (-11) + 1 \cdot C_{12} + 3 \cdot C_{13}$$

Continuamos calculando los cofactores $C_{12}$ y $C_{13}$ y reemplazamos los valores correspondientes hasta obtener el determinante final.

Por lo tanto, el determinante de la matriz $A$ es igual a -35.

La expansión por cofactores es un método general para calcular determinantes de matrices de cualquier tamaño. Aunque puede ser laborioso para matrices grandes, es una herramienta esencial en el álgebra lineal y permite comprender y analizar las propiedades de las matrices y las transformaciones lineales.


# Aplicaciones de los determinantes

Los determinantes son herramientas fundamentales en el álgebra lineal y tienen una amplia gama de aplicaciones en diversas áreas de las matemáticas y la ciencia. A continuación, se presentan algunas de las aplicaciones más comunes de los determinantes.

## 1. Determinar la invertibilidad de una matriz
El determinante de una matriz cuadrada se utiliza para determinar si la matriz es invertible o singular. Si el determinante es diferente de cero, la matriz es invertible y tiene una matriz inversa. Si el determinante es cero, la matriz es singular y no tiene inversa.

## 2. Resolver sistemas de ecuaciones lineales
Los determinantes también se utilizan para resolver sistemas de ecuaciones lineales. Al expresar un sistema de ecuaciones lineales en forma matricial, podemos utilizar los determinantes para determinar si el sistema tiene solución única, infinitas soluciones o ninguna solución.

## 3. Calcular áreas y volúmenes
En geometría, los determinantes se utilizan para calcular áreas de paralelogramos y volúmenes de paralelepípedos. El valor absoluto del determinante de una matriz formada por los vectores que definen los lados de la figura geométrica proporciona su área o volumen.

## 4. Encontrar intersecciones y puntos de corte
Los determinantes se utilizan en la geometría analítica para determinar la intersección de líneas y planos. Al analizar las ecuaciones de las líneas y los planos involucrados, se pueden formar matrices y utilizar los determinantes para encontrar los puntos de intersección o los puntos de corte.

## 5. Calcular la orientación de un conjunto de puntos
En geometría computacional, los determinantes se utilizan para determinar la orientación de un conjunto de puntos en el plano. Al tomar tres puntos consecutivos, el signo del determinante formado por sus coordenadas indica si los puntos están dispuestos en sentido horario o antihorario.

## 6. Diagonalización de matrices
Los determinantes también desempeñan un papel importante en la diagonalización de matrices. Un matriz cuadrada es diagonalizable si y solo si todos sus valores propios son distintos, y esto se verifica utilizando los determinantes de las matrices formadas por las diferencias entre los valores propios.

Estas son solo algunas de las aplicaciones más comunes de los determinantes. Su versatilidad y utilidad los convierten en herramientas esenciales para el estudio y la comprensión de la geometría, el álgebra lineal, la física, la estadística y muchas otras áreas de las matemáticas y la ciencia.




'''
