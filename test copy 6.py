class Employee:
    def __init__(self, name, surname, since):
        if not isinstance(name, str):
            raise ValueError('Имя должно быть строкой')
        if not (2019 <= since <= 2024):
            raise ValueError('Год начала работы должен быть в диапазоне 2019–2024')
        self.name = name
        self.surname = surname
        self.since = since

    def show(self):
       print(self.name, self.surname, self.since)

mike = Employee('Михаил', 'Полянин', 2019)
mike.show()