from src.headhunterapi import HeadHunterAPI
from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy


def user_interaction():
    """Функция для взаимодействия с пользователем"""

    profession = input("Введите профессию для поиска: ")

    # Создаю объект класса HeadHunterAPI
    hh_url = HeadHunterAPI()

    # Получаю список экземпляров класса Vacancy, сформированных по ключу: profession
    list_vacancies = hh_url.load_vacancies(profession)

    # Записываю все вакансии в JSON файл
    JSONSaver.add_json(list_vacancies)

    q_sort_vacansies_date = input('Отсортировать вакансии по дате публикации (Да/Нет)? ')

    # Выводим отсортированные по дате публикации вакансии ближайшей к нашей дате из файла json

    date_sorted_vacancies = Vacancy.get_info_json_date(list_vacancies)

    if q_sort_vacansies_date.lower() == 'да':

        for v in date_sorted_vacancies:
            print(v)

        quantity_profession = int(input("Укажите сколько отсортированных по времени вакансий оставить для просмотра? "))

        for v in date_sorted_vacancies[:quantity_profession]:
            print(v)

        q_sort_vacansies_salary = input('Отсортировать вакансии по зарплате - Да, выйти из программы - В)? ')
        if q_sort_vacansies_salary.lower() == 'да':
            sort_vacansies_salary = sorted(date_sorted_vacancies[:quantity_profession], key=lambda x: x.salary_from,
                                           reverse=True)
            for v in sort_vacansies_salary:
                print(v)
        else:
            print("До скорых встреч!")
            return
    else:
        # Выходим из программы
        print("До скорых встреч!")
        return

    # Спрашиваю у пользователя хочет ли он отфильтровать вакансии по названию или по требованиям
    filter_vacansies_name = input('Отфильтровать изначальный список вакансий по названию или по требованиям(Да/Нет)? ')
    if filter_vacansies_name.lower() == 'да':
        # Спрашиваю у пользователя по чему конкретно будем сортировать
        filter_vacansies_name_or_requirements = input('Фильтруем по названию или по требованиям (Н/Т)? ')
        if filter_vacansies_name_or_requirements.lower() == 'н':
            # Спрашиваю у пользователя название вакансии для сортировки
            key_word_vacansies = input('Введите ключевое слово в названии вакансии: ')
            Vacancy.get_info_json_name(key_word_vacansies)

        else:
            key_word_requirements = input('Введите ключевое слово в описании вакансии: ')
            Vacancy.get_info_json_requirements(key_word_requirements)
        salary = input("Введите диапазон зарплат через '-' (100000 - 150000): ")
        salary_split = salary.split('-')

        # Вывожу отсортированные вакансии в том количестве и критериям которые попросил пользователь
        for v in Vacancy.filtered_information:
            if int(v['salary_from']) > int(salary_split[0]):
                print(f'Отфильтрованные вакансии по заданным критериям:')

                print(f"""ID: {v['ID']}
    Наименование вакансии: {v['name']}
    Ссылка: {v['link_to_vacancy']}
    Зарплата от {v['salary_from']} до {v['salary_to']}
    Требования: {v['requirements']}
Дата публикации: {v['published_at']}\n""")

    else:
        print('До скорых встреч')


if __name__ == "__main__":
    user_interaction()
