import doctest


class Person:
    def __init__(self, name: str, age: int, weight: int):
        self.name = name
        if 0 < age < 100:
            self.age = age
        else:
            raise ValueError('Please enter a valid age value')
        if weight > 0:
            self.weight = weight
        else:
            raise ValueError('Please enter a valid weight value')

    def to_eat(self, meals_number: int):
        """If you eat, you gain 500g per meal.
        Usage example:
        >>> person_1.to_eat(2)
        'Now your weight is 71kg'
        """
        self.weight += int(meals_number * 0.5)
        return f'Now your weight is {self.weight}kg'

    def to_sleep(self) -> str:
        ...

    def to_work(self) -> str:
        ...


class Company:
    def __init__(self, name: str, address: str, staff: int):
        self.name = name
        self.address = address
        self.staff = staff

    def to_open(self) -> str:
        ...

    def to_work(self) -> str:
        ...

    def to_close(self) -> str:
        ...


class Movie:
    def __init__(self, title: str, release_date: int, language: str):
        self.title = title
        self.release_date = release_date
        self.language = language

    def to_promote(self):
        ...

    def to_got_watched(self):
        ...


person_1 = Person('Arthur', 35, 70)

if __name__ == "__main__":
    doctest.testmod()
