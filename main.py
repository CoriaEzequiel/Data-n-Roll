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

#Guitarristas rehabilitados
rockstars_rehabilitated = ['nombre','apellido','edad','mensaje_lyrics','emocion_musica','pais','rehabilitado','vivo']
df_rockstars_rehab = df[df['rehabilitado']==True]
print("Guitarristas rehabilitados:\n")
print(df_rockstars_rehab[rockstars_rehabilitated])

#Rehabilitados y que aún viven
df_rockstars_rehab_and_alive =df[(df['rehabilitado']== True) &(df['vivo']== True) ]
print("Guitarristas rehabilitados y que aún viven:")
print(df_rockstars_rehab_and_alive[rockstars_rehabilitated])

#Guitarristas NO rehabilitados
df_rockstars_notrehab = df[df['rehabilitado']==False]
print("Guitarristas NO rehabilitados:\n")
print(df_rockstars_notrehab[rockstars_rehabilitated])


#NO Rehabilitados y fallecidos
df_rockstars_notrehab_and_notalive =df[(df['rehabilitado']== False) &(df['vivo']== False) ]
print("Guitarristas NO rehabilitados y fallecidos:")
print(df_rockstars_notrehab_and_notalive[rockstars_rehabilitated])

#Rehabilitados y fallecidos
df_rockstars_notrehab_and_notalive = df[(df['rehabilitado']==True) & (df['vivo']== False)]
print("Guitarristas rehabilitados y fallecidos:")
print(df_rockstars_notrehab_and_notalive[rockstars_rehabilitated])

#Fallecidos a temprana edad
rockstars_ripyoung=['nombre','apellido','edad','banda','rehabilitado','popularidad','intensidad_escenario','mensaje_lyrics','mediatico']
df_ripyoung = df[(df['edad'] < 40) & (df['vivo'] == False)]
print("Rip Young list:\n")
print(df_ripyoung[rockstars_ripyoung])