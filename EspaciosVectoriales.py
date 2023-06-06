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

'''
