from random import randint
from Baralho import Baralho


class Mesa:
    def __init__(self, baralho: Baralho) -> None:
        self.__baralho = baralho
        self.setCartaInicial()

    def getUltimaCarta(self):
        return self.__ultima_carta

    def setUltimaCarta(self, carta):
        self.__ultima_carta = carta

    def setCartaInicial(self):
        carta = self.__baralho.getCartas().pop()
        self.setUltimaCarta(carta)
        if carta.getFrente().getTipo() == "coringa":
            self.__baralho.getCartas().insert(
                randint(0, len(self.__baralho.getCartas()) - 2), carta
            )
            self.setCartaInicial()

    def getBaralho(self) -> Baralho:
        return self.__baralho
