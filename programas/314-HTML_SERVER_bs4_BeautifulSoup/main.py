import re

import requests
from bs4 import BeautifulSoup

# Web Scraping com Python usando requests e bs4 BeautifulSoup
# - Web Scraping é o ato de "raspar a web" buscando informações de forma
# automatizada, com determinada linguagem de programação, para uso posterior.
# - O módulo requests consegue carregar dados da Internet para dentro do seu
# código. Já o bs4.BeautifulSoup é responsável por interpretar os dados HTML
# em formato de objetos Python para facilitar a vida do desenvolvedor.
# - Doc: https://www.crummy.com/software/BeautifulSoup/bs4/doc.ptbr/
# + Instalação
# - pip install requests types-requests bs4


url = 'http://127.0.0.1:3333/'
response = requests.get(url)
bytes_html = response.content
# converter o html em objetos python
parsed_html = BeautifulSoup(bytes_html, 'html.parser', from_encoding='utf-8')

# if parsed_html.title is not None:
#     print(parsed_html.title.text)

top_jobs_heading = parsed_html.select_one('#intro > div > div > article > h2')

if top_jobs_heading is not None:
    print(top_jobs_heading.text)

    article = top_jobs_heading.parent  # o lemento acima dele o patent

    print('===========================================================')
    print(article)
    print('===========================================================')

    if article is not None:
        for p in article.select('p'):
            print(p.text)
            print(re.sub(r'\s{1,}', ' ', p.text).strip())

    print('===========================================================')
    # tirando os espaços em branco
    if article is not None:
        for p in article.select('p'):
            print(re.sub(r'\s{1,}', ' ', p.text).strip())
            # expreções regulares: substituir todo os
            # espaços "\s" que for maior que 1 espaço{1,}
            # por ' '(um espaço)
