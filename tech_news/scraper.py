import requests
import time
import parsel
# target page(https://blog.betrybe.com)


def fetch(url):
    headers = {"user-agent": "Fake user-agent"}
    timeout = 3
    try:
        response = requests.get(url, headers=headers, timeout=timeout)
        time.sleep(1)
        response.raise_for_status()
    except (requests.exceptions.HTTPError, requests.ReadTimeout):
        return None
    else:
        if response.status_code == 200:
            return response.text
        else:
            return None


def scrape_novidades(html_content):
    selector = parsel.Selector(html_content)
    links = []
    for article in selector.css("article a.cs-overlay-link"):
        href = article.css("::attr(href)").get()
        links.append(href)
    return links


# Requisito 3
def scrape_next_page_link(html_content):
    selector = parsel.Selector(html_content)
    link = selector.css("a.next ::attr(href)").get()
    if link != "":
        return link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
