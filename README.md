# worc

Projeto feito para a reoslução do desafio técnico da Worc.

## Como executar a aplicação

Caso você tenha o docker instalado, basta executar o seguinte comando:
`docker-compose up -d --build`

Se não tiver o docker, nem o docker compose, tem que instalar na mão. Para isso, siga os seguintes passos:

- Baixe o Python, de preferência a versão 3.8 ou mais recente.
- Clonar o projeto: `git clone git@github.com:gabrielloliveira/worc.git`
- Entrar no diretório do projeto: `cd worc`
- Criar o virtualenv: `python -m venv env`
- Ativar o virtualenv: `source env/bin/activate`
- Instalar as dependências do projeto: `pip install -r requirements.txt`
- Rodar o setup inicial com as variáveis de ambiente: `python contrib/generate_env.py`
- Criar o banco de dados: `python manage.py migrate`
- Rodar o servidor: `python manage.py runserver`

## Estrutura dos arquivos/pacotes

- O projeto se chama `worc` e está localizado na pasta raiz do projeto.
- Dentro da pasta worc, eu tenho uma python package chamado `apps`. Nesta pasta, eu tenho todas as minhas apps 
que usarei no projeto (só precisei de uma, mas poderia ter mais, dependendo do projeto).

![Estrutura do projeto](prints/tree.png "Estrutura do projeto")

- A pasta `contrib` situada na raiz do projeto serve para fazer o "setup" do projeto. Nela,
coloquei um script que irá gerar um arquivo com as variáveis de ambiente "padrões" para o projeto.

Para esta aplicação, devido ao objetivo do teste, que era o CRUD de 1 tabela, eu optei por criar somente uma 
app chamada core.

Se o problema descrito pedisse para criar outras entidades, como um gestor ou empresas, provavelmente eu teria optado
por criar outras apps (users e companies, por exemplo).

## Explicando as decisões de design adotadas para a solução do desafio e organização do projeto

** Disclaimer: Todas as decisões sempre são tomadas pensando no futuro da aplicação, quem irá dar manutenção e 
se terá muita gente no time. Para ser mais direto, sempre tento programar de uma forma que possibilite um estagiário 
ou um júnior colocar a mão na massa logo no primeiro dia.

As variáveis de ambiente são informações sensíveis. Gosto de gerenciá-las através do python-decouple.
Isso seria o ideal, pois, ao meu ver, torna mais fácil de manter o projeto. Se esse projeto
fosse ao ar, através de um heroku, tudo o que eu precisaria fazer seria substituir as variáveis de ambiente via painel
ou servidor, caso fosse uma VPS.

No entanto, muita gente adota o padrão de ter uma package settings. Dentro de settings, elas separam entre base.py, 
local.py e prod.py, por exemplo. Esse projeto não justifica essa abordagem. Então, preferi manter simples.

![Estrutura do projeto](prints/settings.png "Estrutura do projeto")

Da mesma forma que pode ser feito uma separação de settings, podeira também ser feito com o requirements.txt, separando
em dependencias de desenvolvimento, como o django-debug-toolbar, e de produção, como o gunicorn, sentry, etc.

Pra poder gerenciar isso tudo, muita gente utiliza o pipenv, embore eu ache que o poetry seja melhor. No entanto, 
mesmo assim, prefiro deixar tudo em um arquivo requirements.txt. Make it simple.

Os frontends precisam saber de tudo da API, de forma minunciosa. Por isso, adotei o swagger como documentação da API. 
Gerei a documentação utilizando a lib `drf-yasg`.

![Swagger](prints/swagger.png "Swagger")

Os endpoints da aplicação são feitos através das GenericsAPIView do Django Rest. É um meio termo entre as 
APIViews e ModelViewSet. Acredito ser mais fácil de entender e manter, pensando em manutenções futuras e novas 
pessoas entrando no projeto.

Fiz testes automatizados utilizando o pyest, que, na minha opinião, é a melhor ferramente que tem para testar.
Aproveitando isso, tomei a liberdade de configurar uma action de CI aqui no github. Toda vez que eh feito um pull
request para a branch main (a branch principal), o CI executa os testes automatizados.

Eu gosto sempre de criar uma pasta de testes para cada app. Nela, posso organizar em testes de models, de views, 
de signals, etc.

Caso eu tivesse mais de um model, eu teria, por exemplo, um arquivo de `test_model_modelname.py`

![Tests](prints/tests.png "Tests")

No problema do desafio, foi pedido para que pudesse ser possível pesquisar um candidato por algum campo específico.
Então, utilizei uma solução pronta, que é o django-filter. Através dele, posso setar o atributo filterset_class 
nos endpoints que quero e passar a classe que irá fazer o filtro. Essa abordagem é interessante, pois desacopla os 
filtros da lógica de view. (é muito comum ter vários filtros personalizados e isso impactando na quantidade de 
linhas do método get_queryset())

![Filtersets](prints/filtersets.png "Filtersets")

## Descreva sua API REST de forma simplificada.

Minha API REST possui 2 endpoints:
`{URL_BASE}/api/candidates/` e `{URL_BASE}/api/candidates/{id}/`.

Como padrão do REST, o primeiro endpoint aceita os métodos GET e POST, como listagem e 
criação de candidatos, respectivamente.

O segundo endpoint aceita os métodos GET, PUT, PATCH e DELETE, como listagem, edição, edição parcial e exclusão de um 
candidato, respectivamente.
