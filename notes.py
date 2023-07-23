from datetime import datetime


def hello():
    print('Приветствую, товарищ! Позволь представить мою вариацию приложения "Заметки". \nМой телеграм на всякий случай: https://t.me/VkusnashkaDamboldora')


def readingNote():
    with open("ListOfNotes.csv", "r", encoding="UTF-8") as f:
        for i in f:
         print(i)


def addingNote():
    global idNote
    with open("ListOfNotes.csv", "a", encoding="UTF-8") as f:
        idNote += 1
        name = input("Введите название заметки: ")
        body = input("Введите тело заметки: ")
        date = datetime.now()
        f.write(str(idNote) + "," + name + "," + body + "," + str(date) + "\n")





idNote = 0
