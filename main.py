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

        for v in vacancies_sorted[:quantity_profession]:
            print(v)
    else:
        print(f'Первые {quantity_profession} вакансий из всего списка вакансий:')
        for v in vacancies[:quantity_profession]:
            print(v)

    # Спрашиваю у пользователя хочет ли он дополнительно отфильтровать вакансии по названию или по требованиям
    filter_vacansies_name = input('Отфильтровать дополнительно вакансии по названию или по требованиям(Да/Нет)? ')
    if filter_vacansies_name.lower() == 'да':
        # Спрашиваю у пользователя по чему конкретно будем сортировать
        filter_vacansies_name_or_requirements = input('Фильтруем по названию или по требованиям (Н/Т)? ')
        if filter_vacansies_name_or_requirements.lower() == 'н':
            # Спрашиваю у пользователя название вакансии для сортировки
            key_word_vacansies = input('Введите ключевое слово в названии вакансии: ')
            JSONSaver.get_info_json_name(key_word_vacansies)
        elif filter_vacansies_name_or_requirements == 'т':
            key_word_requirements = input('Введите ключевое слово в описании вакансии: ')
            JSONSaver.get_info_json_requirements(key_word_requirements)

    salary = input("Введите диапазон зарплат через '-' (100000 - 150000): ")
    salary_split = salary.split('-')

    # Вывожу отсортированные вакансии в том количестве и критериям которые попросил пользователь
    for v in JSONSaver.filtered_information:
        if int(v['salary_from']) > int(salary_split[0]):
            # print(f'{v['name']}, {v['link_to_vacancy']}, {v['salary_from']}, {v['salary_to']}, '
            #       f'{v['requirements']}')
            print(f'Отфильтрованные вакансии по заданным критериям:')
            print(f"""ID: {v['ID']}
    Наименование вакансии: {v['name']}
    Ссылка: {v['link_to_vacancy']}
    Зарплата от {v['salary_from']} до {v['salary_to']}
    Требования: {v['requirements']}
Дата публикации: {v['published_at']}\n""")


if __name__ == "__main__":
    user_interaction()
