### **Dados e Banco de Dados**
 
 - **_Dados :_**

É a representacão de um estado, um evento.


 - **_Bando de Dados :_**

É a persistência de dados contendo uma estrutura com regras e restricões
pré-definidas em tabelas relacionadas com atributos.


### **SGDB, Sistema de Banco de Dados e Catálogo de BD**
 - **_SGDB :_**


  É um sistema para gerenciar banco de dados, proporcionando uma boa performace
isolando o programa dos dados, controlando a concorrência, back-up, recovery.

 
- **_Sistema de Bando de Dados :_**
 
É a forma de se isolar a aplicacão dos dados, tendo um gerenciamento
otimizado do armazenamento, persistência dos dados, monitoramento.  

 - **_Catálogo de BD :_**
 
É a estrutura de organizacão dos dados, nomeando tabelas, colunas.

### **Independência program/data, user view**

 - **_Independência program/data :_**

      É a definicão do isolamento do programa (API, FRONT-END) do Banco de Dados, 
em uma forma geral é criada 3 camadas sendo elas: Mode Conceitual se tem uma abstracão dos levantamentos de requisitos 
em forma de diagrama, Modelo Fisíco onde se encontra o Modelo Lógico com regras de negócios,o SGDB, métodos e o esquema
do banco de dados e o Modelo View que tem a interacão com o usúario ultilizando programacão (front-end e back-end).
      Lembrando que essa independência é implicita, tem que ser implementado de forma manual essa conexão. 

 - **_User View :_**

É constraints (regras/restricões) que define quem e onde vai ser o acesso a determinados entidades no banco de dados.