# PGDPersonalizados

**Aluno:** Rafael Góes da Paz
## Descrição
O **PGDPersonalizados** é um sistema web desenvolvido em **Django** 
que permite gerenciar clientes, produtos e pedidos de uma loja de personalizados, 
com interface moderna, cards de acesso rápido e lista de pedidos funcional.

## Funcionalidades
- Home moderna com menu e cards de navegação  
- Cadastro e listagem de Clientes e Produtos  
- Cadastro, visualização e exclusão de Pedidos  
- Persistência de dados em SQLite  
- Interface estilizada com CSS  

## Tecnologias
- Python 3.13  
- Django 6.0.3  
- SQLite  
- HTML5 e CSS3  
- Git  

## Como Executar o Projeto
Para rodar o **PGDPersonalizados** no seu computador, siga estes passos:

1. Clone o repositório do GitHub para sua máquina.  
2. Entre na pasta do projeto onde está o arquivo `manage.py`.  
3. Crie e ative um ambiente virtual (recomendado).  
4. Instale o Django dentro do ambiente virtual.  
5. Execute as migrations para criar o banco de dados.  
6. Crie um superusuário (opcional) para acessar o painel administrativo.  
7. Rode o servidor de desenvolvimento com `python manage.py runserver`.  
8. Abra o navegador e acesse `http://127.0.0.1:8000/` para usar o sistema.  

## Estrutura do Projeto
PGDPersonalizados/  
├─ loja/  
│  ├─ templates/  # HTML  
│  ├─ static/css/ # CSS  
│  ├─ models.py  
│  ├─ views.py  
│  └─ urls.py  
├─ db.sqlite3  
├─ manage.py  
└─ README.md
