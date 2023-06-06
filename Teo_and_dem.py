import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64




r'''
1.
Sean U y W subespacios del $\mathbb{K}$-espacio Vectorial V, tal que $U \oplus W = V$.
Definiendo
$$\rho : U \bigoplus W \longrightarrow V $$
$$u \oplus w \longrightarrow u + w $$

Probar:


1. $\rho$ es lineal.

2. $\rho$ es inyectiva (Use $A \bigoplus B$ si y solo si $A \cap B = \lbrace \emptyset \rbrace$)

3. $\rho$ es suprayectiva (¿[$A \cup B$] = $A \bigoplus B$?)



## Definición

Si $U$ y $W$ son subespacios vectoriales de $V$ con $U \bigoplus W = V$, decimos que $V$ es suma interna
directa de $U$ y $W$.



## Definición

Si $U,V$ y $W$ son $\mathbb{K}$-espacios vectoriales y $\rho : U \rightarrow V$, $\gamma: V \rightarrow W$ son
tranformaciones lineales entonces denominamos como sucesión o cadena a:
$$U \longrightarrow^{\rho} V \longleftrightarrow^{\gamma} W$$



## Definición

Una sucesión
$$U \longrightarrow^{\alpha} V \longleftrightarrow^{\gamma} W$$
es exacta en $V$ si $im(\alpha) = Ker(\gamma)$.


\textbf{Pregunta}\\
Si $T: U \rightarrow V$ es una tranformación lineal, ¿es exacta en $V$\\
$\lbrace \emptyset \rbrace \longrightarrow^{Id} U \longleftrightarrow^{T} V$?



## Definición

Si $\lbrace \emptyset \rbrace \rightarrow U \rightarrow^{\alpha} V \rightarrow^{\gamma} W \rightarrow \lbrace \emptyset \rbrace$
es una sucesión exacta (en $U,V$ y en $W$), diremos que se separa si existe  $\beta : W \rightarrow V$ lineal (llamada separante)
tal que $\gamma \circ \beta \equiv  Id_W$.




## Teorema

Si $U,V$ y $W$ son espacios vectoriales de dimensión finita y
$$\lbrace O \rbrace \rightarrow U \rightarrow_{\alpha} V \rightarrow_{\gamma} W \rightarrow \lbrace O \rbrace$$
es exacta y $\beta : W \rightarrow V$ descomposición, entonces
$$V \cong \alpha (U) \oplus \beta (W)$$




## Teorema

Si $\dim(U),\dim(V)$, $\dim(W) \in \mathbb{N} \cup\lbrace 0 \rbrace$, entonces si
$$\lbrace O \rbrace \rightarrow U \rightarrow_{\alpha} V \rightarrow_{\gamma} W \rightarrow \lbrace O \rbrace$$
es exacta, entonces también se descompone.



## Teorema

Si $W$ es subespacio vectorial de $V$  entonces $V/W$  es un espacio vectorial con
$$+ : V/W \times  V/W \longrightarrow V/W$$
$$([u],[v]) \mapsto [u]+[v] = [u+v]$$
y $\forall k \in \mathbb{K}, k[u] = [kv]$.


## Teorema

Si $\varphi : U \longrightarrow V$ es lineal entonces $U/\ker \varphi \cong  \varphi(U)$.




## Teorema

Si $U,W$ son subespacios vectoriales de $V$ entonces $(U+V)/W \cong U/(U \cap W)$.




## Teorema

Si $V$ es un espacio vectorial de $\dim V < \infty$ y $U$ es subespacio vectorial de $V$, entonces existe $W$
subespacio vectorial de $V$ tal que




## Teorema
Si $V$ es un espacio vectorial de $\dim V < \infty$ y $U$ es subespacio vectorial de $V$, entonces existe $W$
subespacio vectorial de $V$ tal que

'''

