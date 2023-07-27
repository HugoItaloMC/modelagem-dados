-- Arquivo de levantamento de RELACIONAMENTOS e CONSTRAINT's ao SCHEMA `smooth_ecommerce` aplicando DDL
USE smooth_ecommerce;

SHOW TABLES;

DESC cliente;  -- 1
DESC PJ;  -- 2
DESC pagamentos;  -- 3
DESC cartao_credito;  -- 4
DESC debito_automatico;  -- 5
DESC gerar_boleto;  -- 6
DESC colaborador;  -- 7
DESC setor_secao;  -- 8
DESC setor;  -- 9
DESC estoque;  -- 10
DESC vendedor;  -- 11
DESC pedido;  -- 12
DESC ordem_pedido;  -- 13
DESC transporte;  -- 14
DESC produto;  -- 15
DESC fornecedor;  -- 16

-- Verificando CONSTRAINTS do nosso SCHEMA aplicando 'DQL':
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
	WHERE CONSTRAINT_SCHEMA = 'smooth_ecommerce';

-- ADD FOREIGN KEY's FOR TABLES ->

ALTER TABLE cliente DROP CONSTRAINT fk_id_pagamento_cliente ;
    ADD CONSTRAINT fk_cnpj FOREIGN KEY (CNPJ_)
    REFERENCES PJ(CNPJ),

    ADD CONSTRAINT fk_id_pagamento_cliente FOREIGN KEY (id_forma_pagamentos_)
    REFERENCES pagamentos(id_forma_pagamentos),
    ON UPDATE CASCADE;

 ALTER TABLE PJ
    ADD CONSTRAINT fk_pj_cliente FOREIGN KEY (id_cliente_)
    REFERENCES cliente(id_cliente)
    ON UPDATE CASCADE;

 ALTER TABLE pagamentos
    ADD CONSTRAINT fk_pagamento_cliente FOREIGN KEY (id_cliente_)
    REFERENCES cliente(id_cliente),

    ADD CONSTRAINT fk_pagamento_boleto FOREIGN KEY (id_pagamento_boleto)
    REFERENCES gerar_boleto(id_pagamento),

    ADD CONSTRAINT fk_pagamento_credito FOREIGN KEY (id_pagamento_credito)
     REFERENCES cartao_credito(id_pagamento),

    ADD CONSTRAINT  fk_pagamento_debito FOREIGN KEY (id_pagamento_debito)
     REFERENCES debito_automatico(id_pagamento)
    ON UPDATE CASCADE;

ALTER TABLE colaborador
    ADD CONSTRAINT fk_scpf FOREIGN KEY (SCPF)
    REFERENCES colaborador(CPF)
    ON UPDATE CASCADE;

ALTER TABLE colaborador
    ADD CONSTRAINT fk_secao_colaborador FOREIGN KEY (id_secao_)
    REFERENCES setor_secao(id_secao)
    ON UPDATE CASCADE;

ALTER TABLE setor
    ADD CONSTRAINT fk_setor_gerente FOREIGN KEY (SCPF_)
    REFERENCES colaborador(SCPF)
    ON UPDATE CASCADE;

ALTER TABLE  setor_secao
    ADD CONSTRAINT fk_setor_secao FOREIGN KEY (id_setor_)
    REFERENCES setor(id_setor)
    ON UPDATE CASCADE;

ALTER TABLE estoque
    ADD CONSTRAINT fk_id_setor FOREIGN KEY (id_setor_)
    REFERENCES setor(id_setor),

    ADD CONSTRAINT fk_id_produto FOREIGN KEY (id_produto_)
    REFERENCES produto(id_produto)
    ON UPDATE CASCADE;

ALTER TABLE  vendedor
    ADD CONSTRAINT fk_gerente FOREIGN KEY (SCPF_)
    REFERENCES colaborador(SCPF)
    ON UPDATE CASCADE;

ALTER TABLE ordem_pedido
    ADD CONSTRAINT fk_pedido_ordem FOREIGN KEY (id_pedido_)
    REFERENCES pedido(id_pedido),

    ADD CONSTRAINT fk_cliente_ordem FOREIGN KEY (id_cliente_)
    REFERENCES cliente(id_cliente),

    ADD CONSTRAINT fk_transporte_ordem FOREIGN KEY (cnpj_transportadora_)
    REFERENCES transporte(cnpj_transportadora)
    ON UPDATE CASCADE;

ALTER TABLE pedido ADD CONSTRAINT fk_vendedor_interno;
    ADD CONSTRAINT fk_produto_pedido FOREIGN KEY (id_produto_)
     REFERENCES produto(id_produto),

    ADD CONSTRAINT fk_id_pagamento FOREIGN KEY (id_pagamento_)
    REFERENCES pagamentos(id_forma_pagamentos),

    ADD CONSTRAINT fk_vendedor FOREIGN KEY (id_vendedor_)
     REFERENCES vendedor(id_vendedor),

    ADD CONSTRAINT fk_vendedor_interno FOREIGN KEY (vendedor_interno_CPF)
    REFERENCES colaborador(CPF)
    ON UPDATE CASCADE;

ALTER TABLE transporte
    ADD CONSTRAINT FOREIGN KEY
    REFERENCES ()
    ON UPDATE CASCADE;

ALTER TABLE produto
    ADD CONSTRAINT fk_secao_produto FOREIGN KEY (id_secao_)
    REFERENCES setor_secao(id_secao)
    ON UPDATE CASCADE;

ALTER TABLE fornecedor
    ADD CONSTRAINT fk_fornecedor_produto FOREIGN KEY (id_produto_)
     REFERENCES produto(id_produto)
    ON UPDATE CASCADE;

-- ADD UNIQUE VALUES SCHEMA ->

ALTER TABLE cliente
    ADD CONSTRAINT unique_document UNIQUE (CPF, RG);

ALTER TABLE PJ
    ADD CONSTRAINT unique_cnpj UNIQUE (CNPJ);

ALTER TABLE gerar_boleto
    ADD CONSTRAINT unique_boleto UNIQUE (codigo_boleto);

ALTER TABLE cartao_credito
    ADD CONSTRAINT unique_cartao UNIQUE (numero_cartao);

ALTER TABLE debito_automatico
    ADD CONSTRAINT unique_cpf_debito UNIQUE (CPF_TITULAR);

ALTER TABLE colaborador
    ADD CONSTRAINT unique_document_colaborador UNIQUE (CPF, RG);

ALTER TABLE vendedor
    ADD CONSTRAINT unique_document_vendedor UNIQUE (CPF, RG);

-- ADD CHEKS VALUES SCHEMA ->

ALTER TABLE cliente
    ADD CONSTRAINT  CHECK ;

ALTER TABLE gerar_boleto
    ADD CONSTRAINT chk_boleto CHECK (codigo_boleto <> 0 AND codigo_boleto < 9999999);

ALTER TABLE colaborador
    ADD CONSTRAINT chk_salario CHECK (salario > 1500.00);

ALTER TABLE ordem_pedido
    ADD CONSTRAINT chk_data_pedido CHECK (data_despache < data_entrega);

ALTER TABLE produto
    ADD CONSTRAINT chk_preco CHECK (preco < 100000.00);

