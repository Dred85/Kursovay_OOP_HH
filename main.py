from pprint import pprint

from src.getting_and_working_with_vacancies import HHAPI
from src.add_vacancies_in_json import WorkWithJSON


def hello():
    # Обращения к пользователю
    profession = input("Введите профессию для поиска ")
    quantity_profession = int(input("Какое количество вакансий с наибольшей зарплатой вы хотите увидеть?"))

    # Указываю ссылку на API HH
    hh_url = HHAPI('https://api.hh.ru/vacancies')

    # Получаю вакансии и сортирую их
    vacancies = hh_url.get_info(profession)
    vacancies_sorted = sorted(vacancies, reverse=True)

    # Записываю все вакансии в JSON файл
    WorkWithJSON.add_json(vacancies)

    # Спрашиваю у пользователя вывести ли топ вакансий в количестве которое он указал?
    answer_1 = input('Хотите увидеть вакансии с наибольшей зарплатой?')
    if answer_1 == 'да':
        # Вывожу отсортированные вакансии в том количестве которое попросил пользователь
        pprint(vacancies_sorted[:quantity_profession])

    # Спрашиваю у пользователя хочет ли он отсортировать вакансии
    answer_2 = input('Отсортируем вакансии?')
    if answer_2 == 'да':
        # Спрашиваю у пользователя по чему будем сортировать
        answer_3 = input('Сортируем по названию или по требованиям?')
        if answer_3 == 'по названию':
            # Спрашиваю у пользователя название вакансии для сортировки
            answer_4 = input('Введите ключевое слово в названии вакансии')
            WorkWithJSON.get_info_json_name(answer_4)
        elif answer_3 == 'по требованиям':
            answer_5 = input('Введите ключевое слово в описании вакансии')
            WorkWithJSON.get_info_json_requirements(answer_5)
    answer_6 = input('Введите диапазон зарплат через -(10000-100000)')
    answer_6_split = answer_6.split('-')
    for salary in WorkWithJSON.filtered_information:
        if int(salary['salary_from']) > int(answer_6_split[0]):
            print(f'{salary['name']}, {salary['link_to_vacancy']}, {salary['salary_from']}, {salary['salary_to']}, '
                  f'{salary['requirements']}')


hello()
