#%%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('../data/produto.csv')
# %%
df
# %%
df['Preco_Corrigido'] = df['vlPreco'] * 1.09
# %%
df
# %%
df['Inflacao'] = (df['Preco_Corrigido'] / df['vlPreco']-1) *100
# %%
df
# %%
df['vlPreco_Log'] = np.log(df['vlPreco'])
# %%
df
# %%
def fatorial(x): 
    y=1
    for i in range(2,int(x)+1): 
        y *= i
    return y

fatorial(5)
# %%
df['vlPrecoFatorial'] = df['vlPreco'].apply(fatorial)
# %%
df
# %%
