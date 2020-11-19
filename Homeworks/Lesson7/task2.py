from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def fabric_cons(self):
        pass


class Coat(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.v = size

    @property
    def fabric_cons(self):
        print(F'Расход ткани на пальто "{self.name}" составит {(self.v / 6.5 + 0.5):.2f} ')


class Suit(Clothes):
    def __init__(self, name, size):
        self.name = name
        self.h = size

    @property
    def fabric_cons(self):
        print(F'Расход ткани на костюм "{self.name}" составит {(2 * self.h + 0.3):.2f} ')


c = Coat('Осеннее', 48)
s = Suit('Смокинг', 50)

c.fabric_cons
s.fabric_cons
