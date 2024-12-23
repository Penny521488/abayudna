result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("a меньше, чем b")
        if b > 100:
            raise IndexError("b больше 100")
        return a / b
    except ZeroDivisionError:
        print(f"Ошибка деления на ноль: a = {a}, b = {b}")
    except ValueError as ve:
        print(f"Ошибка значения: {ve}, a = {a}, b = {b}")
    except IndexError as ie:
        print(f"Ошибка индекса: {ie}, a = {a}, b = {b}")
    except TypeError as te:
        print(f"Ошибка типа: {te}, a = {a}, b = {b}")
    except Exception as e:
        print(f"Непредвиденная ошибка: {e}, a = {a}, b = {b}")
    return None

data = {10: 2, 2: 5, "123": 4, 18: 0, 8: 4}

for key in data:
    try:
        res = divider(key, data[key])
        result.append(res)
    except Exception as e:
        print(f"Ошибка обработки ключа {key}: {e}")

print(result)
