import pytest
from src.vacancy import Vacancy


@pytest.fixture
def vacancy():
    return Vacancy( "97223662",
        "Full stack developer (angular + java)",
        "https://hh.ru/vacancy/97223662",
        100000,
        500000,
        "Знание Python",
        "2024-04-17T13:33:10+0300")

def test_init(vacancy):
    assert vacancy.id == "97223662"
    assert vacancy.name == "Full stack developer (angular + java)"
    assert vacancy.link_to_vacancy == "https://hh.ru/vacancy/97223662"
    assert vacancy.salary_from == 100000
    assert vacancy.salary_to == 500000
    assert vacancy.requirements == "Знание Python"
    assert vacancy.published_at == "2024-04-17T13:33:10+0300"






