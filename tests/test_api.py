from src.api_hh import HhApi


def test_hh_api_structure():
    api = HhApi()
    assert hasattr(api, "get_vacancies")
