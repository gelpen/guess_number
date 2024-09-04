class BacteriaProducer:
    caunt_bacteria = 0
    # Допишите инициализатор класса

    def __init__(self, max_bacteria):
        self.max_bacteria = max_bacteria

    # Допишите метод
    def create_new(self):
        if self.caunt_bacteria < self.max_bacteria:
            self.caunt_bacteria += 1
            print(
                f'Добавлена одна бактерия. Количество бактерий в популяции: {self.caunt_bacteria}')
        else:
            print(f'Нет места под новую бактерию')
    # Допишите метод

    def remove_one(self):
        if self.caunt_bacteria > 0:
            self.caunt_bacteria -= 1
            print(
                f'Одна бактерия удалена. Количество бактерий в популяции: {self.caunt_bacteria}')
        else:
            print(f'В популяции нет бактерий, удалять нечего')


# Пример запуска для самопроверки
bacteria_producer = BacteriaProducer(max_bacteria=3)
bacteria_producer.remove_one()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.create_new()
bacteria_producer.remove_one()
