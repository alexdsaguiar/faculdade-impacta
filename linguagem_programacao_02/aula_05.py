class VeiculoAutomotor():

    @property    
    def Motorizacao(self):
        return self.__Motorizacao
    
    @Motorizacao.setter
    def Motorizacao(self, value):
        self.__Motorizacao = value

    def Ligar(self):
        return True

    def Brecar(self):
        return True

Fusca = VeiculoAutomotor()
Fusca.Motorizacao = 1000
print(Fusca.Motorizacao)
Fusca.Brecar()
