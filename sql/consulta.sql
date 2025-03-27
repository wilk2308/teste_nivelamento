-- Top 10 operadoras com maiores despesas em sinistros no último trimestre
SELECT 
    REG_ANS, 
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS total_despesas
FROM 
    demonstracoes_contabeis
WHERE 
    DATA BETWEEN DATE_SUB(CURDATE(), INTERVAL 3 MONTH) AND CURDATE()
    AND DESCRICAO LIKE '%EVENTOS/SINISTROS CONHECIDOS%' -- Filtra pela categoria
GROUP BY 
    REG_ANS
ORDER BY 
    total_despesas DESC
LIMIT 10;

-- Top 10 operadoras com maiores despesas em sinistros no último ano
SELECT 
    REG_ANS, 
    SUM(VL_SALDO_FINAL - VL_SALDO_INICIAL) AS total_despesas
FROM 
    demonstracoes_contabeis
WHERE 
    YEAR(DATA) = YEAR(CURDATE()) - 1
    AND DESCRICAO LIKE '%EVENTOS/SINISTROS CONHECIDOS%' -- Filtra pela categoria
GROUP BY 
    REG_ANS
ORDER BY 
    total_despesas DESC
LIMIT 10;