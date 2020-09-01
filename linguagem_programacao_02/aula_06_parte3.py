class Ignicao():
    def Ligar(self):
        return "Vrum"

class Frenagem():
    def Brecar(self):
        acao = "Brecar com 2 rodas"
        return acao

class VeiculoAutomotor(Frenagem, Ignicao):
    def Buzinar(self, vezes):
        return vezes
    def Brecar(self):
        return super().Brecar()

Fusca = VeiculoAutomotor()
print(Fusca.Brecar())