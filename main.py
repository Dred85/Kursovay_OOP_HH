from src.headhunterapi import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy


def user_interaction() -> None:
    """Функция для взаимодействия с пользователем"""

    profession = input("Введите профессию для поиска: ")

    # Создаю пустой файл add_update_json для записи туда отсортированных вакансий
    JSONSaver.add_update_json()

    # Создаю объект класса HeadHunterAPI
    hh_url = HeadHunterAPI()

    # Получаю список экземпляров класса Vacancy, сформированных по ключу: profession
    list_vacancies = hh_url.load_vacancies(profession)

    # Записываю все вакансии в JSON файл
    JSONSaver.add_json(list_vacancies)

    q_sort_vacansies_date = input(
        'Отсортировать вакансии по дате публикации - Да, перейти к другим вариантам фильтрации - нажмите Enter ')

    if q_sort_vacansies_date.lower() == 'да':
        # Выводим отсортированные по дате публикации вакансии ближайшей к нашей дате из файла json
        date_sorted_vacancies = Vacancy.get_info_json_date(list_vacancies)
        for v in date_sorted_vacancies:
            print(v)

        quantity_profession = int(input("Укажите сколько отсортированных по дате вакансий оставить для просмотра? "))

        for v in date_sorted_vacancies[:quantity_profession]:
            print(v)

        q_sort_vacansies_salary = input(
            '''Отсортировать вакансии по зарплате и добавить отсортированные вакансии в файл vacancies_update.json- Да, 
перейти к другим вариантам фильтрации - нажмите Enter ''')
        if q_sort_vacansies_salary.lower() == 'да':
            sort_vacansies_salary = sorted(date_sorted_vacancies[:quantity_profession], key=lambda x: x.salary_from,
                                           reverse=True)
            for v in sort_vacansies_salary:
                # Добавить отсортированные вакансии в файл vacancies_update.json
                JSONSaver.update_json(v)
                print(v)

    # Спрашиваю у пользователя хочет ли он отфильтровать изначальные вакансии по названию или по требованиям?
    q_filter_vacansies_name = input(
        '''Отфильтровать изначальный список вакансий по названию или по требованиям и 
добавить отсортированные вакансии в файл vacancies_update.json-(Да/Нет)? ''')
    if q_filter_vacansies_name.lower() == 'да':
        # Спрашиваю у пользователя по чему конкретно будем сортировать
        q_filter_vacansies_name_or_requirements = input('Фильтруем по названию или по требованиям (Н/Т)? ')
        if q_filter_vacansies_name_or_requirements.lower() == 'н':
            # Спрашиваю у пользователя название вакансии для сортировки
            key_word_vacansies = input('Введите ключевое слово в наименовании вакансии: ')
            list_name_sorted_vacancies = Vacancy.get_info_json_requirements(list_vacancies, key_word_vacansies)
            for v in list_name_sorted_vacancies:
                # Добавить отсортированные вакансии в файл vacancies_update.json
                JSONSaver.update_json(v)
                print(v)

        else:
            # Спрашиваю у пользователя ключевое слово для сортировки по описанию вакансии
            key_word_requirements = input('Введите ключевое слово в описании вакансии: ')
            list_requirements_sorted_vacancies = Vacancy.get_info_json_requirements(list_vacancies,
                                                                                    key_word_requirements)
            for v in list_requirements_sorted_vacancies:
                # Добавить отсортированные вакансии в файл vacancies_update.json
                JSONSaver.update_json(v)
                print(v)
    else:
        print('вы можете удалить вакансии')

    q_vacancy_delete = input("Хотите удалить вакансию по ID? Да/Нет")
    if q_vacancy_delete.lower() == 'да':
        id_vacancy = input("Введите ID вакансии: ")
        JSONSaver.del_vacancies(id_vacancy)
    else:
        print('До скорых встреч')


if __name__ == "__main__":
    user_interaction()
