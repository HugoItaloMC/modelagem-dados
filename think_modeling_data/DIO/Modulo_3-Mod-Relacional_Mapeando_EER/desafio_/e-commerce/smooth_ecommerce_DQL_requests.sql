USE smooth_ecommerce;
-- Rcuperando dados simples;

SELECT * FROM cliente ;

-- Cliente, Colaborador, Pedido
-- Identificando Pedidos feito por vendedores que são colaboradores;
-- Instâncias agrupadas por data
-- Ordenacão crescente id_cliente

SELECT p.data_pedido, count(*), c.id_cliente, co.CPF, p.id_pedido
    FROM cliente AS c INNER JOIN
        (SELECT p.id_produto_, p.id_pedido, p.id_vendedor_
             FROM colaborador AS co RIGHT JOIN pedido AS p
             ON co.CPF = p.`vendedor_interno_CPF`
             WHERE p.endereco_entrega LIKE '_cep%') AS ordem
    ON c.CPF BETWEEN 00000000000 AND 99999999999
    GROUP BY p.data_pedido
    HAVING p.data_pedido >= 1
    ORDER BY p.id_pedido;


-- Produto Estoque, Secao
-- Recuperando Dados de um  produto e sua marca especifica !!

SELECT concat(p.nome, ' ', p.marca_produto, ' ', p.preco) AS produto, p.id_secao_
       FROM produto p INNER JOIN
            (estoque AS e INNER JOIN setor_secao AS sc
            ON e.id_setor_ = sc.id_setor_) AS setor_produto
       ON p.id_secao_ = sc.id_secao
       WHERE p.marca_produto LIKE '(...)';


-- Vendedor, Produto, Pedido

SELECT concat(v.primeiro_nome, ' ', v.nome_meio, ' ', v.sobre_nome) AS nome_vendedor,pd.id_produto_, count(*),
      concat(p.nome, ' ', p.marca_produto, ' ', p.id_secao_) AS produto
    FROM vendedor AS v INNER JOIN
           (produto AS p INNER JOIN pedido AS pd
           ON p.id_produto = pd.id_produto_)
    ON v.id_vendedor = pd.id_vendedor_;
