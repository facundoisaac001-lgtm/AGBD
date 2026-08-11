import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- EJERCICIO 1: Carga de datos ---
df = pd.read_csv("/Vote Ai.csv")
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

# EJERCICIO 12: .query() 

print("\n--- EJERCICIO 12: FILTRO CON .query() ---")

limite_rondas = 2

resultado_query = df.query(
    'Constituency_Name == "Nagpur" and Round > @limite_rondas'
)

print("\nResultado utilizando .query():")
print(resultado_query)

print(f'\nFilas seleccionadas: {len(resultado_query)}')


# Para pensar y responder en la entrega:
#
# ¿Qué ventaja tiene .query() frente a los corchetes?
#
# .query() permite escribir las condiciones de una manera más
# sencilla y parecida a una consulta, especialmente cuando
# tenemos varias condiciones.
#
# ¿Qué pasa si olvidamos el @ delante de una variable?
#
# Si olvidamos el @, Pandas intenta interpretar el nombre de
# la variable como si fuera una columna del DataFrame y puede
# producir un error.
#
# ¿En qué casos preferirían usar query()?
#
# Preferiría usar query() cuando tengo filtros con varias
# condiciones porque el código puede resultar más fácil
# de leer.


# --- EJERCICIO 13: .isin() y ~ ---

print("\n--- EJERCICIO 13: .isin() y ~ ---")

categorias_elegidas = df['Constituency_Name'].dropna().unique()[:3]

df_incluidos = df[
    df['Constituency_Name'].isin(categorias_elegidas)
]

df_excluidos = df[
    ~df['Constituency_Name'].isin(categorias_elegidas)
]

print("\nCategorías elegidas:")
print(categorias_elegidas)

print(f'\nFilas incluidas: {len(df_incluidos)}')
print(df_incluidos.head())

print(f'\nFilas excluidas: {len(df_excluidos)}')
print(df_excluidos.head())

total = len(df)
suma = len(df_incluidos) + len(df_excluidos)

print(f'\nTotal original: {total}')
print(f'Incluidas + excluidas: {suma}')
print(f'¿Coinciden? {total == suma}')


# Para pensar y responder en la entrega:
#
# ¿Qué diferencia hay entre usar isin() y usar varias condiciones
# con |?
#
# isin() permite comprobar de manera más sencilla si una columna
# contiene alguno de los valores de una lista. Con muchas categorías
# resulta más ordenado que escribir muchas condiciones con |.
#
# ¿Cuándo usarían ~ para excluir categorías?
#
# Usaría ~ cuando quiero obtener todos los registros excepto
# aquellos que pertenecen a determinadas categorías.
#
# ¿Qué pasa si una categoría está repetida muchas veces?
#
# isin() selecciona todas las filas que tengan esa categoría,
# por lo que si está repetida muchas veces se incluyen todas
# sus apariciones.
#
# ¿Qué pasa si la lista está vacía?
#
# Si la lista está vacía, no se seleccionan categorías con isin()
# y el resultado sería un DataFrame sin esas filas.


# --- EJERCICIO 14: .value_counts(), .unique() y .nunique() ---

print("\nEJERCICIO 14: VALORES ÚNICOS Y CATEGORÍAS")

print("\n=== DATAFRAME COMPLETO ===")

print("\nCantidad de apariciones por distrito:")
print(df['Constituency_Name'].value_counts())

print("\nValores únicos:")
print(df['Constituency_Name'].unique())

print(
    "\nCantidad de categorías distintas:",
    df['Constituency_Name'].nunique()
)

print("\nPorcentajes:")
print(
    (df['Constituency_Name']
     .value_counts(normalize=True) * 100)
    .round(1)
)



df_filtrado = df[filtro_avanzado]

print("\n=== DATAFRAME FILTRADO ===")

print("\nCantidad de apariciones por distrito:")
print(df_filtrado['Constituency_Name'].value_counts())

print("\nValores únicos:")
print(df_filtrado['Constituency_Name'].unique())

print(
    "\nCantidad de categorías distintas:",
    df_filtrado['Constituency_Name'].nunique()
)

print("\nPorcentajes:")
print(
    (df_filtrado['Constituency_Name']
     .value_counts(normalize=True) * 100)
    .round(1)
)


# Para pensar y responder en la entrega:
#
# ¿Qué columna tiene más categorías distintas?
#
# En este análisis utilizamos Constituency_Name como columna
# de categoría. La cantidad de categorías distintas se obtiene
# automáticamente utilizando nunique().
#
# ¿Qué significa que una categoría tenga un porcentaje alto?
#
# Significa que esa categoría aparece muchas veces en relación
# con el total de registros analizados.
#
# ¿El porcentaje de categorías cambia entre el DataFrame completo
# y el filtrado?
#
# Sí, puede cambiar porque el filtro elimina algunas filas.
# Por lo tanto, los porcentajes se vuelven a calcular solamente
# utilizando los registros que quedaron después del filtro.
#
# ¿Por qué value_counts(normalize=True) es útil?
#
# Porque permite obtener directamente la proporción de cada
# categoría y facilita comparar su peso dentro del conjunto
# de datos.


# --- EJERCICIO 15: EXPORTAR CSV Y HEATMAP ---

print("\n EJERCICIO 15: EXPORTACIÓN Y HEATMAP ")

import numpy as np

df_filtrado = df[filtro_avanzado]

df_filtrado.to_csv(
    "resultado_filtrado.csv",
    index=False
)

print(
    f"\nArchivo exportado correctamente: "
    f"{len(df_filtrado)} filas guardadas."
)



correlacion = df.corr(numeric_only=True)

print("\nMatriz de correlación:")
print(correlacion.round(2))



plt.figure(figsize=(10, 8))

sns.heatmap(
    correlacion,
    annot=True,
    fmt='.2f',
    cmap='viridis',
    linewidths=0.5,
    vmin=-1,
    vmax=1
)

plt.title(
    'Correlación entre variables - Vote AI',
    fontweight='bold'
)

plt.tight_layout()

plt.savefig(
    "heatmap_vote_ai.png",
    dpi=300
)

plt.close()

print("\nHeatmap guardado como heatmap_vote_ai.png")



mask = np.triu(
    np.ones(correlacion.shape),
    k=0
).astype(bool)

correlacion_sin_diag = correlacion.where(~mask)

pares = correlacion_sin_diag.stack()

if len(pares) > 0:

    par_max = pares.idxmax()
    par_min = pares.idxmin()

    valor_max = pares.max()
    valor_min = pares.min()

    print(
        f'\nPar más correlacionado: '
        f'{par_max[0]} ↔ {par_max[1]} '
        f'({valor_max:.2f})'
    )

    print(
        f'Par menos correlacionado: '
        f'{par_min[0]} ↔ {par_min[1]} '
        f'({valor_min:.2f})'
    )

else:

    print(
        '\nNo hay suficientes columnas numéricas '
        'para calcular la correlación.'
    )


# Para pensar y responder en la entrega:
#
# ¿Qué significa una correlación cercana a 1?
#
# Significa que las dos variables tienen una relación positiva
# fuerte: cuando una aumenta, la otra tiende a aumentar también.
#
# ¿Y una cercana a -1?
#
# Significa que existe una relación negativa fuerte: cuando una
# variable aumenta, la otra tiende a disminuir.
#
# ¿Qué significa una correlación cercana a 0?
#
# Significa que no se observa una relación lineal fuerte entre
# las dos variables.
#
# ¿La correlación implica causalidad?
#
# No. Que dos variables estén correlacionadas no significa que
# una sea necesariamente la causa de la otra.
#
# ¿Qué par de columnas tiene la correlación más alta?
#
# El programa lo calcula automáticamente y lo muestra en la
# terminal como "Par más correlacionado".
#
# ¿Y cuál tiene la más baja?
#
# El programa también lo calcula automáticamente y lo muestra
# como "Par menos correlacionado".
#
# ¿Qué variable es la más correlacionada con Round?
#
# Esto se puede observar en la matriz de correlación que imprime
# el programa y en el heatmap generado.


#ultimo mensaje 
print("\n¡HECHO!")
print("Todos los ejercicios se ejecutaron correctamente.")
print("Se generaron:")
print("- reporte_barras.png")
print("- reporte_torta.png")
print("- grafico_lineas.png")