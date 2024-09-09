class Customer:
    def __init__(self, name):
        self.name = name
        # Добавьте сюда атрибут "скидка" со значением по умолчанию 10.
        self.__discount = 10

    # Реализуйте методы get_price() и set_discount().
    def get_price(self, original_price):
        return round(original_price - ((original_price * self.__discount) / 100), 2)

    def set_discount(self, new_discount):
        if new_discount > 80:
            self.__discount = 80
        else:
            self.__discount = new_discount


# Создаем экземпляр класса Customer
customer = Customer("Иван Иванович")

# Получаем цену с учетом скидки
price_with_discount = customer.get_price(100)
print(f"Цена с учетом скидки: {price_with_discount}")

# Устанавливаем новую скидку
customer.set_discount(80)

# Получаем цену с обновленной скидкой
price_with_updated_discount = customer.get_price(100)
print(f"Цена с обновленной скидкой: {price_with_updated_discount}")
