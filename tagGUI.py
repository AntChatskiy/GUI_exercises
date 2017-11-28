from tkinter import *
import random
keys = {'w': 'up', 'a': 'left', 's': 'down', 'd': 'right'}
root = Tk()
root.title("The best tag ever")


def create_field(n):
    numbers = [i for i in range(n * n)]
    random.shuffle(numbers)
    field = [[numbers.pop() for i in range(n)] for line in range(n)]
    return field


def show_field(field):
    for line in field:
        print(line)


def check_win(field):
    start = 1
    win = len(field)**2 - 1
    for line in field:
        for num in line:
            if num == start:
                start += 1
            elif start == win:
                return True
            else:
                return False


def find_null(field):
    n = len(field)
    for line in range(n):
        for num in range(n):
            if field[line][num] == 0:
                return line, num


def move_cell(key, field):
    direct = {'up': (1, 0), 'down': (-1, 0), 'left': (0, 1), 'right': (0, -1)}
    x, y = find_null(field)
    dx, dy = direct[key]
    n = len(field)
    if x + dx < n and y + dy < n:
        if x + dx >= 0 and y + dy >= 0:
            cell = field[x][y]
            field[x][y] = field[x + dx][y + dy]
            field[x + dx][y + dy] = cell


def insert_figures(field, buttons):
    n = len(field)
    for i in range(n):
        for ii in range(n):
            buttons[i][ii].grid(row=i, column=ii)


def create_buttons(field):
    n = len(field)
    buttons = []
    for i in range(n):
        buttons.append([])
        for ii in range(n):
            if field[i][ii] == 0:
                buttons[i].append(Button(master=root, text="0", width=10, height=5, font="arial 15", relief=SUNKEN))
            else:
                buttons[i].append(Button(master=root, text=str(field[i][ii]), width=10, height=5, font="arial 15"))
    return buttons

"""
if __name__ == "__main__":
    game = create_field(4)
    while not check_win(game):
        show_field(game)
        key = input()
        if key == "c":
            break
        elif key in keys:
            move_cell(keys[key], game)
    else:
        print("You won")
"""

if __name__ == "__main__":
    while True:
        field = create_field(4)
        buttons = create_buttons(field)
        insert_figures(field, buttons)
        root.mainloop()
        key = input("Write here:  ")
        if key == "c":
            break
        elif key in keys:
            move_cell(keys[key], field)
            print(field)