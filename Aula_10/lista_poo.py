#1 - Circulo
class circulo:
    def _init_(self):
        self.__raio = 10
    def set_area(self):
        A = 3,14 * self.__raio**2
        return A
    def get_circuferencia(self):
        C = 2 * 3,14 * self.__raio
        return C
    
x = circulo()
x.__raio = 5
print(x.set__area()) # o self e x
print(x.get__circuferencia()) # o self e x    

#2 - Uma Viagem
class viagem:
    def _init_(self):
        self.distancia = 200
        self.tempo = 2
    def velocidade_media(self):
        vm = self.distancia / self.tempo
        return vm

x = viagem()
x.distancia = 200
x.tempo = 4
print(x.velocidade_media()) # o self e x




