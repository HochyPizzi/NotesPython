from datetime import datetime
from datetime import date as d


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
        date = str(d.today()) + "," + str(datetime.now().hour) + ":" + str(datetime.now().minute)
        f.write(str(idNote) + "," + name + "," + body + "," + str(date) + "\n")


def editingNote():
    readingNote()
    searchData = input("Введите ID заметки для изменения: ")
    dataDictionary = {}
    with open("ListOfNotes.csv", "r", encoding="UTF-8") as f:
        for i in f:
            dataDictionary[i[0]] = i[1:]
        if searchData in dataDictionary:
            dataDictionary.pop(searchData)
    with open("ListOfNotes.csv", "w", encoding="UTF-8") as f:
        for key, value in dataDictionary.items():
            f.write(str(key) + str(value).replace("[", "").replace("]", "").replace("'", ""))
    addingNote()


def deletionNote():
    readingNote()
    searchData = input("Введите ID заметки для удаления: ")
    dataDictionary = {}
    with open("ListOfNotes.csv", "r", encoding="UTF-8") as f:
        for i in f:
            dataDictionary[i[0]] = i[1:]
        if searchData in dataDictionary:
            dataDictionary.pop(searchData)
    with open("ListOfNotes.csv", "w", encoding="UTF-8") as f:
        for key, value in dataDictionary.items():
            f.write(str(key) + str(value).replace("[", "").replace("]", "").replace("'", ""))


def menu():
    global idNote
    hello()
    with open("ListOfNotes.csv", "w", encoding="UTF-8") as f:
        print("Добавь свою первую заметку!")
        name = input("Введите название заметки: ")
        body = input("Введите тело заметки: ")
        date = str(d.today()) + "," + str(datetime.now().hour) + ":" + str(datetime.now().minute)
        f.write(str(idNote) + "," + name + "," + body + "," + str(date) + "\n")
    while True:
        print("1 - посмотреть все заметки\n2 - добавить заметку\n3 - изменить заметку\n4 - удалить заметку\n0 - выход")
        num = int(input("Выберите действие: "))
        match num:
            case 1:
                readingNote()
            case 2:
                addingNote()
            case 3:
                editingNote()
            case 4:
                deletionNote()
            case _:
                print("До новых включений!!!")
                break


idNote = 0
menu()


