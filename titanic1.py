#### Задание 1: Скачайте файл с данными о погибших на титанике
import requests
import os

def to_str(lines):
    # Функция возвращает список преобразованных строк,
    # а принимает список байтовых строк
    
    # Отдельно взятую строку байт можно преобразовать в строку
    # символов следующим образом: str(line, 'utf-8')+'\n'
    # Символ перехода на новую строку добавляется, чтобы при
    # записи в файл каждая запись начиналась с новой строки
    # Удалите pass и представьте ваше решение
    New = []
    for line in lines:
        line = str(line, 'utf-8') + '\n'
        New.append(line)
    return New


def download_file(url):
    # Делаем GET-запрос по указанному адресу
    response = requests.get(url)
    # Получаем итератор строк
    text = response.iter_lines()
    # Каждую строку конвертируем из массива байт в массив символов
    text = to_str(text)

    # Если файла не существует, то создаем его и записываем данные
    if not os.path.isfile("titanic.csv"):
        with open("titanic.csv", "w") as f:
            f.writelines(text)
    return text

#data = download_file("https://raw.githubusercontent.com/haven-jeon/introduction_to_most_usable_pkgs_in_project/master/bicdata/data/titanic.csv")

# Если вы успешно выполнили первое задание, то файл можно не скачивать
# каждый раз, а вместо этого данные читать из файла. Расскомментируйте
# следующую строку и закомментируйте предыдущую
data = open('titanic.csv')

#### Задание 2: Получаем список словарей
# Модуль для работы с файлами в формате CSV
import csv

reader = csv.DictReader(data)
reader.fieldnames[0] = 'lineno'
titanic_data = list(reader) #в конце получаем список словарей

# Модуль для красивого вывода на экран
from pprint import pprint as pp
#pp(titanic_data[37:42])

#### Задание 3: Узнать количество выживших и погибших на Титанике


def survived(tit_data):
    surv, notsurv = 0,0
    for dictionary in tit_data:
        if dictionary['survived'] == '1':
            surv += 1
        else:
            notsurv += 1
    tuple = (surv, notsurv)
    return tuple

    # Функция возвращает кортеж из двух элементов: количество
    # выживших и число погибших
 

pp(survived(titanic_data)) # (500, 809)


#### Задание 4: Узнать количество выживших и погибших на Титанике
#### по отдельности для мужчин и женщин
from operator import itemgetter
from itertools import groupby

def survived_by_sex(tit_data):
    tit_data_sorted = sorted(tit_data, key=itemgetter('sex'))
    groups = groupby(tit_data_sorted, key=itemgetter('sex'))
    for sex, group in groups:
        print(sex, survived(list(group)))

    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, (количество выживших, число погибших))

    # Подумайте над использованием функции survived()
    

survived_by_sex(titanic_data) # [('female', (339, 127)), ('male', (161, 682))]


#### Задание 5: Узнать средний возраст пассажиров
def average_age(tit_data):
    person = ()
    # Функция возвращает средний возраст пассажиров
    age, number = 0,0
    for person in tit_data:
        if person['age'] != 'NA':
            age += float(person['age'])
            number +=1
        average = float(age/number)
    return average

pp(average_age(titanic_data)) # 29.88


#### Задание 6: Узнать средний возраст мужчин и женщин по отдельности
def average_age_by_sex(tit_data):
    # Функция возвращает список кортежей из двух элементов вида:
    # (пол, средний возраст)
    tit_data_sorted = sorted(tit_data, key=itemgetter('sex'))
    groups = groupby(tit_data_sorted, key=itemgetter('sex'))
    for sex, group in groups:
        print(sex, average_age(list(group)))
    # Подумайте над использованием функции average_age()


average_age_by_sex(titanic_data) # [('female', 28.68), ('male', 30.58)]


#### Задание 7: Сколько детей и взрослых было на борту:
#### Получить группы в следующих диапазонах возрастов:
#### [0-14), [14-18), [18-inf]
def groups_by_age(tit_data):
    children, teens, adults = 0, 0, 0
    for person in tit_data:
        if person['age'] != "NA":
            if person['age'] < "14":
                children += 1
            elif person['age'] < "18":
                teens +=1
            else:
                adults+=1
    tuple = (children, teens, adults)
    return tuple

pp(groups_by_age(titanic_data))
#### Задание 8: Сколько в каждой группе выживших
def survived_by_groups(tit_data):
    tit_data_sorted = sorted(tit_data, key=itemgetter('survived'))
    groups = groupby(tit_data_sorted, key=itemgetter('survived'))
    for survived, group in groups:
        for person in group:
            if person['survived'] == '1':
                return(groups_by_age(list(group)))

pp(survived_by_groups(titanic_data))
#### Задание 9: Сколько в каждой группе выживших по отдельности для
#### мужчин и женщин

def survived_by_groups_sex(tit_data):
    tit_data_sorted = sorted(tit_data, key=itemgetter('sex'))
    groups = groupby(tit_data_sorted, key=itemgetter('sex'))
    for sex, group in groups:
        pp(survived_by_groups(list(group)))

survived_by_groups_sex(titanic_data)
