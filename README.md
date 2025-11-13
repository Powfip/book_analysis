# 📚 Book Scraper & Analysis

Bienvenido a **Book Scraper & Analysis**, un proyecto en Python para **extraer información de libros** de [Books to Scrape](https://books.toscrape.com/) y **analizar precios, ratings y disponibilidad** con gráficos y estadísticas.  

---

## 🗂 Archivos del proyecto

| Archivo             | Descripción |
|--------------------|-------------|
| `scraper_book.py`   | Script que obtiene los datos de los libros y los guarda en `libros.csv`. |
| `analysis.py`       | Script que analiza los datos y genera gráficos de precios y ratings. |
| `libros.csv`        | CSV generado por `scraper_book.py` (opcional, solo para análisis). |

---

## ⚡ Requisitos

Python 3.10+ y las siguientes librerías:

```bash
pip install pandas matplotlib beautifulsoup4 requests
🏃‍♂️ Cómo usar el proyecto
1️⃣ Ejecutar el scraper
python scraper_book.py
Descarga información de 1000 libros (50 páginas).
Crea libros.csv con las columnas:
titulo → Título del libro
precio → Precio en libras (£)
rating → Valoración (One, Two, Three, Four, Five)
disponibilidad → Stock disponible
2️⃣ Ejecutar el análisis
python analysis.py
Convierte los datos:
Precio a número flotante
Rating de texto a número
Muestra estadísticas:
Número total de libros
Precio medio, mínimo y máximo
Conteo de libros por rating
Genera tres gráficos:
📊 Histograma de precios
📈 Precio medio por rating (barras)
🔹 Scatter plot: precio vs rating
📊 Ejemplos de gráficos
Histograma de precios	Precio medio por rating	Scatter precio vs rating

💡 Notas importantes
No es necesario subir libros.csv; otros pueden generar sus propios datos ejecutando scraper_book.py.
Asegúrate de usar la codificación correcta al leer CSV (utf-8 o latin-1).
Los gráficos se generan con matplotlib y se pueden personalizar fácilmente.
🚀 Posibles mejoras
Filtrar libros por disponibilidad (in stock).
Analizar más a fondo la relación entre precio y rating.
Crear dashboards interactivos con plotly o streamlit.
Guardar automáticamente gráficos como imágenes (.png).
🔗 Referencias
Books to Scrape
Beautiful Soup Documentation
Pandas Documentation
Matplotlib Documentation
📧 Contacto
Si tienes dudas o sugerencias sobre el proyecto, puedes escribirme a:
123filipi@gmail.com
