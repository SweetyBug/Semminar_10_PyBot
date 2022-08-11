import random
def pr(tb):
    mas = '|'
    for i in range(3):
        for j in range(3):
            mas += tb[i][j] + '|'
        if i != 2:
            mas += '\n' + '|'
    return mas


def bot_go(tb):
    x = random.randint(-1, 2)
    y = random.randint(-1, 2)
    if tb[x][y] == '*':
        tb[x][y] = '0'
    else:
        bot_go(tb)

def game(tb):
    if (tb[0][0] == tb[0][1] == tb[0][2]) and ('*' not in tb[0]):
        if tb[0][0] == 'x':
            a = "Поздравляю, вы победили!"
        else:
            a = 'Упс... Кажется вы проиграли.'
        return a
    elif (tb[1][0] == tb[1][1] == tb[1][2]) and ('*' not in tb[1]):
        if tb[1][0] == 'x':
            a = "Поздравляю, вы победили!"
        else:
            a = 'Упс... Кажется вы проиграли.'
        return a
    elif (tb[2][0] == tb[2][1] == tb[2][2]) and ('*' not in tb[2]):
        if tb[2][0] == 'x':
            a = "Поздравляю, вы победили!"
        else:
            a = 'Упс... Кажется вы проиграли.'
        return a
    elif (tb[0][0] == tb[1][0] == tb[2][0]) and (tb[1][0] != '*'):
        if tb[0][0] == 'x':
            a = "Поздравляю, вы победили!"
        else:
            a = 'Упс... Кажется вы проиграли.'
        return a
    elif (tb[0][1] == tb[1][1] == tb[2][1]) and ('*' not in tb[1][1]):
        if tb[0][1] == 'x':
            a = "Поздравляю, вы победили!"
        else:
            a = 'Упс... Кажется вы проиграли.'
        return a
    elif (tb[0][2] == tb[1][2] == tb[2][2]) and ('*' not in tb[1][2]):
        if tb[0][2] == 'x':
            a = "Поздравляю, вы победили!"
        else:
            a = 'Упс... Кажется вы проиграли.'
        return a
    elif (tb[0][0] == tb[1][1] == tb[2][2]) and ('*' not in tb[1]):
        if tb[0][0] == 'x':
            a = "Поздравляю, вы победили!"
        else:
            a = 'Упс... Кажется вы проиграли.'
        return a
    elif (tb[2][0] == tb[1][1] == tb[0][2]) and ('*' not in tb[1]):
        if tb[2][0] == 'x':
            a = "Поздравляю, вы победили!"
        else:
            a = 'Упс... Кажется вы проиграли.'
        return a
    elif '*' in tb[0] or '*' in tb[1] or '*' in tb[2]:
        a = 'Ваш ход'
        return a
    else:
        return 'Ничья!'
