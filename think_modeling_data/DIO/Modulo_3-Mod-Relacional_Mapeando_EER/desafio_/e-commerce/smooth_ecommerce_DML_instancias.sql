USE smooth_ecommerce;

-- Sign up Client ->

INSERT INTO cliente(primeiro_nome, nome_meio, sobre_nome, CPF, RG, contato, endereco, CNPJ_)
           VALUES ('Maria', 'Amalia', 'Juarez', '46588915433', '849013580', '11983460871',
                   'Rua: Aloisio Teixeira 408, BR-SP/São Paulo', default);

           VALUES ('Renato', 'Moura', 'Souza', '23211400877', '436115064', '11998773340',
                   'Rua: Aloisio Teixeira 408, BR-SP/São Paulo', DEFAULT);

           VALUES ('Mauro', 'Guilherme', 'Aguiar', '37785511854', '651426658', '11933534415',
                   'Av: Manoel Dilva 66, BR-SP/Campinas', default);

           VALUES ('Atilio', 'Batista', 'Bitencourt', '49155677832', '987673443', '11955468876',
                   'Travessa: Raul Mane 54, BR-SP/Guarulhos', default)

INSERT INTO PJ(CNPJ, id_cliente_, razao_social)
    VALUES    ();

-- Register Pay's ->

INSERT INTO gerar_boleto(codigo_boleto)
    VALUES              ();

INSERT INTO cartao_credito(nome_titular, cvv_cartao, numero_cartao, forma_pagamento)
    VALUES                ();

INSERT INTO debito_automatico(titular_conta, agencia, CPF_TITULAR, conta, forma_pagamento)
    VALUES                   ();

-- Team register and company storege stock ->

INSERT INTO colaborador(primeiro_nome, nome_meio, sobre_nome, CPF, RG, data_inicio, id_secao_, SCPF, salario)
           VALUES ('Guilherme', 'Batista', 'Fiel', '44678315688', '33456893', NULL, 2500.00);

INSERT INTO setor(id_setor, SCPF_, descricao)
    VALUES ();

INSERT INTO setor_secao(id_setor, id_secao, descricao)
    VALUES ();

INSERT INTO estoque(id_setor_, id_produto_)
    VALUES ();

INSERT INTO vendedor(primeiro_nome, nome_meio, sobre_nome, CPF, RG, SCPF_)
    VALUES ();

INSERT INTO produto(nome, marca_produto, preco, quantidade, id_secao_)
    VALUES ();

INSERT INTO fornecedor
    VALUES (id_produto_, contato, endereco, segmento_produto);

-- Order Buy ->

INSERT INTO pedido (id_produto_, id_pagamento_, data_pedido, endereco_entrega, id_vendedor_, `vendedor_interno_CPF`)
    VALUES ();

INSERT INTO ordem_pedido (id_pedido_, id_cliente_, cnpj_transportadora_, data_despache, data_despache, status_pedido)
    VALUES ();

INSERT INTO transporte (cnpj_transportadora, raza_social)
    VALUES ();
