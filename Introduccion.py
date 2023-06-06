import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp


st.title('Introducción')



r'''
# Introducción al Álgebra Lineal

El álgebra lineal es una rama de las matemáticas que se centra en el estudio de las propiedades y estructuras de los espacios vectoriales. Su importancia radica en su amplia aplicabilidad en diversas disciplinas científicas y tecnológicas, como la física, la ingeniería y la ciencia de datos. En esta introducción, exploraremos dos conceptos fundamentales en el álgebra lineal: los números reales y las n-plas de números reales.

## Los Números Reales

Los números reales ($\mathbb{R}$) constituyen un conjunto numérico fundamental en el álgebra lineal. Representan una amplia gama de magnitudes y se utilizan para describir cantidades continuas en el mundo real. Los números reales incluyen tanto números racionales como números irracionales.

Los números racionales son aquellos que pueden expresarse como el cociente de dos números enteros. Por ejemplo, $\frac{1}{2}$, $-\frac{3}{4}$ y $5$ son ejemplos de números racionales. Por otro lado, los números irracionales no pueden expresarse como fracciones y tienen una expansión decimal infinita no periódica. Ejemplos conocidos de números irracionales son $\pi$ y $\sqrt{2}$.

Los números reales poseen varias propiedades fundamentales que los distinguen. Algunas de estas propiedades son:

- **Cerradura**: La suma y multiplicación de dos números reales siempre producen otro número real.
- **Existencia de elementos neutros**: El número $0$ actúa como elemento neutro para la suma y el número $1$ actúa como elemento neutro para la multiplicación.
- **Propiedad conmutativa**: Tanto la suma como la multiplicación son operaciones conmutativas en los números reales.
- **Existencia de inversos**: Todo número real, excepto $0$, tiene un inverso aditivo y un inverso multiplicativo.
- **Propiedad distributiva**: La multiplicación se distribuye sobre la suma en los números reales.

## Las n-plas de Números Reales

Una n-pla de números reales es una secuencia ordenada de n números reales. Se denota como $(a_1, a_2, \ldots, a_n)$, donde cada $a_i$ representa el i-ésimo elemento de la secuencia. Las n-plas de números reales son una generalización de los conceptos de números reales individuales y se utilizan para representar conjuntos de datos multidimensionales.

Por ejemplo, una 2-pla de números reales puede representar las coordenadas de un punto en un plano bidimensional, donde el primer número representa la posición en el eje x y el segundo número representa la posición en el eje y. Del mismo modo, una 3-pla de números reales puede representar las coordenadas de un punto en un espacio tridimensional.

Las n-plas de números reales se pueden sumar y multiplicar por escalares de manera similar a los vectores en álgebra lineal. La suma de dos n-plas se realiza sumando componente a componente, y la multiplicación por un escalar implica multiplicar cada componente por el escalar correspondiente.

Además de las operaciones de suma y multiplicación, las n-plas de números reales también tienen propiedades adicionales. Algunas de estas propiedades incluyen:

- **Asociatividad**: La suma de n-plas es asociativa, lo que significa que el resultado de sumar tres n-plas no depende del orden en que se realicen las sumas.
- **Propiedad del elemento neutro**: Existe una n-pla especial, llamada n-pla nula o vector cero, compuesta por ceros en todas sus componentes, que actúa como el elemento neutro de la suma.
- **Propiedad distributiva**: La multiplicación de una n-pla por un escalar distribuye sobre la suma de n-plas.

En resumen, los números reales y las n-plas de números reales constituyen los elementos básicos del álgebra lineal. Su comprensión es fundamental para el estudio y la aplicación de conceptos más avanzados en esta disciplina. En las secciones siguientes, exploraremos propiedades adicionales y operaciones fundamentales en el álgebra lineal, que nos permitirán abordar problemas más complejos y obtener resultados significativos en diversas áreas de conocimiento.
### Antecedentes históricos

El estudio del álgebra lineal tiene sus raíces en la antigüedad, donde los matemáticos de la antigua Grecia, como Euclides, estudiaron las propiedades de las magnitudes y las relaciones entre ellas. Sin embargo, el desarrollo formal del álgebra lineal como una disciplina independiente se produjo en los siglos XIX y XX.

En el siglo XIX, el matemático francés Augustin-Louis Cauchy introdujo el concepto de determinante y desarrolló la teoría de matrices. Su trabajo proporcionó las bases para el estudio de las ecuaciones lineales y las transformaciones lineales.

El álgebra lineal se desarrolló aún más con las contribuciones del matemático británico William Rowan Hamilton y el matemático inglés Arthur Cayley. Hamilton introdujo el concepto de cuaterniones, que generaliza los números complejos, mientras que Cayley desarrolló una notación simbólica para representar matrices y estudió las propiedades de las operaciones matriciales.

En el siglo XX, el matemático alemán David Hilbert y el matemático húngaro John von Neumann hicieron contribuciones significativas al álgebra lineal. Hilbert desarrolló la teoría de espacios vectoriales abstractos y estableció los fundamentos matemáticos rigurosos del álgebra lineal. Von Neumann amplió estas ideas y aplicó el álgebra lineal a la teoría de la mecánica cuántica.

### Conceptos fundamentales

El álgebra lineal se basa en varios conceptos fundamentales:

- **Vectores**: Los vectores son elementos básicos en álgebra lineal. Representan magnitudes y direcciones en un espacio multidimensional. Se pueden sumar, restar y multiplicar por escalares. Los vectores se pueden representar geométricamente como flechas en un espacio, y algebraicamente como listas de números.

- **Matrices**: Las matrices son arreglos rectangulares de números dispuestos en filas y columnas. Se utilizan para representar y operar sobre conjuntos de ecuaciones lineales y transformaciones lineales. Las operaciones matriciales incluyen suma, multiplicación y determinante.

- **Sistemas de ecuaciones lineales**: Los sistemas de ecuaciones lineales son conjuntos de ecuaciones que involucran variables y coeficientes lineales. El álgebra lineal proporciona herramientas para resolver y analizar estos sistemas, utilizando métodos como la eliminación de Gauss y la descomposición LU.

- **Transformaciones lineales**: Las transformaciones lineales son funciones que preservan la estructura lineal entre espacios vectoriales. Estas transformaciones se pueden representar mediante matrices y se utilizan para describir cambios y relaciones lineales en diversos contextos, como el procesamiento de imágenes y el análisis de datos.

### Aplicaciones

El álgebra lineal tiene una amplia gama de aplicaciones prácticas

 en diversos campos:

- En la física, se utiliza para describir y analizar fenómenos como el movimiento de partículas, la propagación de ondas y los sistemas de fuerzas.

- En la ingeniería, se aplica en el diseño y control de sistemas eléctricos, mecánicos y de comunicaciones, así como en la optimización de procesos.

- En la ciencia de datos, el álgebra lineal es esencial para el análisis de datos multivariables, la reducción de dimensionalidad, la regresión lineal y el aprendizaje automático.

- En la economía y las finanzas, se utiliza para modelar y analizar sistemas económicos, como la oferta y demanda, y para realizar cálculos financieros, como la valoración de activos y la gestión de carteras.

En resumen, el álgebra lineal es una disciplina matemática fundamental que proporciona herramientas y conceptos clave para el estudio y análisis de los espacios vectoriales, las transformaciones lineales y las ecuaciones lineales. Su amplia aplicación en numerosos campos lo convierte en un área de estudio relevante y poderosa.

'''
