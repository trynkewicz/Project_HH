from src.utils import filter_by_keywords, top_by_salary
from src.vacancy import Vacancy


def test_filter_by_keywords():
    v1 = Vacancy("Python Dev", "u1", 100, 200, "Работа с Python")
    v2 = Vacancy("Java Dev", "u2", 100, 200, "Java backend")

    filtered = filter_by_keywords([v1, v2], ["python"])
    assert len(filtered) == 1
    assert filtered[0].title == "Python Dev"


def test_top_by_salary():
    v1 = Vacancy("Low", "u1", 100, 200, "")
    v2 = Vacancy("High", "u2", 300, 500, "")

    top = top_by_salary([v1, v2], 1)
    assert top[0].title == "High"
