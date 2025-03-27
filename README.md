# 📌 Testes de Nivelamento

Este repositório contém a implementação dos testes de nivelamento, abordando:

✅ Web Scraping  
✅ Transformação de Dados  
✅ Manipulação de Banco de Dados  
✅ Desenvolvimento de API  

## 🔧 Requisitos  

Antes de executar os scripts, instale as dependências:  

```bash
pip install -r requirements.txt
```  

## 🚀 Estrutura do Projeto  

```
/
├── dados/                      # Arquivos CSV usados no projeto
│   ├── demonstracoes_contabeis.csv
│   ├── Relatorio_cadop.csv
├── scripts/                    # Scripts Python
│   ├── web_scraping_ans.py      # Web Scraping
│   ├── data_transformation.py   # Transformação de dados
├── sql/                        # Scripts SQL
│   ├── consulta.sql             # Consultas analíticas
│   ├── database_operations.sql  # Criação e manipulação do banco
│   ├── import_data.sql          # Importação de dados do CSV
├── mysql-connector-python.py   # Conexão Python com MySQL
├── requirements.txt            # Dependências do projeto
├── README.md                   # Documentação
```

---

## 🏆 Testes Implementados  

### 1️⃣ Web Scraping  
**Objetivo:** Baixar os anexos I e II do site da ANS e compactá-los.  

📌 **Execução:**  
```bash
python scripts/web_scraping_ans.py
```  
✔ **Saída esperada:**  
- PDFs baixados na pasta `downloads/`  
- Arquivo ZIP `anexos_ans.zip` criado  

---

### 2️⃣ Transformação de Dados  
**Objetivo:** Extrair dados da tabela "Rol de Procedimentos" do PDF, gerar um CSV estruturado e compactá-lo.  

📌 **Execução:**  
```bash
python scripts/data_transformation.py
```  
✔ **Saída esperada:**  
- Arquivo `Rol_de_Procedimentos.csv` gerado  
- Arquivo ZIP `Teste_{seu_nome}.zip` criado  

---

### 3️⃣ Banco de Dados  
**Objetivo:** Criar tabelas, importar dados e executar queries analíticas.  

📌 **Passos:**  

1️⃣ **Criar banco de dados e tabelas**  
```bash
mysql -u usuario -p < sql/database_operations.sql
```  

2️⃣ **Importar dados CSV**  
```bash
mysql -u usuario -p < sql/import_data.sql
```  

3️⃣ **Executar consultas analíticas**  
```bash
mysql -u usuario -p < sql/consulta.sql
```  

✔ **Consultas Implementadas:**  
✅ **Top 10 operadoras com maiores despesas em sinistros no último trimestre**  
✅ **Top 10 operadoras com maiores despesas em sinistros no último ano**  

---

### 4️⃣ API (Vue.js + Python)  
**Objetivo:** Criar uma interface web para busca textual na lista de operadoras.  

📌 **Passos:**  

1️⃣ **Rodar o servidor Python**  
```bash
python app.py
```  

2️⃣ **Acessar a API via Postman**  

✔ **Endpoints Implementados:**  
- `/buscar_operadoras?termo=<pesquisa>` → Retorna operadoras mais relevantes  

---

## 📝 Observações  

📌 Os arquivos CSV foram baixados do repositório público da ANS:  
- 📄 [Demonstrações Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)  
- 📄 [Dados cadastrais das operadoras](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)  

📌 Este projeto é **confidencial** e não deve ser compartilhado sem autorização.  
