# Конструктор дочернего класса может принимать дополнительные аргументы, 
# необходимые для инициализации новых параметров:

class Animal:
   def __init__(self, name, breed):
       self.name = name
       self.breed = breed

   def make_sound(self):
       pass

class Bird(Animal):
   def __init__(self, name, breed, can_fly):
       # Вызов конструктора родительского класса
       super().__init__(name, breed)
       self.can_fly = can_fly

   def make_sound(self):
       return "Чик-чирик!"

bird = Bird(name="Твити", breed="канарейка", can_fly=True)
print(bird.name)  # Твити
print(bird.breed)  # канарейка
print(bird.can_fly)  # True