# Статический метод 

class Image:

    test_11 = 11

    def __init__(self, resolution, title='123', extension='321'):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_resolution):
        Image.test_11 += 11
        self.resolution = new_resolution
        # print(self.resolution)

    @staticmethod # Статический метод 
    def merge(first, second):
        return f'{first} {second}'


m_1 = Image.merge('привет', 'пока')
print(m_1)

m_2 = Image(500)
m_3 = m_2.merge(5, 10)
print(m_3)