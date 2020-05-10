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
No site ''IMDb'' fora inserido um ''for'' no ''div#main>h4'' para que fosse possivel obter as datas dentro da tag ''h4'' e também os títulos
obtidos a partir dos textos dentro da tag ''a''.
~~~~
<div id="main">
                <h4>10 July 2020</h4>
                <ul>
                        <li>
                                <a href="/title/tt10327252/?ref_=rlm">The Forever Purge</a> (2020)
                        </li>
                </ul>
                <h4>17 July 2020</h4>
                <ul>
                        <li>
                                <a href="/title/tt6723592/?ref_=rlm">Tenet</a> (2020)
                        </li>
                </ul>
</div>
~~~~
Já no site ''techtudo'' fora inserido um ''for'' dentro da ''div-feed-post-body'' juntamente com a classe ''feed-post-body'',
os titulos foram buscados a partir da tag ''a.feed-post-link'' onde os textos dentro da tag eram obtidos, o resumo foi buscado
atraves da tag ''span.feed-post-datetime, a seção a partir da tag ''span.feed-post-metadata-section''.
Por fim no site ''technoblog'' fora inserido um for na tag ''article.bloco'', onde os titulos das noticias eram buscados a partir da
tag ''h2 a'' e data e o autor a partir da tag ''div.info''.
~~~~
<div class="feed-post-body"><div class="feed-post-header"></div><div class="feed-post-body-title gui-color-primary gui-color-hover "><div class="_s"><div class="_b"><a href="https://www.techtudo.com.br/noticias/2020/05/feliz-dia-das-maes-2020-doodle-permite-criar-cartao-com-mensagem.ghtml" class="feed-post-link gui-color-primary gui-color-hover">'Feliz Dia das Mães 2020': Doodle permite criar cartão com mensagem</a></div></div></div><div class="feed-post-body-resumo"><div class="_s">Mensagens podem ser enviadas para as mães, esposas, sogras, irmãs e amigas; veja como</div></div><div class="feed-media-wrapper"><div class="_s"><a href="https://www.techtudo.com.br/noticias/2020/05/feliz-dia-das-maes-2020-doodle-permite-criar-cartao-com-mensagem.ghtml" class="feed-post-figure-link gui-image-hover"><div class="bstn-fd-item-cover bstn-fd-video-cover" data-video-id="4358782" data-short-url="https://www.techtudo.com.br/noticias/2020/05/feliz-dia-das-maes-2020-doodle-permite-criar-cartao-com-mensagem.ghtml" data-link="https://www.techtudo.com.br/noticias/2020/05/feliz-dia-das-maes-2020-doodle-permite-criar-cartao-com-mensagem.ghtml" data-program-title="Downloads" data-title="'Feliz Dia das Mães 2020': Doodle permite criar cartão com mensagem"><picture class="bstn-fd-cover-picture"><img class="bstn-fd-picture-image" srcset="https://s2.glbimg.com/W-BKAISj749V80X3Hpuy-nJ9jNg=/540x304/top/smart/filters:max_age(3600)/https://s01.video.glbimg.com/deo/vi/82/87/4358782 1x,https://s2.glbimg.com/fbcqj1agnPzaaI90-rrXf87L8q0=/810x456/top/smart/filters:max_age(3600)/https://s01.video.glbimg.com/deo/vi/82/87/4358782 1.5x,https://s2.glbimg.com/ogA4ioP-X4cRdgnWROwUor5Gv0o=/1080x608/top/smart/filters:max_age(3600)/https://s01.video.glbimg.com/deo/vi/82/87/4358782 2x" src="https://s2.glbimg.com/W-BKAISj749V80X3Hpuy-nJ9jNg=/540x304/top/smart/filters:max_age(3600)/https://s01.video.glbimg.com/deo/vi/82/87/4358782"></picture><div class="feed-cover-content"><div class="bstn-fd-play-button"><div class="bstn-fd-video-play"><svg class="bstn-fd-play-icon theme-color-primary" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M8 5v14l11-7z"></path></svg></div><p class="feed-post-video-duration">2 min</p></div></div></div></a></div></div><div class="feed-post-metadata"><span class="feed-post-datetime">Há 9 horas</span><span class="feed-post-metadata-section"> Fique Em Casa </span></div></div>
~~~~

e no Site Tecnoblog fizemos um for na tag "article.bloco" buscando o titulo a data da noticia e o autor responsavel.
~~~~
<article id="post-337908" class="bloco">
<div class="thumb">
<div class="mask"></div>
<a href="https://tecnoblog.net/337908/tb-comunidade-016-robo-aspirador-nokia-auxilio-emergencial-e-mais/" rel="nofollow"><img loading="lazy" src="/wp-content/uploads/2020/01/tb-comunidade-melhores-semana-340x191.png" alt="" style="width:340px;height:191px;" data-lazy-src="/wp-content/uploads/2020/01/tb-comunidade-melhores-semana-340x191.png" class="lazyloaded" data-was-processed="true"><noscript><img loading="lazy" src="/wp-content/uploads/2020/01/tb-comunidade-melhores-semana-340x191.png" alt="" style="width:340px;height:191px;" /></noscript></a>
<div class="spread news">
<a href="/editoria/news" class="cat catname " rel="nofollow">News</a>
</div>
</div>
<div class="texts">
<h2><a href="https://tecnoblog.net/337908/tb-comunidade-016-robo-aspirador-nokia-auxilio-emergencial-e-mais/">TB Comunidade #016: robô aspirador, Nokia, Auxílio Emergencial e mais</a></h2>
<div class="info">
<time class="tb-entry-date" datetime="2020-05-08">08/05</time> às 18h58 por <a href="https://tecnoblog.net/author/lucaslima/" title="Posts by Lucas Lima" rel="author">Lucas Lima</a> </div>
<div class="entry">
<p>Sente falta de rádio FM no celular? E quanto o LED para indicar que tem notificação nova? Funções que foram deixadas de lado em smartphones, este é um dos destaques da Comunidade do Tecnoblog dessa semana. Entre outros assuntos, os membros também debateram sobre robô aspirador, a volta da Nokia, bancos digitais e o novo jogo de corrida da Microsoft para mobile.
Conheça a nova comunidade do Tecnoblog
</p> </div>
</div>
</article>
~~~~