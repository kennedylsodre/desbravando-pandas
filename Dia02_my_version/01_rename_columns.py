#%%
import pandas as pd
# %%
df = pd.read_csv('../data/pedido.csv')
# %%
df  
# %%
df.rename(columns={'descUF':'descEstado'},inplace=True)
# %%
df
# %%
lista_uf = ['São Paulo', 'Rio Grande do Sul','Sergipe']
# %%
filtro = df['descEstado'].isin(lista_uf)
# %%
filtro
# %%
df[filtro]['descEstado'].unique()
# %%
