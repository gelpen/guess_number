class Employee:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position

    def show(self):
        print(self.name, self.surname, self.position)

ira = Employee('Ира', 'Михеева', 'корректор')
ira.show()

masha = Employee('Маша', 'Климентьева', 'Руководитель группы контент-менеджеров')
masha.show()