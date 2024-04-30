from pprint import pprint

from src.headhunterapi import HeadHunterAPI
from src.jsonsaver import JSONSaver


def main():
    # Обращения к пользователю
    profession = input("Введите профессию для поиска: ")
    quantity_profession = int(input("Какое количество вакансий с наибольшей зарплатой вы хотите увидеть? "))

    # Указываю ссылку на API HH
    hh_url = HeadHunterAPI('https://api.hh.ru/vacancies')

    # Получаю вакансии и сортирую их
    vacancies = hh_url.get_info(profession)
    vacancies_sorted = sorted(vacancies, reverse=True)

    # Записываю все вакансии в JSON файл
    JSONSaver.add_json(vacancies)

    # Спрашиваю у пользователя вывести ли топ вакансий в количестве которое он указал?
    answer_1 = input('Хотите увидеть вакансии с наибольшей зарплатой (Да/Нет)? ')
    if answer_1.lower() == 'да':
        # Вывожу отсортированные вакансии в том количестве которое попросил пользователь
        pprint(vacancies_sorted[:quantity_profession])

    # Спрашиваю у пользователя хочет ли он отсортировать вакансии
    answer_2 = input('Отсортируем вакансии (Да/Нет)? ')
    if answer_2.lower() == 'да':
        # Спрашиваю у пользователя по чему будем сортировать
        answer_3 = input('Сортируем по названию или по требованиям (н/т)? ')
        if answer_3.lower() == 'н':
            # Спрашиваю у пользователя название вакансии для сортировки
            answer_4 = input('Введите ключевое слово в названии вакансии: ')
            JSONSaver.get_info_json_name(answer_4)
        elif answer_3 == 'т':
            answer_5 = input('Введите ключевое слово в описании вакансии: ')
            JSONSaver.get_info_json_requirements(answer_5)
    answer_6 = input('Введите диапазон зарплат через -(10000-100000): ')
    answer_6_split = answer_6.split('-')
    for salary in JSONSaver.filtered_information:
        if int(salary['salary_from']) > int(answer_6_split[0]):
            print(f'{salary['name']}, {salary['link_to_vacancy']}, {salary['salary_from']}, {salary['salary_to']}, '
                  f'{salary['requirements']}')

if __name__ == '__main__':
    # Вызываю функцию main()
    main()


