def custom_write(file_name, strings): #file_name - название файла для записи, strings - список строк для записи
    strings_positions = {}
    with open(file_name, 'w', encoding = 'utf-8') as file:
        for line_number, line in enumerate(strings, start = 1):
            byte_position = file.tell()
            file.write(line + '\n')
            strings_positions[(line_number, byte_position)] = line
        return strings_positions



info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('file_name.txt', info)
for elem in result.items():
    print(elem)


