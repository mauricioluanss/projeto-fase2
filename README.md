
---

# Projeto Fase 2: Análise de Dados Meteorológicos

### Projeto da disciplina de Lógica de Programação do curso de ADS, PUCRS.
## Visão Geral

Este projeto consiste na análise de um conjunto de dados meteorológicos do município de Porto Alegre, cobrindo o período de 1961 a 2016. O objetivo é desenvolver um programa em Python capaz de carregar, preparar, analisar e visualizar informações climáticas a partir de um arquivo de texto no formato `.csv`.

## Sobre o Conjunto de Dados (Dataset)

* **Fonte dos Dados:** [INMET - BDMET](https://bdmep.inmet.gov.br/)
* **Formato:** CSV (valores separados por vírgula)
* **Período Coberto:** 1961 a 2016
* **Total de Registros:** 18.564
* **Campos do Arquivo:**
    * `data`: Data do registro.
    * `precipitacao`: Volume de chuva em milímetros por m².
    * `temperatura_maxima`: Temperatura máxima em graus Celsius (°C).
    * `temperatura_minima`: Temperatura mínima em graus Celsius (°C).
    * `umidade_relativa`: Umidade relativa do ar (%).
    * `velocidade_vento`: Velocidade do vento (m/s).

## Objetivos Principais

O programa deve ser capaz de realizar duas tarefas centrais:

1.  **Carga e Preparação de Dados:** Ler o arquivo, filtrar as informações relevantes e armazená-las em estruturas de dados adequadas para consulta (listas, dicionários, etc.).
2.  **Análise e Visualização de Dados:** Realizar análises estatísticas sobre os dados e gerar gráficos para visualização dos resultados.

## Requisitos e Observações Técnicas

* **Estrutura de Dados:** Os dados do arquivo devem ser carregados em uma lista de listas, tuplas ou dicionários.
* **Organização do Código:** O código deve ser modularizado e organizado em funções.
* **Manipulação do Arquivo:**
    * Funções de string, como `.split()`, serão essenciais.
    * Não é necessário o uso de bibliotecas externas (como Pandas), mas são permitidas.
    * **Não modifique o arquivo `.csv` original.** O tratamento dos dados deve ser feito pelo programa.
* **Caminho do Arquivo:**
    * Utilize **caminho relativo** para acessar o arquivo (ex: `open('dados.csv', 'r')`). O programa deve assumir que o `.csv` está na mesma pasta do script.
    * **Não use caminhos absolutos** (ex: `open('C:\Users\...')`). Trabalhos com caminhos absolutos não serão avaliados.
* **Documentação:** Comente no código as decisões tomadas sobre o tratamento dos dados (o que foi desconsiderado, excluído ou corrigido).

## Funcionalidades a Implementar

### a) Visualização de Intervalo de Dados
O programa deve permitir que o usuário visualize os dados de um período específico.
* **Entrada do Usuário:** Mês/Ano inicial e Mês/Ano final.
* **Filtro de Visualização:** O usuário poderá escolher ver:
    1.  Todos os dados do período.
    2.  Apenas os dados de precipitação.
    3.  Apenas os dados de temperatura.
    4.  Apenas os dados de umidade e vento.
* **Requisitos:**
    * Validar todas as entradas do usuário.
    * Exibir um cabeçalho para os dados mostrados.

### b) Mês Mais Chuvoso
O programa deve identificar e exibir o mês/ano com a maior precipitação total, considerando todo o período do arquivo.
* **Saída:** Exibir o mês/ano e o valor total da precipitação.
* **Requisitos:** Utilizar obrigatoriamente um dicionário e implementar ao menos uma função.

### c) Média da Temperatura Mínima (2006-2016)
O programa deve calcular a temperatura mínima média, ano a ano, para um determinado mês informado pelo usuário, considerando os últimos 11 anos de dados (2006 a 2016).
* **Entrada do Usuário:** Um mês válido.
* **Armazenamento:** Os resultados devem ser armazenados em um dicionário (ex: `{'agosto2006': 10.5, 'agosto2007': 11.2, ...}`).
* **Requisitos:** Implementar em uma função e validar a entrada do usuário.

### d) Gráfico de Barras das Médias de Temperatura Mínima
O programa deve gerar um gráfico de barras com as médias calculadas no item anterior.
* **Dados:** Utilizar o dicionário gerado no item **(c)**.
* **Requisitos:**
    * O gráfico pode ser vertical ou horizontal.
    * Deve conter rótulos nos eixos, legendas e ser claro e informativo.

### e) Média Geral da Temperatura Mínima (2006-2016)
O programa deve calcular a média geral das temperaturas para o mês analisado, utilizando os dados do dicionário criado no item **(c)**.
* **Entrada:** O dicionário com as médias anuais.
* **Saída:** Exibir a média geral da temperatura mínima para o mês informado no período de 2006-2016.

## Instruções de Entrega

* **Formato:** Um arquivo `.zip` contendo **apenas** o seu código em Python (`.py` ou `.ipynb`). O arquivo de código não pode estar dentro de uma pasta no `.zip`.
* **Execução:** O programa deve executar acessando o arquivo `.csv` localmente.