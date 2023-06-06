import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import sympy as sp


st.title('Espacio Vectorial de las n-plas de Números Reales')

r'''


El espacio vectorial de las n-plas de números reales es un concepto fundamental en el álgebra lineal que nos permite estudiar y manipular conjuntos de n números reales. En este resumen, exploraremos en detalle las propiedades y características de este espacio vectorial.

### Definición

Denotaremos el espacio vectorial de las n-plas de números reales como $\mathbb{R}^n$. Un vector $\mathbf{v}$ en este espacio se puede representar como:

$$
\mathbf{v} = \begin{bmatrix} v_1 \\ v_2 \\ \vdots \\ v_n \end{bmatrix}
$$

donde $v_1, v_2, \ldots, v_n$ son números reales. Cada elemento $v_i$ se denomina componente del vector $\mathbf{v}$.

### Operaciones

En el espacio vectorial $\mathbb{R}^n$, se definen varias operaciones fundamentales:

1. **Suma de vectores**: Dados dos vectores $\mathbf{v}$ y $\mathbf{u}$ en $\mathbb{R}^n$, su suma se obtiene sumando las componentes correspondientes:

$$
\mathbf{v} + \mathbf{u} =
\begin{bmatrix} v_1 + u_1 \\ v_2 + u_2 \\ \vdots \\ v_n + u_n \end{bmatrix}
$$

2. **Multiplicación por un escalar**: Dado un número real $c$ y un vector $\mathbf{v}$ en $\mathbb{R}^n$, el producto de $c$ por $\mathbf{v}$ se obtiene multiplicando cada componente de $\mathbf{v}$ por $c$:

$$
\mathbf{v} = \begin{bmatrix} cv_1 \\ cv_2 \\ \vdots \\ cv_n \end{bmatrix}
$$

Estas operaciones cumplen ciertas propiedades, como la conmutatividad y asociatividad de la suma de vectores, y la distributividad de la multiplicación por un escalar respecto a la suma de vectores.

### Propiedades y Características

El espacio vectorial $\mathbb{R}^n$ tiene varias propiedades y características importantes:

1. **Dimensión**: El espacio $\mathbb{R}^n$ tiene una dimensión de $n$, lo que significa que cualquier vector en este espacio tiene exactamente $n$ componentes.

2. **Origen**: En $\mathbb{R}^n$, se define un vector especial llamado vector cero, denotado como $\mathbf{0}$, que tiene todas sus componentes iguales a cero.

### Aplicaciones

El espacio vectorial de las n-plas de números reales tiene una amplia gama de aplicaciones en diversas áreas:

- En la física, se utiliza para describir magnitudes como fuerzas, velocidades y campos eléctricos en un espacio tridimensional ($n = 3$).

- En la geometría, se emplea para representar puntos, segmentos y polígonos en un plano ($n = 2$) o en el espacio tridimensional ($n = 3$).

- En la informática, se utiliza en la representación de imágenes, donde cada píxel puede ser considerado como un vector en $\mathbb{R}^n$ donde \(n\) representa el número de componentes de color.

- En el análisis de datos, el espacio vectorial $\mathbb{R}^n$ es esencial para la representación y manipulación de datos multidimensionales, como conjuntos de características y vectores de características.

Estas son solo algunas de las muchas aplicaciones del espacio vectorial de las n-plas de números reales, lo que demuestra su importancia y utilidad en diversos campos.



# Producto Escalar o Producto Punto

El producto escalar, también conocido como producto punto o producto interno, es una operación importante en el álgebra lineal. Permite combinar dos vectores para obtener un escalar. En este resumen, exploraremos la definición y las propiedades del producto escalar.

## Definición

Dado dos vectores $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, el producto escalar se denota como $\mathbf{v} \cdot \mathbf{w}$. El resultado es un escalar que representa la magnitud de la proyección de $\mathbf{v}$ sobre $\mathbf{w}$, multiplicada por la magnitud de $\mathbf{w}$.

En términos matemáticos, si $\mathbf{v} = (v_1, v_2, \ldots, v_n)$ y $\mathbf{w} = (w_1, w_2, \ldots, w_n)$ son dos vectores, entonces el producto escalar se define como:

$$
\mathbf{v} \cdot \mathbf{w} = v_1w_1 + v_2w_2 + \ldots + v_nw_n
$$

## Propiedades

El producto escalar tiene varias propiedades importantes:

1. Conmutatividad: Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$, se cumple $\mathbf{v} \cdot \mathbf{w} = \mathbf{w} \cdot \mathbf{v}$.

2. Distributividad respecto a la suma de vectores: Para cualquier vector $\mathbf{u}$ y dos vectores $\mathbf{v}$ y $\mathbf{w}$, se cumple $\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}$.

3. Propiedad de la multiplicación por escalar: Para cualquier vector $\mathbf{v}$ y escalar $c$, se cumple $(c\mathbf{v}) \cdot \mathbf{w} = c(\mathbf{v} \cdot \mathbf{w}) = \mathbf{v} \cdot (c\mathbf{w})$.

4. Propiedad de la multiplicación por el escalar cero: Para cualquier vector $\mathbf{v}$, se cumple $0 \cdot \mathbf{v} = 0$.

5. Propiedad de la longitud: Para cualquier vector $\mathbf{v}$, se cumple $\mathbf{v} \cdot \mathbf{v} = |\mathbf{v}|^2$, donde $|\mathbf{v}|$ representa la longitud (norma) del vector $\mathbf{v}$.


# Norma de un Vector

La norma de un vector es una medida de su longitud o magnitud en un espacio vectorial. En este resumen, exploraremos la definición de la norma de un vector y algunas de sus propiedades más importantes.

## Definición

Dado un vector $\mathbf{v}$ en un espacio vectorial, la norma del vector, denotada por $\|\mathbf{v}\|$, se define como un número no negativo que representa su longitud o magnitud. Formalmente, la norma de un vector se define utilizando la raíz cuadrada del producto escalar del vector consigo mismo:

$$
\|\mathbf{v}\| = \sqrt{\mathbf{v} \cdot \mathbf{v}}
$$

La norma de un vector cumple las siguientes propiedades:

## Propiedades

1. **No negatividad**: La norma de un vector es siempre no negativa: $\|\mathbf{v}\| \geq 0$, y solo es igual a cero si y solo si el vector es el vector cero $\mathbf{0}$.

2. **Definitividad**: Si la norma de un vector es igual a cero, entonces el vector debe ser el vector cero: $\|\mathbf{v}\| = 0 \iff \mathbf{v} = \mathbf{0}$.

3. **Homogeneidad absoluta**: Para cualquier vector $\mathbf{v}$ y escalar $c$, se cumple $\|c\mathbf{v}\| = |c|\|\mathbf{v}\|$. Esto significa que si escalamos un vector por un factor constante, su norma se escala por el valor absoluto de ese factor constante.

4. **Desigualdad triangular**: Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$, se cumple la desigualdad triangular: $\|\mathbf{v} + \mathbf{w}\| \leq \|\mathbf{v}\| + \|\mathbf{w}\|$. Esto significa que la longitud de la suma de dos vectores siempre es menor o igual a la suma de las longitudes individuales de los vectores.

5. **Propiedad de la multiplicación por un escalar no negativo**: Para cualquier vector $\mathbf{v}$ y un escalar no negativo $c$, se cumple $\|c\mathbf{v}\| = c\|\mathbf{v}\|$. Esto indica que si multiplicamos un vector por un escalar no negativo, la norma del vector se multiplica por ese escalar.

Estas propiedades de la norma de un vector son fundamentales para su estudio y aplicación en diversas áreas de las matemáticas y la física. La norma de un vector proporciona información sobre su magnitud y se utiliza en el cálculo de distancias, determinación de la convergencia de secuencias y en la definición de espacios métricos y normados. Además, la norma de un vector es esencial en la definición de otras estructuras algebraicas como el espacio vectorial y el producto escalar.

## Teoremas

## Teorema 1: Teorema de la Conmutatividad

Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, se cumple:

$$
\mathbf{v} \cdot \mathbf{w} = \mathbf{w} \cdot \mathbf{v}
$$

Este teorema establece que el producto escalar es conmutativo. Es decir, el orden en que se escriben los vectores no afecta el resultado del producto escalar.

## Teorema 2: Teorema de la Distributividad

Para cualquier vector $\mathbf{u}$ y dos vectores $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, se cumple:

$$
\mathbf{u} \cdot (\mathbf{v} + \mathbf{w}) = \mathbf{u} \cdot \mathbf{v} + \mathbf{u} \cdot \mathbf{w}
$$

Este teorema establece la propiedad de la distributividad del producto escalar respecto a la suma de vectores. Significa que podemos distribuir el producto escalar sobre la suma de dos vectores y obtener el mismo resultado que si realizáramos el producto escalar individualmente y luego sumáramos los resultados.

## Teorema 3: Teorema de la Asociatividad con Escalares

Para cualquier vector $\mathbf{v}$ y escalares $c$ y $d$ en un espacio vectorial, se cumple:

$$
(c\mathbf{v}) \cdot \mathbf{w} = c(\mathbf{v} \cdot \mathbf{w}) = \mathbf{v} \cdot (d\mathbf{w})
$$

Este teorema establece la propiedad de la asociatividad del producto escalar con escalares. Indica que podemos multiplicar un vector por un escalar y luego realizar el producto escalar, o podemos realizar primero el producto escalar y luego multiplicar por el escalar, y en ambos casos obtendremos el mismo resultado.

## Teorema 4: Teorema del Producto Escalar y la Longitud

Para cualquier vector $\mathbf{v}$ en un espacio vectorial, se cumple:

$$
\mathbf{v} \cdot \mathbf{v} = \|\mathbf{v}\|^2
$$

Este teorema establece la relación entre el producto escalar de un vector consigo mismo y la longitud (norma) del vector. El cuadrado del producto escalar es igual al cuadrado de la longitud del vector. Esto implica que si el producto escalar de un vector consigo mismo es cero, entonces la longitud del vector es cero, lo cual solo ocurre si el vector es el vector cero.


## Teorema 5: Teorema de la Ortogonalidad

Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, se cumple:

$$
\mathbf{v} \cdot \mathbf{w} = 0 \iff \mathbf{v} \perp \mathbf{w}
$$

Este teorema establece que dos vectores son ortogonales si y solo si su producto escalar es igual a cero. Si el producto escalar de dos vectores es cero, significa que son perpendiculares entre sí.

## Teorema 6: Desigualdad de Cauchy-Schwarz

Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, se cumple:

$$
|\mathbf{v} \cdot \mathbf{w}| \leq \|\mathbf{v}\| \cdot \|\mathbf{w}\|
$$

Este teorema establece una desigualdad importante entre el valor absoluto del producto escalar de dos vectores y el producto de las longitudes (normas) de los vectores. Indica que el valor absoluto del producto escalar siempre es menor o igual al producto de las longitudes de los vectores.

## Teorema 7: Identidad del Ángulo

Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, se cumple:

$$
\mathbf{v} \cdot \mathbf{w} = \|\mathbf{v}\| \cdot \|\mathbf{w}\| \cdot \cos(\theta)
$$

Este teorema establece la relación entre el producto escalar de dos vectores, las longitudes (normas) de los vectores y el ángulo $\theta$ entre ellos. El producto escalar es igual al producto de las longitudes de los vectores y el coseno del ángulo entre ellos.



## Teorema 8: Teorema de la Desigualdad Triangular

Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, se cumple:

$$
\|\mathbf{v} + \mathbf{w}\| \leq \|\mathbf{v}\| + \|\mathbf{w}\|
$$

Este teorema establece la desigualdad triangular en relación a la norma de la suma de dos vectores. Indica que la longitud de la suma de dos vectores es siempre menor o igual a la suma de las longitudes individuales de los vectores.

## Teorema 9: Teorema de la Proyección

Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, se cumple:

$$
\mathbf{v} = \operatorname{proj}_{\mathbf{w}}(\mathbf{v}) + \operatorname{perp}_{\mathbf{w}}(\mathbf{v})
$$

Este teorema establece que cualquier vector $\mathbf{v}$ se puede descomponer en la suma de su proyección sobre $\mathbf{w}$ y el componente perpendicular a $\mathbf{w}$. La proyección de $\mathbf{v}$ sobre $\mathbf{w}$ es paralela a $\mathbf{w}$ y se obtiene multiplicando el vector unitario de $\mathbf{w}$ por el producto escalar de $\mathbf{v}$ y $\mathbf{w}$ dividido por la norma de $\mathbf{w}$. El componente perpendicular a $\mathbf{w}$ se obtiene restando la proyección de $\mathbf{v}$ a $\mathbf{w}$ de $\mathbf{v}$.

## Teorema 10: Teorema del Ángulo entre Vectores

Para cualquier vector $\mathbf{v}$ y $\mathbf{w}$ en un espacio vectorial, se cumple:

$$
\cos(\theta) = \frac{\mathbf{v} \cdot \mathbf{w}}{\|\mathbf{v}\| \cdot \|\mathbf{w}\|}
$$

Este teorema establece la relación entre el ángulo $\theta$ entre dos vectores y el producto escalar de los vectores junto con sus normas. El coseno del ángulo entre los vectores es igual al cociente del producto escalar de los vectores y el producto de sus normas.

Estos teoremas son esenciales en el estudio y la aplicación del producto escalar en el álgebra lineal. Proporcionan herramientas para comprender y analizar la geometría y las propiedades de los vectores en el espacio. Además, son fundamentales para el desarrollo de otras áreas de las matemáticas y su aplicación en diversas disciplinas científicas y técnicas.


'''





# Definir los vectores
vector1 = np.array([2, 3])
vector2 = np.array([-1, 4])

# Definir un escalar
escalar = 2

# Calcular la suma de los vectores
suma = vector1 + vector2

# Calcular la resta de los vectores
resta = vector1 - vector2

# Calcular la multiplicación por escalar
mult_escalar = escalar * vector1

# Crear una figura y ejes para la suma
fig1, ax1 = plt.subplots()

# Graficar la suma de los vectores
ax1.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
ax1.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')
ax1.quiver(0, 0, suma[0], suma[1], angles='xy', scale_units='xy', scale=1, color='g', label='Suma')

# Configurar límites y etiquetas del gráfico de la suma
ax1.set_xlim(-10, 10)
ax1.set_ylim(-10, 10)
ax1.set_xlabel('Eje X')
ax1.set_ylabel('Eje Y')
ax1.legend()

# Mostrar el gráfico de la suma
plt.grid()


# Crear una figura y ejes para la resta
fig2, ax2 = plt.subplots()

# Graficar la resta de los vectores
ax2.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
ax2.quiver(0, 0, vector2[0], vector2[1], angles='xy', scale_units='xy', scale=1, color='b', label='Vector 2')
ax2.quiver(vector1[0], vector1[1], -vector2[0], -vector2[1], angles='xy', scale_units='xy', scale=1, color='m', label='Resta')

# Configurar límites y etiquetas del gráfico de la resta
ax2.set_xlim(-10, 10)
ax2.set_ylim(-10, 10)
ax2.set_xlabel('Eje X')
ax2.set_ylabel('Eje Y')
ax2.legend()

# Mostrar el gráfico de la resta
plt.grid()


# Crear una figura y ejes para la multiplicación por escalar
fig3, ax3 = plt.subplots()

# Graficar la multiplicación por escalar
ax3.quiver(0, 0, vector1[0], vector1[1], angles='xy', scale_units='xy', scale=1, color='r', label='Vector 1')
ax3.quiver(0, 0, mult_escalar[0], mult_escalar[1], angles='xy', scale_units='xy', scale=1, color='c', label='Multiplicación por escalar')

# Configurar límites y etiquetas del gráfico de la multiplicación por escalar
ax3.set_xlim(-10, 10)
ax3.set_ylim(-10, 10)
ax3.set_xlabel('Eje X')
ax3.set_ylabel('Eje Y')
ax3.legend()

# Mostrar el gráfico de la multiplicación por escalar
plt.grid()






r'''
# Interpretación Geométrica de los Vectores en $\mathbb{R}^2$ y $\mathbb{R}^3$

Los vectores en $\mathbb{R}^2$ y $\mathbb{R}^3$ tienen una interpretación geométrica que nos permite visualizarlos y comprender su significado en términos de direcciones y magnitudes en el espacio.

## Vectores en $\mathbb{R}^2$

En $\mathbb{R}^2$, los vectores se representan como puntos en un plano cartesiano. Cada vector tiene dos componentes, $x$ e $y$, que indican su posición en el plano. Podemos interpretar un vector como una flecha que va desde el origen hasta el punto representado por sus componentes $x$ e $y$. La longitud de la flecha representa la magnitud del vector.

Por ejemplo, consideremos el vector $\mathbf{v} = (3, 4)$. Podemos trazar una flecha que comienza en el origen y termina en el punto $(3, 4)$. La longitud de la flecha nos indica que el vector tiene una magnitud de $\sqrt{3^2 + 4^2} = 5$. Además, podemos identificar la dirección del vector observando el ángulo que forma con el eje positivo $x$. Si trazamos una línea desde el origen hasta el punto final del vector, podemos medir el ángulo utilizando herramientas geométricas o trigonométricas.

Los vectores en $\mathbb{R}^2$ se utilizan para describir desplazamientos, velocidades, fuerzas y muchas otras magnitudes físicas. También se pueden sumar, restar y multiplicar por escalares. La suma de dos vectores se puede visualizar mediante la regla del paralelogramo, donde colocamos los vectores uno después del otro y trazamos un paralelogramo desde el origen hasta el punto final. La resta de vectores se puede visualizar como la suma de un vector y el opuesto del otro vector.


'''

st.pyplot(fig1)
st.write('')
st.pyplot(fig2)
st.write('')
st.pyplot(fig3)



r'''
## Vectores en $\mathbb{R}^3$

En $\mathbb{R}^3$, los vectores se representan como puntos en un espacio tridimensional. Cada vector tiene tres componentes, $x$, $y$ y $z$, que indican su posición en el espacio. Similar a $\mathbb{R}^2$, podemos interpretar un vector en $\mathbb{R}^3$ como una flecha que va desde el origen hasta el punto representado por sus componentes $x$, $y$ y $z$. La longitud de la flecha representa la magnitud del vector.

Por ejemplo, consideremos el vector $\mathbf{v} = (1, 2, 3)$. Podemos trazar una flecha que comienza en el origen y termina en el punto $(1, 2, 3)$. La longitud de la flecha nos indica que el vector tiene una magnitud de $\sqrt{1^2 + 2^2 + 3^2} = \sqrt{14}$. Además, podemos identificar la dirección del vector observando los ángulos que forma con los ejes $x$, $y$ y $z$.

Los vectores en $\mathbb{R}^3$ son especialmente útiles en aplicaciones de geometría espacial, física y gráficos por computadora, donde se utilizan para representar pos

iciones, velocidades, fuerzas, aceleraciones y otras magnitudes tridimensionales. Al igual que en $\mathbb{R}^2$, los vectores en $\mathbb{R}^3$ se pueden sumar, restar y multiplicar por escalares utilizando las mismas reglas que en $\mathbb{R}^2$.

En resumen, la interpretación geométrica de los vectores en $\mathbb{R}^2$ y $\mathbb{R}^3$ nos permite visualizar y comprender su dirección y magnitud en el espacio. Estos conceptos son fundamentales para el estudio y la aplicación de los vectores en diversas áreas de las matemáticas, la física, la ingeniería y la informática.



'''



# Definir los vectores
vector1d = np.array([2, 3, 4])
vector2d = np.array([-1, 4, 2])

# Definir un escalar
escalard = 2

# Calcular la suma de los vectores
sumad = vector1d + vector2d

# Calcular la resta de los vectores
restad = vector1d - vector2d

# Calcular la multiplicación por escalar
mult_escalard = escalard * vector1d

# Graficar la suma de los vectores
fig1d = plt.figure()
ax1d = fig1d.add_subplot(111, projection='3d')
ax1d.quiver(0, 0, 0, vector1d[0], vector1d[1], vector1d[2], color='r', label='Vector 1')
ax1d.quiver(0, 0, 0, vector2d[0], vector2d[1], vector2d[2], color='b', label='Vector 2')
ax1d.quiver(0, 0, 0, sumad[0], sumad[1], sumad[2], color='g', label='Suma')
ax1d.set_xlabel('Eje X')
ax1d.set_ylabel('Eje Y')
ax1d.set_zlabel('Eje Z')
ax1d.set_xlim([-10, 10])
ax1d.set_ylim([-10, 10])
ax1d.set_zlim([-10, 10])
ax1d.legend()

# Graficar la resta de los vectores
fig2d = plt.figure()
ax2d = fig2d.add_subplot(111, projection='3d')
ax2d.quiver(0, 0, 0, vector1d[0], vector1d[1], vector1d[2], color='r', label='Vector 1')
ax2d.quiver(0, 0, 0, vector2d[0], vector2d[1], vector2d[2], color='b', label='Vector 2')
ax2d.quiver(vector1d[0], vector1d[1], vector1d[2], -vector2d[0], -vector2d[1], -vector2d[2], color='m', label='Resta')
ax2d.set_xlabel('Eje X')
ax2d.set_ylabel('Eje Y')
ax2d.set_zlabel('Eje Z')
ax2d.set_xlim([-10, 10])
ax2d.set_ylim([-10, 10])
ax2d.set_zlim([-10, 10])
ax2d.legend()

# Graficar la multiplicación por escalar
fig3d = plt.figure()
ax3d = fig3d.add_subplot(111, projection='3d')
ax3d.quiver(0, 0, 0, vector1d[0], vector1d[1], vector1d[2], color='r', label='Vector 1')
ax3d.quiver(0, 0, 0, mult_escalard[0], mult_escalard[1], mult_escalard[2], color='c', label='Multiplicación por escalar')
ax3d.set_xlabel('Eje X')
ax3d.set_ylabel('Eje Y')
ax3d.set_zlabel('Eje Z')
ax3d.set_xlim([-10, 10])
ax3d.set_ylim([-10, 10])
ax3d.set_zlim([-10, 10])
ax3d.legend()

# Mostrar los gráficos
st.pyplot(fig1d)
st.write('')
st.pyplot(fig2d)
st.write('')
st.pyplot(fig3d)
st.write('')




r'''
# Proyecciones y Ángulos en Vectores en $\mathbb{R}^n$ y el Producto Cruz y Producto Mixto

En el estudio del álgebra lineal, los conceptos de proyecciones, ángulos y productos cruz y mixto son fundamentales para comprender la geometría y las relaciones entre vectores en el espacio euclidiano $\mathbb{R}^n$. En este artículo, exploraremos estos conceptos y su aplicación en el ámbito vectorial.

## Proyecciones

La proyección de un vector sobre otro es una operación que nos permite descomponer un vector en una combinación de componentes paralelas y perpendiculares a otro vector dado. En el espacio $\mathbb{R}^n$, la proyección de un vector $\mathbf{v}$ sobre un vector $\mathbf{u}$ se puede calcular utilizando la fórmula de la proyección ortogonal:

$$
\text{Proy}_{\mathbf{u}}(\mathbf{v}) = \frac{\mathbf{v} \cdot \mathbf{u}}{\|\mathbf{u}\|^2} \cdot \mathbf{u}
$$

donde $\cdot$ denota el producto punto, $\|\mathbf{u}\|$ es la norma (longitud) del vector $\mathbf{u}$ y el resultado de la proyección es un vector que se encuentra en la dirección de $\mathbf{u}$.

Además de la proyección ortogonal, también podemos hablar de la proyección de un vector sobre un plano o un subespacio. En estos casos, se utilizan métodos similares pero con algunas modificaciones para adaptarse a la dimensionalidad del espacio.

## Ángulos entre Vectores

El ángulo entre dos vectores $\mathbf{u}$ y $\mathbf{v}$ en el espacio $\mathbb{R}^n$ se puede calcular utilizando la fórmula del producto punto:

$$
\cos(\theta) = \frac{\mathbf{u} \cdot \mathbf{v}}{\|\mathbf{u}\| \|\mathbf{v}\|}
$$

donde $\theta$ es el ángulo entre los vectores, $\cdot$ denota el producto punto y $\|\mathbf{u}\|$ y $\|\mathbf{v}\|$ son las normas (longitudes) de los vectores $\mathbf{u}$ y $\mathbf{v}$, respectivamente.

El resultado de esta fórmula es el coseno del ángulo entre los vectores. Si deseamos obtener el ángulo en sí, podemos utilizar la función inversa del coseno (arcocoseno), generalmente expresado en radianes o grados.

Los ángulos entre vectores nos permiten determinar la relación de orientación y dirección entre ellos, lo cual es útil en diversas aplicaciones, como la geometría, la física y la computación gráfica.

## Producto Cruz

El producto cruz es una operación que se aplica exclusivamente en el espacio tridimensional $\mathbb{R}^3$. El resultado del producto cruz entre dos vectores $\mathbf{u}$ y $\mathbf{v}$, denotado como $\mathbf{u} \times \mathbf{v}$, es un vector que es perpendicular a ambos vectores de entrada.

El cálculo del producto cruz se puede realizar utilizando la siguiente fórmula:

$$
\mathbf{u} \times \mathbf{v} = \begin{bmatrix}
u_2v_3 - u_3v_2 \\
u_3v_1 - u_1v_3 \\
u_1v_2 - u_2v_1 \\
\end{bmatrix}
$$

donde $u_1, u_2, u_3$ son las componentes del vector $\mathbf{u}$ y $v_1, v_2, v_3$ son las componentes del vector $\mathbf{v}$.

El vector resultante del producto cruz es perpendicular al plano definido por los vectores de entrada $\mathbf{u}$ y $\mathbf{v}$. Su dirección viene dada por la regla de la mano derecha, donde el pulgar representa la dirección del producto cruz.

El producto cruz es utilizado en diversas áreas, como la física (momento angular), la geometría (área de un paralelogramo) y la representación gráfica de objetos tridimensionales.

## Producto Mixto

El producto mixto, también conocido como producto escalar triple, es una operación que involucra tres vectores en el espacio tridimensional $\mathbb{R}^3$. El resultado del producto mixto entre los vectores $\mathbf{u}$, $\mathbf{v}$ y $\mathbf{w}$, denotado como $[\mathbf{u}, \mathbf{v}, \mathbf{w}]$, es un escalar que representa el volumen del paralelepípedo formado por los tres vectores.

El cálculo del producto mixto se puede realizar utilizando la siguiente fórmula:

$$
[\mathbf{u}, \mathbf{v}, \mathbf{w}] = \mathbf{u} \cdot (\mathbf{v} \times \mathbf{w})
$$

donde $\cdot$ denota el producto punto y $\times$ denota el producto cruz.

El producto mixto tiene algunas propiedades interesantes. Por ejemplo, si el producto mixto es igual a cero, esto indica que los tres vectores son coplanares (se encuentran en un mismo plano). Además, el producto mixto es invariante bajo permutaciones cíclicas, lo que significa que no importa el orden en el que se tomen los vectores.

El producto mixto es utilizado en diversas áreas, como la física (cálculo de torque), la geometría (volumen de un tetraedro) y la mecánica de fluidos (flujo volumétrico).


'''
