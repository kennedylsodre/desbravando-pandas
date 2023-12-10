#%% 
import pandas as pd
import datetime
# %%
df = pd.read_csv('../data/produto.csv')
# %%
df
# %%
df.sort_values('vlPreco',ascending=False)
# %%
pd.DataFrame() 

#%%
datas = []
data_inicio = datetime.datetime.strptime('2022-12-31' , "%Y-%m-%d")
for x in range(0,365): 
   
    data = data_inicio + datetime.timedelta(days=1)
    datas.append(data)
    data_inicio =data
    

# %%
df_datas = pd.DataFrame(datas)

# %%
df_datas.rename(columns={0:'Datas'},inplace=True)
# %%
df_datas.dtypes
# %%
df['key'] = 0
df_datas['key'] = 0
df_produto_data = df.merge(df_datas,left_on='key',right_on='key',how='inner')
# %%
df_produto_data.drop(columns='key',inplace=True)
# %%
df_produto_data

#%%
pd.set_option('display.max_rows',)

# %%

df_produto_data.sort_values(by=["vlPreco",'Datas'],ascending=[False,True])
df_produto_data
# %%
