from src.vacancy import Vacancy


def convert_dicts_to_objects(vac_list):
    """Упрощённый конвертер из JSON в объекты Vacancy."""
    result = []
    for v in vac_list:
        obj = Vacancy(
            title=v["title"],
            url=v["url"],
            salary_from=v["salary_from"],
            salary_to=v["salary_to"],
            description=v["description"]
        )
        result.append(obj)
    return result


def filter_by_keywords(vacancies: list, words: list) -> list:
    words = [w.lower() for w in words]

    result = []
    for vac in vacancies:
        text_title = (vac.title or "").lower()
        text_description = (vac.description or "").lower()

        if any(word in text_title or word in text_description for word in words):
            result.append(vac)

    return result



def top_by_salary(vacancies, n):
    return sorted(vacancies, reverse=True)[:n]
