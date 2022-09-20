-- Aplicando 'DDL'

CREATE SCHEMA IF NOT EXISTS company;

USE company;

CREATE TABLE company.employee(
	Fname VARCHAR(15) NOT NULL,
    Minit CHAR,
    Lname VARCHAR(15) NOT NULL,
    Ssn CHAR(9),
    Bdata DATE,
    Address VARCHAR(40) NOT NULL,
    sex ENUM("F", "M", "Other"),
    Salary DECIMAL(10,2) NOT NULL,
    Super_ssn CHAR(9),
    Dno INT NOT NULL,
    
    -- Nomeando CONSTRAINTS
	CONSTRAINT pk_employee PRIMARY KEY (Ssn),
    
    -- CONSTRAINT de checagem :
	CONSTRAINT chk_salary_employee CHECK (Salary > 2000.0)
);

CREATE TABLE department(
	Dname VARCHAR(15),
    Dnumber INT NOT NULL,
    Mgr_ssn CHAR(9),
    Mgr_start_date DATE,
    Dept_start_date DATE,
    CONSTRAINT chk_date_dept CHECK (Dept_start_date < Mgr_start_date),
    CONSTRAINT pk_department PRIMARY KEY (Dnumber),
    CONSTRAINT unique_name_dept UNIQUE (Dname),
    FOREIGN KEY (Mgr_ssn) REFERENCES employee(Ssn)
);

CREATE TABLE dep_location(
	Dnumber INT NOT NULL,
    Dlocation VARCHAR(15) NOT NULL,
    -- OBS: Definimos nomes das CONSTRAINTS de PRIMARY KEY quando for mais de um Atributo ao mesmo.
    CONSTRAINT pk_dept_locat PRIMARY KEY (Dnumber, Dlocation),
    CONSTRAINT fk_dept_locat FOREIGN KEY (Dnumber) REFERENCES department(Dnumber)
);

CREATE TABLE project(
	Pname VARCHAR(15) NOT NULL,
    Pnumber INT NOT NULL,
    Plocation VARCHAR(15),
    PRIMARY KEY (Pnumber),
    CONSTRAINT unique_project UNIQUE (Pname),
    CONSTRAINT fk_project FOREIGN KEY (Pnumber) REFERENCES department(Dnumber)
);

CREATE TABLE works_on(
	Essn CHAR(9) NOT NULL,
    Pno INT NOT NULL,
    Hours DECIMAL(3,1) NOT NULL,
    PRIMARY KEY (Essn, Pno),
    CONSTRAINT fk_work_on_employee FOREIGN KEY (Essn) REFERENCES employee(Ssn),
    CONSTRAINT fk_works_on_dept FOREIGN KEY (Pno) REFERENCES project(Pnumber)
);

CREATE TABLE dependent(
	Essn CHAR(9) NOT NULL,
    Dependent_name VARCHAR(15) NOT NULL,
    Sex CHAR, -- feminino ou masculino
    Bdate DATE,
    CONSTRAINT pk_dependent PRIMARY KEY (Essn, Dependent_name),
    CONSTRAINT fk_dependent FOREIGN KEY (Essn) REFERENCES employee(Ssn)
);

-- Verificando CONSTRAINTS do nosso SCHEMA aplicando 'DQL':
SELECT * FROM INFORMATION_SCHEMA.TABLE_CONSTRAINTS
	WHERE CONSTRAINT_SCHEMA = 'company';

-- OBS : Para listarmos as REFERENCES das nossas FK ultilizamos INFORMATION_SCHEMA.REFERENTIAL_CONSTRAINTS


-- Modificando entidades com ALTER TABLE, aplicando 'DML';
ALTER TABLE employee
    ADD CONSTRAINT fk_employee
    FOREIGN KEY (Super_ssn) REFERENCES employee(Ssn)
    ON DELETE SET NULL  -- Para Atributos com persiste valores nulos
    ON UPDATE CASCADE; -- Atualizando todos atributos que erdam dessa da Entidade em que foi aplicada a CONSTRAINT

ALTER TABLE employee
    ADD CONSTRAINT pk_employee_dno PRIMARY KEY (Dno);

ALTER TABLE employee
    ADD CONSTRAINT fk_employee_dno FOREIGN KEY (Dno) REFERENCES department(Dnumber)
    ON UPDATE CASCADE;

-- Modificando uma CONSTRAINT ultilizando DROP e ADD:
ALTER TABLE department
    DROP CONSTRAINT department_ibfk_1;

ALTER TABLE department
    ADD CONSTRAINT fk_department FOREIGN KEY (Mgr_ssn) REFERENCES employee(Ssn)
    ON UPDATE CASCADE;