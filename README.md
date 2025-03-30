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

## 🌱 Ambiente Virtual (Virtual Environment)

Recomenda-se o uso de um ambiente virtual para garantir que todas as dependências sejam isoladas e não interfiram em outros projetos. Para criar e ativar um ambiente virtual, siga os passos abaixo:

1. **Criar o ambiente virtual**:
   ```bash
   python -m venv venv
   ```

2. **Ativar o ambiente virtual**:
   - No **Windows**:
     ```bash
     .\venv\Scripts\activate
     ```
   - No **Mac/Linux**:
     ```bash
     source venv/bin/activate
     ```

3. **Instalar as dependências**:
   Após ativar o ambiente virtual, instale as dependências do projeto:
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Estrutura do Projeto

```
/
├── dados/                        # Arquivos CSV usados no projeto
│   ├── demonstracoes_contabeis.csv
│   ├── Relatorio_cadop.csv
├── meu-projeto-vue/              # Frontend Vue.js
├── scripts/                      # Scripts Python
│   ├── web_scraping_ans.py       # Web Scraping
│   ├── data_transformation.py    # Transformação de dados
├── sql/                          # Scripts SQL
│   ├── consulta.sql              # Consultas analíticas
│   ├── database_operations.sql   # Criação e manipulação do banco
│   ├── import_data.sql           # Importação de dados do CSV
├── API Busca Operadoras.postman_collection.json  # Coleção do Postman
├── mysql-connector-python.py     # Conexão Python com MySQL
├── api_operadoras.py             # API Python para busca de operadoras
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação
```

## 📝 Passos para Execução

### 1️⃣ Rodar o Backend (API Python)

A API está implementada no arquivo `api_operadoras.py`. Para rodar a API, use o `uvicorn`:

- **Rodar a API com Uvicorn**:
  ```bash
  python -m uvicorn api_operadoras:app --reload
  ```

A API também está disponível online em: [API Online](https://teste-nivelamento.onrender.com/)

### 2️⃣ Rodar o Frontend (Vue.js)

Entre na pasta `meu-projeto-vue` e execute o servidor de desenvolvimento:

- **Instalar dependências do Vue.js**:
  ```bash
  cd meu-projeto-vue
  npm install
  ```

- **Rodar o servidor Vue.js**:
  ```bash
  npm run serve
  ```
  Além disso, o frontend Vue.js também está disponível online em: [Frontend](https://teste-nivelamento-1ypjm1qcl-willl23s-projects.vercel.app/)

### 3️⃣ Testar a API no Postman

Importe o arquivo `API Busca Operadoras.postman_collection.json` para o Postman e execute os endpoints configurados.

- Para rodar localmente, a URL da API deve ser `http://localhost:8000`
- Para testar na API online, use `https://teste-nivelamento.onrender.com/`

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
- Arquivo ZIP `Teste_William_Sousa.zip` criado  
- Substituição das abreviações das colunas OD e AMB pelas descrições completas, conforme a legenda no rodapé

---

### 3️⃣ Banco de Dados  
**Objetivo:** Criar tabelas, importar dados e executar queries analíticas.  

📌 **Passos:**  

1️⃣ **Criar banco de dados e tabelas**  
```bash
mysql -u usuario -p < sql/database_operations.sql
```  

2️⃣ **Importar dados CSV**  

🔹 Opção 1: Importação via SQL (import_data.sql)  
```bash
mysql -u usuario -p < sql/import_data.sql
```  

🔹 Opção 2: Importação via Python (mysql-connector-python.py)  
```bash
python mysql-connector-python.py
```  

3️⃣ **Executar consultas analíticas**  
```bash
mysql -u usuario -p banco < sql/consulta.sql
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
python -m uvicorn api_operadoras:app --reload
```  

2️⃣ **Acessar a API via Postman**  

✔ **Endpoints Implementados:**  
- `/buscar?q=<pesquisa>` → Retorna operadoras conforme pesquisa realizada  

---

## 📝 Observações  

📌 Os arquivos CSV foram baixados do repositório público da ANS:  
- 📄 [Demonstrações Contábeis](https://dadosabertos.ans.gov.br/FTP/PDA/demonstracoes_contabeis/)  
- 📄 [Dados cadastrais das operadoras](https://dadosabertos.ans.gov.br/FTP/PDA/operadoras_de_plano_de_saude_ativas/)  

📌 Este projeto é **confidencial** e não deve ser compartilhado sem autorização.

