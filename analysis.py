import os
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------
# 1️⃣ Ruta segura del CSV
# -------------------------
current_dir = os.path.dirname(__file__)  # Carpeta del script
file_path = os.path.join(current_dir, "libros.csv")  # CSV en la misma carpeta

# Leer CSV con codificación UTF-8
try:
    df = pd.read_csv(file_path, encoding="utf-8")
except UnicodeDecodeError:
    df = pd.read_csv(file_path, encoding="latin-1")

# -------------------------
# 2️⃣ Limpieza de datos
# -------------------------
# Normalizar nombres de columna a minúsculas
df.columns = df.columns.str.lower()

# Limpiar columna 'precio' y convertir a float
df["precio"] = df["precio"].str.replace(r"[^0-9.]", "", regex=True).astype(float)

# Convertir rating de texto a número
rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
df["rating"] = df["rating"].map(rating_map)

# -------------------------
# 3️⃣ Estadísticas básicas
# -------------------------
print("Número total de libros:", len(df))
print("Precio medio:", df["precio"].mean())
print("Precio mínimo:", df["precio"].min())
print("Precio máximo:", df["precio"].max())
print("Libros por rating:\n", df["rating"].value_counts())

# -------------------------
# 4️⃣ Visualización
# -------------------------
# Histograma de precios
plt.figure(figsize=(8,5))
df["precio"].hist(bins=20, color="skyblue")
plt.title("Distribución de precios de libros")
plt.xlabel("Precio (£)")
plt.ylabel("Número de libros")
plt.show()

# Precio medio por rating
plt.figure(figsize=(6,4))
df.groupby("rating")["precio"].mean().plot(kind="bar", color="orange")
plt.title("Precio medio por rating")
plt.xlabel("Rating (estrellas)")
plt.ylabel("Precio medio (£)")
plt.show()

# Scatter: Precio vs Rating
plt.figure(figsize=(6,4))
plt.scatter(df["rating"], df["precio"], alpha=0.5, color="green")
plt.title("Precio vs Rating")
plt.xlabel("Rating (estrellas)")
plt.ylabel("Precio (£)")
plt.show()
