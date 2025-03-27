-- Importar os dados do CSV para a tabela operadoras
LOAD DATA INFILE '/dados/Relatorio_cadop.csv'
INTO TABLE operadoras
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(Registro_ANS, CNPJ, Razao_Social, Nome_Fantasia, Modalidade, Logradouro, Numero, 
 Complemento, Bairro, Cidade, UF, CEP, DDD, Telefone, Fax, Endereco_eletronico, 
 Representante, Cargo_Representante, Regiao_de_Comercializacao, Data_Registro_ANS);

-- Importar os dados do CSV para a tabela demonstracoes_contabeis
LOAD DATA INFILE '/dados/demonstracoes_contabeis.csv'
INTO TABLE demonstracoes_contabeis
FIELDS TERMINATED BY ';'
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(DATA, REG_ANS, CD_CONTA_CONTABIL, DESCRICAO, VL_SALDO_INICIAL, VL_SALDO_FINAL);