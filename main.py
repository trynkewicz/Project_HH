from src.api_hh import HhApi
from src.vacancy import Vacancy
from src.json_storage import JsonStorage
from src.utils import convert_dicts_to_objects, filter_by_keywords, top_by_salary


def user_interaction():
    print("=== Поиск вакансий на hh.ru ===")

    search = input("Введите поисковый запрос: ")
    api = HhApi()

    # Получаем вакансии
    items = api.get_vacancies(search)

    # Переводим словари в объекты
    vacancies = [Vacancy.from_hh(i) for i in items]

    # Хранилище
    storage = JsonStorage()

    for v in vacancies:
        storage.add(v)

    print(f"Сохранено {len(vacancies)} вакансий.")

    # Загружаем из файла
    stored = convert_dicts_to_objects(storage.get_all())

    # Фильтрация
    words = input("Ключевые слова: ").split()
    filtered = filter_by_keywords(stored, words)

    # Топ N
    n = int(input("Сколько вывести вакансий: "))
    top = top_by_salary(filtered, n)

    print("\n=== Результаты ===")
    for v in top:
        print(v.title, v.average_salary(), v.url)

    # Удаление
    url_to_delete = input("\nВведите URL для удаления (или Enter): ")
    if url_to_delete:
        storage.delete(url_to_delete)
        print("Удалено (если было найдено).")


if __name__ == "__main__":
    user_interaction()
