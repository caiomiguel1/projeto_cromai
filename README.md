## Introdução
Esta documentação descreve a estrutura e funcionamento da minha aplicação Flask. A aplicação é um monitor de recursos que exibe o uso de CPU, RAM e disco, além de armazenar esses dados em um banco de dados SQLite.

## Requisitos
Para executar esta aplicação, você precisará ter os seguintes requisitos instalados:

- Python 3.x
- As bibliotecas listadas no arquivo `requirements.txt`
- SQLite (já incluído na biblioteca padrão do Python)

### Instalação de Requisitos
Você pode instalar todas as bibliotecas necessárias usando o comando:

```bash
pip install -r requirements.txt
```

O arquivo `requirements.txt` contém uma lista das bibliotecas e suas versões exatas.

## Estrutura de Arquivos
```
projeto_cromai/
    ├── hello.py
    ├── templates/
    │   ├── index.html
    ├── dados_mainframe.db
    ├── requirements.txt
    └── README.md
```

- `hello.py`: O arquivo principal da aplicação Flask.
- `templates/`: Diretório que contém os modelos HTML.
- `dados_mainframe.db`: Banco de dados SQLite para armazenar os dados.
- `requirements.txt`: Arquivo que lista as dependências do Python.
- `README.md`: Este arquivo de documentação.

## Configuração
Nenhuma configuração especial é necessária para a nossa aplicação Flask.

## Como Executar
1. Clone o repositório do projeto para o seu computador.
2. Navegue até o diretório `projeto_cromai` no terminal.
3. Execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

4. Execute o seguinte comando para iniciar a aplicação:

```bash
python hello.py
```

A aplicação estará disponível em `http://localhost:5000`.

## Rotas

### Rota Principal
- **URL:** `/`
- **Descrição:** Página inicial da aplicação que exibe o uso de CPU, RAM e disco em tempo real.
- **Método HTTP:** GET
- **Template:** `index.html`

## Banco de Dados
Os dados de uso de CPU, RAM e disco são armazenados em um banco de dados SQLite chamado `dados_mainframe.db`. A tabela `data` é usada para armazenar esses valores.

## Autores
- Caio Darzi - caiodarzi@gmail.com
- 
## Contato
Para obter suporte ou entrar em contato conosco, envie um e-mail para caiodarzi@gmail.com
