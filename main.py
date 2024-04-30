# from pprint import pprint

from src.headhunterapi import HeadHunterAPI
from src.jsonsaver import JSONSaver


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    profession = input("Введите профессию для поиска: ")
    quantity_profession = int(input("Какое количество вакансий вы хотите увидеть? "))

    # Создаю объект класса HeadHunterAPI
    hh_url = HeadHunterAPI()

    # Получаю список экземпляров класса Vacancy, сформированных по ключу: profession
    vacancies = hh_url.load_vacancies(profession)


    # Записываю все вакансии в JSON файл
    JSONSaver.add_json(vacancies)

    # Спрашиваю у пользователя вывести ли топ вакансий в количестве которое он указал?
    sort_vacansies_pay = input('Хотите увидеть топ вакансий по зарплате (Да/Нет)? ')
    if sort_vacansies_pay.lower() == 'да':
        # Вывожу отсортированные вакансии в том количестве которое попросил пользователь
        vacancies_sorted = sorted(vacancies, reverse=True)
        # pprint(vacancies_sorted[:quantity_profession])
        for v in vacancies_sorted[:quantity_profession]:
            print(v)
    else:
        print(f'Первые {quantity_profession} вакансий из всего списка:')
        for v in vacancies[:quantity_profession]:
            print(v)


    # Спрашиваю у пользователя хочет ли он дополнительно отсортировать вакансии по названию или по требованиям
    sort_vacansies_name = input('Отсортируем дополнительно вакансии по названию или по требованиям(Да/Нет)? ')
    if sort_vacansies_name.lower() == 'да':
        # Спрашиваю у пользователя по чему конкретно будем сортировать
        sort_vacansies_name_or_requirements = input('Сортируем по названию или по требованиям (н/т)? ')
        if sort_vacansies_name_or_requirements.lower() == 'Н':
            # Спрашиваю у пользователя название вакансии для сортировки
            key_word_vacansies = input('Введите ключевое слово в названии вакансии: ')
            JSONSaver.get_info_json_name(key_word_vacansies)
        elif sort_vacansies_name_or_requirements == 'Т':
            key_word_requirements = input('Введите ключевое слово в описании вакансии: ')
            JSONSaver.get_info_json_requirements(key_word_requirements)


    salary = input("Введите диапазон зарплат через '-' (100000 - 150000): ")
    salary_split = salary.split('-')

    # Вывожу отсортированные вакансии в том количестве и критериям которые попросил пользователь
    for salary in JSONSaver.filtered_information:
        if int(salary['salary_from']) > int(salary_split[0]):
            print(f'{salary['name']}, {salary['link_to_vacancy']}, {salary['salary_from']}, {salary['salary_to']}, '
                  f'{salary['requirements']}')


if __name__ == "__main__":
    user_interaction()
