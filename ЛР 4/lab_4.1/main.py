import json


def multiplication(score, weight) -> float:
    """Умножение двух чисел типа int или float"""
    if not (isinstance(score, float) or isinstance(score, int)):
        raise TypeError(f"У переменной score должен быть тип int или float, не {str(type(score))[8:-2]}")
    if not (isinstance(weight, float) or isinstance(weight, int)):
        raise TypeError(f"У переменной weight должен быть тип int, не {str(type(weight))[8:-2]}")
    return score*weight


def task(filename) -> float:
    """считывание значений из файла с суммированием
    произведений значений в представленных словарях"""
    values_sum = 0

    with open(filename, "r") as f:
        data = json.load(f)

    for string in data:
        values_sum += multiplication(string["score"], string["weight"])

    return round(values_sum, 3)


if __name__ == "__main__":
    print(task("input.json"))
