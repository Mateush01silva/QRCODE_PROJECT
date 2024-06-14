# QRCODE_PROJECT

## Descrição

O QRCODE_PROJECT é uma aplicação web desenvolvida com o framework Django que permite a geração de QR Codes de maneira simples e eficiente. Este projeto disponibiliza uma API que pode ser acessada por meio de requisições HTTP GET para gerar QR Codes dinamicamente com base nos dados fornecidos pelo usuário. O QR Code gerado é retornado como uma imagem PNG, que pode ser utilizada em diversas aplicações, como automação de processos, geração de etiquetas, marketing e muito mais.

## Funcionalidades

Geração Dinâmica de QR Codes: Gera QR Codes com base nos dados fornecidos na requisição.
API Simples e Intuitiva: A API é acessível por meio de uma URL e aceita parâmetros de dados diretamente na requisição.
Integração Fácil: Pode ser facilmente integrada a outros sistemas e aplicações que necessitem de QR Codes.

## Tecnologias Utilizadas

Django: Framework web de alto nível que facilita o desenvolvimento rápido e com design limpo.
qrcode: Biblioteca Python para geração de QR Codes.
SQLite: Banco de dados leve utilizado durante o desenvolvimento (pode ser substituído por outro banco de dados conforme a necessidade).

## Estrutura do Projeto

QRCODE_PROJECT/
├── manage.py
├── qrapp/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
└── qrcode_project/
├── init.py
├── asgi.py
├── settings.py
├── urls.py
└── wsgi.py


## Requisitos

- Python 3.x
- Django
- qrcode

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/seu-usuario/QRCODE_PROJECT.git
    cd QRCODE_PROJECT
    ```

2. Crie e ative um ambiente virtual:
    ```sh
    python -m venv venv
    source venv/bin/activate  # Para Windows: venv\Scripts\activate
    ```

3. Instale as dependências:
    ```sh
    pip install -r requirements.txt
    ```

4. Configure o banco de dados:
    ```sh
    python manage.py migrate
    ```

5. Inicie o servidor:
    ```sh
    python manage.py runserver 0.0.0.0:8000
    ```

## Uso

Para gerar um QR Code, envie uma requisição GET para o endpoint `/qrapp/generate_qr` com o parâmetro `data`.

Exemplo:

http://192.168.1.100:8000/qrapp/generate_qr?data=SEU_TEXTO


## Estrutura de Pastas e Arquivos

- `manage.py`: Script de utilidade para gerenciar o projeto.
- `qrapp/`: Aplicação principal para gerar QR Codes.
  - `__init__.py`: Marca o diretório como um módulo Python.
  - `admin.py`: Configurações do admin (atualmente vazio).
  - `apps.py`: Configurações da aplicação.
  - `models.py`: Definições de modelos (atualmente vazio).
  - `tests.py`: Definições de testes (atualmente vazio).
  - `urls.py`: Definições de URLs para a aplicação.
  - `views.py`: Lógica das views para gerar QR Codes.
- `qrcode_project/`: Diretório de configurações do projeto Django.
  - `__init__.py`: Marca o diretório como um módulo Python.
  - `asgi.py`: Configurações para ASGI.
  - `settings.py`: Configurações do projeto Django.
  - `urls.py`: URLs raiz do projeto.
  - `wsgi.py`: Configurações para WSGI.


