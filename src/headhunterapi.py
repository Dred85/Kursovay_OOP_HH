import requests
from abc import ABC, abstractmethod

from src.vacancy import Vacancy


class HeadHunterAPIAbstract(ABC):
    """Абстрактный Класс для работы с API HeadHunter"""

    @abstractmethod
    def load_vacancies(self, profession):
        """Абстрактный метод для получения и сохранения данных с сайта"""
        pass


class HeadHunterAPI(HeadHunterAPIAbstract):
    """Класс для работы с API HeadHunter по указанной вакансии."""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__()

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1

        # return response.json()['items']
        return [
            Vacancy(id=info['id'],
                    name=info['name'],
                    link_to_vacancy=info['alternate_url'],
                    salary_from=(info.get('salary', {}) or {}).get('from', 0),
                    salary_to=(info.get('salary', {}) or {}).get('to', 0),
                    requirements=info['snippet']['requirement'],
                    published_at=info['published_at'])
            for info in response.json()['items']
        ]


if __name__ == '__main__':
    hh = HeadHunterAPI()
    hh.load_vacancies('java')
    # print()
    print(hh.vacancies[:2])
