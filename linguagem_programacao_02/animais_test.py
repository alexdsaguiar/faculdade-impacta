import unittest

from animais import Gato
from animais import Cobra

gato_01 = Gato("nomeGato", "marron", 1, "pataGato")

cobra_01 = Cobra("nomeCobra", "marrom", 1, True )

print(gato_01.nome, gato_01.cor_pelo, gato_01.idade, gato_01.tipo_pata)
print(gato_01.miar())
print(gato_01.morrer())
print(gato_01.morrer())
print(gato_01.morrer())
print(gato_01.morrer())
print(gato_01.morrer())
print(gato_01.morrer())
print(gato_01.morrer())
print(gato_01.morrer())
print(gato_01.mamar())

print(cobra_01.veneno)