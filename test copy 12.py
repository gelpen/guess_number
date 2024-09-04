class MushroomsCollector:
    # Проверьте, нет ли здесь ошибки:
    def __init__(self):
        self.mushrooms = []

    def is_poisonous(self, mushroom_name):
        self.mushroom_name = mushroom_name
        if self.mushroom_name == 'Мухомор' or self.mushroom_name == 'Поганка':
            return True
        return False

    # Допишите метод.
    def add_mushroom(self, mushroom_name):
        self.mushroom_name = mushroom_name
        if self.is_poisonous(self.mushroom_name):
            print('Нельзя добавить ядовитый гриб')
        else:
            list.append(self.mushrooms, mushroom_name)
    # Напишите магический метод __str__,
    # возвращающий перечень грибов из списка mushrooms
    # через запятую.

    def __str__(self):
        result = ', '.join(map(str, self.mushrooms))
        return result


# Пример запуска для самопроверки
collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1)
print(collector_2)
