import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64



r'''
# Transformaciones Lineales

En álgebra lineal, las transformaciones lineales son funciones que preservan las operaciones de suma vectorial y multiplicación por escalar. Estas transformaciones juegan un papel fundamental en el estudio de las relaciones y propiedades de los espacios vectoriales. En este artículo, exploraremos en detalle qué son las transformaciones lineales, sus propiedades y algunos ejemplos para comprender su importancia en el álgebra lineal.

## Definición de Transformación Lineal

Una transformación lineal, también conocida como aplicación lineal o función lineal, es una función $T: \mathbb{V} \rightarrow \mathbb{W}$ que asigna vectores de un espacio vectorial $\mathbb{V}$ a vectores de otro espacio vectorial $\mathbb{W}$, y cumple con las siguientes propiedades:

1. Preserva la suma vectorial: Para cualquier par de vectores $\mathbf{u}$ y $\mathbf{v}$ en $\mathbb{V}$, se cumple que $T(\mathbf{u} + \mathbf{v}) = T(\mathbf{u}) + T(\mathbf{v})$.

2. Preserva la multiplicación por escalar: Para cualquier escalar $c$ y vector $\mathbf{u}$ en $\mathbb{V}$, se cumple que $T(c\mathbf{u}) = cT(\mathbf{u})$.

Estas propiedades garantizan que la estructura vectorial se mantiene en la transformación, lo que implica que las relaciones entre los vectores, como la linealidad, se preservan.

## Matriz de Transformación Lineal

Una transformación lineal se puede representar mediante una matriz. Si $\mathbb{V}$ y $\mathbb{W}$ son espacios vectoriales con bases ordenadas $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ y $\{\mathbf{w}_1, \mathbf{w}_2, \ldots, \mathbf{w}_m\}$, respectivamente, entonces una transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$ se puede representar mediante una matriz $A$, donde cada columna de la matriz es la imagen de la correspondiente base ordenada de $\mathbb{V}$ bajo la transformación $T$. La matriz $A$ se denomina matriz de transformación lineal.

La representación matricial de una transformación lineal permite realizar cálculos y análisis algebraicos de manera más eficiente, ya que se aprovechan las propiedades de las matrices.

## Propiedades de las Transformaciones Lineales

Las transformaciones lineales poseen varias propiedades importantes:

1. La transformación lineal de un vector nulo siempre es el vector nulo en el espacio de llegada: $T(\mathbf{0}) = \mathbf{0}$.

2. La transformación lineal de una combinación lineal de vectores es igual a la combinación lineal de las transformaciones lineales de los vectores individuales:

$T(c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \ldots + c_n\mathbf{v}_n) = c_1T(\mathbf{v}_1) + c_2T(\mathbf{v}_2) + \ldots + c_nT(\mathbf{v}_n)$.

3. La composición de dos transformaciones lineales es también una transformación lineal.

4. La identidad del espacio vectorial se mapea a sí misma bajo cualquier transformación lineal: $T(\mathbf{v}) = \mathbf{v}$.

Estas propiedades garantizan que las transformaciones lineales preserven las operaciones y propiedades fundamentales de los espacios vectoriales.

## Ejemplos de Transformaciones Lineales

1. La traslación en el plano: Consideremos el espacio vectorial $\mathbb{R}^2$ y una transformación lineal $T$ que toma un vector $\mathbf{v} = \begin{bmatrix} x \\ y \end{bmatrix}$ y lo traslada en una dirección fija por una cantidad fija. Por ejemplo, $T(\mathbf{v}) = \begin{bmatrix} x + 2 \\ y - 3 \end{bmatrix}$. Esta transformación preserva la estructura vectorial, ya que la suma de vectores se mantiene y la multiplicación por escalar también.

2. La proyección ortogonal en el plano: Consideremos el espacio vectorial $\mathbb{R}^2$ y una transformación lineal $T$ que proyecta un vector $\mathbf{v}$ sobre un subespacio dado. Por ejemplo, $T(\mathbf{v})$ es la proyección ortogonal de $\mathbf{v}$ sobre una línea recta dada. Esta transformación también cumple con las propiedades de una transformación lineal.


'''



r'''
# Núcleo y Recorrido de una Transformación Lineal

En álgebra lineal, el núcleo y el recorrido (o imagen) son conceptos fundamentales asociados a las transformaciones lineales entre espacios vectoriales. Estos conceptos nos permiten entender la estructura y las propiedades de las transformaciones lineales en términos de los vectores de entrada y salida. En este artículo, exploraremos en detalle qué son el núcleo y el recorrido de una transformación lineal, así como su relación con la dimensión de los espacios involucrados.

## Núcleo de una Transformación Lineal

El núcleo de una transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$, denotado como $\text{ker}(T)$, es el conjunto de vectores en el dominio $\mathbb{V}$ que se mapean al vector cero en el espacio de llegada $\mathbb{W}$. Formalmente, se define como:

$$\text{ker}(T) = \{\mathbf{v} \in \mathbb{V} \mid T(\mathbf{v}) = \mathbf{0}\}$$

El núcleo representa los vectores en $\mathbb{V}$ que "desaparecen" después de aplicar la transformación lineal. Es decir, son los vectores que se transforman en el vector cero de $\mathbb{W}$. El núcleo siempre incluye al vector cero, ya que cualquier transformación lineal debe mapear el vector cero al vector cero.

## Recorrido de una Transformación Lineal

El recorrido (o imagen) de una transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$, denotado como $\text{Im}(T)$, es el conjunto de todos los vectores en el espacio de llegada $\mathbb{W}$ que se obtienen al aplicar la transformación a los vectores en el dominio $\mathbb{V}$. Formalmente, se define como:

$$\text{Im}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in \mathbb{V}\}$$

El recorrido representa el conjunto de vectores en $\mathbb{W}$ que se pueden obtener mediante la transformación lineal. Es decir, son los vectores que "aparecen" en $\mathbb{W}$ como resultado de aplicar la transformación lineal a los vectores en $\mathbb{V}$. El recorrido puede ser todo el espacio $\mathbb{W}$ o un subespacio de $\mathbb{W}$, dependiendo de la transformación lineal.

## Dimensión del Núcleo y el Recorrido

La dimensión del núcleo de una transformación lineal, denotada como $\text{dim}(\text{ker}(T))$, es el número de vectores linealmente independientes en el núcleo. Indica la cantidad de restricciones que impone la transformación lineal en el dominio. Si el núcleo tiene dimensión cero, esto significa que la única solución para $T(\mathbf{v}) = \mathbf{0}$ es el vector cero, lo que implica que la transformación lineal es inyectiva.

La dimensión del recorrido de una transformación lineal, denotada como $\text{dim}(\text{Im}(T))$, es el número de vectores linealmente independientes en el recorrido. Indica la cantidad de vectores únicos que se obtienen al aplicar la transformación lineal. Si el recorrido tiene la misma dimensión que el espacio de llegada, esto significa que la transformación lineal es sobreyectiva.

Un resultado importante en álgebra lineal es el Teorema del Núcleo e Imagen, que establece que la suma de las dimensiones del núcleo y el recorrido de una transformación lineal es igual a la dimensión del espacio de partida:

$$\text{dim}(\text{ker}(T)) + \text{dim}(\text{Im}(T)) = \text{dim}(\mathbb{V})$$

Este teorema nos brinda información sobre cómo se relacionan el núcleo y el recorrido de una transformación lineal y cómo se relacionan con las dimensiones de los espacios vectoriales involucrados.

## Ejemplos

1. Consideremos la transformación lineal $T: \mathbb{R}^2 \rightarrow \mathbb{R}^3$ definida por $T\left(\begin{bmatrix} x \\ y \end{bmatrix}\right) = \begin{bmatrix} x \\ y \\ 0 \end{bmatrix}$. En este caso, el núcleo de $T$ consiste en los vectores $\begin{bmatrix} x \\ y \end{bmatrix}$ tales que $x = 0$ y $y = 0$, es decir, el núcleo es el vector cero. El recorrido de $T$ consiste en todos los vectores de la forma $\begin{bmatrix} x \\ y \\ 0 \end{bmatrix}$, que forman un subespacio de $\mathbb{R}^3$ de dimensión 2.

2. Consideremos la transformación lineal $T: \mathbb{R}^3 \rightarrow \mathbb{R}^2$ definida por $T\left(\begin{bmatrix} x \\ y \\ z \end{bmatrix}\right) = \begin{bmatrix} x + y \\ 2y - z \end{bmatrix}$. En este caso, el núcleo de $T$ consiste en los vectores $\begin{bmatrix} x \\ y \\ z \end{bmatrix}$ tales que $x + y = 0$ y $2y - z = 0$. Esto implica que el núcleo está dado por los vectores de la forma $\begin{bmatrix} -y \\ y \\ 2y \end{bmatrix}$, donde $y$ puede tomar cualquier valor. Por lo tanto, el núcleo de $T$ es un subespacio de $\mathbb{R}^3$ de dimensión 1. El recorrido de $T$ consiste en todos los vectores de la forma $\begin{bmatrix} x + y \\ 2y - z \end{bmatrix}$, que forman un subespacio de $\mathbb{R}^2$ de dimensión 2.


'''



r'''
# Transformaciones Lineales Inversas

En álgebra lineal, una transformación lineal inversa es aquella que deshace los efectos de otra transformación lineal. En otras palabras, si tenemos una transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$, una transformación lineal inversa sería otra transformación $T^{-1}: \mathbb{W} \rightarrow \mathbb{V}$ que nos permite regresar al espacio original.

## Definición de una Transformación Lineal Inversa

Dada una transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$, una transformación lineal inversa $T^{-1}: \mathbb{W} \rightarrow \mathbb{V}$ cumple las siguientes condiciones:

1. La composición de $T$ con $T^{-1}$ y la composición de $T^{-1}$ con $T$ resultan en las identidades de cada espacio vectorial:

   $$T \circ T^{-1} = \text{id}_{\mathbb{W}}$$
   $$T^{-1} \circ T = \text{id}_{\mathbb{V}}$$

   Donde $\text{id}_{\mathbb{W}}$ es la transformación identidad en el espacio $\mathbb{W}$ y $\text{id}_{\mathbb{V}}$ es la transformación identidad en el espacio $\mathbb{V}$.

2. La transformación inversa $T^{-1}$ es también lineal, lo que significa que preserva la estructura de los espacios vectoriales, es decir, cumple con las propiedades de linealidad.

La existencia de una transformación lineal inversa depende de la biyectividad de la transformación $T$. Si la transformación es biyectiva, es decir, es inyectiva (cada vector de $\mathbb{V}$ se mapea a un vector único en $\mathbb{W}$) y sobreyectiva (todos los vectores en $\mathbb{W}$ tienen un preimagen en $\mathbb{V}$), entonces existe una única transformación lineal inversa.

## Ejemplos de Transformaciones Lineales Inversas

1. Consideremos la transformación lineal de rotación en el plano, $T: \mathbb{R}^2 \rightarrow \mathbb{R}^2$, que rota cada vector en sentido antihorario por un ángulo fijo. La transformación inversa $T^{-1}$ sería una rotación en sentido horario por el mismo ángulo, lo que nos permitiría regresar al vector original.

2. Consideremos la transformación lineal de proyección en el plano, $T: \mathbb{R}^2 \rightarrow \mathbb{R}^2$, que proyecta cada vector sobre una línea recta fija. La transformación inversa $T^{-1}$ sería una transformación de expansión que mapea el vector proyectado de vuelta al vector original.

Estos ejemplos ilustran cómo una transformación lineal inversa puede deshacer los efectos de una transformación lineal, permitiéndonos regresar al espacio original.

## Importancia de las Transformaciones Lineales Inversas

Las transformaciones lineales inversas son fundamentales en álgebra lineal debido a su capacidad para deshacer transformaciones y restablecer el estado original del sistema.
Estas transformaciones juegan un papel crucial en la resolución de sistemas de ecuaciones lineales, el análisis de la estructura de los espacios vectoriales y la comprensión de las propiedades y comportamientos de las transformaciones lineales.

Además, las transformaciones lineales inversas nos permiten establecer una correspondencia biunívoca entre los espacios vectoriales de partida y llegada, lo que nos brinda una forma de relacionar y comparar las propiedades y estructuras de los espacios involucrados.


# Transformaciones Lineales Uno a Uno

En álgebra lineal, una transformación lineal uno a uno, también conocida como una transformación inyectiva, es aquella en la que cada vector en el espacio de partida se mapea a un vector único en el espacio de llegada. Esto implica que no hay dos vectores diferentes en el espacio de partida que se mapeen al mismo vector en el espacio de llegada.

## Definición de Transformación Lineal Uno a Uno

Dada una transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$, se dice que $T$ es uno a uno si se cumple la siguiente propiedad:

Para cualquier par de vectores $\mathbf{v}_1$ y $\mathbf{v}_2$ en $\mathbb{V}$, si $\mathbf{v}_1 \neq \mathbf{v}_2$, entonces $T(\mathbf{v}_1) \neq T(\mathbf{v}_2)$.

En otras palabras, si dos vectores diferentes en el espacio de partida se mapean a vectores iguales en el espacio de llegada, la transformación no es uno a uno. Si todos los vectores diferentes se mapean a vectores diferentes en el espacio de llegada, entonces la transformación es uno a uno.

## Características de las Transformaciones Lineales Uno a Uno

Las transformaciones lineales uno a uno tienen algunas características importantes:

1. Cada vector en el espacio de partida tiene una única imagen en el espacio de llegada. Esto significa que no hay redundancia en la transformación y no se pierde información.

2. La inversa de una transformación lineal uno a uno existe y es una transformación lineal también. Esto permite deshacer la transformación y recuperar los vectores originales.

3. Si la transformación lineal es uno a uno y sobreyectiva (cada vector en el espacio de llegada tiene una preimagen en el espacio de partida), entonces se dice que la transformación es una biyección. En este caso, la transformación tiene una inversa única y establece una correspondencia uno a uno entre los espacios de partida y llegada.

## Ejemplos de Transformaciones Lineales Uno a Uno

1. La transformación lineal de rotación en el plano es uno a uno. Cada vector en el espacio de partida se mapea a un vector único en el espacio de llegada, sin que haya dos vectores diferentes que se mapeen al mismo vector.

2. La transformación lineal de proyección sobre una línea recta en el plano no es uno a uno. Varios vectores en el espacio de partida se mapean al mismo vector en el espacio de llegada, lo que resulta en una pérdida de información y no permite recuperar los vectores originales.

'''




r'''
# Isomorfismos y Transformaciones Lineales

En álgebra lineal, los isomorfismos son transformaciones lineales que establecen una correspondencia biunívoca entre dos espacios vectoriales, preservando la estructura y las propiedades algebraicas. Los isomorfismos son de gran importancia, ya que nos permiten relacionar y comparar diferentes espacios vectoriales, simplificando el estudio y la resolución de problemas.

## Definición de Isomorfismo

Dadas dos espacios vectoriales $\mathbb{V}$ y $\mathbb{W}$, una transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$ se dice que es un isomorfismo si cumple las siguientes condiciones:

1. Inyectividad: Cada vector diferente en $\mathbb{V}$ se mapea a un vector diferente en $\mathbb{W}$. En otras palabras, si $T(\mathbf{v}_1) = T(\mathbf{v}_2)$, entonces $\mathbf{v}_1 = \mathbf{v}_2$.

2. Sobreyectividad: Cada vector en $\mathbb{W}$ tiene al menos una preimagen en $\mathbb{V}$. En otras palabras, para todo vector $\mathbf{w}$ en $\mathbb{W}$, existe al menos un vector $\mathbf{v}$ en $\mathbb{V}$ tal que $T(\mathbf{v}) = \mathbf{w}$.

3. Preservación de la estructura: La operación de suma de vectores y la multiplicación por escalares se preservan en la transformación. Esto significa que para cualquier par de vectores $\mathbf{v}_1, \mathbf{v}_2$ en $\mathbb{V}$ y cualquier escalar $c$, se cumple:

   $$T(\mathbf{v}_1 + \mathbf{v}_2) = T(\mathbf{v}_1) + T(\mathbf{v}_2)$$
   $$T(c \mathbf{v}) = c T(\mathbf{v})$$

Si una transformación lineal cumple estas condiciones, se dice que es un isomorfismo entre los espacios vectoriales $\mathbb{V}$ y $\mathbb{W}$. En este caso, los espacios vectoriales son isomorfos y se denota como $\mathbb{V} \cong \mathbb{W}$.

## Propiedades de los Isomorfismos

Los isomorfismos tienen varias propiedades importantes:

1. Los isomorfismos conservan la dimensión de los espacios vectoriales. Si $\mathbb{V} \cong \mathbb{W}$, entonces $\dim(\mathbb{V}) = \dim(\mathbb{W})$.

2. La composición de dos isomorfismos es también un isomorfismo. Si $T: \mathbb{V} \rightarrow \mathbb{W}$ y $S: \mathbb{W} \rightarrow \mathbb{U}$ son isomorfismos, entonces $S \circ T: \mathbb{V} \rightarrow \mathbb{U}$ también es un isomorfismo.

3. Todo espacio vectorial es isomorfo a sí mismo a través de la transformación identidad $\text{id}_{\mathbb{V}}: \mathbb{V} \rightarrow \mathbb{V}$, donde $\text{id}_{\mathbb{V}}(\mathbf{v}) = \mathbf{v}$ para todo $\mathbf{v}$ en $\mathbb{V}$.

## Teorema del Isomorfismo

El teorema del isomorfismo establece que si $T: \mathbb{V} \rightarrow \mathbb{W}$ es un isomorfismo, entonces el núcleo y el recorrido de $T$ están relacionados con los espacios vectoriales $\mathbb{V}$ y $\mathbb{W}$ de la siguiente manera:

1. $\text{null}(T) = \{\mathbf{v} \in \mathbb{V} \mid T(\mathbf{v}) = \mathbf{0}\}$ es el núcleo de $T$, y es un subespacio vectorial de $\mathbb{V}$.

2. $\text{range}(T) = \{T(\mathbf{v}) \mid \mathbf{v} \in \mathbb{V}\}$ es el recorrido de $T$, y es un subespacio vectorial de $\mathbb{W}$.

Además, el teorema del isomorfismo establece que el cociente $\mathbb{V}/\text{null}(T)$ es isomorfo a $\text{range}(T)$, es decir:

$$\mathbb{V}/\text{null}(T) \cong \text{range}(T)$$

Este teorema es fundamental en el estudio de las transformaciones lineales, ya que nos permite comprender la relación entre los espacios de partida y llegada, y proporciona una forma de visualizar y manipular los espacios vectoriales a través de isomorfismos.

## Ejemplos de Isomorfismos

1. La transformación lineal de rotación en el plano es un isomorfismo entre $\mathbb{R}^2$ y $\mathbb{R}^2$. Cada vector en $\mathbb{R}^2$ tiene una única imagen bajo la rotación, y la operación de suma de vectores y multiplicación por escalares se preserva.

2. La transformación lineal de escalamiento en el plano, donde cada vector se multiplica por un escalar, es un isomorfismo entre $\mathbb{R}^2$ y $\mathbb{R}^2$. Esta transformación conserva la estructura del espacio vectorial y establece una correspondencia biunívoca entre los vectores de partida y llegada.

'''


r'''
# Teoremas


## 1. Teorema de la imagen de un subespacio:
   Si $T: \mathbb{V} \rightarrow \mathbb{W}$ es una transformación lineal y $\mathbb{U}$ es un subespacio de $\mathbb{V}$, entonces $T(\mathbb{U})$ es un subespacio de $\mathbb{W}$.

## 2. Teorema del núcleo e imagen:
   Para cualquier transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$, se cumple:
   - $\text{null}(T)$ es un subespacio de $\mathbb{V}$.
   - $\text{range}(T)$ es un subespacio de $\mathbb{W}$.
   - $\dim(\text{null}(T)) + \dim(\text{range}(T)) = \dim(\mathbb{V})$.

## 3. Teorema del rango y la nulidad:
   Para cualquier transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$, se cumple:
   - $\dim(\text{range}(T)) \leq \dim(\mathbb{W})$.
   - $\dim(\text{null}(T)) \geq 0$ y $\dim(\text{null}(T)) \leq \dim(\mathbb{V})$.
   - Si $\dim(\text{null}(T)) = 0$, entonces $T$ es inyectiva (uno a uno).
   - Si $\dim(\text{range}(T)) = \dim(\mathbb{W})$, entonces $T$ es sobreyectiva (sobre).

## 4. Teorema del isomorfismo:
   Si $T: \mathbb{V} \rightarrow \mathbb{W}$ es una transformación lineal, entonces $\mathbb{V}/\text{null}(T) \cong \text{range}(T)$.

## 5. Teorema de la composición de transformaciones lineales:
   Si $T: \mathbb{U} \rightarrow \mathbb{V}$ y $S: \mathbb{V} \rightarrow \mathbb{W}$ son transformaciones lineales, entonces la composición $S \circ T: \mathbb{U} \rightarrow \mathbb{W}$ también es una transformación lineal.

## 6. Teorema del isomorfismo para matrices:
   Si $A$ es una matriz $m \times n$ y $T: \mathbb{R}^n \rightarrow \mathbb{R}^m$ es la transformación lineal asociada a $A$, entonces $\mathbb{R}^n/\text{null}(A) \cong \text{range}(T)$.



## 7. Teorema de la inversa para transformaciones lineales:
   Sea $T: \mathbb{V} \rightarrow \mathbb{W}$ una transformación lineal biyectiva (uno a uno y sobre). Entonces existe una transformación lineal inversa $T^{-1}: \mathbb{W} \rightarrow \mathbb{V}$ tal que $T \circ T^{-1} = \text{id}_{\mathbb{W}}$ y $T^{-1} \circ T = \text{id}_{\mathbb{V}}$. En otras palabras, $T^{-1}$ deshace la transformación realizada por $T$.

## 8. Teorema del rango-defecto:
   Para cualquier transformación lineal $T: \mathbb{V} \rightarrow \mathbb{W}$, se cumple:
   - $\dim(\text{range}(T)) = \text{rango}(T)$, que es el número máximo de columnas linealmente independientes en la matriz asociada a $T$.
   - $\dim(\text{null}(T)) = \text{defecto}(T)$, que es el número de soluciones linealmente independientes de la ecuación homogénea $T(\mathbf{v}) = \mathbf{0}$.

## 9. Teorema del cambio de base para transformaciones lineales:
   Sea $T: \mathbb{V} \rightarrow \mathbb{W}$ una transformación lineal, y sean $B$ y $B'$ bases de $\mathbb{V}$, y $C$ y $C'$ bases de $\mathbb{W}$. Si $P_{B \rightarrow B'}$ y $P_{C \rightarrow C'}$ son las matrices de cambio de base respectivas, entonces la matriz asociada a $T$ en las bases $B$ y $C$ es similar a la matriz asociada a $T$ en las bases $B'$ y $C'$, es decir:
   $$[T]_{B,C} = P_{B \rightarrow B'}^{-1} \cdot [T]_{B',C'} \cdot P_{C \rightarrow C'}$$

## 10. Teorema de la dimensión del núcleo y el rango:

Para cualquier matriz $A$, se cumple:
    - $\text{rango}(A) + \text{defecto}(A) = \text{columnas}(A)$, donde $\text{columnas}(A)$ es el número de columnas de $A$.
    - $\text{rango}(A) + \text{nulidad}(A) = \text{columnas}(A)$, donde $\text{nulidad}(A)$ es el número de soluciones linealmente independientes de la ecuación homogénea $A\mathbf{x} = \mathbf{0}$.


'''
