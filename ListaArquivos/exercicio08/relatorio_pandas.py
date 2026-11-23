
# RELATÓRIO: UTILIZAÇÃO DA BIBLIOTECA PANDAS
#
# O Pandas é uma biblioteca do Python utilizada para manipular e analisar dados.
# Com ela, conseguimos organizar informações em tabelas, filtrar registros,
# realizar cálculos e trabalhar com arquivos como CSV e Excel.
#
# Para instalar:
# pip install pandas

import pandas as pd


# 1. CRIANDO UMA TABELA (DATAFRAME)
# O DataFrame é uma estrutura parecida com uma planilha,
# onde os dados são organizados em linhas e colunas.

dados = {
    "produto": ["Teclado", "Mouse", "Monitor", "Teclado", "Mouse"],
    "preco": [120, 60, 850, 120, 60],
    "quantidade": [2, 5, 1, 3, 4]
}

df = pd.DataFrame(dados)

print("\nTabela completa:")
print(df)


# 2. VISUALIZANDO OS DADOS
# head() mostra as primeiras linhas da tabela.
# tail() mostra as últimas linhas.
# info() apresenta informações sobre as colunas e seus tipos.
# describe() apresenta um resumo estatístico dos dados numéricos.

print("\nPrimeiras linhas:")
print(df.head(3))

print("\nÚltimas linhas:")
print(df.tail(2))

print("\nInformações da tabela:")
df.info()

print("\nResumo dos dados:")
print(df.describe())


# 3. ACESSANDO COLUNAS
# Podemos selecionar uma coluna pelo nome.
# Também podemos selecionar várias colunas utilizando uma lista.

print("\nNomes dos produtos:")
print(df["produto"])

print("\nProdutos e preços:")
print(df[["produto", "preco"]])


# 4. FILTRANDO DADOS
# A filtragem permite encontrar registros que atendem a uma condição.
# Neste exemplo, serão exibidos apenas produtos com preço acima de 100.

produtos_caros = df[df["preco"] > 100]

print("\nProdutos acima de R$ 100:")
print(produtos_caros)


# 5. ORDENANDO OS DADOS
# sort_values() organiza os registros de acordo com uma coluna.
# ascending=False define a ordem decrescente.

ordenado = df.sort_values(by="preco", ascending=False)

print("\nProdutos ordenados pelo preço:")
print(ordenado)


# 6. CRIANDO NOVAS COLUNAS
# Podemos criar novas colunas realizando operações com os dados existentes.
# Aqui calculamos o valor total de cada venda.

df["total"] = df["preco"] * df["quantidade"]

print("\nTabela com o valor total:")
print(df)


# 7. AGRUPANDO INFORMAÇÕES
# groupby() permite agrupar registros que possuem um mesmo valor.
# Neste exemplo, calculamos o total vendido de cada produto.

vendas_por_produto = df.groupby("produto")["total"].sum()

print("\nTotal vendido por produto:")
print(vendas_por_produto)


# 8. TRATANDO VALORES AUSENTES
# isnull() identifica valores que estão vazios.
# fillna() permite substituir esses valores por outro conteúdo.

dados_com_falhas = pd.DataFrame({
    "nome": ["Ana", "Carlos", "Marina"],
    "idade": [22, None, 28]
})

print("\nVerificando valores ausentes:")
print(dados_com_falhas.isnull())

# Substituindo os valores ausentes por zero.
dados_com_falhas["idade"] = dados_com_falhas["idade"].fillna(0)

print("\nTabela após o tratamento:")
print(dados_com_falhas)


# 9. REMOVENDO REGISTROS DUPLICADOS
# drop_duplicates() remove registros repetidos da tabela.
# Isso é útil quando existem informações cadastradas mais de uma vez.

dados_duplicados = pd.DataFrame({
    "email": ["ana@email.com", "carlos@email.com", "ana@email.com"]
})

sem_duplicados = dados_duplicados.drop_duplicates()

print("\nRegistros sem duplicidade:")
print(sem_duplicados)


# 10. IMPORTANDO E EXPORTANDO ARQUIVOS
# read_csv() permite carregar dados de um arquivo CSV.
# to_csv() permite salvar os dados em um arquivo CSV.
#
# Os exemplos abaixo estão comentados porque precisam de um arquivo externo.

# tabela = pd.read_csv("vendas.csv")
# print(tabela.head())

# tabela.to_csv("vendas_tratadas.csv", index=False)


# CONCLUSÃO
# O Pandas facilita o trabalho com dados dentro do Python.
# Com suas funções, conseguimos organizar tabelas, realizar cálculos,
# filtrar informações e tratar registros de maneira simples.
# Por isso, é uma biblioteca bastante utilizada na análise de dados.
