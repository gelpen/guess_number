#Приватные атрибуты и методы
# Для Python атрибут или метод, имя которого начинается с 
# двойного подчёркивания __, — приватный. 
# К этому атрибуту можно обратиться внутри класса, а вот вне 
# класса просто так сделать это не получится.

class Phone:

    ...


class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        # Вот он - приватный атрибут.
        self.__network_type = network_type
        super().__init__(dial_type_value)

    def ring(self):
        print('Дзынь-дзынь!')

    def get_info(self):
        # Из метода класса можно обратиться к приватному атрибуту.
        print(
            f'Серийный №: {self._serial_number}, '
            f'тип сети: {self.__network_type}'
        )


mobile_phone_1 = Phone('дисковый')
mobile_phone_2 = MobilePhone('сенсорный', 'LTE')

# Вызвать метод, в котором используется приватный атрибут
mobile_phone_2.get_info()
# Вывести приватный атрибут на печать.
#print(mobile_phone_2.__network_type)


# Выведется:

# Серийный номер: 140169170458192, тип сети: LTE
# Traceback (most recent call last):
#  File "lesson.py", line 40, in <module>
#    print(mobile_phone_2.__network_type)
# AttributeError: 'MobilePhone' object has no attribute '__network_type'