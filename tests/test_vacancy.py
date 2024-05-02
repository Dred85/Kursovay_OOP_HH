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
    """Тестирую переопределенный дандер метод __lt__"""
    assert vacancy1 < vacancy2


def test_to_json(vacancy1):
    assert vacancy1.to_json() == {'ID': '97223662',
                                  'name': 'Full stack developer (angular + java)',
                                  'link_to_vacancy': 'https://hh.ru/vacancy/97223662',
                                  'salary_from': 100000,
                                  'salary_to': 500000,
                                  'requirements': 'Знание Python',
                                  'published_at': '2024-04-17T13:33:10+0300'}
