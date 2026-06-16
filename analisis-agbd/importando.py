import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('Vote Ai.csv')

print('OKEY! Archivo cargado correctamente')

# Cantidad de filas y columnas
filas, columnas = df.shape
print(f"La tabla contiene {filas} filas y {columnas} columnas")

print('---Analisis Avanzado de datos---')

# Filtro por coincidencia exacta
filtro_exacto = df['Constituency_Name'] == 'Nagpur'
df_exacto = df[filtro_exacto]

print('\n---Filtro Exacto---')
print(df_exacto.head())

# Filtro por texto parcial
filtro_avanzado = df['Constituency_Name'].str.startswith('N', na=False)
df_filtrado = df[filtro_avanzado]

# Selección de columnas clave
columnas_clave = df_filtrado[['Constituency_Name', 'Round']]

print('\n---Columnas Clave---')
print(columnas_clave.head())

# Suma de rondas
sumo_Rondas = df_filtrado['Round'].sum()

print('\n--Reporte de rondas--')
print(f"Rondas total analizadas: {sumo_Rondas}")

# Agrupación y resumen
agrupado = (
    df.groupby('Constituency_Name')['Round']
    .sum()
    .sort_values(ascending=False)
)

print('\n---Agrupacion y Resumen---')
print(agrupado)

# Condicional con operador morsa
if (total_rondas := sumo_Rondas) > 20:
    print("¡Alerta! Prioridad Alta")
else:
    print("Estado Normal")

# Grafico de barras
print("\n[Generando GRAFICO de barras]")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

sns.barplot(
    data=df,
    x="Constituency_Name",
    y="Round",
    estimator=sum,
    errorbar=None,
    palette="viridis"
)

plt.title("Comparativa de rondas por distrito")
plt.xticks(rotation=20)

plt.tight_layout()

plt.savefig("reporte_barras.png", dpi=300)

plt.close()

# Grafico de torta
top_datos = agrupado.nlargest(5)

plt.figure(figsize=(8, 8))

plt.pie(
    top_datos,
    labels=top_datos.index,
    autopct='%1.1f%%',
    wedgeprops={
        'edgecolor': 'white',
        'linewidth': 2
    }
)

plt.title("Top 5 distritos por rondas")

plt.savefig("reporte_torta.png", dpi=300)

plt.close()

print("\n¡Hecho! Los graficos se guardaron correctamente en tu carpeta.")