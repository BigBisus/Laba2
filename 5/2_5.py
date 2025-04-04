
numbers = list(range(1, 21))
print("Исходный список:", numbers)

# Фильтрация: оставляем только чётные числа
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Четные числа:", even_numbers)

# Применяем лямбда-функцию для увеличения каждого числа на 10
increased_numbers = list(map(lambda x: x + 10, numbers))
print("Список после увеличения на 10:", increased_numbers)

# Сортировка исходного списка по убыванию
sorted_numbers = sorted(numbers, key=lambda x: x, reverse=True)
print("Список, отсортированный по убыванию:", sorted_numbers)

