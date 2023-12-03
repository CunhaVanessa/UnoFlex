class Face:
    def __init__(self, id: str, cor: str, simbolo: str, tipo: str) -> None:
        self.__id = id
        self.__cor = cor
        self.__simbolo = simbolo
        self.__tipo = tipo

    def getId(self) -> str:
        return self.__id
    
    def setId(self, id: str) -> None:
        self.__id = id 

    def getCor(self) -> str:
        return self.__cor
    
    def setCor(self, cor: str) -> None:
        self.__cor = cor

    def getSimbolo(self) -> str:
        return self.__simbolo

    def getTipo(self) -> str:
        return self.__tipo
