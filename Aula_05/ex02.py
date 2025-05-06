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