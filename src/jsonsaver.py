import json
from abc import ABC, abstractmethod

from config import path_to_file


class SaverInToFile(ABC):
    """Абстрактный класс для добавления/удаления вакансий в  файл"""

    @staticmethod
    @abstractmethod
    def add_json(vacancies):
        """Абстрактный метод для записи вакансий в файл JSON"""
        pass

    @staticmethod
    @abstractmethod
    def update_json(vacancies):
        """Абстрактный метод для добавления вакансий в файл JSON"""
        pass

    @staticmethod
    @abstractmethod
    def del_vacancies(vacancies):
        """Абстрактный метод для удаления вакансий из файла JSON"""
        pass


class JSONSaver(SaverInToFile):
    """Класс для добавления вакансий в JSON файл"""

    @staticmethod
    def add_json(vacancies):
        """Метод для записи вакансий в файл JSON"""

        with open(path_to_file, mode='w', encoding='utf-8') as vacancies_json:
            json.dump([v.to_json() for v in vacancies], vacancies_json, indent=4, ensure_ascii=False)

    @staticmethod
    def update_json(vacancies):
        """Метод для добавления вакансий в файл JSON"""
        with open(path_to_file, mode='a', encoding='utf-8') as vacancies_json:
            json.dump([v.to_json() for v in vacancies], vacancies_json, indent=4, ensure_ascii=False)

    @staticmethod
    def del_vacancies(vacancies):
        """Метод для удаления вакансий из файла JSON"""
        with open(path_to_file, mode='a', encoding='utf-8') as vacancies_json:
            json.dump([v.to_json() for v in vacancies], vacancies_json, indent=4, ensure_ascii=False)

        user_for_del = input('Введите id удаляемой вакансии\n')
        print(user_for_del)
        with open(path_to_file, 'r', encoding='utf-8') as f:  # открыли файл
            data = json.load(f)  # загнали все из файла в переменную
        minimal = 0
        for txt in data['id']:
            print('Запись c id:', minimal)

            if txt['name'] == user_for_del:
                print('Запись будет удалена')
                data['personal'].pop(minimal)

            minimal = minimal + 1
        print('Итоговый результат: ')
        print(data)
        print('А теперь записываем итоговый файл')
        with open('personal.json', 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)
