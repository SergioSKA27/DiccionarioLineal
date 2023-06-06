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

        Page("Campo.py", "Campos", ":books:"),
        Page("EspaciosVectoriales.py", "Espacios Vectoriales ", ":books:"),


    ]
)
