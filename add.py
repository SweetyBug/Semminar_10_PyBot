import csv
courses = ('I', 'II', 'III', 'IV')


def addStudent():
    global courses
    mas_user = []
    with open('students.csv', encoding='utf-8') as stud:
        file = csv.reader(stud, delimiter=';')
        count = -1
        for row in file:
            count += 1
        count += 1
        mas_user.append(count)
    user = input('Введите ФИО студента: ')
    mas_user.append(user)
    user = input('Введите дату рождения студента: ')
    mas_user.append(user)
    user = input('Введите дату поступления студента: ')
    mas_user.append(user)
    with open('faculties.csv', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        print('Выберите факультет: ')
        count = 0
        for row in file:
            if count != 0:
                print(f'{row[0]}. {row[1]}')
                count += 1
            else:
                count += 1
        user = int(input('Введите номер факультета: '))
        while user > count or user < 1:
            print('Вы ввели номер, которого нет в списке!')
            user = int(input('Введите щеё раз: '))
        count = 0
    with open('faculties.csv', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        for row in file:
            if count == user:
                user_fac = row[1]
                break
            else:
                count += 1
        mas_user.append(user_fac)
    print('Выберите курс: ')
    count = 1
    for i in courses:
        print(f'{count}. {i}')
        count += 1
    user = int(input('Введите номер курса: '))
    while user > count or user < 0:
        print('Вы ввели номер, которого нет в списке!')
        user = int(input('Введите щеё раз: '))
    mas_user.append(courses[user-1])
    with open('teachers.csv', encoding='utf-8') as teach:
        file = csv.reader(teach, delimiter=';')
        print('Выберите куратора: ')
        count = 0
        for row in file:
            if count != 0:
                print(f'{row[0]}. {row[1]}')
                count += 1
            else:
                count += 1
        user = int(input('Введите номер куратора: '))
        while user > count or user < 0:
            print('Вы ввели номер, которого нет в списке!')
            user = int(input('Введите щеё раз: '))
        count = 0
    with open('teachers.csv', encoding='utf-8') as teach:
        file = csv.reader(teach, delimiter=';')
        for row in file:
            if count == user:
                user_teach = row[1]
                break
            else:
                count += 1
    mas_user.append(user_teach)
    with open('students.csv', mode='a', encoding='utf-8') as stud:
        stud_writer = csv.writer(stud, delimiter=';', lineterminator='\r')
        stud_writer.writerow(mas_user)
    output = 'Студент добавлен!'
    return output


def addTeacher():
    user_mas = []
    with open('teachers.csv', encoding='utf-8') as teach:
        file = csv.reader(teach, delimiter=';')
        count = -1
        for row in file:
            count += 1
        count += 1
        user_mas.append(count)
    user = input('Введите ФИО преподавателя: ')
    user_mas.append(user)
    user = input('Введите дату рождения преподавателя: ')
    user_mas.append(user)
    user = input('Введите дату трудоустройтсва преподавателя: ')
    user_mas.append(user)
    user = input('Введите предмет преподавателя: ')
    user_mas.append(user)
    with open('teachers.csv', mode='a', encoding='utf-8') as file:
        file_write = csv.writer(file, delimiter=';', lineterminator='\r')
        file_write.writerow(user_mas)


def addFaculties():
    user = input('Введите название факультета: ')
    with open('faculties.csv', mode='r', encoding='utf-8') as fac:
        file = csv.reader(fac, delimiter=';')
        b = True
        count = -1
        for row in file:
            if user == row[1]:
                b = False
                output = 'Данный факультет уже есть в списках!'
                break
            count += 1
    with open('faculties.csv', mode='a', encoding='utf-8') as fac:
        fac_writer = csv.writer(fac, delimiter=';', lineterminator="\r")
        if b:
            count += 1
            user_vvod = []
            user_vvod.append(str(count))
            user_vvod.append(user)
            fac_writer.writerow(user_vvod)
            output = 'Факультет добавлен!'
    return output


