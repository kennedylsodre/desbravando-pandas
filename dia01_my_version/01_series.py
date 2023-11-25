# %%
import pandas as pd
# %%
idade = [31,33,2,29,60,58,31,45,24]
# %%
idade
# %%
type(idade)
# %%
media = sum(idade)/len(idade)
media
# %%
s_idade = pd.Series(idade)
# %%
s_idade
# %%
s_idade[0]
# %%
media = s_idade.mean()
# %%
variancia = s_idade.var()
variancia
# %%
des_pad = s_idade.std()
des_pad
# %%
s_idade.describe()
# %%

###Filtrando dados em séries

###Como seria na lista para pegar dados maior que 30

#%%
nova_idade = [x for x in idade if x >=30]
# %%
nova_idade
# %%
s_idade[s_idade >= 30 ]
# %%
s_idade
# %%
filtro = s_idade >=30
s_idade[~filtro]

# %%
