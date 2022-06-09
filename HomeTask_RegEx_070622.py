import re
import csv
from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
def read_csv_file():
    with open("phonebook_raw.csv", encoding='utf-8') as f:
      rows = csv.reader(f, delimiter=",")
      contacts_list = list(rows)
    # pprint(contacts_list)
    return contacts_list

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
# приведение телефонов к форматам +7(999)999-99-99 и +7(999)999-99-99 доб.9999
def modify_phones_data():
    contacts_list = read_csv_file()
    newphone_contlist = []
    for persons in contacts_list:
        correct_phone_list = []
        for data in persons:
            pattern = r"(\+7|8)?\s?\(?(\d+)\)?\s?\-?(\d{3})\-?(\d{2})\-?(\d{2}\,?)(\s*\(?(\доб.)?\s*(\d+)\)?)?"
            substitution = r"+7(\2)\3-\4-\5 \7\8"
            res = re.sub(pattern, substitution, data)
            correct_phone_list.append(res.strip())
        newphone_contlist.append(correct_phone_list)
    # pprint(newphone_contlist)
    return newphone_contlist

# поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно
def create_names_data():
    cont_list = modify_phones_data()
    for persons in cont_list:
        if len(persons[0].split()) == 3:
            persons[2] = persons[0].split()[2]
            persons[1] = persons[0].split()[1]
            persons[0] = persons[0].split()[0]
        elif len(persons[0].split()) == 2:
            persons[1] = persons[0].split()[1]
            persons[0] = persons[0].split()[0]
        elif len(persons[0].split()) == 1 and len(persons[1].split()) == 2:
            persons[2] = persons[1].split()[1]
            persons[1] = persons[1].split()[0]
        for index in range(len(persons)):
            if index >= 7 and persons[index] == '':
                persons.pop(index)
    # pprint(cont_list)
    return cont_list

# объединить все дублирующиеся записи о человеке в одну
# в этой функции реализован поиск повторений
def search_double_data():
    double_cont_list = create_names_data()
    double_dict = {}
    double_persons_list = []
    for persons in double_cont_list:
        count = 0
        for last_name in double_cont_list:
            if last_name[0] in persons:
                count += 1
                if count > 1:
                    double_dict[last_name[0]] = count
    print('Данные о повторениях данных сотрудников (фамилия, кол-во повторений):', double_dict)
    for last_name in double_dict:
        for persons in double_cont_list:
            if last_name == persons[0]:
                double_persons_list.append(persons)
    # print(double_persons_list)
    return double_dict, double_persons_list

# в этой функции реализована зачистка повторений
def delete_double_data():
    double_dict, double_persons_list = search_double_data()
    double_cont_list = create_names_data()
    nonedouble_cont_list = []
    for persons in double_cont_list:
        if persons[0] not in double_dict:
            nonedouble_cont_list.append(persons)
    for last_name in double_dict:
        totalpers_contlist = []
        for data in double_persons_list:
            if last_name == data[0]:
                for index in range(len(data)):
                    totalpers_contlist.append(data[index])
        for item in range(int(len(totalpers_contlist) / 2)):
            if totalpers_contlist[item] == '' and totalpers_contlist[item + 7] != '':
                totalpers_contlist[item] = totalpers_contlist[item + 7]
            elif totalpers_contlist[item] == '' and totalpers_contlist[item + 7] == '':
                totalpers_contlist[item] = ''
        totalpers_contlist = totalpers_contlist[:int(len(totalpers_contlist) / 2)]
        nonedouble_cont_list.append(totalpers_contlist)
    print(f'Всего было {len(double_cont_list)} строк и {len(double_cont_list) - 1} записей о сотрудниках, теперь '
          f'после устранения дублей стало {len(nonedouble_cont_list)} строк и {len(nonedouble_cont_list) - 1} '
          f'записей о сотрудниках.')
    pprint(nonedouble_cont_list)

    return nonedouble_cont_list

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
def write_new_csvfile():
    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      # Вместо contacts_list подставьте свой список
      contacts_list = read_csv_file() # потом поменять на новый список
      datawriter.writerows(contacts_list)


if __name__ == '__main__':
    # read_csv_file()
    # write_new_csvfile()
    # modify_phones_data()
    # create_names_data()
    # search_double_data()
    delete_double_data()