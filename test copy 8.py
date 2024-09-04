# Иногда полезно вынести часть инициализации в отдельные 
# методы для упрощения конструктора и улучшения читаемости кода:

class Employee:
   def __init__(self, name, surname, since):  # Замена точки на запятую
       self.name = name
       self.surname = surname
       self.set_since(since)

   def set_since(self, since):
       if not (2019 <= since <= 2024):
           raise ValueError('Год начала работы должен быть в диапазоне 2019–2024')
       self.since = since

ira = Employee('Ира', 'Михеева', 2019)