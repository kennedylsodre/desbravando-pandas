# %%
import pandas as pd


# %%
df = pd.read_csv('../data/pedido.csv')
# %%
df
# %%
df['descUF'].value_counts()
df.head

# %%
#Aprendizado com o Téo: Caso queira apenas uma coluna pode ser
#passado a string sem uma lista, caso seja mais de uma coluna precisa
#estar em uma lista

colunas = [ 
'idPedido', 
'descUF', 
'flKetchup',
'txtRecado', 
'dtPedido'
]
# %%
df[colunas]
# %%
df[df['idPedido']>6]
# %%
#Cria um dataframa com uma amoastra de 100 dados do dataframe antigo

df_sample = df.sample(100)
df_sample
# %%
#Diferença entre loc e iloc:
#iloc: traz a linha na posição do parametro
#loc: traz a linha no indice do parametro

df_sample.iloc[[0]]
# %%
df.loc[[0]]
# %%
df_sample.iloc[0:4]

# %%
teste =df_sample.iloc[0].to_dict()
# %%
teste
# %%
df.loc[0:9]

# %%
