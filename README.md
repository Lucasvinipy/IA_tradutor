# Tradutor de Texto com IA

Este é um projeto de tradução de texto utilizando a API do OpenAI GPT-3.5 e a biblioteca LangChain. O objetivo do projeto é criar uma aplicação simples que traduza textos para diferentes idiomas usando IA.

## Funcionalidade

A aplicação recebe um texto fornecido pelo usuário e traduz para o idioma desejado. O modelo de IA utilizado para tradução é o **GPT-3.5** da OpenAI.

## Como Funciona

1. **Entrada de Dados**: O usuário fornece um texto que deseja traduzir.
2. **Processamento com IA**: O texto é enviado para a API do OpenAI GPT-3.5, que processa e traduz para o idioma especificado.
3. **Resposta**: A tradução é devolvida ao usuário.

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal do projeto.
- **FastAPI**: Framework para a criação da API.
- **LangChain**: Framework para a integração com modelos de linguagem e construção de cadeias de processamento.
- **OpenAI GPT-3.5**: Modelo de linguagem utilizado para realizar as traduções.
- **dotenv**: Para gerenciamento de variáveis de ambiente (como a chave da API).
- **uvicorn**: Servidor ASGI para rodar a aplicação FastAPI.

## Como Rodar o Projeto

### Pré-requisitos

- **Python 3.8+**
- **Chave de API da OpenAI**: Você pode obter uma chave de API no [site da OpenAI](https://platform.openai.com/).
- **Instalar dependências**: Execute o seguinte comando para instalar as dependências do projeto:

    ```bash
    pip install -r requirements.txt
    ```

### Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto e adicione a sua chave da API da OpenAI:

