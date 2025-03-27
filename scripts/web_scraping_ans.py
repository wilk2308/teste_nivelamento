import requests
from bs4 import BeautifulSoup
import os
import zipfile

# URL da página da ANS
url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

# Pasta para salvar os PDFs
download_dir = "downloads"
os.makedirs(download_dir, exist_ok=True)

# Fazendo requisição para a página
response = requests.get(url)
response.raise_for_status()

# Parsing do HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrando links para os PDFs
pdf_links = []
for link in soup.find_all('a', href=True):
    if "Anexo" in link.text and link['href'].endswith(".pdf"):
        pdf_links.append(link['href'])

# Baixando os arquivos PDF
downloaded_files = []
for pdf_url in pdf_links:
    pdf_name = os.path.join(download_dir, os.path.basename(pdf_url))
    pdf_response = requests.get(pdf_url)
    with open(pdf_name, 'wb') as file:
        file.write(pdf_response.content)
    downloaded_files.append(pdf_name)
    print(f"Baixado: {pdf_name}")

# Compactando os PDFs em um arquivo ZIP
zip_name = "anexos_ans.zip"
with zipfile.ZipFile(zip_name, 'w') as zipf:
    for file in downloaded_files:
        zipf.write(file, os.path.basename(file))

print(f"Arquivos compactados em: {zip_name}")
