import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

df = pd.read_excel("C:\\Users\\gusta\\Desktop\\Pessoal\\Estudos TI\\Boot camp DIO data science\\Intro Ciência de Dados\\Projeto pandas DIO\\AdventureWorks.xlsx")

print(df)

print(df["Valor Venda"].sum())

df["Custo"] = df["Custo Unitário"].mul(df["Quantidade"])

print(df["Custo"].sum())


df["Lucro"] = df["Valor Venda"] - df["Custo"]

print(df["Lucro"].sum())


#Tempo entre Venda e Envio do produto

df["Delay Envio"] = df["Data Envio"] - df["Data Venda"]

print(df["Delay Envio"])

#Tempo médio de envio para cada marca

df["Delay Envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days

a = (df.groupby("Marca")["Delay Envio"].mean())

print(a)


#Verificar se temos valores ausentes

print(df.isnull().sum())

#Vamos agrupar por ano e marca

print(df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum())

#pd.options.display.float.float_format = '{:20, .2f}'.format

lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["Lucro"].sum().reset_index()
print(lucro_ano)

print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

#Gráfico total de produto vendidos

b = df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True)
b.plt.xlabel("Total")
b.plt.ylabel("Produto")
plt.show()