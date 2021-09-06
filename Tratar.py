import pandas as pd

DadosCovid = pd.read_csv('DadosCovid.csv' )

ajusteColunas = {
    "city" : "Cidade",
    "city_ibge_code" : "Código IBGE",
    "date" : "Data",
    "epidemiological_week" : "Semana Epidemiológica",
    "estimated_population" : "População Estimada Atual",
    "estimated_population_2019" : "População Estimada 2019",
    "is_last" : "Última atualização?",
    "is_repeated" : "É repetido?",
    "last_available_confirmed" : "Últimos Casos Confirmados",
    "last_available_confirmed_per_100k_inhabitants" : "Confirmados por 100k Habitantes",
    "last_available_date" : "Data do Último Registro",
    "last_available_death_rate" : "Taxa de Mortes Atualizada",
    "last_available_deaths" : "Total de Mortes",
    "order_for_place" : "Índice do Registro",
    "place_type" : "Tipo de Local",
    "state" : "Estado",
    "new_confirmed" : "Novos casos Confirmados",
    "new_deaths" : "Novas Mortes Confirmadas",
     }

DadosCovid.rename(columns = ajusteColunas, inplace = True)


DadosCovidAjustadosUF = DadosCovid[DadosCovid['Cidade'].isna()]

DadosCovid = DadosCovid.dropna()

DadosCovidAjustados = DadosCovid

print(DadosCovidAjustados.columns)
print(DadosCovidAjustados)

DadosCovidAjustados.to_csv('DadosCovidAjustados.csv', encoding = 'utf-8')

DadosCovidAjustadosUF.to_csv('DadosCovidAjustadosUF.csv', encoding = 'utf-8')