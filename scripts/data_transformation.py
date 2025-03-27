import pandas as pd
import pdfplumber
import os
import zipfile

# Nome do arquivo PDF baixado no teste 1
pdf_path = "downloads/Anexo_I_Rol_2021RN_465.2021_RN627L.2024.pdf"

# Nome do arquivo CSV de saída
csv_path = "Rol_de_Procedimentos.csv"

data = []

# Abrindo o PDF e extraindo as tabelas
with pdfplumber.open(pdf_path) as pdf:
    for page in pdf.pages:
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                data.append(row)

# Convertendo para DataFrame
df = pd.DataFrame(data)

# Renomeando colunas
df.columns = df.iloc[0]
df = df[1:].reset_index(drop=True)

# Substituindo abreviações
abreviacoes = {"OD": "Odontologia", "AMB": "Ambulatorial"}
df.replace(abreviacoes, inplace=True)

# Salvando como CSV
df.to_csv(csv_path, index=False, encoding='utf-8')

# Compactando o CSV
zip_name = "Teste_William_Sousa.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    zipf.write(csv_path, os.path.basename(csv_path))

print(f"CSV salvo e compactado em: {zip_name}")
