-- Schema  ->
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS smooth_ecommerce DEFAULT CHARACTER SET utf8;
USE smooth_ecommerce;
SHOW TABLES;
-- -----------------------------------------------------
-- Stored Cliente relationship ->
-- -----------------------------------------------------
DROP TABLE cliente;
CREATE TABLE IF NOT EXISTS cliente (
  id_cliente INT NOT NULL AUTO_INCREMENT,
  primeiro_nome VARCHAR(15) NULL,
  nome_meio VARCHAR(15) NULL,
  sobre_nome VARCHAR(15) NULL,
  CPF CHAR(11) NOT NULL,
  RG CHAR(9) NOT NULL,
  contato VARCHAR(45) NOT NULL,
  endereco VARCHAR(45) NOT NULL,
  CNPJ_ INT NOT NULL DEFAULT 0,
  id_pagamento_ INT NOT NULL,
  id_transporte_ INT NOT NULL,
  PRIMARY KEY (id_cliente, CNPJ_, id_pagamento_, id_transporte_)
 );

CREATE TABLE IF NOT EXISTS PJ (
  CNPJ INT NOT NULL,
  id_cliente_ INT NOT NULL,
  razao_social VARCHAR(45),
  PRIMARY KEY (CNPJ, id_cliente_)
);

-- -----------------------------------------------------
-- Formas de Pagamento Cliente ->
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS pagamentos(
  id_cliente_ INT NOT NULL,
  id_pagamento INT NOT NULL,
  forma_pagamento ENUM("Informado", "N Informado"),
  PRIMARY KEY (id_pagamento, id_cliente_)
);

CREATE TABLE IF NOT EXISTS gerar_boleto (
  id_pagamento_boleto INT NOT NULL AUTO_INCREMENT,
  codigo_boleto INT(25),
  PRIMARY KEY (id_pagamento_boleto)
);

CREATE TABLE IF NOT EXISTS cartao_credito (
  id_pagamento_credito INT NOT NULL AUTO_INCREMENT,
  nome_titular VARCHAR(30),
  cvv_cartao CHAR(3),
  numero_cartao CHAR(16),
  forma_pagamento ENUM("Aprovado", "Em analise", "Reprovado"),
  PRIMARY KEY (id_pagamento_credito)
);

CREATE TABLE IF NOT EXISTS debito_automatico (
  id_pagamento_debito INT NOT NULL AUTO_INCREMENT,
  titular_conta VARCHAR(45) NULL,
  agencia VARCHAR(7) NULL,
  conta VARCHAR(13) NULL,
  forma_pagamento ENUM("Aprovado", "Em analise", "Reprovado"),
  PRIMARY KEY (id_pagamento_debito)
);

-- -----------------------------------------------------
-- Company Team ->
-- -----------------------------------------------------

CREATE TABLE IF NOT EXISTS colaborador(
  primeiro_nome VARCHAR(15) NULL,
  nome_meio VARCHAR(15) NULL,
  sobre_nome VARCHAR(15) NULL,
  CPF CHAR (11) NOT NULL,
  RG CHAR (9) NOT NULL,
  id_secao_ CHAR (4) NOT NULL,
  SCPF CHAR (11),
  salario DECIMAL(10,2),
  PRIMARY KEY (CPF, SCPF, id_secao_)
  );

CREATE TABLE IF NOT EXISTS setor (
  id_setor CHAR(5) NOT NULL,
  SCPF_ CHAR(11),
  PRIMARY KEY (id_setor, SCPF_)
);

CREATE TABLE IF NOT EXISTS setor_secao (
  id_setor_ CHAR(5) NOT NULL,
  id_secao CHAR(4) NOT NULL,
  PRIMARY KEY (id_secao,  id_setor_)
 );
DROP TABLE vendedor;
CREATE TABLE IF NOT EXISTS estoque (
  id_estoque INT NOT NULL AUTO_INCREMENT,
  id_setor_ CHAR(5) NOT NULL,
  id_produto_ INT NOT NULL,
  PRIMARY KEY (id_estoque, id_setor_, id_produto_)
 );


CREATE TABLE IF NOT EXISTS vendedor (
  id_vendedor INT NOT NULL AUTO_INCREMENT,
  primeiro_nome VARCHAR(15) NULL,
  nome_meio VARCHAR(15) NULL,
  sobre_nome VARCHAR(15) NULL,
  CPF CHAR (11) NOT NULL,
  RG CHAR (9) NOT NULL,
  SCPF_ CHAR (11),
  id_pedido_ INT NOT NULL,
  PRIMARY KEY (id_vendedor, SCPF_, id_pedido_)
);


CREATE TABLE IF NOT EXISTS ordem_pedido (
  id_pedido_ INT NOT NULL,
  id_transporte_ INT NOT NULL,
  descricao VARCHAR(45) NULL,
  status_pedido ENUM("Despache", "A Caminho") NOT NULL,
  data_entrega_ DATE NOT NULL,
  PRIMARY KEY (id_pedido_, id_transporte_, data_entrega_)
 );

CREATE TABLE IF NOT EXISTS transporte (cli
  id_transporte INT NOT NULL AUTO_INCREMENT,
  nome_transportadora VARCHAR(45) NULL,
  data_pedido_ DATE,
  data_despache DATE,
  data_entrega DATE NOT NULL,
  PRIMARY KEY (id_transporte, data_entrega, data_pedido_)
 );

CREATE TABLE IF NOT EXISTS pedido (
  id_pedido INT NOT NULL AUTO_INCREMENT,
  id_cliente_ VARCHAR(45) NOT NULL,
  id_produto_ INT NOT NULL,
  id_pagamento_ INT NOT NULL,
  data_pedido VARCHAR(45) NULL,
  endereco_entrega VARCHAR(45) NULL,
  id_vendedor INT NOT NULL,
  vendedor_interno_CPF CHAR (11),
  PRIMARY KEY (id_pedido, id_cliente_, id_produto_, id_vendedor)
);

-- ----------------------------------------------------
-- Products for buy
-- ----------------------------------------------------
CREATE TABLE IF NOT EXISTS produto (
  id_produto INT NOT NULL AUTO_INCREMENT,
  nome VARCHAR(20) NULL,
  descricao VARCHAR(20) NULL,
  preco DECIMAL(10, 2) NULL,
  quantidade INT NOT NULL ,
  id_secao_ INT NOT NULL,
  id_fornecedor_ INT NOT NULL,
  PRIMARY KEY (id_produto, id_secao_, id_fornecedor_)
);

CREATE TABLE IF NOT EXISTS fornecedor (
  id_fornecedor INT NOT NULL AUTO_INCREMENT,
  contato VARCHAR(45) NULL,
  endereco VARCHAR(45) NULL,
  segmento_produto VARCHAR(45) NULL,
  marca_produto VARCHAR(45) NULL,
  PRIMARY KEY (id_fornecedor)
);
