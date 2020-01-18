
# Movies Application

<h3>SOBRE O DESENVOLVIMENTO<h3>

A API foi desenvolvida com :

* Python 3.7
* Django 2.2.7
* Postgres 11
* Pandas/SqlAlchemy
* Angular/Typescript/Angular Material
* Docker
* Docker Compose


- Python/Django/Postgres
        Já trabalho há algum tempo com python, django e postgres, pela produtividade que essas tecnologias oferecem optei por elas. O django se mostra bastante produtivo na criação de api restfull.
        No decorrer do projeto, percebi que além disso Python foi uma boa escolha por possuir o *Pandas* e facilitar esse tratamento e inserção de grande quantidade de dados.
  
  - Pandas/SqlAlchemy
  
      A performance e facilidade de trabalhar com as libs me fizeram optar por elas, foi um novo conhecimento adquirido que apreciei bastante.
  
  - Angular/Typescript/Angular Material
  
      Optei pela produtividade, assim como o django e python. 
  
  - Docker

      Preferi reduzir o caminho para executar a aplicação quando fosse testada, também foi um aprendizado gratificante.


<h3>BUILD DA API<h3>


Ferramentas necessárias para build:
* Docker
* Docker Compose

<h3>Executando API:<h3>


Após fazer as instalações necessárias faça os seguintes passos via terminal:
* Navegar até o diretório /composes_movie
* Executar o comando: docker-compose up
* O docker irá fazer download das images com a versão mais atual da API. 
* Quando o download  for concluído a api irá executar.
* Após a inicialização da aplicação pelo terminal linux, quando estiver executando pela primeira vez recomendo aguardar 3 minutos para poder as informações dos arquivos serem importadas através do migrations do banco *

<h3>Teste API:<h3>

Não é necessário autenticação na API. 
O Django tem uma interface que pode ser usado para teste diretamento do browser.

Para testar basta acessar a url:

    http://127.0.0.1:8000/api/titles/


Ao acessar a url acima o sistema exibe as rotas disponíveis com auxílio da interface do DJANGO.

    "title": "http://127.0.0.1:8000/api/titles/title/",
    "person": "http://127.0.0.1:8000/api/titles/person/"


<h3>Listar<h3>

Método `GET`:
    
    http://127.0.0.1:8000/api/titles/title/?limit=10&offset=0

Response:

Exemplo de resultado:
json
[
    {
      "tconst": "tt1326929",
      "titleType": "movie",
      "primaryTitle": "?",
      "originalTitle": "?",
      "isAdult": false,
      "startYear": 2008,
      "endYear": 0,
      "runtimeMinutes": 0,
      "genres": "Mystery,Thriller",
      "averageRating": 6.3,
      "numVotes": 7
    }
]


*Filtrar Títulos*

Por start year

Método `GET`
 
    http://127.0.0.1:8001/api/titles/title/?limit=10&offset=0&startYear=2019
    
* A api retorna a lista de todos os titles por ano.
