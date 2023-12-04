import doctest
from typing import Union


# TODO Написать 3 класса с документацией и аннотацией типов
class Car:
    def __init__(self, color: str, free_seat_number: int, brand: str, broken: bool):
        """
        Создание и подготовка к работе класса 'Машина'
        :param color: Цвет машины
        :param free_seat_number: Количество свободных сидений автомобиля
        :param brand: Марка автомобиля
        :param broken: Является ли машина сломанной

        Пример:
        >>> car1 = Car("red", 5, "Audi", False) # инициализация экземпляра класса

        """
        if not isinstance(color, str):
            raise TypeError("Цвет автомобиля должен быть строкой!")
        self.color = color

        if not isinstance(free_seat_number, int):
            raise TypeError("Количество свободных людей должно быть типа int")
        if free_seat_number < 0:
            raise ValueError("Свободных сидений в автомобил не может быть меньше 0!")
        self.free_seat_number = free_seat_number

        if not isinstance(brand, str):
            raise TypeError(" Марка автомобиля должна быть строкой!")
        self.brand = brand

        if not isinstance(broken, bool):
            raise TypeError("Факт поломки машины должен быть типа bool")
        self.broken = broken

    def recolor(self, new_color: str) -> None:
        """
        Смена цвета автомобиля

        :param new_color: Новый цвет автомобиля

        Примеры:
        >>> car1 = Car("red", 5, "Audi", False)
        >>> car1.recolor("green")
        """
        if not isinstance(new_color, str):
            raise TypeError("Цвет автомобиля должен быть строкой!")
        ...

    def take_a_seat(self, new_people: int) -> None:
        """
        Занятие свободных мест автомобиля

        :param new_people: Количество людей, занимающих свободные места

        Примеры:
        >>> car1 = Car("red", 5, "Audi", False)
        >>> car1.take_a_seat(2)
        """

        if not isinstance(new_people, int):
            raise TypeError("Количество занимаемых мест должно быть типа int")
        ...

    def is_broken(self) -> bool:
        """
        Проверка машины на факт поломки

        :return: Является ли машина сломанной

        Примеры:
        >>> car1 = Car("red", 5, "Audi", False)
        >>> car1.is_broken()

        """
        ...


class Animal:
    def __init__(self, color: str, height: Union[int, float], wild: bool):
        """
        Создание и подготовка к работе класса 'Животное'
        :param color: Цвет животного
        :param height: Высота животного
        :param wild: Дикое ли животное

        Пример:
        >>> animal1 = Animal("brown", 1.75, True) # инициализация экземпляра класса

        """

        if not (isinstance(color, str)):
            raise TypeError("Цвет должен быть типа str")
        self.color = color

        if not (isinstance(height, (int, float))):
            raise TypeError("Высота животного должна быть типа int или float")
        if height <= 0:
            raise ValueError("Высота животного должна быть больше 0")
        self.height = height

        if not (isinstance(wild, bool)):
            raise TypeError("Дикость животного должно быть типа bool")
        self.wild = wild

    def ride(self) -> bool:
        """
        Проверка на факт того, можно ли оседлать животное

        :return: Можно ли оседлать животное

        Примеры:
        >>> animal1 = Animal("brown", 1.75, True)
        >>> animal1.ride()
        """
        ...


    def pet(self) -> bool:
        """
        Проверка на факт того, можно ли приласкать животное

        :return: Можно ли приласкать животное

        Примеры:
        >>> animal1 = Animal("brown", 1.75, True)
        >>> animal1.pet()
        """
        ...


class Sword:
    def __init__(self, durability: Union[int, float], sharpness: Union[int, float]):
        """
        Создание и подготовка к работе класса 'Меч'
        :param durability: Прочность меча
        :param sharpness: Острота меча

        Пример:
        >>> sword1 = Sword(50, 100) # инициализация экземпляра класса

        """

        if not(isinstance(durability, (int, float))):
            raise TypeError("Прочность меча должна быть типа int или float")
        if durability < 0:
            raise ValueError("Прочность меча не может быть меньше 0!")
        self.durability = durability

        if not(isinstance(sharpness, (int, float))):
            raise TypeError("Острота меча должна быть типа int или float")
        if sharpness < 0:
            raise ValueError("Острота меча не может быть меньше 0!")
        self.sharpness = sharpness


    def slice(self, object_durability) -> None:
        """
        Разрезание мечом объекта

        :param object_durability: Прочность объекта

        Примеры:
        >>> sword1 = Sword(50, 100)
        >>> sword1.slice(10)
        """
        ...


    def sharpening(self) -> None:
        """
        Заточка меча

        Примеры:
        >>> sword1 = Sword(50, 100)
        >>> sword1.sharpening()
        """
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
