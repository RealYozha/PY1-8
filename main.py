import string
import random

all_characters = list(string.printable.replace(string.whitespace, ""))
status = False


password_len = int(input("Какой длинны ты хочешь пароль? (7-20)"))
while password_len > 20 or password_len < 7:
    if password_len < 20 and password_len > 7:
        print("OK.")
    elif password_len > 20 or password_len < 7:
        print("Такая длинна пароля не подходит.")
        password_len = int(input("Какой длинны ты хочешь пароль? (7-20)"))
    else:
        print("Я тебя не понимаю.")
        password_len = int(input("Какой длинны ты хочешь пароль? (7-20)"))

while status == False:
    password = list([random.choice(all_characters) for i in range(password_len)])
    print("Пароль:", "".join(password))
    answer = input("Вам нравится этот пароль? (да/нет)")
    if answer == "да":
        status = True
        print("Отлично! Ваш пароль:",  "".join(password))
        break
    elif answer == "нет":
        print("Хорошо, меняю")
    else:
        print("Я тебя не понимаю.")
        break
