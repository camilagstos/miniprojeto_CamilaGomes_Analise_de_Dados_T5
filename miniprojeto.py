# %% [markdown]
# ## Miniprojeto - Análise de Dados com Pyhton T5 ##

# %%
# Importando as bibliotecas

import csv
from datetime import datetime
from IPython.display import display
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# %%
# Realizando a leitura do CSV com DictReader (Manipulação de Arquivos CSV)

with open ("basevarejo.csv", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo, delimiter=";")
    dados = list(leitor)

# %%
# Verificando as informações sobre a composição do arquivo

print("Quantidade de registros:", len(dados))
print("Colunas:", dados[0].keys())

dados[0]

# %%
# Após verificação inicial dos dados, optei por converter para dataframe para facilitar e aglizar a análise exploratória

df = pd.DataFrame(dados)

# %%
# Validando as informações e dados do dataframe

df.info()

# %%
# Padronizando os nomes das colunas

df.columns = df.columns.str.strip().str.lower()

df.columns

# %%
# Verificando valores nulos ou ausentes

print(df.isnull().sum())

print((df == "").sum())

display(df["pr_nome"].value_counts())

display(df["pr_cat"].value_counts())

display(((df["pr_cat"] == "#N/D") & (df["pr_nome"] == "#N/D")).sum())

# %%
# Verificando a quantidade de registros duplicados

display(df.duplicated().sum())


# %%
# Analisando os registros das duplicatas

duplicados = df[df.duplicated(keep=False)]

display(duplicados.head(20))

# %%
# Como foram identificados itens repetidos na mesma compra, verificarei os produtos registrados em uma mesma compra
display(df[df['co_id'] == '1000'][['co_id', 'pr_id', 'pr_nome']])

# %% [markdown]
# Como não temos na base uma coluna sobre a quantidade de itens, optei por manter os registros duplicados, pois podem representar mais de uma unidade adquirida na compra.

# %%
# Conforme documentação da base, verificando a quantidade de compras e clientes únicos

print("Quantidade de compras:", df["co_id"].nunique())
print("Quantidade de clientes conforme cl_id:", df["cl_id"].nunique())

# %%
# Como a quantidade de compras não coincidiu com o informado no documento base (50.000), seguirei com análise possiveis inconsistências na coluna CO_ID

display(df["co_id"].value_counts())

display(df["co_id"].str.len().value_counts())

display ((~df["co_id"].str.isdigit()).sum())

datas_por_compra = df.groupby("co_id")["data"].nunique()

if (datas_por_compra > 1).any():
    print("Identificador de compra em mais de uma data!")
else:
    print("Cada identificador de compra possui uma única data!")

# %% [markdown]
##Insight:
#Durante a validação da coluna co_id, foram encontradas 18.471 compras únicas, quantidade diferente das 50.000 compras informadas na documentação da base. Foram verificadas possíveis inconsistências nos identificadores e também a relação entre compra, data e produtos. Apesar das verificações realizadas, não foi possível identificar uma informação na base que explique essa diferença.

# %%
# Removendo coluna vazia

df = df.drop(columns=[""])
df.info()

# %%
# Verificando espaços extras nos valores das colunas de texto

for coluna in df.columns:
    if df[coluna].dtype == "str":
        quantidade = (df[coluna] != df[coluna].str.strip()).sum()
        print(coluna, ":", quantidade)

# %%
# Substituindo na coluna pr_cat os valores #N/D por "Sem Categoria" e na coluna pr_nome os mesmos #N/D por "Não Informado"

categorias = []

for valor in df["pr_cat"]:
    if valor == "#N/D":
        categorias.append("Sem Categoria")
    else:
        categorias.append(valor)

df["pr_cat"] = categorias

display(df['pr_cat'].value_counts())


produtos = []

for valor in df["pr_nome"]:
    if valor == "#N/D":
        produtos.append("NÃO INFORMADO")
    else:
        produtos.append(valor)

df["pr_nome"] = produtos

display(df['pr_nome'].value_counts())

# %%
# Convertendo a coluna data com datetime

datas_convertidas = []

for data in df["data"]:
    datas_convertidas.append(datetime.strptime(data, "%d/%m/%Y"))

df["data"] = datas_convertidas

df.info()

# %%
# Analisando a coluna da quantidade de filhos e realizando a conversão para int

print("Valores não numéricos:", (~df["cl_fhl"].str.isdigit()).sum())

df["cl_fhl"] = df["cl_fhl"].astype(int)

df.info()

df["cl_fhl"].value_counts()

# %%
# Verificando os valores das demais colunas referentes a informações sobre os clientes

display(df["cl_genero"].value_counts())
display(df["cl_ec"].value_counts())
display(df["cl_seg"].value_counts())

# %%
# Frequência de compras de acordo com o genêro dos clientes 

compras_genero = df.groupby("cl_genero")["co_id"].nunique()

clientes_genero = df.groupby("cl_genero")["cl_id"].nunique()

media_por_genero = (compras_genero / clientes_genero).round(2)

display(compras_genero)
display(clientes_genero)
display(media_por_genero)

# %% [markdown]
# ## INSIGHT
# Ao analisar a frequência de compras de acordo com o gênero, notei que as mulheres representam a maioria dos clientes e também possuem maior quantidade de compras. Ao considerar a média por cliente, as mulheres apresentam 18,53 compras e os homens 18,41, demonstrando uma diferença pequena na frequência de compras por gêneros. 

# %%
# Frequência de compras por estado civil

compras_ec = df.groupby("cl_ec")["co_id"].nunique()
clientes_ec = df.groupby("cl_ec")["cl_id"].nunique()
media_compras_ec = (compras_ec/clientes_ec).round(2)

display(compras_ec)
display(clientes_ec)
display(media_compras_ec)

# %%
# Criando uma base com um registro por cliente

clientes_estado_civil = df[['cl_id', 'cl_ec', 'cl_fhl']].drop_duplicates()

clientes_com_filhos = clientes_estado_civil[clientes_estado_civil["cl_fhl"]> 0]
display(clientes_com_filhos)

filhos_por_ec = clientes_com_filhos.groupby("cl_ec")["cl_id"].nunique()
display(filhos_por_ec)

percentual_filhos_ec = (filhos_por_ec/clientes_ec * 100).round(2)
display(percentual_filhos_ec)

ids_com_filhos = clientes_com_filhos["cl_id"]
compras_clientes_com_filhos = df[df["cl_id"].isin(ids_com_filhos)]

compras_filhos_ec = compras_clientes_com_filhos.groupby("cl_ec")["co_id"].nunique()

media_compras_filhos_ec = (compras_filhos_ec / filhos_por_ec).round(2)

display(compras_filhos_ec)
display(media_compras_filhos_ec)

# %% [markdown]
# ## INSIGHT
# Ao analisar o estado civil dos clientes que possuem filhos, notei que todos os clientes viúvos possuem filhos. Porém, ao analisar a frequência de compras, os clientes separados com filhos apresentam a maior média, com aproximadamente 19,22 compras por cliente, enquanto os viúvos apresentam a menor média, com 17,54.

# %%
# Calculando as estatísticas da quantidade de filhos por cliente

clientes = df[["cl_id", "cl_fhl"]].drop_duplicates()

print("Quantidade de clientes:", clientes["cl_id"].nunique())
print("Quantidade de registros:", len(clientes))

display(clientes["cl_fhl"].describe())

print("Moda:", clientes["cl_fhl"].mode())

# %% [markdown]
# # INSIGHT
# Ao analisar os dados, notei que apesar da média de filhos por cliente ser de 1,14, ao verificar o segundo quartil (50%) e a moda. fica perceptível que pelo menos
# metade dos clientes não possui filhos, sendo 0 também a quantidade de filhos mais frequente na base.

# %%
# Analisando a quantidade de compras por segmento econômico e por cliente

compras_segmento = df.groupby("cl_seg")["co_id"].nunique()
display(compras_segmento)

clientes_segmento = df.groupby("cl_seg")["cl_id"].nunique()
display(clientes_segmento)

media_compras = (compras_segmento / clientes_segmento).round(2)
display(media_compras)

# %% [markdown]
# ## INSIGHT 
# Após analisar a quantidade de por cliente de acordo com o segmento econômico, foi possível perceber que, apesar de o segmento B possuir maior número de clientes e compras,
# o segmento C é o grupo que, segundo a média, realiza cmpras com maior frequência, apresentando aproximadamente 18,95 compras por cliente, enquanto os segmentos B e A 
# apresentam médias de 18,36 e 17,76, respectivamente.

# %%
# Analisando as categorias presentes nas compras de cada segmento econômico

compras_categoria_segmento = df.groupby(["cl_seg", "pr_cat"])["co_id"].nunique()

display(compras_categoria_segmento)

segmento_a = compras_categoria_segmento["A"]
percentual_a = (segmento_a / compras_segmento["A"]) * 100
display(percentual_a.round(2))

segmento_b = compras_categoria_segmento["B"]
percentual_b = (segmento_b / compras_segmento["B"]) * 100
display(percentual_b.round(2))

segmento_c = compras_categoria_segmento["C"]
percentual_c = (segmento_c / compras_segmento["C"]) * 100
display(percentual_c.round(2))

# %% [markdown]
# ## INSIGHT
# Analisando os dados de compras dos segmentos por categoria, é possível notar que todos são liderados por Alimentos, presente em mais de 98% das comprs, seguido por Higiene, com percentuais em torno de 95%, e Limpeza, com aproximadamente 94%. A ordem das categorias se mantém semelhante entre os segmentos, apresentando apenas algumas variações nos percentuais das demais categorias. Isso demonstra que apesar de pertecerem a segmentos econômicos diferentes, os clientes apresentam um padrão semelhante em relação às categorias presentes em suas compras.

# CONCLUSÕES FINAIS

# 1. Apesar da média ser de aproximadamente 1,14 filho por cliente,
# a mediana e a moda são iguais a zero, demonstrando que pelo menos
# metade dos clientes da base não possui filhos.

# 2. O segmento B apresentou a maior quantidade de clientes e de compras.
# Porém, o segmento C apresentou a maior média de compras por cliente,
# com aproximadamente 18,95 compras.

# 3. Alimentos apresentou o maior percentual entre as categorias analisadas
# nos três segmentos econômicos, seguido por Higiene e Limpeza, mantendo
# um comportamento semelhante entre os segmentos.

# 4. As mulheres representam a maior quantidade de clientes e realizaram
# mais compras. Porém, a média de compras por cliente apresentou pouca
# diferença entre mulheres (18,53) e homens (18,41).

# 5. Foram identificados registros duplicados, porém optei por mantê-los,
# pois a base não informa a quantidade de unidades adquiridas. Dessa forma,
# não é possível confirmar se são duplicidades indevidas ou compras de
# mais de uma unidade do mesmo produto.
