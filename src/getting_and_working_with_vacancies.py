import requests
from abc import ABC, abstractmethod


class WorkWithVacanciesAbstract(ABC):
    """Абстрактный класс для работы с вакансиями"""
    @abstractmethod
    def __str__(self):
        """Абстрактный метод для вывода информации по вакансиям для пользователя"""
        pass

    @abstractmethod
    def __repr__(self):
        """Абстрактный метод для вывода информации для отладки программы"""

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def to_JSON(self):
        """Абстрактный метод, насколько я понял, для конвертации информации которая будет добавлена в файл JSON"""
        pass


class WorkWithVacancies(WorkWithVacanciesAbstract):
    """Класс для работы с вакансиями
    name - название вакансии
    link_to_vacancy - ссылка на вакансию
    salary_from начальная зарплата
    salary_to - максимальная зарплата
    requirements - требования к вакансии
    Так же если зарплата не указана то вывожу об этом сообщение"""
    def __init__(self, name, link_to_vacancy, salary_from, salary_to, requirements):
        self.name = name
        self.link_to_vacancy = link_to_vacancy
        if salary_from:
            self.salary_from = salary_from
        else:
            self.salary_from = 0
        if salary_to:
            self.salary_to = salary_to
        else:
            self.salary_to = 0
        self.requirements = requirements

    def __str__(self):
        """Метод вывода информации по вакансиям"""
        return f'{self.name} - {self.link_to_vacancy}, {self.salary_from} - {self.salary_to}: {self.requirements}'

    def __repr__(self):
        """Метод вывода информации по вакансиям"""
        return f'{self.name} - {self.link_to_vacancy}, {self.salary_from} - {self.salary_to}: {self.requirements}'

    def __lt__(self, other):
        return self.salary_to < other.salary_to

    def to_JSON(self):
        """Метод для подготовки информации к записи в файл JSON"""
        return {
            'name': self.name,
            'link_to_vacancy': self.link_to_vacancy,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'requirements': self.requirements
        }


class HHAPIAbstract(ABC):
    """Абстрактный класс для получения API с сайта"""

    @abstractmethod
    def get_info(self, profession):
        """Абстрактный метод для получения API с сайта и преобразования его в json-объекта"""
        pass


class HHAPI(HHAPIAbstract):
    """Класс для получения API с сайта по указанной вакансии. Дальше переношу список этих вакансий в класс
    WorkWithVacancies"""

    def __init__(self, url):
        self.url = url

    def get_info(self, profession):
        """Метод для получения API с сайта и перенос профессий в класс WorkWithVacancies"""
        params = {
            'text': profession,
            'page': 0,
            'per_page': 100
        }
        response = requests.get(url=self.url, params=params)
        return [
            WorkWithVacancies(
                name=info['name'],
                link_to_vacancy=info['alternate_url'],
                salary_from=(info.get('salary', {}) or {}).get('from', 0),
                salary_to=(info.get('salary', {}) or {}).get('to', 0),
                requirements=info['snippet']['requirement'])
            for info in response.json()['items']
        ]