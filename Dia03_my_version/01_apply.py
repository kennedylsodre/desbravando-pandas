#%%
import pandas as pd
# %%
df = pd.read_csv('../data/produto.csv')
# %%
df
# %%
df['descItem'].unique()
# %%
def is_queijo(x): 
    return x.lower().startswith('queijo')


# %%
filtro = df['descItem'].apply(is_queijo)
df[filtro]

# %%
df['flMassa'] = df['descItem'].apply(lambda x: x.lower().startswith(('massa','queijo')))
# %%
df[df['flMassa']]
# %%
