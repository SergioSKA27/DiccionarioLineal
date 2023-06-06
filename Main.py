from st_pages import Page, show_pages, add_page_title

# Optional -- adds the title and icon to the current page
add_page_title()

# Specify what pages should be shown in the sidebar, and what their titles and icons
# should be
show_pages(
    [
        Page("Portada.py", "Portada", "🏠"),
        Page("Introduccion.py", "1. Introducción al Álgebra Lineal", ":books:"),
        Page("vectores_Rn.py", "2. Vectores en el Espacio", ":books:"),
        Page("SistemasEL.py", "3. Sistemas de Ecuaciones Lineales", ":books:"),
        Page("EspaciosVectoriales.py", "4. Espacios Vectoriales ", ":books:"),
        Page("Tlineales.py", "5. Transformaciones Lineales", ":books:"),
        Page("Diagonalizacion.py", "6. Diagonalización de Matrices", ":books:"),
        Page("EV_ortogonal.py", "7. Espacios Vectoriales Ortogonales", ":books:"),
        Page("Determinates.py", "8. Determinantes", ":books:"),
        Page("InnerP.py", "9. Espacios Vectoriales con Producto Interno", ":books:"),
        Page("eigenval.py", "10. Valores y Vectores Propios", ":books:"),



        Page("Campo.py", "Apéndice  Campos", ":notebook:"),


    ]
)
