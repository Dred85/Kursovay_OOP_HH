import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy1():
    return Vacancy("97223662",
                   "Full stack developer (angular + java)",
                   "https://hh.ru/vacancy/97223662",
                   100000,
                   500000,
                   "Знание Python",
                   "2024-04-17T13:33:10+0300")


@pytest.fixture
def vacancy2():
    return Vacancy("97223663",
                   "Full stack developer (angular + java)",
                   "https://hh.ru/vacancy/97223662",
                   200000,
                   600000,
                   "Знание Python",
                   "2018-04-17T13:33:10+0300")


@pytest.fixture
def vacancy_list():
    return [
        Vacancy(
            "97338839",
            "Senior Python разработчик",
            "https://hh.ru/vacancy/97338839",
            0,
            570000,
            "Опыт разработки на <highlighttext>Java</highlighttext> не менее 3 лет. ",
            "2020-04-18T15:03:00+0300"
        ),
        Vacancy(
            "98209966",
            "Программист-разработчик",
            "https://hh.ru/vacancy/98209966",
            200000,
            500000,
            "Программирование: Python, Go",
            "2024-05-02T09:49:03+0300"
        ),
        Vacancy(
            "98196422",
            "java",
            "https://hh.ru/vacancy/98196422",
            800,
            1200,
            "Знание модульности javascript",
            "2023-05-02T06:31:04+0300"
        )]


def test_init(vacancy1):
    """Тестирую конструктор класса дандер метод __init__"""
    assert vacancy1.id == "97223662"
    assert vacancy1.name == "Full stack developer (angular + java)"
    assert vacancy1.link_to_vacancy == "https://hh.ru/vacancy/97223662"
    assert vacancy1.salary_from == 100000
    assert vacancy1.salary_to == 500000
    assert vacancy1.requirements == "Знание Python"
    assert vacancy1.published_at == "2024-04-17T13:33:10+0300"


def test_str(vacancy1):
    """Тестирую переопределенный дандер метод __str__"""
    assert vacancy1.__str__() == '''ID: 97223662
    Наименование вакансии: Full stack developer (angular + java)
    Ссылка: https://hh.ru/vacancy/97223662
    Зарплата от 100000 до 500000
    Требования: Знание Python
Дата публикации: 2024-04-17T13:33:10+0300
'''


def test_repr(vacancy1):
    """Тестирую переопределенный дандер метод __repr__"""
    assert vacancy1.__repr__() == '''Vacancy(97223662, Full stack developer (angular + java), https://hh.ru/vacancy/97223662, 100000 - 500000, Знание Python, 2024-04-17T13:33:10+0300)'''


def test_lt(vacancy1, vacancy2):
    """Тестирую переопределенный дандер метод __lt__ c двумя экземплярами класса"""
    assert vacancy1 < vacancy2


def test_lt_int(vacancy1):
    """Тестирую переопределенный дандер метод __lt__ с числом"""
    assert (vacancy1 < 10) == False


def test_lt_raise(vacancy1):
    """Тестирую переопределенный дандер метод __lt__ со строкой(д.б. исключение TypeError)"""
    with pytest.raises(TypeError) as e_info:
        vacancy1 < '10'


def test_to_json(vacancy1):
    assert vacancy1.to_json() == {'ID': '97223662',
                                  'name': 'Full stack developer (angular + java)',
                                  'link_to_vacancy': 'https://hh.ru/vacancy/97223662',
                                  'salary_from': 100000,
                                  'salary_to': 500000,
                                  'requirements': 'Знание Python',
                                  'published_at': '2024-04-17T13:33:10+0300'}


def test_get_info_json_date(vacancy_list):
    assert [v.published_at for v in Vacancy.get_info_json_date(vacancy_list)] == ["2024-05-02T09:49:03+0300",
                                                                                  "2023-05-02T06:31:04+0300",
                                                                                  "2020-04-18T15:03:00+0300"]


def test_get_info_json_name(vacancy_list):
    assert [v.name for v in Vacancy.get_info_json_name(vacancy_list, 'java')] == ["java"]


def test_get_info_json_requirements(vacancy_list):
    assert [v.requirements for v in Vacancy.get_info_json_requirements(vacancy_list, 'Python')] == [
        "Программирование: Python, Go"]
