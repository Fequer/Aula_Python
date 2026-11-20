class Pessoa:
    "Isto é uma classe nova chamada Pessoa"
    idade = 15;
    
    def saudacao(self):
        print('Óla pessoas!')

print(Pessoa.idade)
print(Pessoa.saudacao)
print(Pessoa.__doc__)

felipe = Pessoa()
print(felipe.idade)
print(felipe.saudacao)

felipe.saudacao()

#-----------------------------#

import math

class Esfera:
    def __init__(self, cor, raio):
        self.cor = cor
        self.raio = raio
    def volume(self):
        vol = (4/3) * math.pi * (self.raio ** 3)
        return vol
    def area(self):
        ar = 4 * math.pi * (self.raio ** 2)
        return ar

bola1 = Esfera('vermelha', 4)
bola2 = Esfera('azul', 7)
bola3 = Esfera('verde', 10)

print(f'O volume da bola 1 é: {bola1.volume()} cm³' )
print(f'A área superficial da bola 1 é: {bola1.area()} cm²' )

print(bola1.volume())
print(Esfera.volume(bola1))

#-----------------------------#
