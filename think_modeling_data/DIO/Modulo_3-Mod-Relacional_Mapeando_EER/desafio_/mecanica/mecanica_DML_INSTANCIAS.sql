INSERT INTO cliente(primeiro_nome, nome_meio, sobre_nome, CPF, RG, contato, endereco, placa_veiculo_passeio, placa_veiculo_ultilitario, CNPJ_)
    VALUES()  -- 1

INSERT INTO veiculo_passeio(id_cliente_, placa, modelo, marca, ano_modelo, ano_fabricacao, combustivel)
    VALUES()  -- 2

INSERT INTO veiculo_ultilitario(id_cliente_, placa, modelo, marca, ano_fabricacao, ano_modelo, peso_eixo)
    VALUES()  -- 3


INSERT INTO gerar_boleto(codigo_boleto)
    VALUES()  -- 4

INSERT INTO cartao_credito(nome_titular, cvv_cartao, numero_cartao, forma_pagamento)
    VALUES()  -- 5
INSERT INTO debito_automatico(titular_conta, agencia, CPF_TITULAR, conta, forma_pagamento)
    VALUES()  -- 6

INSERT INTO ordem_servico(id_cliente_, servico, data_pedido)
    VALUES()  -- 7

INSERT INTO pericia_ordem(id_ordem_servico_, id_operacional_, descricao, receita_ordem, data_pedido, data_entrega, SCPF_)
    VALUES()  -- 8

INSERT INTO departamento(id_departamento, SCPF_, descricao)
    VALUES()  -- 9

INSERT INTO departamento_operacional(id_departamento_, id_operacional, descricao)
    VALUES()  -- 10

INSERT INTO mecanico_auxiliar(CPF_, salario_auxiliar, data_promocao)
    VALUES()  -- 11

INSERT INTO mecanico_especialista(CPF_, salario_mecanico, data_promocao)
    VALUES()  -- 12

INSERT INTO produto(nome, marca_produto, preco, quantidade, id_departamento_)
    VALUES()  -- 13

INSERT INTO estoque(id_departamento_, id_produto_)
    VALUES()  -- 14

INSERT INTO colaborador(primeiro_nome, nome_meio, sobre_nome, CPF, RG, data_inicio, id_departamento_, SCPF, salario)
    VALUES() -- 15