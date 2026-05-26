import pandas as pd

df=pd.read_csv('Vote Ai.csv')
print ('OKEY! Archivo cargado correctamente')

#print(df.head())

#resultado = df['Election_ID'].count()
#resultado = df['Round'].sum()


#print(resultado)

print('---Analizis Avanzado de datos---')

filtro_avanzado = df['Constituency_Name'].str.startswith('Nagpur', na = False)
df_filtrado = df[filtro_avanzado]

sumo_Rondas = df_filtrado ['Round'].sum()

print('--reporte de rondas--')
print(f"rondas total analizadas:Rondas {sumo_Rondas} rondas.\n")

filtro_numero = df['Round'] > 8
