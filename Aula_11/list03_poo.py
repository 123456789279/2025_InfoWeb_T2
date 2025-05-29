# 1 - Um Retangulo
class Retangulo:
    def __init__(self):
        self.__base = ""
        self.__altura = ""
    def set__base(self, base):
        if base < 0: raise ValueError("A base deve ser maior que 0")
        self.__base = base
    def set__altura(self, altura):
        if altura < 0: raise ValueError("A altura deve ser maior que 0")
        self.__altura = altura
    def get__base(self):
        return self.__base
    def get__altura(self):
        return self.__altura
    def calcular_area(self):
        return self.__base * self.__altura
    def calcular_diagonal(self):
        return (self.__base ** 2 + self.__altura ** 2) ** 0.5

x = Retangulo()
x.set__base(10)
x.set__altura(20)
print(x.calcular_area())
print(x.calcular_diagonal())

# 2 - Um Frete