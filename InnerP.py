import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64



r'''

# Espacios Vectoriales con Producto Interno

En el álgebra lineal, un espacio vectorial con producto interno, también conocido como espacio vectorial euclidiano o espacio euclidiano, es un espacio vectorial equipado con una operación adicional llamada producto interno. El producto interno es una función que toma dos vectores y devuelve un número real, y está diseñado para capturar la noción de longitud y ángulo en el espacio vectorial. A continuación, se presentan los conceptos básicos y propiedades de los espacios vectoriales con producto interno.

## Definición
Un espacio vectorial con producto interno se define como un par $(V, \langle \cdot, \cdot \rangle)$, donde $V$ es un espacio vectorial sobre un campo de escalares, y $\langle \cdot, \cdot \rangle$ es una función que asigna a cada par de vectores en $V$ un número real, satisfaciendo las siguientes propiedades:

1. Propiedad de linealidad en el primer argumento:
   - $\langle \alpha \mathbf{u} + \beta \mathbf{v}, \mathbf{w} \rangle = \alpha \langle \mathbf{u}, \mathbf{w} \rangle + \beta \langle \mathbf{v}, \mathbf{w} \rangle$

2. Propiedad de conmutatividad:
   - $\langle \mathbf{u}, \mathbf{v} \rangle = \langle \mathbf{v}, \mathbf{u} \rangle$

3. Propiedad de aditividad:
   - $\langle \mathbf{u} + \mathbf{v}, \mathbf{w} \rangle = \langle \mathbf{u}, \mathbf{w} \rangle + \langle \mathbf{v}, \mathbf{w} \rangle$

4. Propiedad de homogeneidad:
   - $\langle \alpha \mathbf{u}, \mathbf{v} \rangle = \alpha \langle \mathbf{u}, \mathbf{v} \rangle$

5. Propiedad de positividad definida:
   - $\langle \mathbf{v}, \mathbf{v} \rangle \geq 0$, con igualdad si y solo si $\mathbf{v} = \mathbf{0}$

## Propiedades y Características
Los espacios vectoriales con producto interno tienen varias propiedades y características notables:

1. Norma: El producto interno define una norma en el espacio vectorial, que se denota por $\|\mathbf{v}\|$ o $||\mathbf{v}||$. La norma de un vector es la raíz cuadrada del producto interno del vector consigo mismo: $\|\mathbf{v}\| = \sqrt{\langle \mathbf{v}, \mathbf{v} \rangle}$.

2. Ortogonalidad: Dos vectores $\mathbf{u}$ y $\mathbf{v}$ se dicen ortogonales si su producto interno es cero: $\langle \mathbf{u}, \mathbf{v} \rangle = 0$. Esto significa que los vectores son perpendiculares entre sí.

3. Proyección: Dado un vector $\mathbf{v}$ y un subespacio vectorial $W$, la proyección ortogonal de $\mathbf{v}$ en $W$, denotada por $\text{proj}_W(\math

bf{v})$, es el vector en $W$ que es más cercano a $\mathbf{v}$ en términos de distancia euclidiana. Se puede calcular utilizando el producto interno.

4. Base ortonormal: Un conjunto de vectores $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ se dice que es una base ortonormal si los vectores son ortogonales entre sí y tienen una norma unitaria ($\|\mathbf{v}_i\| = 1$). Una base ortonormal es especialmente útil en el estudio de los espacios vectoriales con producto interno.

## Ejemplos
A continuación se presentan algunos ejemplos de espacios vectoriales con producto interno:

1. Espacio Euclidiano Tridimensional: El espacio vectorial $\mathbb{R}^3$ equipado con el producto interno estándar, el producto punto, es un ejemplo común de un espacio vectorial con producto interno. El producto punto entre dos vectores $\mathbf{u} = (u_1, u_2, u_3)$ y $\mathbf{v} = (v_1, v_2, v_3)$ se define como $\langle \mathbf{u}, \mathbf{v} \rangle = u_1v_1 + u_2v_2 + u_3v_3$.

2. Espacio de Polinomios: El espacio de polinomios de grado $n$, denotado por $P_n$, también puede considerarse como un espacio vectorial con producto interno. El producto interno de dos polinomios $p(x)$ y $q(x)$ se define como $\langle p(x), q(x) \rangle = \int_a^b p(x)q(x) \, dx$, donde $a$ y $b$ son los límites de integración.


'''


r'''
# Ortogonalidad y Ortonormalidad en Espacios Vectoriales con Producto Interno

En un espacio vectorial con producto interno, como se mencionó anteriormente, los conceptos de ortogonalidad y ortonormalidad son fundamentales. Estas propiedades permiten definir relaciones especiales entre vectores y forman la base de muchos cálculos y aplicaciones en el álgebra lineal.

## Ortogonalidad

Dos vectores $\mathbf{u}$ y $\mathbf{v}$ en un espacio vectorial con producto interno se denominan ortogonales si su producto interno es igual a cero, es decir, $\langle \mathbf{u}, \mathbf{v} \rangle = 0$. Esto implica que los vectores son perpendiculares entre sí, formando un ángulo de 90 grados.

La ortogonalidad tiene varias implicaciones y aplicaciones importantes:

1. Espacio Ortogonal: Un subespacio vectorial $W$ se llama espacio ortogonal si cada par de vectores en $W$ es ortogonal entre sí. Por ejemplo, el conjunto de todos los vectores con coordenadas $(x, y, 0)$ en un espacio tridimensional es un subespacio ortogonal.

2. Base Ortogonal: Un conjunto de vectores se llama una base ortogonal si todos los vectores en el conjunto son ortogonales entre sí. Una base ortogonal es especialmente útil en el cálculo de coordenadas y resolución de sistemas de ecuaciones lineales.

3. Proyección Ortogonal: Dado un vector $\mathbf{v}$ y un subespacio vectorial $W$, la proyección ortogonal de $\mathbf{v}$ sobre $W$, denotada como $\text{proj}_W(\mathbf{v})$, es el vector en $W$ que es más cercano a $\mathbf{v}$ en términos de distancia euclidiana. Se puede calcular utilizando el producto interno y la ortogonalidad de los vectores.

## Ortonormalidad

Un conjunto de vectores se llama una base ortonormal si todos los vectores son ortogonales entre sí y tienen una norma unitaria, es decir, $\|\mathbf{v}\| = 1$. Una base ortonormal es una base especial que simplifica muchos cálculos y tiene varias propiedades útiles:

1. Ortonormalización de Gram-Schmidt: Dado un conjunto de vectores linealmente independientes, es posible transformarlo en una base ortogonal o ortonormal utilizando el proceso de ortogonalización de Gram-Schmidt. Este proceso consiste en tomar cada vector del conjunto y proyectarlo ortogonalmente sobre el subespacio generado por los vectores anteriores.

2. Coordenadas Ortogonales: En una base ortogonal o ortonormal, las coordenadas de un vector se pueden calcular fácilmente utilizando las proyecciones ortogonales de ese vector sobre cada uno de los vectores base. Esto simplifica los cálculos de coordenadas y facilita el estudio de las relaciones entre vectores.

3. Matriz Ortonormal: Una matriz cuyas columnas forman una base ortonormal se llama una matriz ortogonal. Las matrices ortogonales tienen varias propiedades interesantes, como la conservación de la longitud y el ángulo entre vectores durante las transformaciones lineales.

La ortogonalidad y la ortonormalidad son conceptos fundamentales en los espacios vectoriales con producto interno.

'''



r'''
# Proceso de Gram-Schmidt para Bases Ortogonales y Ortonormales

El proceso de Gram-Schmidt es un método utilizado en el álgebra lineal para convertir un conjunto de vectores linealmente independientes en una base ortogonal o ortonormal. Este proceso es útil para simplificar cálculos y establecer relaciones especiales entre los vectores de una base. A continuación, se describe el proceso de Gram-Schmidt para obtener bases ortogonales y ortonormales.

Supongamos que tenemos un conjunto de vectores $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ que son linealmente independientes y queremos obtener una base ortogonal o ortonormal a partir de ellos.

## Base Ortogonal

El proceso de Gram-Schmidt para obtener una base ortogonal se realiza de la siguiente manera:

1. Inicialización: Definimos un nuevo conjunto de vectores $\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n\}$, donde $\mathbf{u}_1 = \mathbf{v}_1$.

2. Iteración: Para cada $i$ desde 2 hasta $n$, realizamos los siguientes pasos:
   a. Calculamos el proyector ortogonal de $\mathbf{v}_i$ sobre los vectores anteriores:
      $\mathbf{p}_i = \frac{\langle \mathbf{v}_i, \mathbf{u}_1 \rangle}{\|\mathbf{u}_1\|^2} \mathbf{u}_1 + \frac{\langle \mathbf{v}_i, \mathbf{u}_2 \rangle}{\|\mathbf{u}_2\|^2} \mathbf{u}_2 + \ldots + \frac{\langle \mathbf{v}_i, \mathbf{u}_{i-1} \rangle}{\|\mathbf{u}_{i-1}\|^2} \mathbf{u}_{i-1}$.
   b. Definimos el nuevo vector ortogonal como $\mathbf{u}_i = \mathbf{v}_i - \mathbf{p}_i$.

Al final del proceso, obtendremos una base ortogonal $\{\mathbf{u}_1, \mathbf{u}_2, \ldots, \mathbf{u}_n\}$ a partir del conjunto inicial de vectores $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$.

## Base Ortonormal

Para obtener una base ortonormal, simplemente normalizamos cada vector de la base ortogonal obtenida en el paso anterior dividiéndolo por su norma:

1. Para cada $i$ desde 1 hasta $n$, definimos el nuevo vector ortonormal como $\mathbf{e}_i = \frac{\mathbf{u}_i}{\|\mathbf{u}_i\|}$.

Al final del proceso, obtendremos una base ortonormal $\{\mathbf{e}_1, \mathbf{e}_2, \ldots, \mathbf{e}_n\}$ a partir del conjunto inicial de vectores $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$.

El proceso de Gram-Schmidt es muy útil en muchas aplicaciones del álgebra lineal. Proporciona una forma sistemática de construir bases ortogonales y ortonormales, lo que facilita el cálculo de proyecciones, resolución de sistemas de ecuaciones y análisis de transformaciones lineales. Además, las bases ortogonales y ortonormales tienen propiedades especiales que simplifican los cálculos y permiten una mejor comprensión de los vectores en un espacio vectorial.

'''
