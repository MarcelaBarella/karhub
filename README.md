# Karhub

O repositório contém a solução para o desafio de engenheiro de dados da Karhub.

## Instruções para executar a solução
Para executar a solução, é necessário que tenha o jupyter notebook instalado (e outras ferramentas do ecosistema python) em seu computador, caso não tenha, crie um ambiente virtual e em seguida o ative
```
# cria o ambiente virtual
virtualenv myvenv

# ativa o ambiente virtual
source myvenv/bin/activate
```

Em seguida, instale o jupyter notebook com o gerenciador de pacotes de sua preferência, neste exemplo será usado o [**pip**](https://pypi.org/project/pip/).
```
pip install notebook
```
Depois, configure o kernel de seu notebook em seu ambiente virtual.
```
python -m ipykernel install --user --name=myvenv
```
Por fim inicialize seu notebook com o comando:
```
jupyter notebook
```
Após abrir o notebook selecione o arquivo *products.ipynb* e execute as células selecionando a opão Cells >> Run All, ou execute elas individualmente utilizando SHIFT + ENTER.
O destalhes das decisões tomadas se encontram dentro dos notebooks, porém, algumas deciões mais gerais serão documentadas neste arquivo.

### Cosumo e persistencia dos dados

No arquivo *products_pandas.ipynb* é feita a leitura e persistencia  dos arquivos *karhub_autoparts_1.xlsx*, *karhub-alias.csv* e *cars_data.json*, onde a biblioteca **pandas** foi usada para a manipulação dos dados e obtenção do data frame de produtos que foi persistido como tabela no **BigQuery**, para tal, sua biblioteca local foi usada. Apesar de mais robusto e integrar um ecosistema maior dentro do contexto de dados não foi feito o uso do **apache spark**, porém, pensando num contexto aplicação em produção, seu uso faz mais sentido uma vez que é melhor para processamentos em larga escala, suporta outras linguagens de programação, usa RDD etc.<br>
A extração dos dados de veículos contidos na API é feita no arquivo *karhub_extraction.py* e usa a biblioteca **requests** para tal. Considerando possíveis erros na API de veículos e sua execução num ambiente de produção, seria necessário a captura de tais erros por logs da aplicação.

### Queries BigQuery

As queries SQL contendo os valores de **produtos unicos**, **veiculos unicos** e **produtos unicos por categoria**, se encontra no arquivos *products_queries.ipynb*.
É possivel também utilizar as queries contidas nesses arquivo diretamente no console do BiQuery uma vez que se trata de SQL.

## Melhorias
* Adicionar uma proposta de arquitetura de dados que cubra desde a extração até a visualização dos dados utilizando a cloud GCP e outras possiveis ferramentas.
* Incluir um notebook com o processamento e persistencia dos dados utilizando apache spark.