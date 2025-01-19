def validate_user_input(value):
    # Проверка, что data является словарем
    if not isinstance(value, dict):
        raise TypeError("Данные должны быть словарем.")

    try:
        # Проверка типа значения (строка) для ключа 'name'
        if not isinstance(value['name'], str):
            raise ValueError("Ключ 'name' должен быть строкой.")

        # Проверка типа значения (число) для ключа 'age'
        if not isinstance(value['age'], int):
            raise TypeError(f"Значение ключа 'age' должно быть числом, а не {type(value['age']).__name__}.")

        # Проверка ключа 'age' (положительное число)
        elif int(value['age']) <= 0:
            raise ValueError("Возраст не может быть меньше 0.")

    except KeyError as ke:
        raise ValueError(f"Отсутсвует нужный ключ: {ke}")

# Корректный словарь
data = {"name": "Alice", "age": 30}

try:
    validate_user_input(data)
    print("Валидация успешна!")
except Exception as e:
    print(f"Валидация провалена: {e}")

# Словарь без ключа 'name'
# data = {"age": 30}

# Словарь где значение 'name' - число
data = {'name': 30, "age": 30}

try:
    validate_user_input(data)
    print("Валидация успешна!")
except Exception as e:
    print(f"Валидация провалена: {e}")

# Словарь со строковым значением для 'age'
data = {"name": "Bob", "age": "thirty"}

try:
    validate_user_input(data)
    print("Валидация успешна!")
except Exception as e:
    print(f"Валидация провалена: {e}")

# Словарь с отрицательным значением для 'age'
data = {"name": "Charlie", "age": -10}

try:
    validate_user_input(data)
    print("Валидация успешна!")
except Exception as e:
    print(f"Валидация провалена: {e}")

# Строка вместо словаря
data = "какие-то данные"

try:
    validate_user_input(data)
    print("Валидация успешна!")
except Exception as e:
    print(f"Валидация провалена: {e}")
