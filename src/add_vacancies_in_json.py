import os
import json
from abc import ABC, abstractmethod

from config import ROOT_DIR

path_to_file = os.path.join(ROOT_DIR, 'data', 'vacancies.json')


class WorkWithJSONAbstract(ABC):
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


class WorkWithJSON(WorkWithJSONAbstract):
    """Класс для добавления вакансий в JSON файл"""

    filtered_information = []

    @staticmethod
    def add_json(vacancies):
        """Метод для добавления вакансий в файл JSON"""
        with open(path_to_file, mode='w', encoding='utf-8') as vacancies_json:
            json.dump([v.to_JSON() for v in vacancies], vacancies_json, indent=4, ensure_ascii=False)

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
