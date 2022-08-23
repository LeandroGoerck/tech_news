import requests
import time

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


# Requisito 2
def scrape_novidades(html_content):
    """Seu código deve vir aqui"""


# Requisito 3
def scrape_next_page_link(html_content):
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
