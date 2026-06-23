# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns

# df = pd.read_csv('Vote Ai.csv')

# print('OKEY! Archivo cargado correctamente')


# filas, columnas = df.shape
# print(f"La tabla contiene {filas} filas y {columnas} columnas")

# print('---Analisis Avanzado de datos---')

# filtro_exacto = df['Constituency_Name'] == 'Nagpur'
# df_exacto = df[filtro_exacto]

# print('\n---Filtro Exacto---')
# print(df_exacto.head())

# df_recordato = df.nlargest(100,"Round" )
# filtro_avanzado = df['Constituency_Name'].str.startswith('N', na=False)
# df_filtrado = df[filtro_avanzado]

# columnas_clave = df_filtrado[['Constituency_Name', 'Round']]

# print('\n---Columnas Clave---')
# print(columnas_clave.head())

# sumo_Rondas = df_filtrado['Round'].sum()

# print('\n--Reporte de rondas--')
# print(f"Rondas total analizadas: {sumo_Rondas}")

# agrupado = (
#     df.groupby('Constituency_Name')['Round']
#     .sum()
#     .sort_values(ascending=False)
# )

# print('\n---Agrupacion y Resumen---')
# print(agrupado)

# if (total_rondas := sumo_Rondas) > 20:
#     print("¡Alerta! Prioridad Alta")
# else:
#     print("Estado Normal")

# print("\n[Generando GRAFICO de barras]")

# sns.set_theme(style="whitegrid")

# plt.figure(figsize=(10, 6))

# sns.barplot(
#     data=df,
#     x="Constituency_Name",
#     y="Round",
#     estimator=sum,
#     errorbar=None,
#     palette="viridis"
# )

# plt.title("Comparativa de rondas por distrito")
# plt.xticks(rotation=20)

# plt.tight_layout()

# plt.savefig("reporte_barras.png", dpi=300)

# plt.close()

# top_datos = agrupado.nlargest(5)

# plt.figure(figsize=(8, 8))

# plt.pie(
#     top_datos,
#     labels=top_datos.index,
#     autopct='%1.1f%%',
#     wedgeprops={
#         'edgecolor': 'white',
#         'linewidth': 2
#     }
# )

# plt.title("Top 5 distritos por rondas")

# plt.savefig("reporte_torta.png", dpi=300)

# plt.close()

# print("\n¡Hecho! Los graficos se guardaron correctamente en tu carpeta.")

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Cargamos el archivo
df = pd.read_csv("Vote Ai.csv")

# 2. Agrupamos por Partido Político y SUMAMOS sus votos totales
votos_por_partido = df.groupby('Party')['Total_Votes'].sum().reset_index()

# 3. Configuramos el gráfico de barras vertical
plt.figure(figsize=(10, 5))
sns.set_theme(style="whitegrid")

sns.barplot(
    data=votos_por_partido,
    x='Party',
    y='Total_Votes',
    palette="Set2"
)

# Rotamos las siglas de los partidos si llegaran a ser muchas o largas
plt.xticks(rotation=45)

plt.title("Volumen Total de Votos obtenidos por Partido Político", fontsize=14, fontweight="bold")
plt.xlabel("Partido Político", fontsize=11)
plt.ylabel("Votos Totales", fontsize=11)
plt.tight_layout()

# 4. Guardamos
plt.savefig("votos_por_partido.png", dpi=300)
plt.close()

print("¡Hecho! 'votos_por_partido.png' generado con éxito.")