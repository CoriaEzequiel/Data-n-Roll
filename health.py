import pandas as pd

df = pd.read_csv("rockplayers.csv") 


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