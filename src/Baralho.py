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
        cores = ['amarelo', 'vermelho', 'azul', 'verde']

        aux = []

        pos = [12, 25, 38, 51]

        pos_flex = [64, 75, 86, 97]
        
        #OK
        for i in range(4):
            for j in range(1, 9):
                face_numerica = Face(
                    f'card_{pos[i]+j-1}', cores[i], str(j), 'numerica')
                for _ in range(1):
                    aux.append(face_numerica)
        
        for i in range(4):
            for j in range(1, 9):
                numerica_flex = Face(
                    f'card_{pos_flex[i]+j-1}', cores[i], str(j), 'numerica')
                for _ in range(1):
                    aux.append(numerica_flex)

           #OK
            face_compre_dois_flex = Face(
                f'card_{pos[i]+8}', cores[i], 'todos_mais_um', 'colorida_poder')
            for _ in range(1):
                aux.append(face_compre_dois_flex)
            
            #OK
            face_pular_vez_flex = Face(
                f'card_{pos[i]+9}', cores[i], 'pular_todos_flex', 'colorida_poder')
            for _ in range(1):
                aux.append(face_pular_vez_flex)
            
           #OK
            face_inverter_ordem_flex = Face(
                f'card_{pos[i]+10}', cores[i], 'pular_todos_flex', 'colorida_poder')
            for _ in range(1):
                aux.append(face_inverter_ordem_flex)
           
            #OK
            face_compre_dois = Face(
                f'card_{pos[i]+8}', cores[i], 'mais_dois', 'colorida_poder')
            for _ in range(1):
                aux.append(face_compre_dois)
            
            #OK
            face_pular_vez = Face(
                f'card_{pos[i]+9}', cores[i], 'pular_vez', 'colorida_poder')
            for _ in range(1):
                aux.append(face_pular_vez)
            
            # OK
            face_inverter_ordem = Face(
                f'card_{pos[i]+10}', cores[i], 'inverter_ordem', 'colorida_poder')
            for _ in range(1):
                aux.append(face_inverter_ordem)
            
            # OK
            coringa_flex = Face(f'card_4', cores[i], 'flex', 'coringa')
            for _ in range(1):
                aux.append(coringa_flex)

            # OK
            coringa_face_mais_quatro = Face(f'card_5', cores[i], 'mais_quatro', 'coringa')
            for _ in range(1):
                aux.append(coringa_face_mais_quatro)
            
            # OK
            coriga_face_proximo_mais_dois = Face(f'card_6', cores[i], 'proximo_mais_dois', 'coringa')
            for _ in range(1):
                aux.append(coriga_face_proximo_mais_dois)

            # OK
            coriga_face_todos_mais_dois = Face(f'card_7', cores[i], 'todos_mais_dois', 'coringa')
            for _ in range(1):
                aux.append(coriga_face_todos_mais_dois)

            for _ in range(10):
                shuffle(aux)

            for i in range(len(aux)):
                self.__cartas.append(Carta(aux[i]))

    def to_json(self) -> dict:
        a = json.dumps(self, default=lambda o: o.__dict__,
                       sort_keys=True, indent=4)
        json_acceptable_string = a.replace("'", "\"")
        json_ = json.loads(json_acceptable_string)
        return json_

    def darCarta(self):
        return self.__cartas.pop(0)
