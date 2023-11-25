# %%

import pandas as pd
# %%
df = pd.read_csv('../data/pedido.csv')
# %%
df
# %%
df.info(memory_usage='deep')
# %%
df.dtypes
# %%
 