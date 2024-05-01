import json
from abc import ABC, abstractmethod

from config import  path_to_file


class JSONSaverAbstract(ABC):
    """Абстрактный класс для добавления вакансий в JSON файл"""

    @staticmethod
    @abstractmethod
    def add_json(vacancies):
        """Абстрактный метод для добавления вакансий в файл JSON"""
        pass

    @classmethod
    @abstractmethod
    def get_info_json_name(cls, key_word):
        """Абстрактный метод для фильтрации вакансий по ключевому слову в названии"""
        pass

    @classmethod
    @abstractmethod
    def get_info_json_requirements(cls, key_word):
        """Абстрактный метод для фильтрации вакансий по ключевому слову в требованиях"""
        pass


class JSONSaver(JSONSaverAbstract):
    """Класс для добавления вакансий в JSON файл"""

    filtered_information = []

    @staticmethod
    def add_json(vacancies):
        """Метод для записи вакансий в файл JSON"""
        with open(path_to_file, mode='w', encoding='utf-8') as vacancies_json:
            json.dump([v.to_json() for v in vacancies], vacancies_json, indent=4, ensure_ascii=False)

    @classmethod
    def get_info_json_name(cls, key_word):
        """Метод для фильтрации вакансий по ключевому слову в названии"""
        with open(path_to_file, 'r', encoding='utf-8') as find_name_json:
            find_name = json.load(find_name_json)
            for key in find_name:
                if key_word in key['name'].lower():
                    cls.filtered_information.append(key)

    @classmethod
    def get_info_json_requirements(cls, key_word):
        """Метод для фильтрации вакансий по ключевому слову в требованиях"""
        with open(path_to_file, 'r', encoding='utf-8') as find_requirements_json:
            find_requirements = json.load(find_requirements_json)
            for key in find_requirements:
                if key['requirements']:
                    if key_word in key['requirements'].lower():
                        cls.filtered_information.append(key)

    @staticmethod
    def update_json(vacancies):
        """Метод для добавления вакансий в файл JSON"""
        with open(path_to_file, mode='a', encoding='utf-8') as vacancies_json:
            json.dump([v.to_json() for v in vacancies], vacancies_json, indent=4, ensure_ascii=False)


    @staticmethod
    def del_json(vacancies):
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
            else:
                None
            minimal = minimal + 1
        print('Итоговый результат: ')
        print(data)
        print('А теперь записываем итоговый файл')
        with open('personal.json', 'w', encoding='utf8') as outfile:
            json.dump(data, outfile, ensure_ascii=False, indent=4)