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
    git clone https://github.com/Mateush01silva/QRCODE_PROJECT.git
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

  ## Exemplo de aplicação

Você pode integrar a API com VBA para gerar QR Codes diretamente de uma aplicação Excel, por exemplo:

    ```sh
Sub print_cartao()
    Dim URL As String
    Dim Texto As String
    Dim URL2 As String
    Dim Texto2 As String
''''''''''''''''''''''''''''''''''''''''''
    Application.EnableEvents = False
    Application.ScreenUpdating = False
Sheets("Reprint").Visible = True
Sheets("Reprint").Activate
    Texto = Planilha23.Range("B1").Text
    URL = "http://192.168.2.100:8000/qrapp/generate_qr?data=" & Texto
    'URL = "https://chart.googleapis.com/chart?chs=95x95&cht=qr&chl=" & Texto

    On Error Resume Next
    Planilha23.Pictures("QRCode").Delete
    Range("A9").Select
    Planilha23.Range("A9").Select
    Planilha23.Pictures.Insert(URL).Select
    With Selection
        .Name = "QRCode"
        .Top = .TopLeftCell.Top + 10
        .Left = .TopLeftCell.Left + 10
        .Width = 70
    End With
    
    Texto2 = Planilha23.Range("E2").Text
    URL2 = "http://192.168.2.100:8000/qrapp/generate_qr?data=" & Texto2

    On Error Resume Next
    Planilha23.Pictures("QRCode2").Delete
    Range("A9").Select
    Planilha23.Range("A9").Select
    Planilha23.Pictures.Insert(URL2).Select
    With Selection
        .Name = "QRCode2"
        .Top = .TopLeftCell.Top - 189
        .Left = .TopLeftCell.Left + 10
        .Width = 50
    End With
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Application.ScreenUpdating = False
    Application.EnableEvents = False
    Sheets("Reprint").Select
    Range("A4:B12").Select
    Selection.PrintOut Copies:=1, Collate:=True
    Application.CutCopyMode = False
    Sheets("Comparador").Select
Sheets("Reprint").Visible = False
    Application.EnableEvents = True
    Application.ScreenUpdating = True
End Sub
    ```