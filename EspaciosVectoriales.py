import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp


st.title('Espacios Vectoriales sobre Campos')


r'''

Un espacio vectorial sobre un campo $F$ es una estructura algebraica que combina un conjunto no vacío $V$ con dos operaciones: la adición de vectores y la multiplicación por escalares. En este resumen, exploraremos los axiomas, operaciones y propiedades fundamentales de los espacios vectoriales sobre campos.

### Axiomas

Para que un conjunto $V$ junto con las operaciones de adición de vectores y multiplicación por escalares forme un espacio vectorial sobre un campo $F$, se deben cumplir los siguientes axiomas:

1. **Cerradura de la adición**: Para todo $\mathbf{u}, \mathbf{v} \in V$, la suma de vectores $\mathbf{u} + \mathbf{v}$ está definida y pertenece a $V$.

2. **Asociatividad de la adición**: Para todo $\mathbf{u}, \mathbf{v}, \mathbf{w} \in V$, se cumple $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$.

3. **Elemento neutro de la adición**: Existe un vector especial $\mathbf{0} \in V$ llamado vector cero tal que $\mathbf{v} + \mathbf{0} = \mathbf{v}$ para todo $\mathbf{v} \in V$.

4. **Elemento opuesto**: Para todo $\mathbf{v} \in V$, existe un vector en $V$ denotado como $-\mathbf{v}$ tal que $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$.

5. **Cerradura de la multiplicación por escalares**: Para todo $\alpha \in F$ y $\mathbf{v} \in V$, el producto escalar $\alpha\mathbf{v}$ está definido y pertenece a $V$.

6. **Asociatividad de la multiplicación por escalares con la adición de vectores**: Para todo $\alpha \in F$ y $\mathbf{u}, \mathbf{v} \in V$, se cumple $\alpha(\mathbf{u} + \mathbf{v}) = \alpha\mathbf{u} + \alpha\mathbf{v}$.

7. **Asociatividad de la multiplicación por escalares con la multiplicación por escalares**: Para todo $\alpha, \beta \in F$ y $\mathbf{v} \in V$, se cumple $(\alpha\beta)\mathbf{v} = \alpha(\beta\mathbf{v})$.

8. **Elemento neutro de la multiplicación por escalares**: Existe un escalar especial $1 \in F$ tal que $1\mathbf{v} = \mathbf{v}$ para todo $\mathbf{v} \in V$.

### Operaciones y Propiedades Fundamentales

Además de los axiomas, los espacios vectoriales sobre campos también presentan operaciones y propiedades fundamentales:

1. **Suma de vectores**: La suma de dos vectores $\mathbf{u}$ y $\mathbf{v}$ en $V$ se define como $\mathbf{u} + \mathbf{v}$. Esta operación cumple las propiedades conmutativa, asociativa y tiene un elemento neutro.

2. **Multiplicación por escalares**: La multiplicación de un vector $\mathbf{v}$ en $V$ por un escalar $\alpha$ en $F$ se denota como $\alpha\mathbf{v}$. Esta operación cumple la propiedad asociativa, distributiva y tiene un elemento neutro.

3. **Propiedad distributiva**: Para todo $\alpha \in F$ y $\mathbf{u}, \mathbf{v} \in V$, se cumple $\alpha(\mathbf{u} + \mathbf{v}) = \alpha\mathbf{u} + \alpha\mathbf{v}$.

4. **Propiedad distributiva**: Para todo $\alpha, \beta \in F$ y $\mathbf{v} \in V$, se cumple $(\alpha + \beta)\mathbf{v} = \alpha\mathbf{v} + \beta\mathbf{v}$.

5. **Asociatividad de la multiplicación por escalares con la multiplicación de campos**: Para todo $\alpha, \beta \in F$ y $\mathbf{v} \in V$, se cumple $(\alpha\beta)\mathbf{v} = \alpha(\beta\mathbf{v})$.

Estas operaciones y propiedades fundamentales permiten realizar cálculos y manipular vectores en los espacios vectoriales sobre campos.


# Ejemplos de Espacios Vectoriales

En el álgebra lineal, un espacio vectorial es un conjunto de elementos llamados vectores, sobre un campo de escalares, que cumple ciertas propiedades. Estos espacios vectoriales se encuentran presentes en diversas áreas de las matemáticas y las ciencias, y tienen aplicaciones prácticas en muchos campos. A continuación, presentaremos algunos ejemplos de espacios vectoriales para ilustrar estas ideas.

## Ejemplo 1: Espacio Vectorial de Vectores en $\mathbb{R}^n$

Un ejemplo fundamental de espacio vectorial es el conjunto de vectores en el espacio euclidiano $\mathbb{R}^n$. En este espacio, los vectores tienen $n$ componentes y se pueden sumar y multiplicar por escalares. Además, se cumplen las siguientes propiedades:

1. Cierre bajo la suma: La suma de dos vectores en $\mathbb{R}^n$ es otro vector en $\mathbb{R}^n$.
2. Asociatividad de la suma: Para cualquier vector $\mathbf{u}$, $\mathbf{v}$ y $\mathbf{w}$ en $\mathbb{R}^n$, se cumple $(\mathbf{u} + \mathbf{v}) + \mathbf{w} = \mathbf{u} + (\mathbf{v} + \mathbf{w})$.
3. Existencia de elemento neutro: Existe un vector cero $\mathbf{0}$ en $\mathbb{R}^n$ tal que $\mathbf{v} + \mathbf{0} = \mathbf{v}$ para cualquier vector $\mathbf{v}$ en $\mathbb{R}^n$.
4. Existencia de elemento opuesto: Para cada vector $\mathbf{v}$ en $\mathbb{R}^n$, existe un vector opuesto $-\mathbf{v}$ en $\mathbb{R}^n$ tal que $\mathbf{v} + (-\mathbf{v}) = \mathbf{0}$.
5. Cierre bajo la multiplicación por escalar: El producto de un vector en $\mathbb{R}^n$ por un escalar es otro vector en $\mathbb{R}^n$.
6. Distributividad de la suma respecto a la multiplicación por escalar: Para cualquier escalar $a$ y vectores $\mathbf{u}$, $\mathbf{v}$ en $\mathbb{R}^n$, se cumple $a(\mathbf{u} + \mathbf{v}) = a\mathbf{u} + a\mathbf{v}$.
7. Distributividad de la multiplicación por escalar respecto a la suma de vectores: Para cualquier escalar $a$, $b$ y vector $\mathbf{v}$ en $\mathbb{R}^n$, se cumple $(a + b)\mathbf{v} = a\mathbf{v} + b\mathbf{v}$.
8. Asociatividad de la multiplicación por escalar: Para cualquier escalar $a$ y $b$, y vector $\mathbf{v}$ en $\mathbb{R}^n$, se cumple $(ab)\mathbf{v} = a(b\mathbf{v})$.
9. Existencia de elemento neutro para la multiplicación por escalar: El escalar $1$ actúa como un elemento neutro

 para la multiplicación por escalar, es decir, $1\mathbf{v} = \mathbf{v}$ para cualquier vector $\mathbf{v}$ en $\mathbb{R}^n$.

Este ejemplo ilustra un espacio vectorial muy utilizado en la práctica, donde los vectores representan puntos en un espacio $n$-dimensional.

## Ejemplo 2: Espacio Vectorial de Polinomios

Otro ejemplo común de espacio vectorial es el conjunto de polinomios con coeficientes en un campo dado, como $\mathbb{R}$ o $\mathbb{C}$. En este caso, los vectores son polinomios y las operaciones de suma y multiplicación por escalar se definen de la siguiente manera:

1. Cierre bajo la suma: La suma de dos polinomios es otro polinomio.
2. Asociatividad de la suma: Para cualquier polinomio $p(x)$, $q(x)$ y $r(x)$, se cumple $(p(x) + q(x)) + r(x) = p(x) + (q(x) + r(x))$.
3. Existencia de elemento neutro: Existe un polinomio cero, denotado como $0(x)$, tal que $p(x) + 0(x) = p(x)$ para cualquier polinomio $p(x)$.
4. Existencia de elemento opuesto: Para cada polinomio $p(x)$, existe un polinomio opuesto $-p(x)$ tal que $p(x) + (-p(x)) = 0(x)$.
5. Cierre bajo la multiplicación por escalar: El producto de un polinomio por un escalar es otro polinomio.
6. Distributividad de la suma respecto a la multiplicación por escalar: Para cualquier escalar $a$ y polinomios $p(x)$, $q(x)$, se cumple $a(p(x) + q(x)) = ap(x) + aq(x)$.
7. Distributividad de la multiplicación por escalar respecto a la suma de polinomios: Para cualquier escalar $a$, $b$ y polinomio $p(x)$, se cumple $(a + b)p(x) = ap(x) + bp(x)$.
8. Asociatividad de la multiplicación por escalar: Para cualquier escalar $a$ y $b$, y polinomio $p(x)$, se cumple $(ab)p(x) = a(bp(x))$.
9. Existencia de elemento neutro para la multiplicación por escalar: El escalar $1$ actúa como un elemento neutro para la multiplicación por escalar, es decir, $1p(x) = p(x)$ para cualquier polinomio $p(x)$.

Este ejemplo muestra cómo los polinomios forman un espacio vectorial, donde los vectores son combinaciones lineales de términos polinómicos.


'''



r'''
# Subespacios Vectoriales

En álgebra lineal, los subespacios vectoriales son conjuntos de vectores que cumplen ciertas propiedades y forman espacios vectoriales más pequeños. El estudio de los subespacios vectoriales es fundamental para comprender la estructura y propiedades de los espacios vectoriales en general.

## Definición de Subespacio Vectorial

Un subespacio vectorial $V$ de un espacio vectorial $W$ es un conjunto no vacío que cumple las siguientes tres condiciones:

1. Cierre bajo la suma: Si $\mathbf{u}$ y $\mathbf{v}$ son vectores en $V$, entonces $\mathbf{u} + \mathbf{v}$ también pertenece a $V$.
2. Cierre bajo la multiplicación por escalar: Si $\mathbf{v}$ es un vector en $V$ y $a$ es un escalar, entonces $a\mathbf{v}$ pertenece a $V$.
3. Contiene el vector cero: El vector cero $\mathbf{0}$ siempre está en $V$.

Estas condiciones garantizan que el subespacio vectorial $V$ herede las operaciones de suma y multiplicación por escalar de $W$, y también garantizan que $V$ sea un espacio vectorial en sí mismo. Es importante destacar que un subespacio vectorial debe ser un conjunto no vacío, por lo que siempre debe contener al menos el vector cero.

## Propiedades de los Subespacios Vectoriales

Los subespacios vectoriales tienen varias propiedades importantes:

1. El vector cero siempre está en cualquier subespacio vectorial, ya que cumple con la condición de contener el vector cero.
2. Si $\mathbf{v}$ es un vector en un subespacio vectorial $V$, entonces el opuesto de $\mathbf{v}$, denotado como $-\mathbf{v}$, también está en $V$.
3. La intersección de dos o más subespacios vectoriales también es un subespacio vectorial.
4. La unión de dos subespacios vectoriales no necesariamente es un subespacio vectorial, a menos que uno de ellos esté contenido dentro del otro.

## Ejemplos de Subespacios Vectoriales

1. En el espacio vectorial $\mathbb{R}^2$, la recta que pasa por el origen de coordenadas es un subespacio vectorial. Todos los vectores en esta recta son múltiplos escalares de un vector fijo que la define.
2. En el espacio vectorial de matrices $2 \times 2$, el conjunto de todas las matrices diagonales forma un subespacio vectorial. Este subespacio incluye la matriz cero y todas las combinaciones lineales de matrices diagonales.
3. En el espacio vectorial de funciones continuas en un intervalo dado, el conjunto de todas las funciones polinómicas forma un subespacio vectorial.
4. En el espacio vectorial de polinomios de grado $n$ o menor, el conjunto de polinomios de grado exactamente $n$ forma un subespacio vectorial.

Estos ejemplos ilustran la diversidad de subespacios vectoriales que se pueden encontrar en distintos contextos matemáticos.

'''



r'''
# Combinaciones Lineales

En álgebra lineal, una combinación lineal es una expresión que involucra la multiplicación de vectores por escalares y la suma de estos productos. Las combinaciones lineales son fundamentales para comprender la relación entre los vectores y la generación de nuevos vectores a partir de un conjunto dado. En este artículo, exploraremos en detalle las combinaciones lineales, su definición, propiedades y ejemplos ilustrativos.

## Definición de Combinación Lineal

Dado un conjunto de vectores $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ en un espacio vectorial, una combinación lineal de estos vectores se define como la suma ponderada de los vectores multiplicados por escalares. Formalmente, para escalares $a_1, a_2, \ldots, a_n$, la combinación lineal de los vectores se representa de la siguiente manera:

$$a_1\mathbf{v}_1 + a_2\mathbf{v}_2 + \ldots + a_n\mathbf{v}_n$$

En esta expresión, cada escalar $a_i$ multiplica al correspondiente vector $\mathbf{v}_i$. La combinación lineal resultante es un nuevo vector que se obtiene al sumar los productos escalares.

## Propiedades de las Combinaciones Lineales

Las combinaciones lineales tienen varias propiedades importantes:

1. Cierre bajo la suma: La combinación lineal de dos o más vectores sigue siendo un vector en el mismo espacio vectorial.
2. Cierre bajo la multiplicación por escalar: La multiplicación de una combinación lineal por un escalar produce otra combinación lineal.
3. Distributividad de la suma de vectores: La suma de dos combinaciones lineales es igual a la combinación lineal de las sumas de los vectores correspondientes.
4. Asociatividad de la suma de vectores: La suma de tres o más combinaciones lineales es independiente del orden en que se realicen las sumas.

Estas propiedades permiten manipular y operar con combinaciones lineales de manera algebraica y establecen la base para la generación de nuevos vectores a partir de combinaciones lineales.

## Ejemplos de Combinaciones Lineales

1. En el espacio vectorial $\mathbb{R}^2$, considere los vectores $\mathbf{v}_1 = (1, 0)$ y $\mathbf{v}_2 = (0, 1)$. La combinación lineal $2\mathbf{v}_1 + 3\mathbf{v}_2$ sería $(2, 0) + (0, 3) = (2, 3)$. Esta combinación lineal genera un nuevo vector en $\mathbb{R}^2$ que es una combinación ponderada de los vectores originales.

2. En el espacio vectorial de polinomios de grado 2 o menor, considere los polinomios $p_1(x) = 2x^2 - x$ y $p_2(x) = x^2 + 3$. La combinación lineal $3p_1(x) - 2p_2(x)$ sería $3(2x^2 - x) - 2(x^2 + 3) = 6x^2 - 3x - 2x^2 - 6 = 4x^2 - 3x - 6$.

Esta combinación lineal genera un nuevo polinomio de grado 2 o menor que es una combinación ponderada de los polinomios originales.

3. En el espacio vectorial de matrices $2 \times 2$, considere las matrices

$$\mathbf{A} = \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix}$$ y $$\mathbf{B} = \begin{bmatrix} -1 & 2 \\ 3 & 0 \end{bmatrix}$$.

La combinación lineal $2\mathbf{A} - 3\mathbf{B}$ sería

$$2 \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} - 3\begin{bmatrix} -1 & 2 \\ 3 & 0 \end{bmatrix} = \begin{bmatrix} 2 & 0 \\ 0 & 2 \end{bmatrix} - \begin{bmatrix} -3 & 6 \\ 9 & 0 \end{bmatrix} = \begin{bmatrix} 5 & -6 \\ -9 & 2 \end{bmatrix}$$.

Esta combinación lineal genera una nueva matriz que es una combinación ponderada de las matrices originales.

Estos ejemplos ilustran cómo las combinaciones lineales permiten generar nuevos vectores o elementos en un espacio vectorial mediante la combinación de vectores o elementos existentes.

'''



r'''
# Conjuntos Generadores

En álgebra lineal, un conjunto generador es un conjunto de vectores que, mediante combinaciones lineales, pueden generar todos los vectores de un espacio vectorial. El estudio de los conjuntos generadores es fundamental para comprender la estructura y las propiedades de los espacios vectoriales. En este artículo, exploraremos en detalle los conjuntos generadores, su definición, propiedades y ejemplos ilustrativos.

## Definición de Conjunto Generador

Dado un espacio vectorial $V$, un conjunto $S$ de vectores en $V$ se llama conjunto generador si cada vector en $V$ puede ser expresado como una combinación lineal de los vectores en $S$. Formalmente, para todo vector $\mathbf{v}$ en $V$, existen escalares $a_1, a_2, \ldots, a_n$ y vectores $\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n$ en $S$ tal que:

$$\mathbf{v} = a_1\mathbf{v}_1 + a_2\mathbf{v}_2 + \ldots + a_n\mathbf{v}_n$$

En otras palabras, el conjunto $S$ genera el espacio vectorial $V$ si cada vector en $V$ puede ser expresado como una combinación lineal de los vectores en $S$.

## Propiedades de los Conjuntos Generadores

Los conjuntos generadores tienen varias propiedades importantes:

1. Un conjunto generador debe ser un conjunto no vacío, ya que debe contener al menos un vector para generar el espacio vectorial.
2. Un conjunto generador puede contener vectores redundantes, es decir, vectores que son combinaciones lineales de otros vectores en el conjunto. En este caso, podemos eliminar los vectores redundantes sin afectar la capacidad del conjunto para generar el espacio vectorial.
3. Si un conjunto generador contiene el vector cero, entonces cualquier vector en el espacio vectorial puede ser generado por este conjunto mediante la combinación lineal que incluye al vector cero.

## Ejemplos de Conjuntos Generadores

1. En el espacio vectorial $\mathbb{R}^2$, el conjunto de vectores $\{(1, 0), (0, 1)\}$ es un conjunto generador, ya que cualquier vector en $\mathbb{R}^2$ puede ser expresado como una combinación lineal de estos dos vectores.
2. En el espacio vectorial de polinomios de grado 2 o menor, el conjunto $\{1, x, x^2\}$ es un conjunto generador, ya que cualquier polinomio de grado 2 o menor puede ser expresado como una combinación lineal de estos tres polinomios.
3. En el espacio vectorial de matrices $2 \times 2$, el conjunto de matrices

$$\left\{ \begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix} \right\}$$

es un conjunto generador, ya que cualquier matriz $2 \times 2$ puede ser expresada como una combinación lineal de estas cuatro matrices.

Estos ejemplos muestran cómo los conjuntos generadores pueden variar dependiendo del espacio vectorial considerado y cómo pueden utilizarse para generar todos los vectores dentro del espacio vectorial.

'''


r'''
# Dependencia e Independencia Lineal

En álgebra lineal, los conceptos de dependencia e independencia lineal son fundamentales para comprender las relaciones entre vectores en un espacio vectorial. Estos conceptos permiten determinar si un conjunto de vectores puede generar todo el espacio vectorial de manera única o si existen relaciones lineales entre ellos. En este artículo, exploraremos en detalle la dependencia e independencia lineal, así como sus propiedades y aplicaciones.

## Dependencia Lineal

Un conjunto de vectores $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ se dice que es linealmente dependiente si existe al menos una combinación lineal no trivial de los vectores que da como resultado el vector cero. Formalmente, se dice que el conjunto es linealmente dependiente si existen escalares $c_1, c_2, \ldots, c_n$, no todos iguales a cero, tales que $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \ldots + c_n\mathbf{v}_n = \mathbf{0}$.

Esto implica que al menos uno de los vectores del conjunto puede expresarse como una combinación lineal de los demás. En otras palabras, un vector puede escribirse como una suma ponderada de los demás vectores.

## Independencia Lineal

Un conjunto de vectores $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ se dice que es linealmente independiente si no existe ninguna combinación lineal no trivial de los vectores que dé como resultado el vector cero. Formalmente, se dice que el conjunto es linealmente independiente si la única combinación lineal que satisface $c_1\mathbf{v}_1 + c_2\mathbf{v}_2 + \ldots + c_n\mathbf{v}_n = \mathbf{0}$ es aquella en la que todos los escalares $c_1, c_2, \ldots, c_n$ son cero.

Esto implica que ningún vector del conjunto puede expresarse como una combinación lineal de los demás vectores. En otras palabras, los vectores son "independientes" entre sí en términos de combinaciones lineales.

## Propiedades de Dependencia e Independencia Lineal

Las propiedades clave de la dependencia e independencia lineal son las siguientes:

1. Si un conjunto de vectores contiene al menos un vector cero, entonces el conjunto es linealmente dependiente, ya que siempre se puede obtener la combinación lineal trivial ($c = 0$) que da como resultado el vector cero.
2. Si un conjunto de vectores contiene al menos dos vectores proporcionales, es decir, uno es múltiplo escalar del otro, entonces el conjunto es linealmente dependiente. Esto se debe a que se puede encontrar una combinación lineal no trivial que resulte en el vector cero (por ejemplo, tomando $c_1 = 1$ y $c_2 = -1$).
3. Un conjunto que contiene solo un vector no nulo es linealmente independiente.
4. Un conjunto que contiene dos vectores no proporcionales es linealmente independiente.
5. Un conjunto que contiene más vectores que la dimensión

 del espacio vectorial no puede ser linealmente independiente.

## Ejemplos de Dependencia e Independencia Lineal

1. Consideremos el conjunto de vectores $\{\mathbf{v}_1 = \begin{bmatrix} 1 \\ 2 \\ 3 \end{bmatrix}, \mathbf{v}_2 = \begin{bmatrix} 2 \\ 4 \\ 6 \end{bmatrix}, \mathbf{v}_3 = \begin{bmatrix} 1 \\ 1 \\ 1 \end{bmatrix}\}$. Observamos que $\mathbf{v}_2$ es el doble de $\mathbf{v}_1$ y que $\mathbf{v}_3$ es la suma de $\mathbf{v}_1$ y $\mathbf{v}_2$. Por lo tanto, este conjunto es linealmente dependiente, ya que podemos expresar $\mathbf{v}_3$ como una combinación lineal de los otros dos vectores: $\mathbf{v}_3 = \mathbf{v}_1 + \mathbf{v}_2$.

2. Consideremos ahora el conjunto de vectores $\{\mathbf{u}_1 = \begin{bmatrix} 1 \\ 0 \\ 0 \end{bmatrix}, \mathbf{u}_2 = \begin{bmatrix} 0 \\ 1 \\ 0 \end{bmatrix}, \mathbf{u}_3 = \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}\}$. Observamos que estos vectores son linealmente independientes, ya que no existe ninguna combinación lineal no trivial de ellos que dé como resultado el vector cero. Cualquier combinación lineal de estos vectores produce un vector no nulo.


'''




r'''
# Bases y Dimensión

En álgebra lineal, las bases y la dimensión son conceptos fundamentales para comprender la estructura y propiedades de los espacios vectoriales. Una base es un conjunto de vectores que generan todos los demás vectores del espacio de manera única, mientras que la dimensión es el número de vectores en una base. En este artículo, exploraremos en detalle las bases, la dimensión y su relación con los espacios vectoriales.

## Bases

Una base de un espacio vectorial es un conjunto de vectores que cumple dos condiciones:

1. Generación: Los vectores de la base pueden generar todos los vectores del espacio vectorial mediante combinaciones lineales. Es decir, cualquier vector del espacio puede expresarse de manera única como una combinación lineal de los vectores de la base.
2. Independencia lineal: Los vectores de la base son linealmente independientes, lo que significa que no existe ninguna combinación lineal no trivial de los vectores de la base que sea igual al vector cero.

Formalmente, sea $\{\mathbf{v}_1, \mathbf{v}_2, \ldots, \mathbf{v}_n\}$ un conjunto de vectores en un espacio vectorial. Este conjunto es una base si y solo si cumple las dos condiciones mencionadas anteriormente.

## Dimensión

La dimensión de un espacio vectorial se define como el número de vectores en una base del espacio. Si un espacio vectorial tiene una base con $n$ vectores, entonces se dice que el espacio es de dimensión $n$, y se denota como $\text{dim}(V) = n$.

Es importante destacar que todos los vectores de un espacio vectorial de dimensión $n$ se pueden expresar de manera única como combinaciones lineales de una base de $n$ vectores.

## Propiedades de las Bases y Dimensión

Las bases y la dimensión tienen varias propiedades importantes:

1. Un espacio vectorial puede tener múltiples bases, pero todas las bases de un espacio tienen la misma cantidad de vectores, lo que define la dimensión del espacio.
2. Dos bases de un mismo espacio vectorial tienen la misma cantidad de vectores, y por lo tanto, el mismo número de elementos en su base. Esto implica que todos los espacios vectoriales del mismo tamaño tienen la misma dimensión.
3. Si un conjunto de vectores es linealmente independiente y contiene exactamente $\text{dim}(V)$ vectores, entonces ese conjunto es una base del espacio vectorial $V$.
4. Si un conjunto de vectores genera un espacio vectorial $V$ y contiene exactamente $\text{dim}(V)$ vectores, entonces ese conjunto es una base de $V$.

## Ejemplos de Bases y Dimensión

1. En el espacio vectorial $\mathbb{R}^3$, una base común es $\{\mathbf{i}=(1,0,0), \mathbf{j}=(0,1,0), \mathbf{k}=(0,0,1)\}$. Estos vectores generan $\mathbb{R}^3$ y forman una base porque son linealmente independientes. Por lo tanto, $\text{dim}(\mathbb{R}^3) = 3$.

2. En el espacio vectorial de polinomios de grado 2 o menor, una base común es $\{1, x, x^2\}$.
Estos polinomios generan el espacio de polinomios de grado 2 o menor y son linealmente independientes. Por lo tanto, $\text{dim}(\text{Espacio de polinomios de grado 2 o menor}) = 3$.

3. En el espacio vectorial de matrices $2 \times 2$, una base común es

$\left\{\begin{bmatrix} 1 & 0 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 1 \\ 0 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 1 & 0 \end{bmatrix}, \begin{bmatrix} 0 & 0 \\ 0 & 1 \end{bmatrix}\right\}$.

Estas matrices generan el espacio de matrices $2 \times 2$ y son linealmente independientes. Por lo tanto, $\text{dim}(\text{Espacio de matrices } 2 \times 2) = 4$.

'''
