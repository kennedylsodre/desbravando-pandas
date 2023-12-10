#%%
import pandas as pd
pd.set_option('display.max_rows',100)

df_produto = pd.read_csv('../data/produto.csv')
# %%
df_produto
# %%
df_produto['Categoria'] = df_produto['descItem'].apply(lambda x: x.split(' ')[0])
# %%
df_produto
# %%
#Removendo duplicatas

df_produto.drop_duplicates('Categoria',keep='last').reset_index(drop=True)
# %%
 