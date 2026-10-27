
# Sales Data Analysis with Python

**Exploratory Data Analysis | Data Cleaning | Business Insights**

🇧🇷 Português Brasileiro · 🇺🇸 English

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NumPy-Scientific%20Computing-013243?logo=numpy&logoColor=white" alt="NumPy">
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-11557c" alt="Matplotlib">
  <img src="https://img.shields.io/badge/Seaborn-Statistics-4c72b0" alt="Seaborn">
</p>

---

# 🇧🇷 Português

## Sobre o projeto

O **Sales Data Analysis with Python** é um projeto de análise exploratória de dados desenvolvido para transformar registros de vendas em informações úteis para análise de desempenho comercial.

A aplicação utiliza Python e bibliotecas de análise de dados para carregar, validar e tratar registros de vendas, calcular indicadores de desempenho, agrupar informações por diferentes dimensões e gerar relatórios e visualizações.

O projeto utiliza uma base fictícia gerada automaticamente quando o arquivo de entrada não existe, permitindo executar e explorar o sistema sem depender de uma base comercial externa.

## Índice

- [Sobre o projeto](#sobre-o-projeto)
- [Funcionalidades](#funcionalidades)
- [Tecnologias](#tecnologias)
- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Execução](#execução)
- [Estrutura do projeto](#estrutura-do-projeto)
- [Relatórios e visualizações](#relatórios-e-visualizações)
- [Exemplo de uso](#exemplo-de-uso)
- [Capturas de tela](#capturas-de-tela)
- [Demonstração em vídeo](#demonstração-em-vídeo)
- [Testes e validação](#testes-e-validação)
- [Possíveis melhorias](#possíveis-melhorias)
- [Autor](#autor)
- [Licença](#licença)

## Funcionalidades

- Geração automática de uma base fictícia de vendas.
- Importação de dados a partir de um arquivo CSV.
- Validação das colunas obrigatórias.
- Remoção de registros duplicados.
- Conversão e validação de datas e valores numéricos.
- Filtragem de registros inválidos.
- Cálculo do faturamento por registro.
- Cálculo de indicadores gerais de desempenho (KPIs).
- Análise de vendas por produto e categoria.
- Análise de faturamento por região.
- Análise mensal de vendas.
- Comparação do desempenho dos representantes de vendas.
- Exportação de relatórios em CSV.
- Geração de gráficos em PNG.

## Tecnologias

| Tecnologia | Utilização |
|---|---|
| Python | Linguagem principal |
| Pandas | Manipulação, limpeza e análise dos dados |
| NumPy | Geração de dados numéricos e aleatórios |
| Matplotlib | Criação e exportação de gráficos |
| Seaborn | Visualizações estatísticas |
| CSV | Armazenamento dos dados e relatórios |

## Requisitos

- Python 3.10 ou superior.
- `pip` para instalar as dependências.
- Terminal ou interpretador de comandos.
- Sistema operacional Windows, macOS ou Linux.

Não é necessário utilizar banco de dados ou serviços externos para executar a versão descrita neste projeto.

## Instalação

### 1. Baixar o projeto pelo GitHub

1. Acesse a página do repositório.
2. Clique no botão **Code**.
3. Selecione **Download ZIP**.
4. Extraia o arquivo baixado.
5. Abra um terminal dentro da pasta extraída.

Não é necessário utilizar `git clone`.

### 2. Criar um ambiente virtual

#### Windows

```powershell
py -m venv .venv
```

#### macOS e Linux

```bash
python3 -m venv .venv
```

### 3. Ativar o ambiente virtual

#### Windows — PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Se estiver utilizando o Prompt de Comando:

```bat
.venv\Scripts\activate.bat
```

#### macOS e Linux

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

Com o ambiente virtual ativado, execute:

```bash
pip install -r requirements.txt
```

## Execução

Execute o programa principal a partir da pasta do projeto.

#### Windows

```powershell
python main.py
```

Também é possível utilizar:

```powershell
py main.py
```

#### macOS e Linux

```bash
python3 main.py
```

Se o comando `python` estiver configurado para o ambiente virtual, ele também poderá ser utilizado.

### O que acontece durante a execução?

1. O programa verifica a existência do arquivo de entrada.
2. Caso necessário, gera uma base fictícia com 200 registros.
3. Carrega e valida os dados.
4. Remove duplicidades e registros inválidos.
5. Calcula o faturamento e os indicadores gerais.
6. Gera relatórios agrupados.
7. Cria gráficos e salva os arquivos na pasta `outputs/`.

A quantidade de registros válidos pode variar caso você substitua a base de exemplo por seus próprios dados.

## Estrutura do projeto

```text
sales-data-analysis-python/
├── data/
│   └── sales.csv
├── outputs/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

- `data/sales.csv`: base de entrada utilizada pelo programa. É criada automaticamente se não existir.
- `outputs/`: destino dos relatórios e gráficos gerados durante a execução.
- `main.py`: código principal da análise.
- `requirements.txt`: dependências Python.
- `.gitignore`: arquivos e pastas que não devem ser versionados.
- `README.md`: documentação do projeto.

Os arquivos de saída são criados durante a execução e não precisam existir previamente no repositório.

## Relatórios e visualizações

O programa gera os seguintes arquivos na pasta `outputs/`.

| Arquivo | Descrição |
|---|---|
| `kpis.csv` | Indicadores gerais da análise |
| `product_sales.csv` | Vendas, faturamento e pedidos por produto |
| `category_sales.csv` | Vendas e faturamento por categoria |
| `regional_sales.csv` | Faturamento e unidades por região |
| `monthly_sales.csv` | Evolução mensal do faturamento |
| `sales_representatives.csv` | Indicadores por representante de vendas |
| `cleaned_sales.csv` | Base tratada com coluna de faturamento |
| `monthly_revenue.png` | Gráfico de faturamento mensal |
| `top_products.png` | Dez produtos com maior faturamento |
| `category_revenue.png` | Comparação de faturamento por categoria |
| `regional_revenue.png` | Comparação de faturamento por região |
| `revenue_distribution.png` | Distribuição do faturamento por registro |

Os gráficos são salvos como imagens PNG e os relatórios como arquivos CSV, que podem ser abertos em ferramentas de planilhas compatíveis.

## Exemplo de uso

A base de entrada utiliza as seguintes colunas:

| Coluna | Significado |
|---|---|
| `order_id` | Identificador do pedido |
| `date` | Data do registro |
| `product` | Produto vendido |
| `category` | Categoria do produto |
| `quantity` | Quantidade vendida |
| `unit_price` | Preço unitário |
| `region` | Região da venda |
| `sales_rep` | Representante de vendas |

O faturamento de cada registro é calculado pela multiplicação da quantidade pelo preço unitário:

```python
df["revenue"] = df["quantity"] * df["unit_price"]
```

Para visualizar o relatório de produtos depois da execução, abra:

```text
outputs/product_sales.csv
```

Para visualizar o gráfico de faturamento mensal, abra:

```text
outputs/monthly_revenue.png
```

Os valores e as conclusões dependem dos dados efetivamente analisados.

## Capturas de tela

As capturas de tela devem representar a execução real do programa. Nenhuma imagem demonstrativa fictícia é apresentada nesta documentação.

Para adicionar imagens reais, crie a pasta `docs/images/` e salve nela capturas da execução e dos gráficos gerados.

Quando os arquivos existirem, adicione-os ao README, por exemplo:

```markdown
### Execução no terminal

![Execução real do sistema](docs/images/terminal-execution.png)

### Faturamento mensal

![Gráfico real de faturamento mensal](docs/images/monthly-revenue.png)

### Produtos com maior faturamento

![Gráfico real dos produtos](docs/images/top-products.png)
```

Os caminhos acima são exemplos de organização e só devem ser utilizados depois de criar e adicionar as imagens correspondentes ao repositório.

## Demonstração em vídeo

Ainda não há um vídeo de demonstração confirmado para este projeto.

### Como gravar uma demonstração real

1. Execute o programa no terminal.
2. Mostre o início e o término da execução.
3. Abra a pasta `outputs/`.
4. Mostre os relatórios CSV gerados.
5. Abra dois ou três gráficos PNG.
6. Salve a gravação como `sales-analysis-demo.mp4`.

No Ubuntu, uma opção é utilizar o gravador de tela integrado ao ambiente GNOME, quando disponível, ou instalar um gravador como o OBS Studio.

Depois de gravar, você poderá publicar o vídeo em uma plataforma de hospedagem ou adicionar um GIF curto ao repositório. Inclua neste README somente um link ou arquivo que realmente exista.

## Testes e validação

O código implementa verificações durante a execução, incluindo:

- Verificação das colunas obrigatórias.
- Conversão de datas e campos numéricos.
- Remoção de duplicidades.
- Filtragem de registros sem dados obrigatórios.
- Exclusão de quantidades não positivas e preços negativos.
- Interrupção da análise caso não existam registros válidos.

Essas verificações fazem parte da execução do programa. Não há, na versão documentada, uma suíte independente de testes automatizados confirmada.

## Possíveis melhorias

- Adicionar testes automatizados com `pytest`.
- Criar análises de margem de lucro, caso existam dados de custos.
- Desenvolver um dashboard interativo.
- Comparar períodos e identificar tendências.
- Adicionar indicadores de crescimento e variação percentual.
- Utilizar uma base pública de vendas para um estudo de caso real.

Esses itens são sugestões futuras, não funcionalidades já implementadas.

## Autor

**Israel Vitor**

GitHub: [@vitor1914](https://github.com/vitor1914)

Projeto desenvolvido para praticar análise de dados com Python e construir um portfólio de projetos.

## Licença

Nenhum arquivo de licença foi confirmado nesta versão. Antes de declarar uma licença de código aberto, adicione o arquivo `LICENSE` com os termos escolhidos.

---

# 🇺🇸 English

## About the project

**Sales Data Analysis with Python** is an exploratory data analysis project designed to turn sales records into useful information for understanding business performance.

The application uses Python data analysis libraries to load, validate, and clean sales records, calculate key performance indicators, aggregate information across different dimensions, and generate reports and visualizations.

A fictional sample dataset is generated automatically when the input file does not exist, allowing the application to run without relying on an external commercial dataset.

## Table of Contents

- [Project Overview](#about-the-project)
- [Features](#features)
- [Technologies](#technologies)
- [Requirements](#requirements)
- [Installation](#installation)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [Reports and Visualizations](#reports-and-visualizations)
- [Usage Example](#usage-example)
- [Screenshots](#screenshots)
- [Video Demonstration](#video-demonstration)
- [Testing and Validation](#testing-and-validation)
- [Potential Improvements](#potential-improvements)
- [Author](#author-1)
- [License](#license-1)

## Features

- Automatic generation of a fictional sales dataset.
- CSV data import.
- Required-column validation.
- Duplicate record removal.
- Date and numeric data conversion and validation.
- Invalid record filtering.
- Revenue calculation for each record.
- Overall key performance indicators (KPIs).
- Product and category sales analysis.
- Regional revenue analysis.
- Monthly sales analysis.
- Sales representative performance analysis.
- CSV report exports.
- PNG chart generation.

## Technologies

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Pandas | Data manipulation, cleaning, and analysis |
| NumPy | Numeric operations and random sample data generation |
| Matplotlib | Chart creation and export |
| Seaborn | Statistical visualizations |
| CSV | Input data and report storage |

## Requirements

- Python 3.10 or newer.
- `pip` for installing dependencies.
- A terminal or command-line interface.
- Windows, macOS, or Linux.

The documented version does not require a database or external services to run.

## Installation

### 1. Download the project from GitHub

1. Open the repository page.
2. Click the **Code** button.
3. Select **Download ZIP**.
4. Extract the downloaded archive.
5. Open a terminal in the extracted project folder.

You do not need to use `git clone`.

### 2. Create a virtual environment

#### Windows

```powershell
py -m venv .venv
```

#### macOS and Linux

```bash
python3 -m venv .venv
```

### 3. Activate the virtual environment

#### Windows — PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Alternatively, use Command Prompt:

```bat
.venv\Scripts\activate.bat
```

#### macOS and Linux

```bash
source .venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

## Running the Application

Run the main program from the project directory.

#### Windows

```powershell
python main.py
```

You can also use:

```powershell
py main.py
```

#### macOS and Linux

```bash
python3 main.py
```

### What happens during execution?

1. The program checks whether the input file exists.
2. If necessary, it generates a sample dataset containing 200 fictional records.
3. It loads and validates the data.
4. It removes duplicates and invalid records.
5. It calculates revenue and overall KPIs.
6. It generates grouped reports.
7. It creates charts and saves the output files in the `outputs/` directory.

The number of valid records may vary if you replace the sample dataset with your own data.

## Project Structure

```text
sales-data-analysis-python/
├── data/
│   └── sales.csv
├── outputs/
├── main.py
├── requirements.txt
├── .gitignore
└── README.md
```

- `data/sales.csv`: input dataset, created automatically if missing.
- `outputs/`: destination for generated reports and charts.
- `main.py`: main analysis script.
- `requirements.txt`: Python dependencies.
- `.gitignore`: files and directories excluded from version control.
- `README.md`: project documentation.

Output files are created during execution and do not need to exist in the repository beforehand.

## Reports and Visualizations

The program generates the following files in the `outputs/` directory.

| File | Description |
|---|---|
| `kpis.csv` | Overall analysis indicators |
| `product_sales.csv` | Sales, revenue, and orders by product |
| `category_sales.csv` | Sales and revenue by category |
| `regional_sales.csv` | Revenue and units by region |
| `monthly_sales.csv` | Monthly revenue trends |
| `sales_representatives.csv` | Performance indicators by sales representative |
| `cleaned_sales.csv` | Cleaned dataset with a revenue column |
| `monthly_revenue.png` | Monthly revenue chart |
| `top_products.png` | Top ten products by revenue |
| `category_revenue.png` | Revenue comparison by category |
| `regional_revenue.png` | Revenue comparison by region |
| `revenue_distribution.png` | Distribution of revenue per record |

Charts are saved as PNG images and reports as CSV files, which can be opened in compatible spreadsheet applications.

## Usage Example

The input dataset uses the following columns:

| Column | Meaning |
|---|---|
| `order_id` | Order identifier |
| `date` | Record date |
| `product` | Product sold |
| `category` | Product category |
| `quantity` | Quantity sold |
| `unit_price` | Unit price |
| `region` | Sales region |
| `sales_rep` | Sales representative |

Revenue for each record is calculated by multiplying quantity by unit price:

```python
df["revenue"] = df["quantity"] * df["unit_price"]
```

After running the application, open the product report:

```text
outputs/product_sales.csv
```

To view the monthly revenue chart, open:

```text
outputs/monthly_revenue.png
```

Values and business conclusions depend on the dataset actually analyzed.

## Screenshots

No real screenshots have been confirmed for this project yet.

To document the actual application, create a `docs/images/` directory and save screenshots of the execution and generated charts.

Once the files exist, add them to the README using paths such as:

```markdown
### Terminal Execution

![Actual application execution](docs/images/terminal-execution.png)

### Monthly Revenue

![Actual monthly revenue chart](docs/images/monthly-revenue.png)

### Top Products by Revenue

![Actual product revenue chart](docs/images/top-products.png)
```

These paths are examples of the intended organization. Use them only after adding the corresponding image files to the repository.

## Video Demonstration

A real demonstration video has not yet been confirmed for this project.

### How to record a demonstration

1. Run the application in a terminal.
2. Show the beginning and completion of the execution.
3. Open the `outputs/` directory.
4. Show the generated CSV reports.
5. Open two or three PNG charts.
6. Save the recording as `sales-analysis-demo.mp4`.

On Ubuntu, you can use the built-in GNOME screen recorder when available, or install a recorder such as OBS Studio.

After recording, publish the video on a hosting platform or add a short GIF to the repository. Include only links or files that actually exist.

## Testing and Validation

The application implements runtime checks, including:

- Required-column validation.
- Date and numeric field conversion.
- Duplicate record removal.
- Filtering records with missing required data.
- Exclusion of non-positive quantities and negative prices.
- Stopping the analysis if no valid records remain.

These checks are part of the application execution. An independent automated test suite has not been confirmed in the documented version.

## Potential Improvements

- Add automated tests with `pytest`.
- Analyze profit margins if cost data becomes available.
- Build an interactive dashboard.
- Compare periods and identify trends.
- Add growth and percentage-change indicators.
- Use a public sales dataset for a real-world case study.

These are potential future enhancements, not existing features.

## Author

**Israel Vitor**

GitHub: [@vitor1914](https://github.com/vitor1914)

This project was developed to practice Python data analysis and build a data analytics portfolio.

## License

No license file has been confirmed in this version. Before declaring an open-source license, add a `LICENSE` file containing the terms you choose.
