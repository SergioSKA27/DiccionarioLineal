import streamlit as st
import plotly.graph_objects as graph
import numpy as np
import pandas as pd
import  matplotlib.pyplot as plt
import sympy as sp
import base64


import streamlit as st
import numpy as np
from numpy.linalg import eig, det


# Matrix Calculator
def matrix_calculator():
    st.title("Matrix Calculator")
    st.write("Perform various operations on matrices")

    # Matrix Input
    st.header("Matrix Input")
    rows = st.number_input("Enter the number of rows:", min_value=1, step=1)
    cols = st.number_input("Enter the number of columns:", min_value=1, step=1)

    matrix_elements = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = st.number_input(f"Element [{i+1}, {j+1}]:", key=f"element_{i}_{j}")
            row.append(element)
        matrix_elements.append(row)

    matrix = np.array(matrix_elements)

    # Matrix Operations
    st.header("Matrix Operations")

    # Matrix Addition
    if st.button("Matrix Addition"):
        st.subheader("Result (Matrix Addition):")
        matrix2_elements = []
        for i in range(rows):
            row = []
            for j in range(cols):
                element = st.number_input(f"Matrix 2 Element [{i+1}, {j+1}]:", key=f"matrix2_element_{i}_{j}")
                row.append(element)
            matrix2_elements.append(row)

        matrix2 = np.array(matrix2_elements)
        result = matrix + matrix2
        st.write(result)

    # Matrix Subtraction
    if st.button("Matrix Subtraction"):
        st.subheader("Result (Matrix Subtraction):")
        matrix2_elements = []
        for i in range(rows):
            row = []
            for j in range(cols):
                element = st.number_input(f"Matrix 2 Element [{i+1}, {j+1}]:", key=f"matrix2_element_{i}_{j}")
                row.append(element)
            matrix2_elements.append(row)

        matrix2 = np.array(matrix2_elements)
        result = matrix - matrix2
        st.write(result)

    # Matrix Multiplication
    if st.button("Matrix Multiplication"):
        st.subheader("Result (Matrix Multiplication):")
        cols2 = st.number_input("Enter the number of columns for Matrix 2:", min_value=1, step=1)
        matrix2_elements = []
        for i in range(cols):
            row = []
            for j in range(cols2):
                element = st.number_input(f"Matrix 2 Element [{i+1}, {j+1}]:", key=f"matrix2_element_{i}_{j}")
                row.append(element)
            matrix2_elements.append(row)

        matrix2 = np.array(matrix2_elements)
        result = np.matmul(matrix, matrix2)
        st.write(result)

    # Determinant
    st.header("Determinant")
    determinant = det(matrix)
    st.subheader("Result (Determinant):")
    st.write(determinant)

    # Eigenvalues and Eigenvectors
    st.header("Eigenvalues and Eigenvectors")
    eigenvalues, eigenvectors = eig(matrix)
    st.subheader("Eigenvalues:")
    st.write(eigenvalues)
    st.subheader("Eigenvectors:")
    st.write(eigenvectors)

    # Diagonalization
    st.header("Diagonalization")
    eigen_diag = np.diag(eigenvalues)
    diagonalized_matrix = np.matmul(np.matmul(eigenvectors, eigen_diag), np.linalg.inv(eigenvectors))
    st.subheader("Diagonalized Matrix:")
    st.write(diagonalized_matrix)

    # Characteristic Polynomial
    st.header("Characteristic Polynomial")
    characteristic_poly = np.poly(matrix)
    st.subheader("Characteristic Polynomial Coefficients:")
    st.write(characteristic_poly)


# Run the calculator
matrix_calculator()
