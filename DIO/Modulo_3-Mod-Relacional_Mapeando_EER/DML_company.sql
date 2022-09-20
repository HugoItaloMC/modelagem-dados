-- Persistindo dados. Povoando Tabelas,  'Aplicando DML'
USE company;

INSERT INTO employee VALUES ('Jose', 'V', 'Silva', '987654321', '1980-05-16',
                            'BR-SP Rua Ricardo Bueno, 88', 'M', 30000, NULL, '5'),

                            ('Joao', 'F', 'Gomes', '321654987', '1988-12-18',
                            'BR-RJ Rua Marianalva, 44', 'M', 30500, '987654321', '5'),

                            ('Maria', 'R', 'Batista', '789456123', '1977-07-22',
                            'BR-MG Rua Jose Faria, 55', 'F', 22000, '987654321', '3');


INSERT INTO department VALUES ('Operation', 5, '987654321', '2020-05-03', '2019-01-05'),
                              ('Admin', 3, '987654321', '2020-05-03', '2019-05-15');

INSERT INTO dep_location VALUES (3, '3 Andar'),
                                (5, '0 a 2 andar');

INSERT INTO project VALUES ('Balanco', 3, '3 Andar'),
                           ('feature', 5, 'Terreo');

INSERT INTO works_on VALUES ('987654321', 3, 30),
                            ('987654321', 5, 30);

INSERT INTO dependent VALUES ('987654321', 'Gabriel', 'M', '2015-05-04'),
                             ('321654987', 'Maria', 'F', '2018-06-01'),
                             ('789456123', 'Pedro', 'M', '2019-08-12');
