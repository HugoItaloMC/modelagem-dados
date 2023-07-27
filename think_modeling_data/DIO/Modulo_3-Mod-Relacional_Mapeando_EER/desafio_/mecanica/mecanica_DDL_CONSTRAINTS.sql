-- Arquivo de levantamento de RELACIONAMENTOS e CONSTRAINT's ao SCHEMA `smooth_ecommerce` aplicando DDL
USE mecanica;

SHOW TABLES;

DESC cliente;  -- 1
DESC veiculo_passeio;  -- 2
DESC veiculo_ultilitario;  -- 3
DESC pagamentos;  -- 4
DESC gerar_boleto;  -- 5
DESC cartao_credito;  -- 6
DESC debito_automatico;  -- 7
DESC ordem_servico;  -- 8
DESC uso_produto_ordem -- 9
DESC pericia_ordem;  -- 10
DESC departamentos;  -- 11
DESC departamento_secao;  -- 12
DESC mecanico_auxiliar;  -- 13
DESC mecanico_especialista;  -- 14
DESC produto_objeto; -- 15
DESC produto_mao_de_obra; -- 16
DESC estoque;  -- 17
DESC colaborador;  -- 18

-- Verificando CONSTRAINTS do nosso SCHEMA aplicando 'DQL':
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
	WHERE CONSTRAINT_SCHEMA = 'mecanica';

-- ADD FOREIGN KEY's FOR TABLES ->

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


ALTER TABLE ordem_servico
    ADD CONSTRAINT fk_ordem_cliente FOREIGN KEY (id_cliente_)
    REFERENCES cliente(id_cliente)
    ON UPDATE CASACADE;

ALTER TABLE uso_produto_ordem
    ADD CONSTRAINT fk_ordem FOREIGN KEY (id_ordem_servico_)
    REFERENCES ordem_servico(id_ordem_servico)

    ADD CONSTRAINT fk_uso_produto FOREIGN KEY (id_produto_objeto)
    REFERENCES produto_objeto(id_produto_objeto)

    ADD CONSTRAINT fk_uso_mao_de_obra FOREIGN KEY (id_uso_mao_de_obra)
    REFERENCES produto_mao_de_obra(id_produto_mao_de_obra)

    ON UPDATE CASCADE;

ALTER TABLE departamentos
    ADD CONSTRAINT fk_departamentos_gerente FOREIGN KEY (SCPF_)
    REFERENCES colaborador(SCPF)
    ON UPDATE CASCADE;

ALTER TABLE  departamento_secao
    ADD CONSTRAINT fk_departamentos FOREIGN KEY (id_departamentos_)
    REFERENCES departamentos(id_departamentos)

    ADD CONSTRAINT fk_mecanico_auxiliar FOREIGN KEY (id_mecanico_auxiliar_)
    REFERENCES mecanico_auxiliar(id_mecanico_auxiliar)

    ADD CONSTRAINT fk_mecanico_especialista FOREIGN KEY (id_mecanico_especialista_)
    REFERENCES mecanico_especialista(id_mecanico_especialista)
    ON UPDATE CASCADE;


ALTER TABLE produto_objeto
    ADD CONSTRAINT fk_departamentos_produto_objeto FOREIGN KEY (id_departamentos_)
    REFERENCES departamentos(id_departamentos)
    ON UPDATE CASCADE;

ALTER TABLE produto_mao_de_obra
    ADD CONSTRAINT fk_departamentos_mao_de_obra FOREIGN KEY(id_departamentos_)
    REFERENCES produto_mao_de_obra(id_mao_de_obra)
    UPDATE ON CASCADE;

ALTER TABLE estoque
    ADD CONSTRAINT fk_departamentos FOREIGN KEY (id_departamentos_)
    REFERENCES departamentos(id_departamentos),

    ADD CONSTRAINT fk_produto_objeto FOREIGN KEY (id_produto_objeto_)
    REFERENCES produto_objeto(id_produto_objeto)
    ON UPDATE CASCADE;


ALTER TABLE colaborador
    ADD CONSTRAINT fk_scpf FOREIGN KEY (SCPF)
    REFERENCES colaborador(CPF)
    ON UPDATE CASCADE;

ALTER TABLE colaborador
    ADD CONSTRAINT fk_departamentos_colaborador FOREIGN KEY (id_departamentos_)
    REFERENCES departamentos(id_departamentos)
    ON UPDATE CASCADE;

-- ADD UNIQUE VALUES SCHEMA ->

ALTER TABLE cliente
    ADD CONSTRAINT unique_document UNIQUE (CPF, RG);
    ADD CONSTRAINT unique_veiculo UNIQUE (placa_veiculo_passeio, placa_veiculo_ultilitario)

ALTER TABLE gerar_boleto
    ADD CONSTRAINT unique_boleto UNIQUE (codigo_boleto);

ALTER TABLE cartao_credito
    ADD CONSTRAINT unique_cartao UNIQUE (numero_cartao);

ALTER TABLE debito_automatico
    ADD CONSTRAINT unique_cpf_debito UNIQUE (CPF_TITULAR);

ALTER TABLE colaborador
    ADD CONSTRAINT unique_document_colaborador UNIQUE (CPF, RG);

-- ADD CHEKS VALUES SCHEMA ->

ALTER TABLE gerar_boleto
    ADD CONSTRAINT chk_boleto
    CHECK (codigo_boleto <> 0 AND codigo_boleto < 9999999);

ALTER TABLE colaborador
    ADD CONSTRAINT chk_salario
    CHECK (salario > 1500.00);

ALTER TABLE pericia_ordem
    ADD CONSTRAINT chk_data_pedido CHECK (data_pedido < data_entraga);

ALTER TABLE produto_objeto
    ADD CONSTRAINT chk_preco CHECK (preco < 100000.00);
