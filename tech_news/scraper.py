import requests
import time
import parsel
from .database import create_news
# target page(https://blog.betrybe.com)


def fetch(url):
    print("url= ", url)
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
    link = selector.css("a.next-link ::attr(href)").get()
    if link != "":
        return link
    else:
        return None


# Requisito 4
def scrape_noticia(html_content):
    selector = parsel.Selector(html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1::text").get()
    timestamp = selector.css(".meta-date::text").get()
    writer = selector.css(".author > a::text").get()
    comments_count = 0
    summary = selector.css("div.entry-content > p:first-of-type *::text"
                           ).getall()
    tags = selector.css(".post-tags a::text").getall()
    category = selector.css("a > span.label::text").get()

    summary_formatted = "".join(summary).strip()
    title_formatted = "".join(title).strip()

    result = {
        "url": url,
        "title": title_formatted,
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count,
        "summary": summary_formatted,
        "tags": tags,
        "category": category,
    }
    return result


# Requisito 5
def get_tech_news(amount):
    if amount is None:
        return None
    news_list = []
    page = fetch("https://blog.betrybe.com/")

    news_links_list = scrape_novidades(page)

    # obter uma lista de noticias do tamanho de amount
    while len(news_links_list) < amount:
        next_link = scrape_next_page_link(page)
        current_page = fetch(next_link)
        scrapped_news = scrape_novidades(current_page)
        news_links_list.extend(scrapped_news)

    news_links_list = news_links_list[:amount]

    # buscar as paginas da lista

    for new_link in news_links_list:
        current_page = fetch(new_link)
        scrapped_new = scrape_noticia(current_page)

        news_list.append(scrapped_new)

    create_news(news_list)

    return news_list
