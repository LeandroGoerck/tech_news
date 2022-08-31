import tech_news.database as db
import datetime as dt


# Requisito 6
def search_by_title(title):
    mongoData = db.search_news({"title": {"$regex": title, "$options": "i"}})
    list = []
    for item in mongoData:
        list.append((item["title"], item["url"]))
    return list


# Requisito 7
def search_by_date(date):
    # date received "2021-04-04"
    # ISO Date: 2021-04-04T00:00:00.000000

    try:
        mydate = dt.date.fromisoformat(date).strftime("%d/%m/%Y")
        mongoData = db.search_news({"timestamp": mydate})

        list = []
        for item in mongoData:
            list.append((item["title"], item["url"]))

        return list
    except ValueError:
        raise ValueError("Data inválida")


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""
    print(tag)
    mongoData = db.search_news({"tags": {"$regex": tag, "$options": "i"}})
    list = []
    for item in mongoData:
        list.append((item["title"], item["url"]))
    return list


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
