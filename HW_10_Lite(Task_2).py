def validate_user_input(value):
    # Проверка, что data является словарем
    if not isinstance(value, dict):
        raise TypeError("Data must be a dictionary")

    try:
        # Проверка типа значения (строка) для ключа 'name'
        if not isinstance(value['name'], str):
            raise ValueError("Name must be a string")

        # Проверка типа значения (число) для ключа 'age'
        if not isinstance(value['age'], int):
            raise TypeError(f"Age must be a positive integer not a {type(value['age']).__name__}")

        # Проверка ключа 'age' (положительное число)
        elif int(value['age']) <= 0:
            raise ValueError("Age must be a positive integer")



    except KeyError as ke:
        raise ValueError(f"Missing required key: {ke}")

# Корректный словарь
data = {"name": "Alice", "age": 30}

try:
    validate_user_input(data)
    print("Validation successful!")
except Exception as e:
    print(f"Validation failed: {e}")

# Словарь без ключа 'name'
# data = {"age": 30}

# Словарь где значение 'name' - число
data = {'name': 30, "age": 30}

try:
    validate_user_input(data)
    print("Validation successful!")
except Exception as e:
    print(f"Validation failed: {e}")

# Словарь со строковым значением для 'age'
data = {"name": "Bob", "age": "thirty"}

try:
    validate_user_input(data)
    print("Validation successful!")
except Exception as e:
    print(f"Validation failed: {e}")

# Словарь с отрицательным значением для 'age'
data = {"name": "Charlie", "age": -10}

try:
    validate_user_input(data)
    print("Validation successful!")
except Exception as e:
    print(f"Validation failed: {e}")

# Строка вместо словаря
data = "incorrect_data_type"

try:
    validate_user_input(data)
    print("Validation successful!")
except Exception as e:
    print(f"Validation failed: {e}")
