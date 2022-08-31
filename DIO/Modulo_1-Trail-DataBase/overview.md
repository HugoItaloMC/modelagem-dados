### **Dados e Banco de Dados**
 ___________________________________________________________________________________________
 - **_Dados :_**

       É a representacão de um estado, um evento, um objeto e ou um ser


 - **_Bando de Dados :_**

        É a persistência de dados contendo uma estrutura com regras e restricões
       pré-definidas em tabelas com atributos, relacionadas ou não.


### **SGDB, Sistema de Banco de Dados e Catálogo de BD**
 ___________________________________________________________________________________________
 - **_SGDB :_**


      É um sistema para gerenciar banco de dados, proporcionando uma boa performace
     isolando o programa dos dados, controlando a concorrência, back-up, recovery.

 
- **_Sistema de Banco de Dados :_**
 
        É a forma de se isolar a aplicacão dos dados, tendo um gerenciamento
       otimizado do armazenamento, persistência dos dados, monitoramento.  

 - **_Catálogo de BD :_**
 
       É a estrutura de organizacão dos dados, nomeando tabelas, colunas.

### **Independência program/data, User View**
___________________________________________________________________________________________
 - **_Independência program/data :_**

      
     É a definicão do isolamento do programa (API, FRONT-END) do Banco de Dados, 
    em uma forma geral é criada 3 camadas sendo elas: Mode Conceitual se tem 
    uma abstracão dos levantamentos de requisitos em forma de diagrama, Modelo Fisíco onde 
    se encontra o Modelo Lógico com regras de negócios,o SGDB, métodos e o esquema do 
    banco de dados e o Modelo View que tem a interacão como usúario ultilizando programacão 
    (front-end e back-end). Lembrando que essa independência é implicita, tem que ser 
    implementado de forma manual essa conexão. 

 - **_User View :_**

        É constraints (regras/restricões) que define quem e onde vai ser o acesso 
       a determinadas entidades no banco de dados.

 ### **_DBA, transacões canned, metadados e aplicacão de processamento de transacões_**
___________________________________________________________________________________________

 - **_DBA :_**


      É o administrador do banco de dados, em sua staff inclui, Design de dados, 
    Modelagem de Dados, e geranciar os bancos de dados no SGDB.


 - **_Transacões Canned :_**

         É uma "camada" onde está acontecendo as instâncias no banco de dados 
       (transacões em um canudo), o nome já é bem auto-descritivo.

 - **_Metadados :_**

       É a informacão da estrutura, regras, atributos de um esquema de banco de dados.    


 - **_Aplicacão de Processamento de Transacão :_** 
          
        
        Regras para instânciar os dados recebidos na view para o esquema de banco de dados.