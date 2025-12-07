class Vacancy:
    """Класс вакансии с самыми важными атрибутами.
    Здесь же делаем сравнение по зарплате.
    """

    __slots__ = ("title", "url", "salary_from", "salary_to", "description")

    def __init__(self, title, url, salary_from, salary_to, description):
        self.title = title
        self.url = url
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.description = description

    # ----- Приватная валидация зарплаты -----
    def _validate_salary(self, value):
        if value is None:
            return 0
        return int(value)

    # ----- Метод средней зарплаты -----
    def average_salary(self):
        if self.salary_from and self.salary_to:
            return (self.salary_from + self.salary_to) // 2
        return self.salary_from or self.salary_to or 0

    # ----- Сравнение через магические методы -----
    def __lt__(self, other):
        return self.average_salary() < other.average_salary()

    def __repr__(self):
        return f"{self.title} ({self.average_salary()} руб.)"

    # Конвертер из словаря HH в объект Vacancy
    @classmethod
    def from_hh(cls, item):
        salary = item.get("salary") or {}
        return cls(
            title=item.get("name"),
            url=item.get("alternate_url"),
            salary_from=salary.get("from"),
            salary_to=salary.get("to"),
            description=item.get("snippet", {}).get("responsibility", "")
        )
