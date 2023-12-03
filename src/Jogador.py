import json


class Jogador:
    def __init__(self, id: str, nome: str, mao: list) -> None:
        self.__id = id
        self.__nome = nome
        self.__mao = mao

        self.__denunciavel = False
        self.__jogou_carta = False
        self.__comprou_carta = False
        self.__flex = True


    def getId(self):
        return self.__id
        
    def getNome(self):
        return self.__nome
    
    def setNome(self, nome):
        self.__nome = nome
        
    def getMao(self):
        return self.__mao
        
    def getDenunciavel(self):
        return self.__denunciavel
    
    def setDenunciavel(self, estado):
        self.__denunciavel = estado
    
    def getJogouCarta(self):
        return self.__jogou_carta

    def setJogouCarta(self, jogou):
        self.__jogou_carta = jogou
        
    def getComprouCarta(self):
        return self.__comprou_carta
    
    def setComprouCarta(self, comprou):
        self.__comprou_carta = comprou

    def gritarUno(self):
        self.__denunciavel = False

    def comprarCarta(self, baralho):
        self.__mao.insert(0, baralho.darCarta())
        self.__comprou_carta = True
        self.__denunciavel = False
    
    # para quando recebe punição
    def receberCartas(self, quantidade, baralho):  
        for _ in range(quantidade):
            self.__mao.insert(0, baralho.darCarta())

        self.__denunciavel = False
        
    def verificarDenunciavel(self):
        if len(self.__mao) == 1: 
            self.__denunciavel = True
    
    def getFlex(self):
        return self.__flex
    
    def setFlex(self, flex):
        self.__flex = flex
    
    def to_json(self) -> dict:
        a = json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_acceptable_string = a.replace("'", "\"")
        json_ = json.loads(json_acceptable_string)
        return json_