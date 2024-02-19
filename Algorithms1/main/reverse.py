#Задача 1
def reverse_file_content(input_file_path, output_file_path):
    try:
        with open(input_file_path, 'r', encoding='utf-8') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Файл {input_file_path} не знайдено.")
        return

    reversed_content = content[::-1]

    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(reversed_content)

reverse_file_content('Rtext1.txt', 'Rtext2.txt')
