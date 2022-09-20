USE smooth_ecommerce;
-- Rcuperando dados simples;

SELECT * FROM cliente ;

-- Cliente, Colaborador, Pedido
-- Identificando Pedidos feito por vendedores que são colaboradores;
-- Instâncias agrupadas por data
-- Ordenacão crescente id_cliente

SELECT p.data_pedido, count(*), c.id_cliente, co.CPF, p.id_pedido FROM
    cliente AS c INNER JOIN (colaborador AS co INNER JOIN pedido AS p ON co.CPF = p.`vendedor_interno_CPF`)
    ON c.id_cliente = 4;
    GROUP BY data_pedido
    HAVING data_pedido >= 1
    ORDER BY p.id_pedido;


-- Produto Estoque, Secao

SELECT concat(p.nome, ' ', p.marca_produto, ' ', p.preco) AS produto, p.id_secao_
       FROM produto p INNER JOIN (estoque AS e INNER JOIN setor_secao AS sc ON e.id_setor_ = sc.id_setor_)
            ON p.id_secao_ = sc.id_secao;


-- Vendedor, Cliente, Ordem_pedido

SELECT * FROM vendedor AS v, cliente AS c, ordem_pedido AS op;
