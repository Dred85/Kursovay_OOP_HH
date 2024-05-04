import json
from abc import ABC, abstractmethod

from config import path_to_file_new, path_to_file_update


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
        """Абстрактный метод для удаления вакансии из файла JSON"""
        pass


class JSONSaver(SaverInToFile):
    """Класс для добавления вакансий в JSON файл"""

    @staticmethod
    def add_json(vacancies) -> None:
        """Метод для записи вакансий в файл vacancies_all.json"""

        with open(path_to_file_new, mode='w', encoding='utf-8') as vacancies_json:
            json.dump([v.to_json() for v in vacancies], vacancies_json, indent=4, ensure_ascii=False)

    @staticmethod
    def add_update_json() -> None:
        """Метод для создания файла vacancies_update.json"""

        with open(path_to_file_update, mode='w', encoding='utf-8') as vacancies_json:
            json.dump([], vacancies_json, indent=4, ensure_ascii=False)

    @staticmethod
    def update_json(vacancies) -> None:
        """Метод для добавления вакансий в файл vacancies_update.json"""
        with open(path_to_file_update, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # vacancies.to_json() - вернет словарь
            data_update = data + [vacancies.to_json()]

        with open(path_to_file_update, 'w', encoding='utf-8') as f:
            json.dump(data_update, f, indent=4, ensure_ascii=False)

    @staticmethod
    def del_vacancies(id_vacancy) -> None:
        """Метод для удаления вакансии из файла vacavcies_update.json по ID"""

        with open(path_to_file_update, 'r', encoding='utf-8') as f:  # открыли файл
            data_update = json.load(f)  # загнали все из файла в переменную
            print(f'Запись c ID: {id_vacancy} будет удалена')
            for v in data_update:
                if v['ID'] == id_vacancy:
                    data_update.pop(data_update.index(v))
                    print('Запись удалена')

        print(id_vacancy)
        print('Записываем итоговый файл')
        with open(path_to_file_update, 'w', encoding='utf-8') as f:
            json.dump(data_update, f, indent=4, ensure_ascii=False)
