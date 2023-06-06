import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64



r'''
# Valores y Vectores Propios

En el álgebra lineal, los valores propios y los vectores propios son conceptos fundamentales que se utilizan para analizar transformaciones lineales y matrices. Proporcionan información importante sobre las propiedades y el comportamiento de estas transformaciones y matrices. A continuación, se explica en qué consisten los valores y vectores propios y se presentan definiciones y teoremas más rigurosos.

## Valores Propios

Sea $A$ una matriz cuadrada de tamaño $n\times n$. Un número complejo $\lambda$ se denomina valor propio (o autovalor) de la matriz $A$ si existe un vector no nulo $\mathbf{v}$ tal que se cumple la siguiente ecuación:

$$A\mathbf{v} = \lambda \mathbf{v}$$

Esta ecuación puede ser reescrita como:

$$(A - \lambda I)\mathbf{v} = \mathbf{0}$$

donde $I$ es la matriz identidad de tamaño $n\times n$ y $\mathbf{0}$ es el vector nulo de tamaño $n\times 1$.

La ecuación $(A - \lambda I)\mathbf{v} = \mathbf{0}$ tiene soluciones no triviales si y solo si la matriz $(A - \lambda I)$ no es invertible, es decir, su determinante es igual a cero. Esto lleva a la siguiente definición de valores propios:

**Definición 1:** Un número complejo $\lambda$ es un valor propio de la matriz $A$ si $\det(A - \lambda I) = 0$.

La ecuación $\det(A - \lambda I) = 0$ se conoce como la ecuación característica de la matriz $A$. Los valores propios son las raíces de esta ecuación.

## Vectores Propios

Dado un valor propio $\lambda$ de la matriz $A$, un vector no nulo $\mathbf{v}$ se denomina vector propio asociado a $\lambda$ si satisface la ecuación:

$$A\mathbf{v} = \lambda \mathbf{v}$$

Esta ecuación puede ser reescrita como:

$$(A - \lambda I)\mathbf{v} = \mathbf{0}$$

El conjunto de todos los vectores propios asociados a un valor propio $\lambda$ forma un subespacio vectorial llamado espacio propio correspondiente a $\lambda$.

## Teoremas y Propiedades

A continuación, se presentan algunos teoremas y propiedades importantes relacionados con los valores y vectores propios:

**Teorema 1:** Si $\lambda$ es un valor propio de la matriz $A$, entonces $\lambda^k$ es un valor propio de la matriz $A^k$ para cualquier entero positivo $k$.

**Teorema 2:** Si $\mathbf{v}$ es un vector propio asociado a $\lambda$ para la matriz $A$, entonces cualquier múltiplo escalar de $\mathbf{v}$ también es un vector propio asociado a $\lambda$.

**Propiedad 1:** La suma de los valores propios de una matriz $A$ es igual a la traza de la matriz, es decir, $\sum_{i=1}^{n}\lambda_i = \text{tr}(A)$.

**Propiedad 2:** El producto de los valores propios de una matriz

 $A$ es igual al determinante de la matriz, es decir, $\prod_{i=1}^{n}\lambda_i = \det(A)$.

## Aplicaciones de los Valores y Vectores Propios

Los valores y vectores propios tienen numerosas aplicaciones en diversas áreas, incluyendo la física, la ingeniería, la ciencia de datos y la computación. Algunas de las aplicaciones más comunes incluyen:

- Diagonalización de matrices: Los valores propios y los vectores propios permiten diagonalizar matrices, lo que simplifica muchos cálculos y análisis.
- Estabilidad de sistemas dinámicos: Los valores propios se utilizan para analizar la estabilidad de sistemas dinámicos, como en la teoría de control.
- Análisis de redes y grafos: Los valores y vectores propios se utilizan para analizar la estructura y la conectividad de redes y grafos.
- Compresión de datos: Los valores y vectores propios se utilizan en técnicas de compresión de datos, como la descomposición en valores singulares (SVD).




# Diagonalización de Matrices Simétricas

En el álgebra lineal, la diagonalización de matrices simétricas es un proceso fundamental que permite descomponer una matriz en una forma diagonal mediante una matriz de cambio de base. Las matrices simétricas tienen propiedades especiales que facilitan su diagonalización y ofrecen diversas aplicaciones en diferentes áreas. En este artículo, exploraremos en detalle el concepto de diagonalización de matrices simétricas, sus propiedades y algunas aplicaciones importantes.

## Definición

Sea $A$ una matriz cuadrada de tamaño $n\times n$. Diremos que $A$ es simétrica si se cumple que $A = A^T$, es decir, si la matriz es igual a su traspuesta. Esta propiedad implica que los elementos de la matriz se reflejan a lo largo de su diagonal principal. La diagonalización de una matriz simétrica consiste en encontrar una matriz diagonal $D$ y una matriz de cambio de base $P$ tal que se cumpla la siguiente relación:

$$A = PDP^{-1}$$

Donde $D$ es una matriz diagonal cuyos elementos son los valores propios de $A$, y $P$ es una matriz cuyas columnas son los vectores propios correspondientes a los valores propios de $A$. Esta descomposición permite simplificar muchos cálculos y análisis de la matriz original.

## Propiedades

La diagonalización de matrices simétricas tiene propiedades importantes que se derivan de la simetría y de la naturaleza de los valores y vectores propios:

1. **Simetría de la matriz diagonal**: Si $A$ es una matriz simétrica y $A = PDP^{-1}$ es su descomposición diagonal, entonces la matriz diagonal $D$ también es simétrica. Esto se debe a que $D$ está compuesta por los valores propios de $A$, los cuales son reales debido a la simetría de la matriz.

2. **Vectores propios ortogonales**: Los vectores propios correspondientes a valores propios distintos de una matriz simétrica son ortogonales entre sí. Esto significa que si $\lambda_1$ y $\lambda_2$ son dos valores propios distintos de $A$, y $\mathbf{v}_1$ y $\mathbf{v}_2$ son los vectores propios asociados, entonces $\mathbf{v}_1 \cdot \mathbf{v}_2 = 0$, donde $\cdot$ representa el producto punto. Esta propiedad es fundamental para la construcción de la matriz de cambio de base $P$.

3. **Diagonalización ortogonal**: En el caso de las matrices simétricas, la matriz de cambio de base $P$ en la descomposición $A = PDP^{-1}$ puede ser elegida de forma que sea una matriz ortogonal. Esto implica que $P^{-1} = P^T$, lo cual simplifica aún más la diagonalización y tiene importantes implicaciones geométricas.

## Aplicaciones

La diagonalización de matrices simétricas tiene diversas aplicaciones en diferentes áreas:

- **Análisis de sistemas físicos**: Las matrices simétricas aparecen en problemas físicos como el análisis de estructuras, la resolución de ecuaciones diferenciales parciales y la mecánica cuántica. La diagonalización permite simplificar la resolución de estos sistemas y obtener información sobre sus modos de vibración y estados

 fundamentales.

- **Análisis de datos**: En estadística y ciencia de datos, la diagonalización de matrices simétricas se utiliza en técnicas de reducción de dimensionalidad, como el análisis de componentes principales (PCA). Estas técnicas permiten extraer información relevante de conjuntos de datos de alta dimensionalidad, simplificando su interpretación y análisis.

- **Optimización y control**: La diagonalización de matrices simétricas es útil en problemas de optimización y control, donde se busca encontrar soluciones óptimas o estables. Permite simplificar la formulación y análisis de estos problemas, facilitando la identificación de soluciones óptimas y la estabilidad del sistema.

En resumen, la diagonalización de matrices simétricas es un proceso matemático fundamental que permite descomponer una matriz en una forma diagonal mediante una matriz de cambio de base. Las propiedades especiales de las matrices simétricas facilitan esta descomposición y ofrecen diversas aplicaciones en áreas como la física, la estadística, la optimización y el control. Comprender y aplicar este concepto es esencial para el análisis y la resolución de problemas en múltiples disciplinas.

'''



r'''

# Aplicaciones de los Valores y Vectores Propios

Los valores y vectores propios son conceptos fundamentales en el álgebra lineal y tienen una amplia gama de aplicaciones en diversas áreas. Estas aplicaciones se basan en la capacidad de los valores y vectores propios para capturar información importante sobre las propiedades y el comportamiento de las matrices. En este artículo, exploraremos algunas de las aplicaciones más comunes de los valores y vectores propios.

## Análisis de sistemas lineales

Los valores y vectores propios son ampliamente utilizados en el análisis de sistemas lineales. En este contexto, las matrices representan sistemas de ecuaciones lineales o transformaciones lineales, y los valores y vectores propios proporcionan información esencial sobre el comportamiento y las propiedades de estos sistemas.

- **Estabilidad de sistemas**: Los valores propios de una matriz de coeficientes en un sistema de ecuaciones diferenciales representan las tasas de crecimiento o decrecimiento de las soluciones del sistema. Si todos los valores propios tienen parte real negativa, el sistema se considera estable. Esta información es crucial para el análisis y el diseño de sistemas de control y estabilidad en ingeniería.

- **Modos de vibración**: En problemas de mecánica estructural o acústica, los valores y vectores propios proporcionan información sobre los modos de vibración de un sistema. Los valores propios representan las frecuencias naturales de vibración, mientras que los vectores propios describen las formas de vibración asociadas. Esta información es relevante para el diseño de estructuras y la predicción de resonancias.

## Reducción de dimensionalidad

Los valores y vectores propios son fundamentales en técnicas de reducción de dimensionalidad, que se utilizan para simplificar y visualizar conjuntos de datos de alta dimensionalidad. Estas técnicas buscan encontrar una representación más compacta del conjunto de datos sin perder información importante.

- **Análisis de componentes principales (PCA)**: El PCA utiliza los valores y vectores propios de la matriz de covarianza de un conjunto de datos para encontrar nuevas variables que expliquen la mayor parte de la variabilidad de los datos. Los vectores propios se utilizan para definir las nuevas variables (componentes principales), mientras que los valores propios indican la importancia relativa de cada componente. El PCA es ampliamente utilizado en estadística, aprendizaje automático y visión por computadora.

- **Análisis de factores**: Similar al PCA, el análisis de factores busca identificar variables latentes o factores subyacentes que expliquen las correlaciones observadas en un conjunto de datos. Los valores y vectores propios de la matriz de correlación se utilizan para determinar la estructura de los factores y su contribución a los datos observados.

## Optimización y descomposición de matrices

Los valores y vectores propios también se utilizan en problemas de optimización y descomposición de matrices.

- **Optimización cuadrática**: En problemas de optimización cuadrática, los valores y vectores propios de la matriz Hessiana se utilizan para determinar la convexidad o concavidad de la función objetivo. Si todos los valores propios son positivos (o negativos), la función objetivo es convexa (o concava), lo que simplifica la búsqueda de un mínimo o máximo global.

- **Descomposición espectral**: La descomposición espectral de una matriz diagonaliza la matriz en términos de sus valores y vectores propios. Esta descomposición es útil en diversas aplicaciones, como el cálculo de la potencia de una matriz, la resolución de sistemas de ecuaciones lineales y la simulación de sistemas dinámicos.

'''
