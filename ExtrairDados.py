
#Arquivo que baixa e extrai dados do site https://brasil.io/dataset/covid19/files/

import requests 
import gzip
import shutil

url = 'https://data.brasil.io/dataset/covid19/caso_full.csv.gz'

r = requests.get(url, allow_redirects = True)

open('DadosCovid.csv.gz', 'wb').write(r.content)

with gzip.open('DadosCovid.csv.gz', 'rb') as f_in:
    with open('DadosCovid.csv', 'wb') as f_out:
        shutil.copyfileobj(f_in, f_out)



