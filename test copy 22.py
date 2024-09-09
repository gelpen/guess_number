class Product:
    # Опишите инициализатор класса и метод get_info()
    def __init__(self, product_name, quantity):
        self.product_name = product_name
        self.quantity = quantity

    def get_info(self):
        return f'{self.product_name} (в наличии: {self.quantity})'


class Kettlebell(Product):
    # Опишите инициализитор класса и метод get_weight()

    def __init__(self, product_name, quantity, weight):
        self.weight = weight
        super().__init__(product_name, quantity)

    def get_weight(self):
        return f'{self.product_name} (в наличии: {self.quantity}). Вес: {self.weight} кг'


class Clothing(Product):
    # Опишите инициализатор класса и метод get_size()
    def __init__(self, product_name, quantity, size):
        self.size = size
        super().__init__(product_name, quantity)

    def get_size(self):
        return f'{self.product_name} (в наличии: {self.quantity}). Размер: {self.size}'

# Для проверки вашего кода создадим пару объектов
# и вызовем их методы:

small_kettlebell = Kettlebell('Гиря малая', 15, 2)
shirt = Clothing('Футболка', 5, 'L')

print(small_kettlebell.get_weight())
print(shirt.get_size())