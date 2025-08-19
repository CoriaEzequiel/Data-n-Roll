import pandas as pd

df = pd.read_csv("rockplayers.csv") 

#renombro columna

df= df.rename(columns={"velocidad_promedio_bpm": "bpm"})

print(df.columns)

#selecciono por columnas
cols = ['técnica_fav','repertorio_tecnicas','bpm','intensidad_escenario','popularidad']
print("\n Columnas técnicas y popularidad")
print(df[cols].head(4))

rockstars_por_nacionalidad =['nombre','apellido','banda', 'pais']
print(df[rockstars_por_nacionalidad])

albumfamoso= ['banda','album_famoso','estilo'] #
print("extraordinario los muchachos\n", df[albumfamoso].head(6))


#selecciono por etiqueta
print("\n Esnseño al artista en la posición índice+1")
print(df.loc[2])

print("\n Enseño solo algunos atributos del artísta en la posición índice+1")
print(df.loc[2,['apellido','técnica_fav']])

print("\nEnseño un rango específico de artistas:")
print(df.loc[2:6])

print("\n Enseño un rango específico y reducido de artistas:")
print(df.loc[2:6,['nombre','apellido', 'banda']])

#Filtro por condiciones
#Guitarristas más populares
print("\n Listado de guitarristas que aún siguen vivos:")
print(df[df['vivo']== True].head(4))

print("\n Guitarristas más populares:")
print(df[df['popularidad'] >8].head(4) )

most_popular = ['nombre','apellido','banda','estilo','popularidad']
df_most_popular_filtered = df[df['popularidad']>8]
print("\nGuitarristas más populares:")
print(df_most_popular_filtered[most_popular].head(4))   

most_fast_rockstars = ['nombre','apellido','bpm','banda']
df_most_fast = df[df['bpm'] > 150]
print("Los artistas más veloces:\n")
print(df_most_fast[most_fast_rockstars])