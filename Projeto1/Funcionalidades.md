# TPW - Projeto 1 - Descriçao/Funcionalidades

#

**Deploy**: (PythonAnywhere) http://tiagosora.pythonanywhere.com/ | http://pjnp5.pythonanywhere.com/

Grupo 7

- 102491 - Raquel Paradinha

- 103234 - Paulo Pinto

- 104142 - Tiago Carvalho

# Descriçao da Web App

A nossa aplicação baseia-se num site de suporte a uma clínica de saúde. Para tal desenhamos algumas funcionalidades que se adequavam ao tema e que conseguissem ir de encontro aos objetivos propostos no guião do projeto.

Para a criação deste projeto, usámos maioritariamente as tecnologias aprofundadas em ambiente de aula, focando a nossa atenção na exploração das aplicabilidades do Django. Para além disso, aproveitamos o nosso conhecimento em HTML, CSS e JS para tratar da camada de apresentação da nossa aplicação. Para melhor tratar das migrações, existe um ficheiro Bash, na root do projeto, criado com esse objetivo.

# Funcionalidades da Aplicação

As funcionalidades podem ser facilmente explicadas se forem tidos em causa os nossos 3 tipos de utilizador.

## Utilizador Não Autenticado

Quando o utilizador visita a aplicação pela primeira vez, e até se registar, encontra-se não autenticado. O utilizador tem acesso a navegar pela página principal (*home*), assim como pelas outras páginas de teor mais informativo (*about* e *contact*). O utilizador poderá ainda, ver os botões de "*new* *appointment*", "*login*" e "*sign* *up*" no *header* de cada uma das páginas.

O botão de *login* dá a possibilidade de o utilizador se autenticar com uma conta existente no sistema. No entanto, caso o utilizador não possua nenhuma conta na aplicação, poderá ainda recorrer ao *sign up* para se registar no sistema. Para um registo adequado, o utilizador deverá fornecer um *username* (que não coincida com nenhum outro no sistema), o primeiro e último nome, um endereço, uma conta de email e uma palavra-passe.

Caso o utilizador não autenticado tente criar um novo *appointment*, através de qualquer meio na aplicação, será automaticamente reencaminhado para a página de *login*.

## Utilizador Autenticado

Com o *login* feito, o utilizador torna-se um utilizador autenticado (no nosso caso um paciente) do sistema. Este tem acesso às mesmas funcionalidades do utilizador não autenticado e a outras exclusivas dos pacientes.

Duas dessas funcionalidades estão relacionadas com as marcações (*appointments*) que todos os pacientes podem fazer. Para realizar uma marcação, o paciente deve, primeiramente, utilizar um dos botões "new appointment" disponíveis na aplicação. De seguida, é direcionado para uma nova página onde poderá escolher um dos departamentos médicos disponíveis no sistema, uma data para a marcação e ainda poderá submeter uma pequena mensagem descritiva da marcação. Para finalizar esta interação, o paciente deve apenas submeter a marcação, através do botão "add appointment".

O paciente pode ainda aceder, através do header, à página "my appointments", onde poderá ver todos as suas marcações. Caso o utilizador não tenha feito até à data qualquer marcação, a tabela dessa página não terá qualquer linha. Caso já tenham sido feitas marcações, o utilizador poderá ver essas marcações, assim como modificá-las ou removê-las.

Relativamente à sua conta, o utilizador pode ainda aceder ao seu *profile* e também fazer *logout*. Na página de perfil, o utilizador pode verificar todos os dados que submeteu durante o registo (sign up), à excessão da palavra-passe (para fins de privacidade). O utilizador pode personalizar essas informações.

## Utilizador Admin (Superuser)

Caso a conta com que o utilizador se autenticar, seja uma das que o sistema reconhece como administrador. O utilizador (superuser), tem acesso a um novo modelo de aplicação, mais focado para fins administrativos. Nele, o utilizador poderá aceder a todos os appointments submetidos pelos pacientes, assim como modificá-los e ainda removê-los.

O utilizador poderá ainda acrescentar novos departamentos e remover departamentos atuais, através da aba "departments".

# Database

Assim como indicado pelo professor, foi feito o recurso a uma base de dados SQLite, diretamente ligada ao Django, que  facilita a recolha e o fornecimento de dados.

