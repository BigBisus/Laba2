def main():
    try:
        # Открываем файл data.txt для чтения
        with open('data.txt', 'r', encoding='utf-8') as file:
            numbers = []
            # Читаем файл построчно
            for line in file:
                line = line.strip()  # Удаляем лишние пробелы и символы переноса строки
                if line:  # Если строка не пустая
                    try:
                        num = float(line)  # Преобразуем строку в число
                        numbers.append(num)
                    except ValueError:
                        print(f"Не удалось преобразовать строку '{line}' в число.")

        if numbers:
            total = sum(numbers)
            average = total / len(numbers)
            maximum = max(numbers)
            minimum = min(numbers)

            # Формируем строку с результатами
            result_text = (
                f"Сумма: {total}\n"
                f"Среднее: {average}\n"
                f"Максимум: {maximum}\n"
                f"Минимум: {minimum}\n"
            )

            # Записываем результаты в файл result.txt
            with open('result.txt', 'w', encoding='utf-8') as result_file:
                result_file.write(result_text)

            print("Результаты вычислений записаны в файл result.txt")
        else:
            print("Файл data.txt не содержит чисел.")
    except FileNotFoundError:
        print("Файл data.txt не найден. Создайте файл с 10 строками чисел.")


if __name__ == '__main__':
    main()
