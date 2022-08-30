/*  SQL é uma linguagem declarativa, ultiliza a Teoria dos Conjuntos da Matemática para ter as relacões entre
as tabelas.
*/

CREATE DATABASE firstexample;
CREATE TABLE periodicos(
    id INTEGER AUTO_INCREMENT PRIMARY KEY,
    nome varchar(120),
    issn INTEGER,
    id_editora INT,
);

CREATE TABLE editora(
    id INTEGER,
    nome_editora VARCHAR(120) UNIQUE,
    Pais INTEGER,
    id_autor INT
    PRIMARY KEY (id)
);

/* Adicionando Dados em uma entidade : */
INSERT INTO editora (nome_editora, pais) VALUES ('IEEE', 'EUA'), ('DataScienceAcademy', 'EUA');
INSERT INTO periodicos(nome_periodicos, issn, id_editora) VALUES ('Special Issue', '15437609', '1');
/* OBS: No caso de redundância de dados, mesmo em instâncias diferentes, será gerado um erro !!
   ###  ERROR 1062 (23000): Duplicate entry 'IEEE' for key ###

   ^^ Desafio :
         Criar Entidades  Pesquisador/Autor Artigo/Work gerar e passar relacionamento entre elas, ultilizar modelo
       conceitual de ER (fluxo-grama).
*/

CREATE TABLE autor(
    id INTEGER PRIMARY KEY,
    nome_autor VARCHAR(120),
    id_pesquisa INTEGER,
);

CREATE TABLE pesquisa(
    id INTEGER PRIMARY KEY,
    nome VARCHAR(120),
    inquiry VARCHAR(200) /*  Descrevendo pesquisa */
);

/* Criando link'S entre as entidades aplicando constraint(restricao) */

ALTER TABLE periodicos ADD CONSTRAINT fk_periodicos_editora FOREIGN KEY(id_editora) REFERENCES editora(id);
ALTER TABLE editora ADD CONSTRAINT fk_editora_autor FOREIGN KEY(id_autor) REFERENCES autor(id);
ALTER TABLE autor ADD CONSTRAINT fk_autor_pesquisa FOREIGN KEY(id_pesquisa) REFERENCES pesquisa(id);
