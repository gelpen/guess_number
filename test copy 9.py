# Если есть несколько вариантов инициализации, нужно использовать 
# внутренние методы во избежание дублирования кода:

class MyClass:
    def __init__(self, value, flag):
        if flag:
            self._initialize_with_flag(value)
        else:
            self._initialize_without_flag(value)
    
    def _initialize_with_flag(self, value):
        self.value = value * 2
    
    def _initialize_without_flag(self, value):
        self.value = value


