-- Criando a estrutura do banco de dados para operadoras
CREATE TABLE operadoras (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) UNIQUE NOT NULL,
    cnpj VARCHAR(20) NOT NULL,
    razao_social VARCHAR(255) NOT NULL,
    nome_fantasia VARCHAR(255),
    modalidade VARCHAR(50),
    uf VARCHAR(2),
    data_registro DATE
);

-- Criando a estrutura do banco de dados para demonstrações contábeis
CREATE TABLE demonstracoes_contabeis (
    id SERIAL PRIMARY KEY,
    registro_ans VARCHAR(20) NOT NULL,
    ano INT NOT NULL,
    trimestre INT NOT NULL,
    sinistros_conhecidos NUMERIC(15,2) NOT NULL,
    FOREIGN KEY (registro_ans) REFERENCES operadoras(registro_ans)
);

-- Importando os dados cadastrais das operadoras
COPY operadoras(registro_ans, cnpj, razao_social, nome_fantasia, modalidade, uf, data_registro)
FROM '/caminho/para/Relatorio_cadop.csv'
DELIMITER ';'
CSV HEADER ENCODING 'LATIN1'
DATEFORMAT 'YYYY-MM-DD';

-- Importando os dados financeiros das demonstrações contábeis
COPY demonstracoes_contabeis(registro_ans, ano, trimestre, sinistros_conhecidos)
FROM '/caminho/para/demonstracoes_contabeis.csv'
DELIMITER ','
CSV HEADER ENCODING 'UTF8';

-- Consultas analíticas
-- Top 10 operadoras com maiores despesas em sinistros no último trimestre
SELECT registro_ans, SUM(sinistros_conhecidos) AS total_despesas
FROM demonstracoes_contabeis
WHERE ano = EXTRACT(YEAR FROM CURRENT_DATE) AND trimestre =
    CASE
        WHEN EXTRACT(MONTH FROM CURRENT_DATE) IN (1,2,3) THEN 4
        WHEN EXTRACT(MONTH FROM CURRENT_DATE) IN (4,5,6) THEN 1
        WHEN EXTRACT(MONTH FROM CURRENT_DATE) IN (7,8,9) THEN 2
        ELSE 3
    END
GROUP BY registro_ans
ORDER BY total_despesas DESC
LIMIT 10;

-- Top 10 operadoras com maiores despesas em sinistros no último ano
SELECT registro_ans, SUM(sinistros_conhecidos) AS total_despesas
FROM demonstracoes_contabeis
WHERE ano = EXTRACT(YEAR FROM CURRENT_DATE) - 1
GROUP BY registro_ans
ORDER BY total_despesas DESC
LIMIT 10;
