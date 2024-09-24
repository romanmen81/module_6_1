class Animal:
    def __init__(self, name):
        self.alive = True  # Живой
        self.fed = False   # Накормленный
        self.name = name   # Имя животного

    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Plant:
    def __init__(self, name):
        self.edible = False  # Съедобность
        self.name = name     # Имя растения


class Mammal(Animal):
    pass  # Здесь мы убираем метод eat, так как он теперь есть в Animal


class Predator(Animal):
    pass  # Здесь мы убираем метод eat, так как он теперь есть в Animal


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True  # Переопределяем, чтобы фрукт был съедобным


# Создание объектов
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

# Печатаем информацию о животных и растениях
print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)  # Хищник пытается съесть несъедобный цветок
a2.eat(p2)  # Млекопитающее ест съедобный фрукт
print(a1.alive)
print(a2.fed)
