import pandas as pd
import os

DadosCovidAjustados = pd.read_csv('DadosCovidAjustados.csv')

try:
    os.makedirs('./Brasil')
except:
    print('Erro ou já existe')

def df_estados(estado):
    
    estado_atual = estado.iloc[0]["Estado"]

    estado.to_csv('Brasil/' + estado_atual + '.csv', encoding = 'utf-8')

    ##############################################################################
    try:
        os.makedirs('./Brasil/' + estado_atual)
    except:
        print('Erro ou já existe Estado')

    def df_cidades(cidade):
        
        cidade.to_csv("./Brasil/" + estado_atual + "/" + cidade.iloc[0]["Cidade"] + '.csv', encoding = 'utf-8')


        return cidade

    dfCidades = estado.groupby('Cidade').apply(df_cidades).reset_index(drop=True)

    #############################################################################
    return estado

df_Estados_total = DadosCovidAjustados.groupby('Estado').apply(df_estados).reset_index(drop=True)