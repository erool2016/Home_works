from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import pandas as pd
import re
my_list = []
from thre_words import all_names
from one_word import one_name
from two_words import two_names
from check_pfone import check_pfone_num

#df = pd.DataFrame({'lastname': [], 'firstname': [], 'surname': [], 'organization': [], 'position': [], 'phone': [], 'email': []})

def load_file():
    with open('phonebook_raw.csv', encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=',')
        contacts_list = list(rows)
        print('conact list',contacts_list)
    return contacts_list

def string_to_list_start():
    contact = load_file()
    # print(type(contact))
    del contact[0]
    # print(contact)
    # contact.remove([0])
    for line in contact:
        # print(line)
        check_line(line)

def update_data(dict_):
    for item in my_list:
        if dict_['lastname'] == item['lastname'] and dict_['firstname'] == item['firstname']:
            # print(f'{item} - данные есть в списке\n{dict_} - новые данные')
            # new_dict = dict_|item
            # item.update(new_dict)
            if item['organization'] == '' and dict_['organization'] != '':
                item['organization'] = dict_['organization']
            if item['position'] == '' and dict_['position'] != '':
                item['position'] = dict_['position']
            if item['phone'] == '' and dict_['phone'] != '':
                item['phone'] = dict_['phone']
            if item['email'] == '' and dict_['email'] != '':
                item['email'] = dict_['email']

            print(f'данные обновлены {item}')

def check_dict(dict_):
    for item in my_list:
        if dict_['lastname'] == item['lastname'] and dict_['firstname'] == item['firstname']:
            print(f'Данные есть в списке: {item}')
            update_data(dict_)
            return True
    return False
def check_line(line):
    sent_list = re.findall(r'[\w]+', line[0])
    #
    if len(sent_list) == 3:#Если 3 слова сразу в первом поел
        dict_=all_names(sent_list, line)
        if check_dict(dict_) is False:
            my_list.append(dict_)
            print(f'данные добавлены в список: {dict_}')


    elif len(sent_list) == 2:
        dict_ = two_names(sent_list, line)
        if check_dict(dict_) is False:
            my_list.append(dict_)
            print(f'данные добавлены в список: {dict_}')
        # my_list.append(two_names(sent_list, line))
    else:
        dict_ = one_name(sent_list, line)
        if check_dict(dict_) is False:
            my_list.append(dict_)
            print(f'данные добавлены в список: {dict_}')
        # my_list.append(one_name(sent_list, line))
    return my_list

def save_list(my_list):
    print('save_list')
    list = []
    for item in my_list:
        for key,value in item.items():
            list.append(value)
    print(list)
    fields = ['lastname', 'firstname', 'surname', 'organization', 'position', 'phone', 'email']
    with open('phonebook.csv', 'a',newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fields,delimiter=',',restval='Unknown', extrasaction='ignore')# datawriter = csv.writer(f, delimiter=',')
            writer.writerows(my_list)
        # for item in my_list:
        #     print(item)


    print(f'Список записан в файл phonebook.csv')

if __name__ == '__main__':
    string_to_list_start()
    # print(my_list)
    check_pfone_num(my_list)

    save_list(my_list)

