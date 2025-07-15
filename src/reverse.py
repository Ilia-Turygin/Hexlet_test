from pathlib import Path


def reverse(string):
    return string[::-1]


# Прочитаем входной файл
input_path = Path('input.txt')
original_text = input_path.read_text()

# Применим функцию reverse и сохраним результат
reversed_text = reverse(original_text)

# Запишем результат в новый файл
output_path = Path('output.txt')
output_path.write_text(reversed_text)

print("Тест завершен. Проверьте файл output.txt для результата.")