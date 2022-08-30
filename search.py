from search import *
import csv
courses = ('I', 'II', 'III', 'IV')



def cr():
    global courses
    print('Выберите курс: ')
    count = 1
    for i in courses:
        print(f'{count}. {i}')
        count += 1
    user = input()
    while int(user) > count or int(user) < 1:
        print('Такого числа нет в списке!')
        user = input('Попробуйте ещё раз: ')
    course = courses[int(user) - 1]
    return course


def pr_fac():
    with open('faculties.csv', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        count = 0
        s = ''
        for row in file:
            if count != 0:
                s += f'{row[0]}. {row[1]}\n'
            else:
                count += 1
        return s


def pr_stud_poln():
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        count = 0
        for row in file:
            f = row.remove('[', '')
            f = row.remove(']', '')
            s += f'{f}\n'
    return s

def pr_stud_course():
    course = cr()
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        for row in file:
            if row[5] == str(course):
                print(f'{row[1]}; {row[5]}')


def pr_stud_course_fac():
    course = cr()
    print('Выберите номер факультета: ')
    pr_fac()
    user = input()
    with open('faculties.csv', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        for row in file:
            if row[0] == user:
                user_fac = row[1]
                break
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        for row in file:
            if row[5] == course and row[4] == user_fac:
                print(f'{row[1]}; {row[4]}; {row[5]}')


def pr_stud_fac():
    print('Выберите номер факультета: ')
    pr_fac()
    user = input()
    with open('faculties.csv', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        for row in file:
            if row[0] == user:
                user_fac = row[1]
                break
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        for row in file:
            if row[4] == user_fac:
                print(row[1], row[4])


'''def pr_stud_date():
    user_date_1 = list(map(int, input('Введите дату начала диапазона: ').split('.')))
    user_date_2 = list(map(int, input('Введите дату окончания диапазона: ').split('.')))
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        count = 0
        for row in file:
            if count != 0:
                mas_stud = list(map(int, row[3].split('.')))
                print(mas_stud)
                if (mas_stud[0] >= user_date_1[0] or mas_stud[1] >= user_date_1[1]) and mas_stud[2] >= user_date_1[2]:
                    if mas_stud[0] <= user_date_2[0] and mas_stud[1] <= user_date_2[1] and mas_stud[2] <= user_date_2[2]:
                        print(f'{row[1]} поступил {row[3]}')
            else:
                count += 1'''


def pr_tech_poln():
    with open('teachers.csv', encoding='utf-8') as teach:
        file = csv.reader(teach, delimiter=';')
        for row in file:
            print(*row + ';')


def pr_tech_les():
    user = input('Введите название предмета: ')
    if user.lower == 'end':
        a = 'До встречи!'
        return a
    else:
        with open('teachers.csv', encoding='utf-8') as teach:
            file = csv.reader(teach, delimiter=';')
            count = 0
            for row in file:
                if user.lower() == row[4].lower():
                    print(f'{row[1]}, {row[4]}')
                    count += 1
            if count == 0:
                print('Такого предмета нет! \n Попробуйте ещё раз')
                pr_tech_les()
