import json
from pathlib import Path
from src.storage_base import StorageBase


class JsonStorage(StorageBase):

    def __init__(self, filename="data/vacancies.json"):
        self.filename = Path(filename)
        self.filename.parent.mkdir(exist_ok=True)

        if not self.filename.exists():
            self._save([])

    def _load(self):
        with open(self.filename, "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    def _save(self, data):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)

    def add(self, vacancy):
        data = self._load()

        # Не добавляем дубликаты по ссылке
        if vacancy.url not in [item["url"] for item in data]:
            data.append({
                "title": vacancy.title,
                "url": vacancy.url,
                "salary_from": vacancy.salary_from,
                "salary_to": vacancy.salary_to,
                "description": vacancy.description
            })

        self._save(data)

    def get_all(self):
        return self._load()

    def delete(self, url):
        data = self._load()
        new_data = [vac for vac in data if vac["url"] != url]
        self._save(new_data)
