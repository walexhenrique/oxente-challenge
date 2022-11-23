# Projeto MoraAQUI

Um projeto de divulgação de alugueis, onde o usuário pode encontrar casas para morar e também divulgar seus alugueis!

***

## Serviços usados
- Github


## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

<ul>
    <li>Versão do python utilizada: 3.10.7</li>
    <li>Versão do django: 4.1.2</li>
</ul>


#### 1 - Passo: Clone
Realize um clone do projeto em seu computador

```
git clone https://github.com/walexhenrique/oxente-challenge.git
```

#### 2 - Passo: Ambiente virtual
Crie um ambiente virtual na pasta <b>raiz</b> do projeto. No seu terminal use:

Comando para a criação do ambiente virtual no Windows:
```
python -m venv venv
```

Comando para a criação do ambiente virtual no Linux:
```
python3 -m venv venv
```

#### 3 - Passo: Ativação do ambiente virtual
Agora você precisa ativar o ambiente virtual para a posterior instalação das dependências do projeto.

Na pasta raiz do projeto, onde você criou o seu ambiente virtual anteriormente. Use:

Comando para a ativação do ambiente virtual no Windows:
```
.\venv\Scripts\activate
```

Comando para a ativação do ambiente virtual no Linux:
```
source venv/bin/activate
```
Se tudo estiver ocorrido bem, terá (venv) em seu <b>terminal!</b>

#### 4 - Passo: Instalação de depedências
É preciso instalar as depedências do projeto para o funcionamento correto. Com o seu ambiente virtual <b>ativo</b> use o comando no seu terminal:

```
pip install -r requirements.txt
```

#### 5 - Passo: Variáveis de ambiente
Para a correta execução do projeto é necessário a configuração das variáveis de ambiente.

* Renomeie o arquivo .env-example para .env

Dentro do arquivo .env (já renomeado), coloque sua PRIMARY KEY do projeto.
```
# /.env

# Django secret key
SECRET_KEY = 'COLOQUE SUA SECRET-KEY AQUI'
```

#### 6 - Passo: Realize as migrações
Para o correto funcionamento do projeto é preciso que seja feito as migrações do banco de dados.

No seu terminal digite:
Windows:
```
python manage.py migrate
```

Linux:
```
python3 manage.py migrate
```

#### 7 - Passo: Executar o projeto
Comando para a execução do projeto no windows:

```
python manage.py runserver
```

Comando para a execução do projeto no linux:

```
python3 manage.py runserver
```

## 🛠️ Construído com

Tecnologias utilizadas na criação desse projeto

* [Django Framework](https://www.djangoproject.com/) - O framework web usado na criação do projeto
* [Bootstrap](https://getbootstrap.com/) - Utilizado para estilização da página
* [Jquery](https://jquery.com/) - Utilizado para algumas funcionalidades do JS
* [HTML](https://developer.mozilla.org/pt-BR/docs/Web/HTML) - Estruturação da página
* [CSS](https://developer.mozilla.org/pt-BR/docs/Web/CSS) - Estilização da página
* [Bing Maps](https://www.bing.com/maps/) - Api utilizada para encontrar a localização aproximada


## Como usar

### 1 - Quando entrar no site, você vai se deparar com a tela de listagem de alugueis (Estará vazio no seu até adicionar eles).
![pagina inicial](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginainicial.png)

### 2 - Ao colocar nos filtros o bairro "aldeia" e o preço máximo de "120" reais, pude filtrar e receber esse resultado.
![pagina inicial com filtro](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginainicialbusca.png)

### 3 - Ao visualizar um anúncio, você terá todas as informações necessárias, inclusive a localização aproximada.
![pagina aluguel informações](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginadetail.png)

### 4 - Caso você queira criar um anúncio, crie uma conta.
![pagina de registro de usuário](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginaregister.png)

### 5 - Após a conclusão da criação da conta, faça login.
![pagina login de usuário](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginalogin.png)

### 6 - Ao entrar pela primeira vez, você se deparará com essa tela, onde você tem a opção de criar um anúncio.
![pagina dashboard vazia](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginadashboard.png)

### 7 - Aqui onde você pode criar o seu anúncio de casa para aluguel.
![pagina criar aluguel](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginacreate.png)

### 8 - Pronto, finalizamos a criação, a sua dashboard já mudou também
![pagina dashboard com o aluguel](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginadashboardcomaluguel.png)

### 9 - Você pode excluir caso queira refazer o anúncio com outras imagens
![pagina aluguel apagado](https://github.com/walexhenrique/oxente-challenge/blob/main/.github/paginaapagar.png)

## Funcionalidades

As principais funcionalidades da aplicação são:
- Criação de anúncios de alugueis
- Localização da casa a partir do endereço fornecido
- Apagar, editar os anúncios
- Registro de usuário
- Login de usuário
- Busca por alugueis com auxílio de filtros

## Links
- Repositório: https://github.com/walexhenrique/oxente-challenge
    - Em caso de encontrar bugs ou alguma sugestão entre em contato com o meu email: walex999067@gmail.com

## Versionamento
1.0.0.0

## Autor
- **Walex Henrique**
Obrigado pela visita, se curtiu me siga no Github!

