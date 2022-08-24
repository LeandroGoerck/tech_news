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
    """Seu código deve vir aqui"""
