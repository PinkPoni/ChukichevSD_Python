# Задача 38: Дополнить телефонный справочник возможностью 
# изменения и удаления данных. Пользователь также может ввести 
# имя или фамилию, и Вы должны реализовать функционал для изменения 
# и удаления данных.


# Функция добавления данных
def add_contact(f):
    input_name = input('Введите Имя: ')
    input_last_name = input('Введите Фамилию: ')
    input_phone = input('Введите номер телефона: ')
    data = f'{input_last_name}; {input_name}; {input_phone}'
    with open(f, 'a', encoding='utf-8') as fd:
        fd.write(f'\n{data}')
    print(f'Запись {data} добавлена')


# Функция чтения данных
def read_all(f):
    with open(f, 'r', encoding='utf-8') as fd:
        file_list = fd.readlines()
        return file_list


# Функция вывода телефонного справочника на экран
def print_all(f):
    adr_book = read_all(f)
    for line in adr_book:
        line = line.replace('; ', ' ')
        line = line.replace('\n', ' ')
        print(line)


# Функция изменения данных
def search_contact(f):
    last_name = input('Введите фамилию для поиска: ')
    adr_book = read_all(f)
    print("\nИндекс Фамилия; Имя; Телефон")
    print("")
    for i in range(len(adr_book)):
        if last_name in adr_book[i]:
            print(i, adr_book[i])
    idx = int(input('Введите индекс для замены: '))
    last_name, name, _ = adr_book[idx].split('; ')
    last_name = input('Введите новую фамилию: ')
    name = input('Введите новое имя: ')
    phone = input('Введите новый номер телефона: ')
    new_record = f'{last_name}; {name}; {phone}\n'
    adr_book[idx] = new_record
    print(f"\nЗапись с индексом — {idx}, изменена на — {new_record}\n")
    with open(f, 'w', encoding='utf-8') as fd:
        fd.writelines(adr_book)


# Функция удаления информации
def delete_data(f):
    last_name = input('Введите фамилию для поиска: ')
    adr_book = read_all(f)
    print("\nИндекс Фамилия; Имя; Телефон")
    print("")
    for i in range(len(adr_book)):
        if last_name in adr_book[i]:
            print(i, adr_book[i])
    with open(f, "r", encoding='utf-8') as fd:
        adr_book = fd.read()
    print("")
    idx = int(input("Введите индекс строки для удаления: "))
    adr_book_lines = adr_book.split("\n")
    del_adr_book_lines = adr_book_lines[idx]
    adr_book_lines.pop(idx)
    print(adr_book_lines)
    print(f"\nУдалена запись: {del_adr_book_lines}\n")
    with open(f, "w", encoding='utf-8') as fd:
        fd.write("\n".join(adr_book_lines))


def main():
    file = 'address_book.txt'
    while True:
        user_choice = input('1 - Добавить запись,\n2 - Прочитать всю телефонную книгу,\n'
                            '3 - Найти и изменить запись,\n4 - Удалить запись,\nz - Выход: ')
        if user_choice == '1':
            add_contact(file)
        elif user_choice == '2':
            print_all(file)
        elif user_choice == '3':
            search_contact(file)
        elif user_choice == '4':
            delete_data(file)
        elif user_choice == 'z':
            print('Всего хорошего')
            break


if __name__ == '__main__':
    main()