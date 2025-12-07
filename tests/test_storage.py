import os
from src.json_storage import JsonStorage
from src.vacancy import Vacancy


def test_json_storage_add_and_get(tmp_path):
    file = tmp_path / "vacancies.json"
    storage = JsonStorage(filename=file)

    v = Vacancy("Dev", "url", 100, 200, "desc")
    storage.add(v)

    data = storage.get_all()
    assert len(data) == 1
    assert data[0]["title"] == "Dev"


def test_json_storage_delete(tmp_path):
    file = tmp_path / "vacancies.json"
    storage = JsonStorage(filename=file)

    v = Vacancy("Dev", "url", 100, 200, "desc")
    storage.add(v)
    storage.delete("url")

    assert storage.get_all() == []
