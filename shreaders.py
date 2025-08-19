import pandas as pd

df = pd.read_csv("rockplayers.csv") 
df= df.rename(columns={"velocidad_promedio_bpm": "bpm"})

Artists = df[['nombre','apellido','bpm','pais','repertorio_tecnicas','técnica_fav','estilo','guitar']]

# Más virtuosos
Artists['num_tecnics'] = Artists['repertorio_tecnicas'].str.split(',').apply(len)

mas_virtuosos = Artists.sort_values(by='num_tecnics', ascending=False)
print("Artistas más virtuosos (por cantidad de técnicas en su repertorio):")
print(mas_virtuosos[['nombre','apellido','num_tecnics','repertorio_tecnicas','bpm','estilo']].head(10))

#top 10 guitarristas más veloces
df_fast = Artists.sort_values(by='bpm', ascending=False)
print("Top 10 guitarristas más rápidos:")
print(df_fast.head(10))

#virtuosos por estilo:
Artists['estilos'] = Artists['estilo'].str.split(',').apply(len)

columns_virtuosos = ['estilo','num_tecnics','guitar','nombre','apellido']
virtuosos_por_estilo = Artists.sort_values(by='num_tecnics', ascending=False).groupby('estilo').head()
print("\nTop virtuosos por estilo:")
print(virtuosos_por_estilo[columns_virtuosos])