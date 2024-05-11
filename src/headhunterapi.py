import requests
from abc import ABC, abstractmethod


class Parcer(ABC):
    """Абстрактный Класс для работы с API HeadHunter"""

    @abstractmethod
    def load_vacancies(self, profession):
        """Абстрактный метод для получения и сохранения данных с сайта"""
        pass


class HeadHunterAPI(Parcer):
    """Класс для работы с API HeadHunter по указанной вакансии."""

    def __init__(self) -> None:
        self.url: str = 'https://api.hh.ru/vacancies'
        self.headers: dict = {'User-Agent': 'HH-User-Agent'}
        self.params: dict = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies: list = []
        super().__init__()

    def load_vacancies(self, keyword: str) -> None:
        """Метод для получения данных с сайта """
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1
