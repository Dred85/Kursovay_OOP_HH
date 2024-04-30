import requests
from abc import ABC, abstractmethod

from src.Vacancy import Vacancy


class HeadHunterAPIAbstract(ABC):
    """Абстрактный класс для получения API с сайта"""

    @abstractmethod
    def get_info(self, profession):
        """Абстрактный метод для получения API с сайта и преобразования его в json-объекта"""
        pass


class HeadHunterAPI(HeadHunterAPIAbstract):
    """Класс для получения API с сайта по указанной вакансии. Дальше переношу список этих вакансий в класс
    Vacancy"""

    def __init__(self, url):
        self.url = url

    def get_info(self, profession):
        """Метод для получения API с сайта и перенос профессий в класс Vacancy"""
        params = {
            'text': profession,
            'page': 0,
            'per_page': 100
        }
        response = requests.get(url=self.url, params=params)
        return [
            Vacancy(name=info['name'],
                    link_to_vacancy=info['alternate_url'],
                    salary_from=(info.get('salary', {}) or {}).get('from', 0),
                    salary_to=(info.get('salary', {}) or {}).get('to', 0),
                    requirements=info['snippet']['requirement'])
            for info in response.json()['items']
        ]
