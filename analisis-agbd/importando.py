import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- EJERCICIO 1: Carga de datos ---
df = pd.read_csv("Vote Ai.csv")
print("OKEY! Archivo cargado correctamente")


# --- EJERCICIO 2: Dimensiones de la tabla ---
filas, columnas = df.shape
print(f"La tabla contiene {filas} filas y {columnas} columnas")
print('--- Analisis Avanzado de datos ---')


# --- EJERCICIO 3: Filtro exacto ---
filtro_exacto = df['Constituency_Name'] == 'Nagpur'
df_exacto = df[filtro_exacto]

print('\n--- Filtro Exacto ---')
print(df_exacto.head())


# --- EJERCICIO 4: Filtro parcial por texto ---
filtro_avanzado = df['Constituency_Name'].str.startswith('N', na=False)
df_filtrado = df[filtro_avanzado]


# --- EJERCICIO 5: Selección de columnas clave ---
columnas_clave = df_filtrado[['Constituency_Name', 'Round']]

print('\n--- Columnas Clave ---')
print(columnas_clave.head())


# --- EJERCICIO 6: Agrupación y resumen ---
agrupado = (
    df.groupby('Constituency_Name')['Round']
    .sum()
    .sort_values(ascending=False)
)

print('\n--- Agrupacion y Resumen ---')
print(agrupado)


# --- EJERCICIO 7: Estructura de control con operador morsa ---
if (total_rondas := df_filtrado['Round'].sum()) > 20:
    print("¡Alerta! Prioridad Alta")
else:
    print("Estado Normal")


# --- EJERCICIO 8: Gráfico de barras ---
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


# --- EJERCICIO 9: Gráfico de torta ---
top_datos = agrupado.nlargest(5)

plt.figure(figsize=(8, 8))
plt.pie(
    top_datos,
    labels=top_datos.index,
    autopct='%1.1f%%',
    wedgeprops={'edgecolor': 'white', 'linewidth': 2}
)

plt.title("Top 5 distritos por rondas")
plt.savefig("reporte_torta.png", dpi=300)
plt.close()

 

# --- EJERCICIO 9: Filtro doble con .loc[] ---
print("\n--- EJERCICIO 9: FILTRO DOBLE CON .loc[] ---")

condicion_extra = df['Round'] > 2
resultado = df.loc[
    filtro_avanzado & condicion_extra,
    ['Constituency_Name', 'Round', 'Party']
]

print(resultado)
print(f'\nFilas seleccionadas: {len(resultado)}')

#¿Cuántas filas quedaron después de aplicar el doble filtro?
#¿El resultado con .loc[] es igual al que hubieran obtenido en dos pasos separados?
#¿Qué pasa si cambian & por | en el filtro? ¿Tiene sentido para sus datos?

#Después de aplicar la doble condición quedaron X filas. 
#El resultado obtenido con .loc[] es equivalente al que se 
#conseguiría filtrando primero las filas y 
#luego seleccionando las columnas. Si se cambia & por 
#|, se obtienen más filas porque alcanza 
#con que se cumpla una de las dos condiciones.
 



# --- EJERCICIO 10: Manejo de nulos ---
print("\n--- EJERCICIO 10: VALORES NULOS ---")

print("\nNulos por columna:")
print(df.isnull().sum())

df_con_nulos = df.copy()
df_con_nulos.loc[[0, 3, 7], 'Round'] = None

print("\nNulos después de modificar:")
print(df_con_nulos.isnull().sum())

df_sin_nulos = df_con_nulos.dropna()

media = df_con_nulos['Round'].mean()
df_rellenado = df_con_nulos.fillna({'Round': round(media, 2)})

print(f'\nOriginal: {len(df_con_nulos)} filas')
print(f'Con dropna: {len(df_sin_nulos)} filas (se eliminaron filas)')
print(f'Con fillna: {len(df_rellenado)} filas (se rellenaron los huecos)')

#¿Cuál de las dos estrategias (dropna o fillna) es más conveniente para sus datos? ¿Por qué?
#¿Qué problema puede generar fillna con la media si los nulos son muchos?
#¿Cambiaría algo en sus análisis anteriores si hubiera nulos reales en sus datos?


#En este caso, fillna() resulta conveniente porque permite conservar la cantidad original de filas. 
#Sin embargo, si existen muchos valores nulos, reemplazarlos por la media 
#puede modificar los resultados y hacer que los datos 
#sean menos representativos.


# --- EJERCICIO 11: Gráfico de líneas con anotación ---
print("\n--- EJERCICIO 11: GRÁFICO DE LÍNEAS ---")

agrupado_lineas = (
    df.groupby('Constituency_Name')['Round']
    .sum()
    .sort_values()
)

fig, ax = plt.subplots(figsize=(12, 6))

ax.plot(
    agrupado_lineas.index,
    agrupado_lineas.values,
    marker='o',
    linewidth=2,
    markersize=6
)

idx_max = agrupado_lineas.idxmax()
val_max = agrupado_lineas.max()

ax.annotate(
    f'Máximo: {val_max:,.0f}',
    xy=(idx_max, val_max),
    xytext=(idx_max, val_max * 0.85),
    arrowprops=dict(arrowstyle='->', color='red'),
    fontsize=11,
    color='red',
    fontweight='bold'
)

ax.set_title('Evolución de rondas por distrito', fontsize=14, fontweight='bold')
ax.set_xlabel('Distrito')
ax.set_ylabel('Total de rondas')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

plt.savefig("grafico_lineas.png", dpi=300)
plt.close()

#¿La línea que generaron tiene un patrón claro (sube, baja, tiene picos)? ¿A qué lo atribuyen?
#¿Tiene sentido usar un gráfico de líneas para sus datos o hubiera sido mejor otro tipo?
#¿Qué pasa si usan agrupado.sort_index() en vez de sort_values()? ¿Cuál conviene?

#El gráfico presenta variaciones y picos según la cantidad total de rondas de cada distrito. Para estos datos,
#un gráfico de barras puede ser más adecuado porque las categorías no representan necesariamente una evolución temporal.
#sort_index() ordena alfabéticamente las categorías, mientras que sort_values() 
#las ordena según sus valores.




# --- MENSAJE FINAL ---
print("\n¡HECHO!")
print("Todos los ejercicios se ejecutaron correctamente.")
print("Se generaron:")
print("- reporte_barras.png")
print("- reporte_torta.png")
print("- grafico_lineas.png")