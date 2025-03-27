# Testes de Nivelamento

Este repositório contém a implementação dos testes de nivelamento solicitados, incluindo web scraping, transformação de dados, manipulação de banco de dados e desenvolvimento de API.

## 📌 Requisitos

Antes de executar os scripts, instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## 🚀 Executando os Testes

### 1️⃣ Web Scraping
Baixa arquivos PDF do site da ANS e os compacta em um ZIP.

```bash
python scripts/web_scraping_ans.py
```

✔ **Saída esperada:**
- PDFs baixados na pasta `downloads/`
- Arquivo ZIP `anexos_ans.zip` criado

### 2️⃣ Transformação de Dados
Extrai tabelas de um PDF, gera um CSV estruturado e compacta o arquivo.

```bash
python scripts/data_transformation.py
```

✔ **Saída esperada:**
- Arquivo `Rol_de_Procedimentos.csv` gerado
- Arquivo ZIP `Teste_William_Sousa.zip` criado

### 3️⃣ Operações de Banco de Dados
Criação e manipulação das tabelas no banco de dados.

```bash
psql -U usuario -d banco -f sql/database_operations.sql
```

✔ **Saída esperada:**
- Tabelas `operadoras` e `demonstracoes_contabeis` criadas e populadas.
- Consultas SQL executadas com sucesso.

## 📂 Estrutura do Projeto
```
/
├── dados/                    # Arquivos CSV e outros dados brutos
├── downloads/                # PDFs baixados
├── scripts/                  # Scripts Python
│   ├── web_scraping_ans.py   # Script de Web Scraping
│   ├── data_transformation.py # Script de transformação de dados
├── sql/                      # Scripts SQL
│   ├── database_operations.sql # Criação e manipulação do banco
├── requirements.txt          # Dependências do projeto
├── README.md                 # Documentação
```

## 📜 Licença
Este projeto é apenas para fins de avaliação técnica.