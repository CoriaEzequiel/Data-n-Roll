import pandas as pd

df=pd.read_csv("rockplayers.csv")
#print(df)
#print(df.head(3))
#print(df.shape) #36x21

orderby_df = df.sort_values('mediatico')
#print(orderby_df)

filter_df = df[df['controversial']< 5]
print(filter_df)

filter_df = df[df['mediatico'] >8].sort_values(by='mediatico', ascending=False)

print("Los muchachos mas mediáticos\n", filter_df)