class Ingredient:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return f'{self.name}, {self.size} ml'

# sparkled
# Primary Key - такой столбец в таблице,
# что по нему можно найти только запись в этой таблице

# Foreign Key - внешний ключ - первыичный ключ из другой таблицы
