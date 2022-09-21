SELECT concat(c.primeiro_nome,' ', c.nome_meio, ' ', c.sobre_nome) AS nome_cliente,
        concat(vp.placa, ' ', vp.modelo, ' ', vp.marca) AS passeio,
        concat(vu.placa, ' ', vu.modelo, ' ', vu.marca) AS ultilitario
        FROM cliente AS c JOIN veiculo_passeio AS vp
        ON c.id_cliente = vp.id_cliente_
        JOIN veiculo_ultilitario AS vu
        ON c.id_cliente = vu.id_cliente_


SELECT p.status_forma_pagamento, da.forma_pagamento, cc.forma_pagamento
        CASE
        WHERE p.status_forma_pagamento = 'OFF'
        AND (da.forma_pagamento = 'Reprovado' OR da.forma_pagamento = 'Em Analise')
        AND  (cc.forma_pagamento = 'Reprovado' OR cc.forma_pagamento = 'Em Analise')
        THEN 'PAYMENT INVALID'
        ELSE 'PAYMENT VALID',
        END AS status_forma_pagamento_
    FROM pagamentos AS P, debito_automatico AS da, cartao_credito AS cc;  -- 4

SELECT concat(c.primeiro_nome,' ', c.nome_meio, ' ', c.sobre_nome) AS nome_cliente
    FROM cliente AS c JOIN ( uso_produto_ordem AS upo JOIN produto_objeto AS po
                            ON upo.id_produto_objeto_ = po.id_produto_objeto) AS uso_objeto
                            ( uso_produto_ordem AS upo JOIN produto_mao_de_obra AS pmo
                            ON upo.id_produto_mao_de_obra_ = pmo.id_produto_mao_de_obra) AS uso_mao_de_obra;