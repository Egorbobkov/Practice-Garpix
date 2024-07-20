import json
import itertools
import csv
import io


def is_unique_combination(data, columns):
    """
    Проверяет, делает ли комбинация колонок уникальной каждую запись в данных.
    """
    seen = set()
    for record in data:
        identifier = tuple(record.get(col, None) for col in columns)
        if identifier in seen:
            return False
        seen.add(identifier)
    return True


def find_minimal_unique_combination(data, priority):
    """
    Находит минимальный набор колонок,
    которые однозначно идентифицируют каждую запись в данных,
    с учетом приоритета колонок.
    """
    if not data:
        return []

    # Извлекает все имена колонок
    columns = set()
    for record in data:
        columns.update(record.keys())

    # Сортирует колонки в соответствии с приоритетом
    sorted_columns = [col for col in priority if col in columns]

    # Проверяет все комбинации колонок
    for r in range(1, len(sorted_columns) + 1):
        for combination in itertools.combinations(sorted_columns, r):
            if is_unique_combination(data, combination):
                return list(combination)
    return sorted_columns


def serialize_to_csv(columns):
    """
    Сериализует список колонок в CSV-формат.
    """
    output = io.StringIO()
    writer = csv.writer(output, lineterminator='\n')
    writer.writerow(["Минимальный уникальный идентификатор"])
    for col in columns:
        writer.writerow([col])
    return output.getvalue().strip()


def main(json_file_path):
    """
    Основная функция,
    вызываемая с путем к JSON-файлу в качестве входных данных.
    """
    # Читает JSON-данные из файла
    with open(json_file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Устанавливает приоритет колонок
    priority = [
        "фамилия", "имя", "отчество", "класс", "подгруппа", "предмет",
        "видДеятельности", "количествоЧасовВнеделю"
    ]

    # Находит минимальный уникальный набор колонок
    minimal_columns = find_minimal_unique_combination(data, priority)

    # Сериализует результат в CSV-формат
    return serialize_to_csv(minimal_columns)


# Пример использования
if __name__ == "__main__":
    json_file_path = 'example.json'  # Замените на путь к вашему JSON-файлу
    result = main(json_file_path)
    print(result)
