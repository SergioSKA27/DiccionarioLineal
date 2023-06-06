import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64




r'''
# Diagonalización de Matrices

La diagonalización de una matriz es un proceso importante en el álgebra lineal que permite expresar una matriz en términos de una matriz diagonal. Esto proporciona información valiosa sobre las propiedades y el comportamiento de la matriz, así como simplifica los cálculos y análisis relacionados.

## Definición
Una matriz cuadrada $A$ de tamaño $n \times n$ se dice diagonalizable si existe una matriz invertible $P$ de tamaño $n \times n$ tal que $P^{-1}AP$ es una matriz diagonal.

## Proceso de Diagonalización
Para diagonalizar una matriz $A$, se siguen los siguientes pasos:
1. Encontrar los valores propios de la matriz $A$ resolviendo la ecuación característica $|A - \lambda I| = 0$, donde $\lambda$ es el valor propio y $I$ es la matriz identidad.
2. Para cada valor propio $\lambda$, encontrar los vectores propios asociados resolviendo el sistema de ecuaciones $(A - \lambda I)\mathbf{v} = \mathbf{0}$.
3. Construir la matriz $P$ utilizando los vectores propios encontrados, donde cada vector propio es una columna de $P$.
4. Calcular la matriz diagonal $D = P^{-1}AP$.
5. La matriz $A$ está diagonalizada si $D$ es una matriz diagonal.

## Propiedades
La diagonalización de una matriz tiene varias propiedades importantes:
- Las matrices diagonales son fáciles de trabajar y calcular, ya que todas sus entradas fuera de la diagonal son cero.
- Los valores propios de una matriz diagonal son simplemente las entradas diagonales.
- Si una matriz tiene $n$ valores propios distintos, entonces es diagonalizable.
- Si una matriz tiene menos de $n$ valores propios distintos, es posible que no sea diagonalizable.
- Si una matriz tiene un solo valor propio, pero su multiplicidad algebraica y su multiplicidad geométrica no coinciden, entonces no es diagonalizable.

## Ejemplo
Consideremos la matriz $A = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$. Siguiendo los pasos de diagonalización, encontramos que los valores propios son $\lambda_1 = 3$ y $\lambda_2 = 2$. Los vectores propios asociados son $\mathbf{v}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$ y $\mathbf{v}_2 = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$. La matriz $P$ se construye con los vectores propios como columnas: $P = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix}$. Calculando $P^{-1}AP$, obtenemos la matriz diagonal $D = \begin{bmatrix} 3 & 0 \\ 0 & 2 \end{bmatrix}$. Por lo tanto, la matriz $A$ está diagonalizada.


# Valores y Vectores Propios

En el álgebra lineal, los valores y vectores propios son conceptos fundamentales para comprender las propiedades y el comportamiento de una matriz. Los valores propios (también conocidos como autovalores) y los vectores propios (también conocidos como autovectores) nos permiten entender cómo una matriz transforma y escala los vectores en el espacio.

## Definición

Dada una matriz cuadrada $A$ de tamaño $n \times n$, un valor propio de $A$ es un escalar $\lambda$ que satisface la ecuación:

$$A\mathbf{v} = \lambda\mathbf{v}$$

donde $\mathbf{v}$ es un vector no nulo llamado vector propio asociado al valor propio $\lambda$. En otras palabras, cuando una matriz $A$ se multiplica por su vector propio, el resultado es un múltiplo escalar del mismo vector propio.

## Ejemplo

Consideremos la matriz $A = \begin{bmatrix} 3 & 1 \\ 0 & 2 \end{bmatrix}$. Para encontrar los valores y vectores propios, resolvemos la ecuación característica $|A - \lambda I| = 0$, donde $I$ es la matriz identidad y $\lambda$ es el valor propio:

$$\begin{vmatrix} 3-\lambda & 1 \\ 0 & 2-\lambda \end{vmatrix} = (3-\lambda)(2-\lambda) - 0 \cdot 1 = 0$$

Expandiendo y simplificando, obtenemos la ecuación $\lambda^2 - 5\lambda + 6 = 0$. Resolviendo esta ecuación, encontramos que los valores propios son $\lambda_1 = 3$ y $\lambda_2 = 2$.

Para encontrar los vectores propios asociados, resolvemos las ecuaciones $(A - \lambda I)\mathbf{v} = \mathbf{0}$ para cada valor propio.

Para $\lambda_1 = 3$, tenemos:

$$\begin{bmatrix} 3-3 & 1 \\ 0 & 2-3 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Simplificando, obtenemos la ecuación $x + y = 0$, que representa la recta $y = -x$. Por lo tanto, el vector propio asociado a $\lambda_1$ es cualquier vector de la forma $\begin{bmatrix} t \\ -t \end{bmatrix}$, donde $t$ es un escalar no nulo.

Para $\lambda_2 = 2$, tenemos:

$$\begin{bmatrix} 3-2 & 1 \\ 0 & 2-2 \end{bmatrix}\begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}$$

Simplificando, obtenemos la ecuación $x + y = 0$, que también representa la recta $y = -x$. Por lo tanto, el vector propio asociado a $\lambda_2$ es cualquier vector de la forma $\begin{bmatrix} t \\ -t \end{bmatrix}$, donde $t$ es un escalar no nulo.

En resumen, los valores propios de $A$ son $\lambda_1 = 3$ y $\lambda_2 = 2$, y los vectores propios asociados son de la forma $\begin{bmatrix} t \\ -t \end{bmatrix}$, donde $t$ es un escalar no nulo.




# Aplicaciones de la Diagonalización

La diagonalización de matrices es un concepto fundamental en el álgebra lineal y tiene numerosas aplicaciones en diversos campos de las matemáticas y la ciencia. A continuación, exploraremos algunas de las principales aplicaciones de la diagonalización.

## Diagonalización y Potencias de Matrices
La diagonalización de una matriz $A$ permite simplificar la expresión de sus potencias. Si $A = PDP^{-1}$, donde $D$ es una matriz diagonal, entonces podemos expresar $A^n$ de la siguiente manera:

$$A^n = (PDP^{-1})^n = PD^nP^{-1}$$

Dado que $D$ es una matriz diagonal, elevarla a la potencia $n$ simplemente implica elevar cada uno de sus elementos diagonales a la potencia $n$. Esto simplifica significativamente el cálculo de potencias de matrices.

## Diagonalización y Resolución de Sistemas de Ecuaciones
La diagonalización también se utiliza en la resolución de sistemas de ecuaciones lineales. Considere un sistema de ecuaciones lineales representado por la matriz aumentada $\begin{bmatrix} A | \mathbf{b} \end{bmatrix}$, donde $A$ es una matriz cuadrada. Si $A$ es diagonalizable, podemos utilizar la diagonalización para resolver el sistema de ecuaciones.

Al diagonalizar $A$ como $A = PDP^{-1}$, donde $D$ es una matriz diagonal y $P$ es una matriz invertible, podemos reescribir el sistema de ecuaciones como $PDP^{-1} \mathbf{x} = \mathbf{b}$. Luego, multiplicando ambos lados por $P^{-1}$, obtenemos $D \mathbf{x}' = P^{-1} \mathbf{b}$, donde $\mathbf{x}' = P^{-1} \mathbf{x}$.

Dado que $D$ es una matriz diagonal, el sistema de ecuaciones se reduce a un conjunto de ecuaciones lineales independientes, donde cada ecuación es de la forma $d_i x_i' = b_i'$, donde $d_i$ es el $i$-ésimo elemento diagonal de $D$, $x_i'$ es la $i$-ésima componente de $\mathbf{x}'$, y $b_i'$ es la $i$-ésima componente de $P^{-1} \mathbf{b}$. Estas ecuaciones se pueden resolver fácilmente para obtener las soluciones correspondientes de $\mathbf{x}'$, y luego se puede encontrar $\mathbf{x}$ aplicando la transformación inversa $\mathbf{x} = P \mathbf{x}'$.

## Diagonalización y Estabilidad de Sistemas Dinámicos
La diagonalización también es útil en el estudio de la estabilidad de sistemas dinámicos. Considere un sistema dinámico descrito por una matriz de transición $A$. Si $A$ es diagonalizable, la diagonalización $A = PDP^{-1}$ proporciona información valiosa sobre la estabilidad del sistema.

Los valores propios de $A$, que son las entradas diagonales de $D$, determinan la estabilidad del sistema. Si todos los valores propios tienen magnitud menor que 1, el sistema es estable y converge a un estado estacionario. Si al menos uno de los valores propios tiene magnitud mayor que 1, el sistema es inestable y puede diverg

ir a lo largo del tiempo.

## Diagonalización y Descomposición Espectral
La diagonalización también está relacionada con la descomposición espectral de matrices simétricas. Una matriz simétrica $A$ se puede diagonalizar como $A = PDP^T$, donde $D$ es una matriz diagonal y $P$ es una matriz ortogonal compuesta por los vectores propios de $A$. Esta descomposición espectral es especialmente útil en problemas de análisis de datos y procesamiento de señales, donde se pueden extraer características importantes de los datos mediante la descomposición espectral.

Estas son solo algunas de las aplicaciones de la diagonalización en el álgebra lineal. La capacidad de diagonalizar una matriz proporciona una mayor comprensión y simplificación de diversas operaciones y problemas en matemáticas y ciencia.
'''
