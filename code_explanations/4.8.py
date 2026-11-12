from abc import ABC, abstractmethod


class NumberBase(ABC):
    @abstractmethod
    def cube(self):
        raise NotImplementedError

    @abstractmethod
    def describe(self):
        raise NotImplementedError


class d(NumberBase):
    def __init__(self, value):
        self.value = value

    def cube(self):
        return self.value ** 3

    def describe(self):
        return f"The cube of {self.value} is {self.cube()}."


number = d(4)
print(number.cube())
print(number.describe())