import requests
from src.api_base import ApiBase


class HhApi(ApiBase):
    """Простой класс для получения вакансий с HH.ru"""

    def __init__(self):
        self.url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_text):
        """Простой запрос с минимальными параметрами"""

        params = {
            "text": search_text,
            "per_page": 20,
            "area": 113  # Россия
        }

        response = requests.get(self.url, params=params)

        # Проверяем, что сервер ответил нормально
        if response.status_code != 200:
            print("Ошибка при запросе к hh.ru")
            return []

        data = response.json()
        return data.get("items", [])
