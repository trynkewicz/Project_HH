from src.vacancy import Vacancy


def test_average_salary():
    v = Vacancy("Dev", "url", 100, 200, "")
    assert v.average_salary() == 150


def test_average_salary_one_side():
    v = Vacancy("Dev", "url", 0, 200, "")
    assert v.average_salary() == 200


def test_compare_vacancies():
    v1 = Vacancy("Dev1", "url1", 100, 200, "")
    v2 = Vacancy("Dev2", "url2", 300, 400, "")
    assert v1 < v2
