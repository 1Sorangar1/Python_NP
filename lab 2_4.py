import doctest
from typing import Union


class Car:
    """Базовый класс машины. """
    def __init__(self, name: str, weight_kg: Union[int, float], color: str, brand: str, wheels_number: int):
        """
        Создание и подготовка к работе класса 'Машина'
        :param name: Названия и модель машины
        :param color: Цвет машины
        :param weight_kg: Вес машины в килограммах
        :param brand: Марка автомобиля
        :param wheels_number: Количество колёс у машины

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4) # инициализация экземпляра класса

        """
        self._name = name
        self._brand = brand
        self.weight_kg = weight_kg
        self.color = color
        self.wheels_number = wheels_number

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователей

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.__str__()
        'Автомобиль Rio производителя Kia, вес 2000 кг, цвет black, 4 колеса'

        """
        return f"Автомобиль {self.name} производителя {self.brand}, вес {self.weight_kg} кг, " \
               f"цвет {self.color}, {self.wheels_number} колеса"

    def __repr__(self):
        """
        Возвращает информацию об объекте класса для разработчиков

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.__repr__()
        "Car(name='Rio', weight=2000, color='black', brand='Kia', wheels_number=4)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight_kg!r}, " \
               f"color={self.color!r}, brand={self.brand!r}, wheels_number={self.wheels_number})"

    def remove_wheels(self, wheels_remove: int) -> int:
        """
        Удаление колёс с автомобиля

        :param wheels_remove: количество удаляемых колёс

        :return: текущее количество колёс автомобиля

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.remove_wheels(2)
        2
        """

        if not isinstance(wheels_remove, int):
            raise TypeError("Количество удаляемых колёс автомобиля должно быть целым числом")
        if wheels_remove < 0:
            raise ValueError("Количество удаляемых колёс автомобиля не может быть меньше 0")
        if self.wheels_number < wheels_remove:
            raise ValueError("Количество колёс автомобиля не может быть меньше 0")
        self.wheels_number -= wheels_remove
        return self.wheels_number

    def add_weight_kg(self, new_weight_kg: Union[int, float]) -> Union[int, float]:
        """
        Добавление веса автомобилю
        :param new_weight_kg: Вес добавляемого груза в килограммах

        :return: Текущий вес автомобиля

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.add_weight_kg(15)
        2015
        """
        if not isinstance(new_weight_kg, (int, float)):
            raise TypeError("Добавляемый вес должен быть величиной типа int или float")
        if new_weight_kg < 0:
            raise ValueError("Добавляемый вес должен быть больше 0")
        self.weight_kg += new_weight_kg
        return self.weight_kg

    @property
    def name(self) -> str:
        """
        Возвращает название автомобиля

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.name
        'Rio'
        """
        return self._name

    @property
    def brand(self) -> str:
        """
        Возвращает марку автомобиля

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.brand
        'Kia'
        """
        return self._brand

    @property
    def weight_kg(self) -> float:
        """
        Возвращает вес автомобиля в килограммах

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.weight_kg
        2000
        """
        return self._weight_kg

    @property
    def color(self) -> str:
        """
        Возвращает цвет автомобиля

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.color
        'black'
        """
        return self._color

    @property
    def wheels_number(self) -> int:
        """
        Возвращает количество колёс у автомобиля

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.wheels_number
        4
        """
        return self._wheels_number

    @weight_kg.setter
    def weight_kg(self, new_weight_kg: Union[int, float]) -> None:
        """
        Устанавливает вес автомобиля в килограммах

        :param new_weight_kg: Устанавливаемый вес автомобиля в килограммах

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.weight_kg = 15
        """
        if not isinstance(new_weight_kg, (int,float)):
            raise TypeError("Вес автомобиля должен быть типа int или float")
        if new_weight_kg <= 0:
            raise ValueError("Вес автомобиля должен быть положительным числом")
        self._weight_kg = new_weight_kg

    @color.setter
    def color(self, new_color: str) -> None:
        """
        Устанавливает цвет автомобиля

        :param new_color: Новый цвет автомобиля

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.color = "Black"
        """
        if not isinstance(new_color, str):
            raise TypeError("Цвет автомобиля должен быть строкой")
        self._color = new_color

    @wheels_number.setter
    def wheels_number(self, new_wheels_number: int) -> None:
        """
        Устанавливает количество колёс автомобиля

        :param new_wheels_number: Устанавливаемое количество колёс автомобиля

        Пример:
        >>> Car1 = Car("Rio", 2000, "black", "Kia", 4)
        >>> Car1.wheels_number = 6
        """
        if not isinstance(new_wheels_number, int):
            raise TypeError("Количество колёс автомобиля должно быть целым числом")
        if new_wheels_number < 0:
            raise ValueError("Количество колёс автомобиля не может быть меньше 0")
        self._wheels_number = new_wheels_number


class FreightCar(Car):
    def __init__(self, name: str, weight_kg: Union[int, float], color: str, brand: str,
                 wheels_number: int, cargo_weight: Union[int, float], cargo_name: str):
        """
        Создание и подготовка к работе подкласса класса 'Машина' 'Грузовая машина'
        :param name: Названия и модель машины
        :param color: Цвет машины
        :param weight_kg: Вес машины в килограммах
        :param brand: Марка автомобиля
        :param wheels_number: Количество колёс у машины
        :param cargo_weight: Вес груза
        :param cargo_name: Название груза

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse") # инициализация экземпляра класса

        """
        self.cargo_name = cargo_name
        self.cargo_weight = cargo_weight
        super().__init__(name, weight_kg, color, brand, wheels_number)

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователей

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse")
        >>> Car2.__str__()
        'Автомобиль Rio производителя Kia, вес 2000 кг, цвет black, 4 колеса'
        """
        return super().__str__()

    def __repr__(self):
        """
        Возвращает информацию об объекте класса для разработчиков. Метод перегружен из-за появления
        новых параметров: cargo_weight, cargo_name.

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse")
        >>> Car2.__repr__()
        "FreightCar(name='Rio', weight=2000, color='black', brand='Kia', wheels_number=4, cargo_name='Corpse', cargo_weight=70)"
        """
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight_kg!r}, " \
               f"color={self.color!r}, brand={self.brand!r}, wheels_number={self.wheels_number}," \
               f" cargo_name={self.cargo_name!r}, cargo_weight={self.cargo_weight!r})"

    def remove_wheels(self, wheels_remove: int) -> int:
        """
        Удаление колёс с автомобиля

        :param wheels_remove: количество удаляемых колёс

        :return: текущее количество колёс автомобиля

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse")
        >>> Car2.remove_wheels(2)
        2
        """
        return super().remove_wheels(wheels_remove)

    def add_weight_kg(self, new_weight_kg: Union[int, float]) -> Union[int, float]:
        """
        Добавление веса автомобилю
        Метод перегружен из-за наличия максимального веса у астомобиля
        :param new_weight_kg: Вес добавляемого груза в килограммах

        :return: Текущий вес автомобиля

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse")
        >>> Car2.add_weight_kg(15)
        2015
        """
        if not isinstance(new_weight_kg, (int, float)):
            raise TypeError("Добавляемый вес должен быть величиной типа int или float")
        if new_weight_kg < 0:
            raise ValueError("Добавляемый вес должен быть больше 0")
        self.weight_kg += new_weight_kg
        if self.weight_kg >= 20000:
            raise ValueError("бщий вес грузового автомобиля не должен превышать 20000кг")
        return self.weight_kg

    @property
    def cargo_name(self) -> str:
        """
        Возвращает название груза

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse")
        >>> Car2.cargo_name
        'Corpse'
        """
        return self._cargo_name

    @property
    def cargo_weight(self) -> float:
        """
        Возвращает вес груза

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse")
        >>> Car2.cargo_weight
        70
        """
        return self._cargo_weight

    @cargo_weight.setter
    def cargo_weight(self, new_cargo_weight: Union[int, float]) -> None:
        """
        Устанавливает вес груза

        :param new_cargo_weight: Устанавливаемый вес груза

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse")
        >>> Car2.cargo_weight = 65
        """
        if not isinstance(new_cargo_weight, (float,int)):
            raise TypeError("Вес груза должен быть числом")
        if new_cargo_weight <= 0:
            raise ValueError("Вес груза должен быть положительным числом")
        self._cargo_weight = new_cargo_weight

    @cargo_name.setter
    def cargo_name(self, new_cargo_name: str) -> None:
        """
        Устанавливает название груза

        :param new_cargo_name: Устанавливаемое название груза

        Пример:
        >>> Car2 = FreightCar("Rio", 2000, "black", "Kia", 4, 70, "Corpse")
        >>> Car2.cargo_name = "Body"
        """
        if not isinstance(new_cargo_name, str):
            raise TypeError("Название груза должно быть строкой")
        self._cargo_name = new_cargo_name


class PassengerCar(Car):
    def __init__(self,name: str, weight_kg: Union[int, float], color: str, brand: str,
                 wheels_number: int, passengers_number: int):
        """
                Создание и подготовка к работе подкласса класса 'Машина' 'Грузовая машина'
                :param name: Названия и модель машины
                :param color: Цвет машины
                :param weight_kg: Вес машины в килограммах
                :param brand: Марка автомобиля
                :param wheels_number: Количество колёс у машины
                :param passengers_number: Количество пассажиров

                Пример:
                >>> Car3 = PassengerCar("Rio", 2000, "black", "Kia", 4, 5) # инициализация экземпляра класса

                """
        self.passengers_number = passengers_number
        super().__init__(name, weight_kg, color, brand, wheels_number)

    def __str__(self):
        """
        Возвращает информацию об объекте класса для пользователей

        Пример:
        >>> Car3 = PassengerCar("Rio", 2000, "black", "Kia", 4, 5)
        >>> Car3.__str__()
        'Автомобиль Rio производителя Kia, вес 2000 кг, цвет black, 4 колеса'
        """
        return super().__str__()

    def __repr__(self):
        """ Возвращает информацию об объекте класса для разработчиков. Метод перегружен из-за появления
         новых параметров: passengers_number

        Пример:
         >>> Car3 = PassengerCar("Rio", 2000, "black", "Kia", 4, 5)
         >>> Car3.__repr__()
         "PassengerCar(name='Rio', weight=2000, color='black', brand='Kia', wheels_number=4,passengers_number=5)"
         """
        return f"{self.__class__.__name__}(name={self.name!r}, weight={self.weight_kg!r}, " \
               f"color={self.color!r}, brand={self.brand!r}, wheels_number={self.wheels_number}," \
               f"passengers_number={self.passengers_number!r})"

    def remove_wheels(self, wheels_remove: int) -> int:
        """
        Удаление колёс с автомобиля

        :param wheels_remove: количество удаляемых колёс

        :return: текущее количество колёс автомобиля
        """
        return super().remove_wheels(wheels_remove)

    def add_weight_kg(self, new_weight_kg: Union[int, float]) -> Union[int, float]:
        """
        Добавление веса автомобилю

        Метод перегружен из-за наличия максимального веса у астомобиля

        :param new_weight_kg: Вес добавляемого груза в килограммах

        :return: Текущий вес автомобиля

        Пример:
        >>> Car3 = PassengerCar("Rio", 2000, "black", "Kia", 4, 5)
        >>> Car3.add_weight_kg(20)
        2020
        """
        if not isinstance(new_weight_kg, (int, float)):
            raise TypeError("Добавляемый вес должен быть величиной типа int или float")
        if new_weight_kg < 0:
            raise ValueError("Добавляемый вес должен быть больше 0")
        self.weight_kg += new_weight_kg
        if self.weight_kg >= 5000:
            raise ValueError("бщий вес грузового автомобиля не должен превышать 5000кг")
        return self.weight_kg

    @property
    def passengers_number(self):
        """
        Возвращает количество пассажиров в автомобиле

        Пример:
        >>> Car3 = PassengerCar("Rio", 2000, "black", "Kia", 4, 5)
        >>> Car3.passengers_number
        5
        """
        return self._passengers_number

    @passengers_number.setter
    def passengers_number(self, new_passengers_number):
        """
        Устанавливает количество пассажиров в автомобиле

        :param new_passengers_number: Устанавливаемое количество пассажиров

        Пример:
        >>> Car3 = PassengerCar("Rio", 2000, "black", "Kia", 4, 5)
        >>> Car3.passengers_number = 2
        """
        if not isinstance(new_passengers_number, int):
            raise TypeError("Количество пассажиров должно быть числом")
        if new_passengers_number < 0:
            raise ValueError("Количество пассажиров не может быть меньше 0")
        self._passengers_number = new_passengers_number


if __name__ == "__main__":
    doctest.testmod()
