from bs4 import BeautifulSoup
def parse_hh_vacancies(html):
    soup = BeautifulSoup(html, "html.parser")
    vacancies = []
    cards = soup.select(
        "[data-qa='vacancy-serp__vacancy']"
    )
    for card in cards:
        title_element = card.select_one(
            "[data-qa='serp-item__title']"
        )
        if not title_element:
            continue
        title = title_element.get_text(" ", strip=True)
        link = title_element.get("href")
        vacancies.append({"title": title, "url": link})
    return vacancies
