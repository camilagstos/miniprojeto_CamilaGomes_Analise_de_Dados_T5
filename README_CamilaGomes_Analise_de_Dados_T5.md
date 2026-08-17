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

- Leitura da base de dados;
- Verificação da estrutura e dos tipos dos dados;
- Conversão dos dados para DataFrame;
- Padronização dos nomes das colunas;
- Verificação de valores nulos, vazios e espaços extras;
- Conversão dos tipos de dados quando necessário;
- Verificação e análise dos registros duplicados;
- Análise das informações dos clientes;
- Análise do comportamento de compras por segmento econômico;
- Análise das categorias de produtos;
- Análise da frequência de compras por gênero;
- Análise da frequência de compras por estado civil e presença de filhos.

## Principais análises e insights

Ao analisar a quantidade de filhos por cliente, foi possível perceber que, apesar da média ser de aproximadamente 1,14 filho por cliente, a mediana e a moda demonstram que pelo menos metade dos clientes da base não possui filhos.

Na análise dos segmentos econômicos, o segmento B possui o maior número de clientes e também a maior quantidade de compras. Porém, ao calcular a média de compras por cliente, o segmento C apresentou uma frequência de compras um pouco maior.

Em relação às categorias presentes nas compras, Alimentos apresentou os maiores percentuais nos três segmentos econômicos, seguida por Higiene e Limpeza. Apesar das diferenças entre os segmentos, o comportamento entre as categorias se mostrou semelhante.

Também foi analisada a frequência de compras de acordo com o gênero dos clientes. As mulheres representam a maior quantidade de clientes e também apresentaram uma média de compras ligeiramente superior à dos homens.

Por último, foi analisado o comportamento dos clientes de acordo com o estado civil e a presença de filhos, permitindo comparar a quantidade de clientes e a frequência média de compras entre os diferentes grupos.

## Registros duplicados

Durante a análise foram encontrados registros duplicados. Como a base não possui uma coluna específica informando a quantidade de unidades adquiridas em cada compra, optei por manter esses registros, pois eles podem representar a compra de mais de uma unidade do mesmo produto.

## Arquivos do projeto

- `miniprojeto.ipynb` - Notebook utilizado durante o desenvolvimento e análise dos dados.
- `miniprojeto.py` - Script Python contendo a lógica desenvolvida no projeto.
- `README.md` - Descrição do projeto e instruções para execução.

## Como executar

Para executar o projeto, é necessário possuir o Python e as bibliotecas utilizadas instaladas.

O arquivo pode ser aberto no VS Code e executado através do seguinte comando:

    python miniprojeto.py

A base de dados utilizada deve estar disponível no mesmo diretório do arquivo Python para que a leitura dos dados seja realizada corretamente.

## Considerações finais

O desenvolvimento deste miniprojeto permitiu aplicar os conhecimentos estudados durante o curso em uma base de dados com grande quantidade de registros. Além da preparação e tratamento dos dados, as análises realizadas permitiram identificar características dos clientes e diferenças no comportamento de compra entre os grupos analisados.