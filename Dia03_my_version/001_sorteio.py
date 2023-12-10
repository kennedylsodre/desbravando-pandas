#%%
import random 
import pandas as pd
# %%
def sorteia_partidas(jogadores):
    mandantes = []
    visitantes = []
    partidas= ['Partida ' + str(x+1) for x in range(0,int(len(jogadores)/2))]
    for x in range(0,len(jogadores)):
        jogador_escolhido = random.choice(jogadores)
        partida = 'Partida ' + str(x)
        if x % 2: 
            visitantes.append(jogador_escolhido)
        else: 
            mandantes.append(jogador_escolhido)
        jogadores.remove(jogador_escolhido)
        
    dados_partidas = {'Partidas': partidas,'Mandantes':mandantes,'Visitantes':visitantes}
    return pd.DataFrame(dados_partidas,columns=dados_partidas.keys())

# %%
sorteia_partidas(['Igor','Kennedy','Caique','Diogo'])
# %%
# %%
