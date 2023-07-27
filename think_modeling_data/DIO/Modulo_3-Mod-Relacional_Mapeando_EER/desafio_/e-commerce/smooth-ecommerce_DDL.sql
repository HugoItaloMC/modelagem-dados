-- Arquivo de levantamento da ESTRUTURA do SCHEMA `smooth_ecommerce` aplicando DDL
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS smooth_ecommerce DEFAULT CHARACTER SET utf8;
USE smooth_ecommerce;
SHOW TABLES;
-- -----------------------------------------------------
-- Stored Cliente relationship ->
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS cliente (
  id_cliente INT NOT NULL AUTO_INCREMENT,
  primeiro_nome VARCHAR(15) NULL, -- Aplicar CHECK nome
  nome_meio VARCHAR(15) NULL,
  sobre_nome VARCHAR(15) NULL,
  CPF CHAR(11) NOT NULL, -- Aplicar UNIQUE
  RG CHAR(9) NOT NULL, -- Aplicar UNIQUE
  contato VARCHAR(45) NOT NULL,
  endereco VARCHAR(45) NOT NULL,
  CNPJ_ INT NOT NULL DEFAULT 0,
  PRIMARY KEY (id_cliente, CNPJ_, id_forma_pagamentos_)
 );

CREATE TABLE IF NOT EXISTS PJ (
  CNPJ INT NOT NULL, -- APlicar UNIQUE
  id_cliente_ INT NOT NULL,
  razao_social VARCHAR(45),
  PRIMARY KEY (CNPJ, id_cliente_)
);

-- -----------------------------------------------------
-- Formas de Pagamento Cliente ->
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS pagamentos(
  id_forma_pagamentos VARCHAR(3) NOT NULL DEFAULT 'OFF',
  id_cliente_ INT NOT NULL,
  id_pagamento_boleto INT NOT NULL,
  id_pagamento_credito INT NOT NULL,
  id_pagamento_debito INT NOT NULL,
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
-- Company Team ->
-- -----------------------------------------------------
DROP TABLE colaborador;
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
  PRIMARY KEY (CPF, id_secao_, SCPF)
  );

CREATE TABLE IF NOT EXISTS setor (
  id_setor CHAR(5) NOT NULL,
  SCPF_ CHAR(11),
  descricao VARCHAR(40) NOT NULL,
  PRIMARY KEY (id_setor, SCPF_)
);

CREATE TABLE IF NOT EXISTS setor_secao (
  id_setor_ CHAR(5) NOT NULL,
  id_secao CHAR(4) NOT NULL,
  descricao VARCHAR(40) NOT NULL,
  PRIMARY KEY (id_secao,  id_setor_)
 );

CREATE TABLE IF NOT EXISTS estoque (
  id_setor_ CHAR(5) NOT NULL,
  id_produto_ INT NOT NULL,
  PRIMARY KEY (id_setor_, id_produto_)
 );

CREATE TABLE IF NOT EXISTS vendedor (
  id_vendedor INT NOT NULL AUTO_INCREMENT,
  primeiro_nome VARCHAR(15) NOT NULL,
  nome_meio VARCHAR(15) NOT NULL,
  sobre_nome VARCHAR(15) NOT NULL,
  CPF CHAR (11) NOT NULL, -- Aplicar UNIQUE
  RG CHAR (9) NOT NULL,
  SCPF_ CHAR (11),
  PRIMARY KEY (id_vendedor, SCPF_)
);

CREATE TABLE IF NOT EXISTS ordem_pedido (
  id_pedido_ INT NOT NULL,
  id_cliente_ INT NOT NULL,
  cnpj_transportadora_ CHAR(14) NOT NULL,
  data_despache DATE NOT NULL,
  data_entrega DATE NOT NULL, -- Aplicar CHECK se a data é menor que a data do pedido
  status_pedido ENUM("Despache", "A Caminho", "Entregue") NOT NULL,
  PRIMARY KEY (id_pedido_, cnpj_transportadora_, id_cliente_)
 );

CREATE TABLE IF NOT EXISTS transporte (
  cnpj_transportadora CHAR(14) NOT NULL,
  raza_social VARCHAR(20) NOT NULL,
  PRIMARY KEY (cnpj_transportadora)
 );

CREATE TABLE IF NOT EXISTS pedido (
  id_pedido INT NOT NULL AUTO_INCREMENT,
  id_produto_ INT NOT NULL,
  id_pagamento_ VARCHAR(3) NOT NULL,
  data_pedido DATE NOT NULL,
  endereco_entrega VARCHAR(45) NOT NULL,
  id_vendedor_ INT NOT NULL,
  vendedor_interno_CPF CHAR (11),
  PRIMARY KEY (id_pedido, id_produto_, id_vendedor_, id_pagamento_, vendedor_interno_CPF)
);

-- ----------------------------------------------------
-- Products for buy
-- ----------------------------------------------------

CREATE TABLE IF NOT EXISTS produto (
  id_produto INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(20) NOT NULL,
  marca_produto VARCHAR(20) NOT NULL,
  preco DECIMAL(10, 2) NOT NULL, -- Aplicar CHECK no preco do produto
  quantidade INT NOT NULl DEFAULT 0,
  id_secao_ CHAR(4) NOT NULL,
  PRIMARY KEY (id_produto, id_secao_)
);

CREATE TABLE IF NOT EXISTS fornecedor (
  id_produto_ INT NOT NULL,
  contato VARCHAR(45) NOT NULL,
  endereco VARCHAR(45) NOT NULL,
  segmento_produto VARCHAR(20) NOT NULL,
  PRIMARY KEY (id_produto_)
);
