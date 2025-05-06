class circulo:
    def _init_(self):
        self.raio = 10
    def area(self):
        A = 3,14 * self.raio**2
        return A
    def circuferencia(self):
        C = 2 * 3,14 * self.raio
        return C

x = circulo()
x.raio = 5
print(x.area()) # o self e x
print(x.circuferencia()) # o self e x