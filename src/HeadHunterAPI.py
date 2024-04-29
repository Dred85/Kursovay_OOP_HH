import requests
from abc import ABC, abstractmethod


class Parser(ABC):
    """
    Абстрактный базовый класс для парсинга вакансий
    """

    @abstractmethod
    def load_vacancies(self, keyword):
        pass


class HeadHunterAPI(Parser, file_worker):
    """
    Класс для работы с API HeadHunter
    """

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HeadHunterAPI-User-Agent'}
        self.params = {'text': '', 'page': 0, 'per_page': 100}
        self.vacancies = []
        super().__init__(file_worker)

    def load_vacancies(self, keyword):
        self.params['text'] = keyword
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            vacancies = response.json()['items']
            self.vacancies.extend(vacancies)
            self.params['page'] += 1


if __name__ == '__main__':
    hh = HeadHunterAPI()
    hh.load_vacancies('python')
    print(hh.vacancies)
