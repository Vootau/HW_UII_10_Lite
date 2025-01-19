
def convert_to_int(x):
    try:
        result = int(x)
    except ValueError:
        print(f'Ошибка: "{x}" должно быть числом, а это {type(x)}')
    except TypeError:
        print(f'Ошибка "{x}" должно быть числом, а это {type(x)}')
    except Exception as e:
        print(f'Упс! Ошибка: {e}')
    else:
        print(f'Успешное преобразование: {result} теперь {type(result)}')
    finally:
        print('\tПреобразование выполнено')


convert_to_int(123)

convert_to_int([1,2,3])

convert_to_int("abc")





