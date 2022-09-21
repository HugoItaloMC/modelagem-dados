
-- Arquivo de levantamento da ESTRUTURA do SCHEMA `mecanica` aplicando DDL
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS mecanica DEFAULT CHARACTER SET utf8 ;

USE mecanica ;

CREATE TABLE IF NOT EXISTS cliente (
  id_cliente INT NOT NULL AUTO_INCREMENT,
  primeiro_nome VARCHAR(15) NULL, -- Aplicar CHECK nome
  nome_meio VARCHAR(15) NULL,
  sobre_nome VARCHAR(15) NULL,
  CPF CHAR(11) NOT NULL, -- Aplicar UNIQUE
  RG CHAR(9) NOT NULL, -- Aplicar UNIQUE
  contato VARCHAR(45) NOT NULL,
  endereco VARCHAR(45) NOT NULL,
  CNPJ INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id_cliente)
 );

-- -----------------------------------------------------
-- Veiculos ->
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS veiculo_passeio (
  id_cliente_ INT NOT NULL ,
  placa CHAR(7) NOT NULL,
  modelo VARCHAR(15) NOT NULL,
  marca VARCHAR(10) NOT NULL,
  ano_modelo DATE NOT NULL,
  ano_fabricacao DATE NOT NULL,
  combustivel VARCHAR(45) NOT NULL,
  PRIMARY KEY (placa, id_cliente_)
  );

CREATE TABLE IF NOT EXISTS veiculo_ultilitario (
  id_cliente_ INT NOT NULL ,
  placa CHAR(7) NULL,
  modelo VARCHAR(15) NOT NULL,
  marca VARCHAR(10) NOT NULL,
  ano_fabricacao DATE NOT NULL,
  ano_modelo DATE NULL,
  peso_eixo VARCHAR(10) NULL,
  PRIMARY KEY (placa, id_cliente_)
);

-- ---------------------------------------------------
-- Formas de Pagamento Cliente ->
-- ---------------------------------------------------

CREATE TABLE IF NOT EXISTS pagamentos(
  id_forma_pagamentos INT NOT NULL AUTO_INCREMENT,
  id_cliente_ INT NOT NULL,
  id_pagamento_boleto INT ,
  id_pagamento_credito INT ,
  id_pagamento_debito INT ,
  status_forma_pagamento ENUM('ON', 'OFF') NOT NULL DEFAULT 'OFF',
  PRIMARY KEY (id_forma_pagamentos, id_cliente_, id_pagamento_boleto, id_pagamento_credito, id_pagamento_debito)
);

CREATE TABLE IF NOT EXISTS gerar_boleto (
  id_pagamento INT NOT NULL AUTO_INCREMENT,
  codigo_boleto INT NOT NULL, -- Aplicar CHECK no codigo do boleto
  PRIMARY KEY (id_pagamento)
);

CREATE TABLE IF NOT EXISTS cartao_credito (
  id_pagamento INT NOT NULL AUTO_INCREMENT,
  nome_titular VARCHAR(30),
  cvv_cartao CHAR(3),
  numero_cartao CHAR(16), -- Aplicar UNIQUE
  forma_pagamento ENUM("Aprovado", "Em analise", "Reprovado"),
  PRIMARY KEY (id_pagamento)
);

CREATE TABLE IF NOT EXISTS debito_automatico (
  id_pagamento INT NOT NULL AUTO_INCREMENT,
  titular_conta VARCHAR(45) NULL,
  agencia VARCHAR(7) NULL,
  CPF_TITULAR CHAR(11) NOT NULL,
  conta VARCHAR(13) NULL,
  forma_pagamento ENUM("Aprovado", "Em analise", "Reprovado"),
  PRIMARY KEY (id_pagamento)
);

-- -----------------------------------------------------
-- Execucão da Ordem ->
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS ordem_servico (
  id_ordem_servico INT NOT NULL AUTO_INCREMENT,
  id_cliente_ INT NOT NULL,
  servico VARCHAR(225) NOT NULL,
  data_pedido DATE NOT NULL,
  PRIMARY  (id_ordem_servico, id_cliente_)
  );

CREATE TABLE IF NOT EXISTS uso_produto_ordem(
    id_uso_produto_ordem INT NOT NULL AUTO_INCREMENT,
    id_ordem_servico_ INT NOT NULL,
    id_produto_objeto_ INT NOT NULL,
    id_produto_mao_de_obra_ INT NOT NULL,
    id_departamentos_ CHAR(5) NOT NULL,
    PRIMARY KEYS (id_uso_produto_ordem, id_ordem_servico_, id_produto_objeto_, id_produto_mao_de_obra_)
);

  CREATE TABLE IF NOT EXISTS pericia_ordem (
     id_pericia INT NOT NULL AUTO_INCREMENT,
     descricao VARCHAR(225) NOT NULL,
     receita_ordem DECIMAL(10, 2) NOT NULL,
     id_forma_pagamentos INT NOT NULL,
     data_entraga DATE NOT NULL,
     id_dp_secao_ CHAR(5) NOT NULL,
     PRIMARY KEY (id_pericia, id_dp_secao)
  );

CREATE TABLE IF NOT EXISTS departamentos (
  id_departamentos CHAR(5) NOT NULL,
  SCPF_ CHAR(11),
  descricao VARCHAR(40) NOT NULL,
  PRIMARY KEY (id_setor, SCPF_)
);

  CREATE TABLE IF NOT EXISTS departamento_secao (
  id_dp_secao CHAR(5) NOT NULL,
  id_departamentos_ CHAR(5) NOT NULL,
  PRIMARY KEY (id_dp_secao, id_departamentos_)
  );

  CREATE TABLE IF NOT EXISTS mecanico_auxiliar (
  id_mecanico_auxiliar INT NOT NULL AUTO_INCREMENT,
  CPF_ CHAR(11) NOT NULL,
  id_dp_secao_ CHAR(5) NOT NULL,
  salario_auxiliar DECIMAL(10, 2) NOT NULL,
  data_promocao DATE NOT NULL,
  PRIMARY KEY (id_mecanico_auxiliar, CPF_)
  );

  CREATE TABLE IF NOT EXISTS mecanico_especialista (
  id_mecanico_especialista INT NOT NULL AUTO_INCREMENT,
  CPF_ CHAR(11) NOT NULL,
  id_dp_secao_ CHAR(5) NOT NULL,
  salario_mecanico DECIMAL(10, 2) NOT NULL,
  data_promocao DATE NOT NULL,
  PRIMARY KEY (id_mecanico_especialista, CPF_)
  );

CREATE TABLE IF NOT EXISTS produto_objeto (
  id_produto_objeto INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(20) NOT NULL,
  marca_produto VARCHAR(20) NOT NULL,
  preco DECIMAL(10, 2) NOT NULL, -- Aplicar CHECK no preco do produto
  quantidade INT NOT NULl DEFAULT 0,
  id_departamento_ CHAR(4) NOT NULL,
  PRIMARY KEY (id_produto_objeto, id_departamento_)
);

CREATE TABLE IF NOT EXISTS produto_mao_de_obra (
  id_produto_mao_de_obra INT NOT NULL AUTO_INCREMENT,
  descricao VARCHAR(20) NOT NULL,
  preco DECIMAL(10, 2) NOT NULL, -- Aplicar CHECK no preco do produto
  id_departamento_ CHAR(5) NOT NULL,
  PRIMARY KEY (id_produto_mao_de_obra, id_departamento_)
);

CREATE TABLE IF NOT EXISTS estoque (
  id_departamento_ CHAR(5) NOT NULL,
  id_produto_objeto_ INT NOT NULL,
  PRIMARY KEY (id_departamento_, id_produto_objeto_)
 );

CREATE TABLE IF NOT EXISTS colaborador(
  primeiro_nome VARCHAR(15) NULL,
  nome_meio VARCHAR(15) NULL,
  sobre_nome VARCHAR(15) NULL,
  CPF CHAR (11) NOT NULL, -- Aplicar UNIQUE
  RG CHAR (9) NOT NULL,
  data_inicio DATE NOT NULL,
  id_secao_ CHAR (4) NOT NULL,
  SCPF CHAR (11),
  salario DECIMAL(10,2), -- Aplicar CHECK salario
  PRIMARY KEY (CPF, SCPF)
  );
