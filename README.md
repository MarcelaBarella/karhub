# Karhub

O repositório contém a solução para o desafio de engenheiro de dados da Karhub.

## Instruções para rodar a solução
* 
*
*

### Cosumo e persistencia dos dados

No arquivo *products_pandas.ipynb* é feita a leitura e persistencia  dos arquivos *karhub_autoparts_1.xlsx*, *karhub-alias.csv* e *cars_data.json*, onde a biblioteca **pandas** foi usada para a manipulação dos dados e obtenção do data frame de produtos que foi persistido como tabela no **BigQuery**, para tal, sua biblioteca local foi usada.
A extração dos dados de veículos contidos na API é feita no arquivo *karhub_extraction.py* e usa a biblioteca **requests** para tal.

### Queries BigQuery

As queries SQL contendo os valores de **produtos unicos**, **veiculos unicos** e **produtos unicos por categoria**, se encontra no arquivos *queries_bigquery.ipynb*.

## Melhorias
* Adicionar uma proposta de arquitetura de dados que cubra desde a extração até a visualização dos dados utilizando a cloud GCP e outras possiveis ferramentas.
* Incluir um notebook com o processamento e persistencia dos dados utilizando apache spark.