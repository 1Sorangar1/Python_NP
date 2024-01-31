from typing import Union

class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)

        if not isinstance(pages, int):
            raise TypeError("Длина книги в страницах должна быть представлена целым числом!")
        if pages <= 0:
            raise ValueError("Длина книги в страницах должна быть больше 0!")
        self.pages = pages

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: Union[int, float]):
        super().__init__(name, author)

        if not isinstance(duration, (int, float)):
            raise TypeError("Продолжительность аудиокниги должна быть представлена числом!")
        if duration <= 0:
            raise ValueError("Продолжительность аудиокниги должна быть больше 0!")
        self.duration = duration

    def __str__(self):
        return super().__str__()

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

