# Teste Técnico Back-End

## Sobre o desafio

Você recebeu um arquivo CNAB com os dados das movimentações financeiras de várias lojas. Precisamos criar uma maneira para que estes dados sejam importados para um banco de dados.

Sua tarefa é criar uma interface web que aceite upload do arquivo CNAB, normalize os dados e armazene-os em um banco de dados relacional e exiba essas informações em tela.

## ✔️ Tecnologias utilizadas
- Python
- Django
- SQLite3

# 🛠️ Abrir e rodar o projeto

### Crie seu ambiente virtual:
```bash 
    python -m venv venv
```

### Ative seu venv:
```bash
 Linux:
source venv/bin/activate

 Windows:
.\venv\Scripts\activate
```

### Atualize o pip
```bash
    pip install --upgrade pip
```

### Instale as dependências
```bash
    pip install -r requirements.txt
```
### Execute as migrações
```bash
    python manage.py migrate
```
### Inicie a aplicação
```bash
    python manage.py runserver
```
### Abra http://127.0.0.1:8000/ para visualizá-lo no navegador.
```bash
    Para parar a execução precione Ctrl + c
```