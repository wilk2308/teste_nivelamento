import mysql.connector
import pandas as pd

# Conectar ao banco de dados MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='test'
)
cursor = conn.cursor()

# Carregar o arquivo CSV para a tabela operadoras
df_operadoras = pd.read_csv('dados\\Relatorio_cadop.csv', sep=';')

# Criar a consulta SQL para inserir dados na tabela operadoras
query_operadoras = """
INSERT INTO operadoras (Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, 
                        Numero, Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico,
                        Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# Inserir os dados da tabela operadoras linha por linha
for _, row in df_operadoras.iterrows():
    cursor.execute(query_operadoras, tuple(row))

# Carregar o arquivo CSV para a tabela demonstracoes_contabeis
df_demonstracoes = pd.read_csv('dados\\demonstracoes_contabeis.csv', sep=';')

# Criar a consulta SQL para inserir dados na tabela demonstracoes_contabeis
query_demonstracoes = """
INSERT INTO demonstracoes_contabeis (DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL)
VALUES (%s, %s, %s, %s, %s, %s)
"""

# Inserir os dados da tabela demonstracoes_contabeis linha por linha
for _, row in df_demonstracoes.iterrows():
    cursor.execute(query_demonstracoes, tuple(row))

# Confirmar as inserções e fechar a conexão
conn.commit()
cursor.close()
conn.close()
