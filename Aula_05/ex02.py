class viagem:
    def _init_(self):
        self.distancia = 20
        self.tempo = 8.00
    def velocidade_media(self):
        vm = self.distancia / self.tempo
        return vm

x = viagem()
x.distancia = 25
x.tempo = 8.30
print(x.velocidade_media()) # o self e x