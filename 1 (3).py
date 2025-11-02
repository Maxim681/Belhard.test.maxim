def manage_zoo(*args: str, **kwargs: int) -> dict:
    if not args:
        raise ValueError("Нет животных")

    # Функция проверки типа
    def check_animal(animal):
        return isinstance(animal, str)

    # Сортировка lambda по длине
    sorted_args = sorted(args, key=lambda x: len(x))

    return {
        'sorted': sorted_args,
        'attrs': kwargs
    }


# Вызовы функции
print("=== Зоопарк 1 ===")
res1 = manage_zoo("слон", "тигр", "кот", age=5)
print(f"Животные: {res1['sorted']}")
print(f"Данные: {res1['attrs']}")

print("\n=== Зоопарк 2 ===")
res2 = manage_zoo("жираф", "лев", "ящерица", "енот", вес=10, возраст=3)
animals_str = " -> ".join(res2['sorted'])
print(f"В порядке: {animals_str}")
print(f"Параметры: {len(res2['sorted'])} животных")

print("\n=== Зоопарк 3 (ошибка) ===")
try:
    res3 = manage_zoo()
except ValueError as e:
    print(f"Проблема: {e}")