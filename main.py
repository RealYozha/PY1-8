import string
import random

all_characters = list(string.printable.replace(string.whitespace, ""))
status = False

password_len = 0

while password_len > 20 or password_len < 7:
    password_len = int(input("Какой длинны ты хочешь пароль? (7-20)"))
    if password_len < 20 and password_len > 7:
        print("OK.")
    elif password_len > 20 or password_len < 7:
        print("Такая длинна пароля не подходит.")
    else:
        print("Я тебя не понимаю.")

while status == False:
    password = "".join(list([random.choice(all_characters) for i in range(password_len)]))
    print("Пароль:", password)
    answer = input("Вам нравится этот пароль? (да/нет)")
    if answer == "да":
        status = True
        print("Отлично! Ваш пароль:", password)
    elif answer == "нет":
        print("Хорошо, меняю")
    else:
        print("Я тебя не понимаю.")
        break
