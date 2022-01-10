"""
МОДУЛЬ 2
Программа из 2-го дз
Сначала пользователь вводит год рождения Пушкина, когда отвечает верно вводит день рождения
Можно использовать свой вариант программы из предыдущего дз, мой вариант реализован ниже
Задание: переписать код используя как минимум 1 функцию
"""
import random


def rand_list(new_list, nums):
    random_nums_names = random.sample(new_list, nums)
    return random_nums_names


famous_peoples = {'Ilon Mask': '28.06.1971', 'Sergei Brin': '21.08.1973', 'Jack Ma': '10.09.1964',
                  'Bruce Lee': '20.07.1940', 'Guido van Rossum': '31.01.1956', 'Magnus Carlsen': '30.11.1990',
                  'Maria Skłodowska-Curie': '07.11.1867', 'Martin Scorsese': '17.11.1942',
                  'Evgeny Kharlamov': '11.06.1985', 'Ekaterina Kharlamova': '11.10.1983'}

day_list = ['первго', 'второго', 'третьего', 'четвёртого', 'пятого', 'шестого', 'седьмого', 'восьмого',
            'девятого', 'десятого', 'одиннадцатого', 'двенадцатого', 'тринадцатого', 'четырнадцатого', 'пятнадцатого',
            'шестнадцатого', 'семнадцатого', 'восемнадцатого', 'девятнадцатого', 'двадцатого', 'двадцать первого',
            'двадцать второго', 'двадцать третьго', 'двадацать четвёртого', 'двадцать пятого', 'двадцать шестого',
            'двадцать седьмого', 'двадцать восьмого', 'двадцать девятого', 'тридцатого', 'тридцать первого']

month_list = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня',
              'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря']

famous_peoples_keys_list = list(famous_peoples.keys())

random_five_names = rand_list(famous_peoples_keys_list, 5)
right_answer_count = 0
wrong_answer_count = 0


while True:
    for i in random_five_names:
        date = famous_peoples[i]
        input_birthday = input("Enter {}'s birthday(dd.mm.yyyy): ".format(i))
        if famous_peoples[i] == input_birthday:
            right_answer_count += 1
        else:
            date_list = date.split('.')
            right_answer = str(
                day_list[int(date_list[0]) - 1] + ' ' + month_list[int(date_list[1]) - 1] + ' ' + date_list[
                    2] + ' года')
            wrong_answer_count += 1
            print("Your answer ist right\n{} was born {} : ".format(i, right_answer))

    print("Right answers: {}".format(right_answer_count))
    print("Wrong answers: {}".format(wrong_answer_count))

    ask_about_play = input('Do you want play again?(yes/no): ')
    if ask_about_play == 'no':
        print('Давай до свиданья!!!')
        break
