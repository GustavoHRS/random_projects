import pandas as pd
import os

DadosCovidAjustados = pd.read_csv('DadosCovidAjustados.csv')

print(DadosCovidAjustados)

RioGrandeDoSul = DadosCovidAjustados[DadosCovidAjustados['state'].str.contains('RS')]

RioGrandeDoSul = RioGrandeDoSul.drop('Unnamed: 0', axis = 1)

print(RioGrandeDoSul)
print(RioGrandeDoSul.columns)




RioGrandeDoSul.to_csv('RioGrandeDoSul.csv', encoding = 'utf-8')




cidades = RioGrandeDoSul.groupby(by = 'city', axis = 1)
print(cidades)

try:
    os.makedirs('./RS')
except:
    print('Cagou')

def f(cidade):
    print( 40*'=')
    print(cidade)

    cidade.to_csv('RS/' + cidade.iloc[0]["city"] + '.csv', encoding = 'utf-8')


    return cidade

dfCidades = RioGrandeDoSul.groupby('city').apply(f).reset_index(drop=True)
