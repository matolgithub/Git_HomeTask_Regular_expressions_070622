import re
import csv
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
def read_csv_file():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
    pprint(contacts_list)
    return contacts_list

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
def create_names_data():
    pass

def modify_phones_data():
    pass

def delete_double_data():
    pass

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def write_new_csvfile():
    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      # Вместо contacts_list подставьте свой список
      contacts_list = read_csv_file() # потом поменять на новый список
      datawriter.writerows(contacts_list)


if __name__ == '__main__':
    read_csv_file()
    # write_new_csvfile()