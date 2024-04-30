from abc import ABC, abstractmethod


class VacanciesAbstract(ABC):
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
    def to_json(self):
        """Абстрактный метод, насколько я понял, для конвертации информации которая будет добавлена в файл JSON"""
        pass


class Vacancy(VacanciesAbstract):
    """Класс для работы с вакансиями
    id -  идентификатор вакансии
    name - название вакансии
    link_to_vacancy - ссылка на вакансию
    salary_from начальная зарплата
    salary_to - максимальная зарплата
    requirements - требования к вакансии
    Так же если зарплата не указана то вывожу об этом сообщение"""

    def __init__(self, id, name, link_to_vacancy, salary_from, salary_to, requirements):
        self.id = id
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
        return f'ID: {self.id}\nНаименование вакансии: {self.name}\nСсылка: {self.link_to_vacancy}\nЗарплата от {self.salary_from} до {self.salary_to}\nТребования: {self.requirements}\n'

    def __repr__(self):
        """Метод вывода информации по вакансиям"""
        return f'{self.__class__.__name__}({self.id}, {self.name}, {self.link_to_vacancy}, {self.salary_from} - {self.salary_to}, {self.requirements})'

    def __lt__(self, other):
        """Метод позволяет использовать оператор меньше (<) для сравнения объектов этого класса"""
        return self.salary_to < other.salary_to

    def to_json(self):
        """Метод для подготовки информации к записи в файл JSON"""
        return {
            'ID': self.id,
            'name': self.name,
            'link_to_vacancy': self.link_to_vacancy,
            'salary_from': self.salary_from,
            'salary_to': self.salary_to,
            'requirements': self.requirements
        }