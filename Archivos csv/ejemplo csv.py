import pandas as pd

df = pd.read_csv("datos.csv")

print(df.head(3)) # Muestra las primeras n filas

print(df.tail(3)) # Muestra las últimas n filas

print(df.columns) # Muestra el nombre de las columnas

print(df["Enero"]) # Revisamos contenido de la columna

print(df["Enero"].max()) # Máximo

print(df["Enero"].min()) # Mínimo

print(df["Enero"].mean()) # Media o promedio

print(df["Enero"].median()) # Mediana

print(df["Enero"].std()) # Desviación estándar

print(df["Tipo de delito"].mode()) # Moda