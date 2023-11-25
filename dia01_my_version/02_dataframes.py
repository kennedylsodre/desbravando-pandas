# %%
import pandas as pd
# %%
data = {
    'nome' : ['Téo', 'Nah','Maria','José','Marina','Jessica','InfoSlack'],
    'idade':[30,33,2,45,65,43,40],
    'cor': ['Preto','Verde','Azul', 'Vermelho','Amarelo','Verde', 'Azul'],
    'renda':[3566,1345,0,6576,4325,5326,10244]
}
# %%
df = pd.DataFrame(data)
# %%
df
# %%
df.mean()
# %%
df.describe().T
# %%
renda = [3566,1345,0,6576,4325,5326,10244]
renda = sorted(renda)
renda
# %%
