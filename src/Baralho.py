from Carta import Carta
from Face import Face
from random import shuffle
import json
class Baralho():
    
    def __init__(self) -> None:
        self.__cartas = []
        self.criar_baralho()

    def getCartas(self):
        return self.__cartas

    def setCartas(self, cartas: list) -> None:
        self.__cartas = cartas

    def criar_baralho(self) -> None:
        cores = ['amarelo','vermelho', 'azul','verde']
        
        aux = []

        pos = [23,34,45,56]
        pos_flex = [67,78,89,100]

        for i in range(4):
            for j in range(1,10):
                face_numerica = Face(f'card_{pos[i]+j-1}',cores[i],str(j),'numerica')
                for _ in range(2):
                    aux.append(face_numerica)

            face_compre_um = Face(f'card_{pos[i]+10}',cores[i],'mais_um','colorida_poder')
            for _ in range(2):
                aux.append(face_compre_um)

            face_pular_vez = Face(f'card_{pos[i]+11}',cores[i],'pular_vez','colorida_poder')
            for _ in range(2):
                aux.append(face_pular_vez)
            
            face_inverter_ordem = Face(f'card_{pos[i]+12}',cores[i],'inverter_ordem','colorida_poder')
            for _ in range(2):
                aux.append(face_inverter_ordem)

            face_coringa1 = Face(f'card_1',cores[i],'troca_cor','coringa')
            for _ in range(2):
                aux.append(face_coringa1)

            face_mais_dois = Face(f'card_6',cores[i],'mais_dois','coringa')
            for _ in range(2):
                aux.append(face_mais_dois)
            
        
            for _ in range(10):
                shuffle(aux)

            for i in range(len(aux)):
                self.__cartas.append(Carta(aux[i]))

    def to_json(self) -> dict:
        a =  json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)
        json_acceptable_string = a.replace("'", "\"")
        json_ = json.loads(json_acceptable_string)
        return json_

    def darCarta(self):
        return self.__cartas.pop(0)
