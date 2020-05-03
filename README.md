# web_crawler

## Eckton Junior  - RA: 318212233
## Rodrigo Pires  - RA: 31725642
## Welbert Issack - RA: 31624772



###Descreva o website em que foi feita a coleta de dados:
Foram utilizados 3 websites para fazer a coleta de dados que são eles o IMDb(https://www.imdb.com), que como o próprio nome já diz, é um
site que funciona como um ''banco de dados'' online com informações, avaliações e opiniões proprias sobre filmes, música, cinema, jogos 
de computador/console, comercias e programas de entretenimento(''como, por exemplo talk shows''); o site techtudo(https://www.techtudo.com.br),
que apresenta uma gama de informações, apresentadas através de notícias sobre diversos aspectos relacionados a tecnologia, como por exemplo
falhas de segurança em dispositivos mobiles e notícias em geral, sobre campeonatos de e-sports e por fim o site tecnoblog(https://tecnoblog.net),
que tem uma proposta parecida a do site ''techtudo'' expondo noticias em geral de cuncho tecnologico mas com as opinioes do autores sobre
determinado assunto sendo expostas com mais clareza e nao com um cunho voltado a imparcialidade.



###Liste e descreva os dados que foram coletados:
Do site ''IMDb'' foram coletados as datas e títulos dos lançamentos presentes no site, já no ''techtudo'' e no ''tecnoblog'' 
fora utilizada da ''spider'' para captar, selecionar e transferir noticias do website.

###Descreva a estratégia utilizada para fazer a coleta de dados, ou seja, como foi feita a seleção dos dados na estrutura do documento HTML:
No site ''IMDb'' fora inserido um ''for'' no ''div>#main>h4'' para que fosse possivel obter as datas dentro da tag ''h4'' e também os títulos
obtidos a partir dos textos dentro da tag ''a''.
Já no site ''techtudo'' fora inserido um ''for'' dentro da ''div-feed-post-body'' juntamente com a classe ''feed-post-body'',
os titulos foram buscados a partir da tag ''a.feed-post-link'' onde os textos dentro da tag eram obtidos, o resumo foi buscado
atraves da tag ''span.feed-post-datetime, a seção a partir da tag ''span.feed-post-metadata-section''.
Por fim no site ''technoblog'' fora inserido um for na tag ''article.bloco'', onde os titulos das noticias eram buscados a partir da
tag ''h2 a'' e data e o autor a partir da tag ''div.info''.