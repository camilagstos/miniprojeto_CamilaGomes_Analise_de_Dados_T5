# Miniprojeto - Análise Exploratória de Dados com Python

## Sobre o projeto

Este miniprojeto foi desenvolvido com o objetivo de realizar uma análise exploratória de uma base de dados de varejo, utilizando Python e os conteúdos estudados durante o curso.

A análise foi realizada inicialmente através da leitura e verificação dos dados, seguida pela conversão para DataFrame, limpeza e padronização das informações. Após essa etapa, foram realizadas análises buscando entender melhor o perfil dos clientes e seus comportamentos de compra.


## Tecnologias utilizadas

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- VS Code


## Etapas realizadas

Durante o desenvolvimento do projeto foram realizadas as seguintes etapas:

- Leitura da base CSV utilizando `DictReader`;
- Conversão dos dados para DataFrame;
- Verificação da estrutura e qualidade dos dados;
- Padronização das colunas e tratamento de valores ausentes;
- Conversão dos tipos de dados, incluindo a coluna de data para `datetime`;
- Verificação e análise dos registros duplicados;
- Aplicação de estatísticas descritivas;
- Agrupamentos para análise do perfil dos clientes e comportamento de compra.


## Principais análises e insights

A análise mostrou que, apesar da média de filhos ser de aproximadamente 1,14 por cliente, a mediana e a moda demonstram que pelo menos metade dos clientes não possui filhos.

O segmento B possui o maior número de clientes e de compras. Porém, ao analisar a média de compras por cliente, o segmento C apresentou uma frequência um pouco maior.

Entre as categorias analisadas, Alimentos apresentou os maiores percentuais nos três segmentos econômicos, seguida por Higiene e Limpeza. Também foi possível perceber que as mulheres representam a maior quantidade de clientes e apresentaram uma média de compras ligeiramente superior à dos homens.

Durante a análise foram encontrados registros duplicados. Como a base não possui uma coluna informando a quantidade de unidades adquiridas, optei por manter esses registros, pois eles podem representar a compra de mais de uma unidade do mesmo produto.


## Reflexão sobre ETL e qualidade dos dados

Durante o desenvolvimento do projeto foi possível perceber a importância das etapas de ETL para preparar os dados antes da realização das análises. A extração ocorreu através da leitura do arquivo CSV, seguida pela transformação dos dados através da padronização das colunas, tratamento de valores ausentes, conversão dos tipos e análise das duplicidades.

Também foi possível perceber que a qualidade dos dados interfere diretamente nos resultados obtidos. Antes dos agrupamentos e cálculos estatísticos, foi necessário verificar possíveis inconsistências e entender as informações presentes na base, evitando que problemas nos dados interferissem nas conclusões da análise.


## Como executar

Os principais arquivos do projeto são:

- `miniprojeto.ipynb` - Notebook utilizado durante o desenvolvimento e análise dos dados.
- `miniprojeto.py` - Script Python contendo a lógica desenvolvida no projeto.

Para executar o script, é necessário possuir o Python e as bibliotecas utilizadas instaladas. A base de dados deve estar no mesmo diretório do arquivo Python.

No terminal do VS Code, execute:

    python miniprojeto.py