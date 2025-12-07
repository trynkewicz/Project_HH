from abc import ABC, abstractmethod


class ApiBase(ABC):
    """Абстрактный класс, который говорит,
    что любой API должен уметь получать вакансии.
    """

    @abstractmethod
    def get_vacancies(self, search_text):
        pass
