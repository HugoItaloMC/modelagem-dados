-- Recuperando dados em um Schema com querys sql:

USE company;

-- Gerente e seu departamento;
SELECT Ssn, Fname, Dname FROM employee e, department d WHERE (e.`Ssn` = d.`Mgr_ssn`);

-- Dependente e seu Responsável
SELECT Ssn, Fname, Dependent_name FROM employee, dependent WHERE `Essn` = `Ssn`;

-- Recuperando dados de empregado;
SELECT Bdata, Address FROM employee
     WHERE `Fname` = 'Joao' AND `Minit` = 'F' AND `Lname` = 'Gomes';

-- Recuperando dados do departamento;
SELECT * FROM department
    WHERE `Dname` = 'Admin';

-- Recuperando funcionários de departamentos especifico;

SELECT Fname, Lname, Address FROM employee, department
     WHERE  `Dname` = 'Operation' AND `Dnumber` = `Dno`;


-- Verificando atributos de entidades com DESC:
DESC works_on

SELECT Pname, Essn, Fname, Hours
FROM project, works_on, employee
WHERE `Pnumber` = `Pno` AND `Essn` = `Ssn`;