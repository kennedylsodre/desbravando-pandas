#%%
import pandas as pd

df = pd.read_csv("../data/produto.csv")
# %%
df['VlPrecoInflacao'] = (df['vlPreco']*1.09).round(2)
# %%
df
# %%
df['Categoria'] = df['descItem'].apply(lambda x: x.lower().split(' ')[0])
# %%
df
# %%
df[['descItem','Categoria']].describe()
# %%
df[['vlPreco','VlPrecoInflacao']].describe().T
# %%
df['Categoria'].value_counts()
# %%
#Agrupando dados com group by

df.groupby("descItem")['vlPreco','VlPrecoInflacao'].describe()
# %%

import random 

def fodase(x):
    return random.choice(x.values)
df.groupby("descItem")[['vlPreco','VlPrecoInflacao']].agg(['min','mean','max',fodase])
# %%
