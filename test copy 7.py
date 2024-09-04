# Параметры могут быть не только простыми типами данных,
# но и сложными объектами, такими как списки, словари
# или даже представители других классов.

class Media:
    def __init__(self, type, name):
        self.type = type
        self.name = name


class Editorial:
    def __init__(self, name, surname, position, media):
        self.name = name
        self.surname = surname
        self.position = position
        self.media = media

    def show(self):
        print(self.name, self.surname, self.position,
              self.media.type, self.media.name)


media = Media('Журнал', '"Код"')
mike = Editorial('Михаил', 'Полянин', 'главный редактор', media)
mike.show()
