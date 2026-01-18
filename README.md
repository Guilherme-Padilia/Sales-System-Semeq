
# Sale System SEMEQ

Sistema de vendas desenvolvido utilizando Django, Javascript, Bootstrap, Postgres e MongoDB.

🧱 Arquitetura do Projeto

O sistema foi dividido em múltiplos apps Django, cada um com responsabilidade bem definida:

* sales     – fluxo de vendas, carrinho, pagamento e histórico
* products  – busca de produtos
* customers – busca de clientes
* addresses – gerenciamento de endereços
* suppliers – gerenciamento de fornecedores

FrontEnd:

* Templates Django (HTML)
* JavaScript

Banco de Dados

* PostgreSQL - dados transacionais (clientes, produtos, vendas, endereços, fornecedores)
* MongoDB - histórico de vendas 

⚙️ Requisitos

* Python 3.10+
* PostgreSQL
* MongoDB
* Virtualenv



# 🚀 Passo a passo para rodar o projeto:

1 - Clonar Respositório:
```javascript
git clone https://github.com/Guilherme-Padilia/Sales-System-Semeq.git
cd Sales-System-Semeq
```

2 - Criar ambiente virtual:
```javascript
python -m venv venv
```

3 - Ativar ambiente virtual:
```javascript
venv\Scripts\activate
```

4 - Instalar dependências do projeto:
```javascript
pip install -r requirements.txt
```

5 - Criar arquivo .env na raiz do projeto:
```javascript
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

MONGO_HOST=localhost
MONGO_PORT=27017
MONGO_DB_NAME=sales_semeq_system
```

6 - Rodar as migrations:
```javascript
python manage.py migrate
```

7 - Popular banco com dados iniciais:
```javascript
python manage.py seed
```

8 - Iniciar servidor:
```javascript
python manage.py runserver
```

9 - Acessar o host:
```javascript
http://127.0.0.1:8000
```

10 - Utilizar o login e senha padrão:
```javascript
email: funcionario@teste.com
senha: 123456
```

## 🧪 Como rodar os testes unitários:

1 - Rodar os testes:
```javascript
coverage run --source='.' manage.py test
```

2 - Gerar relatório HTML:
```javascript
coverage html
```

3 - Abrir arquivo htmlcov/index.html para conferir a % de cobertura:
```javascript
Sales-System-Semeq\htmlcov\index.html
```

## 💻 Como utilizar o sistema:

✔ Criar uma Venda
* Acesse Nova Venda
* Busque um cliente
* Informe o CEP e o Numero de entrega (Consulta pelo ViaCEP)
* Busque um produto
* Adicione ao carrinho
* Selecione a forma de pagamento
* Finalize a venda

✔ Verificar o histórico
* Acesse histórico de vendas
* Verifique as vendas concluídas

## 👨‍💻 Autor

Projeto desenvolvido por Guilherme Henrique Cordeiro Padilia.

