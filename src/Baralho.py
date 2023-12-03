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
            for j in range(1,8):
                
                # cartas muda_flex
                face_numerica_muda_flex = Face(f'card_{pos[i]+j-1}',cores[i],str(j),'muda_flex', False)
                if j % 2 != 0:  # verifica se j é ímpar
                    for _ in range(1):
                        aux.append(face_numerica_muda_flex)
                
                # cartas comuns
                face_numerica = Face(f'card_{pos[i]+j-1}',cores[i],str(j),'numerica', False)
                if j % 2 == 0:  # verifica se j é par
                    for _ in range(1):
                        aux.append(face_numerica)
                                
                # cartas numericas flex
                face_numerica_flex = Face(f'card_{pos_flex[i]+j-1}',cores[i],str(j),'numerica_flex', True)
                for _ in range(1):
                    aux.append(face_numerica_flex)
            

            face_compre_dois = Face(f'card_{pos[i]+9}',cores[i],'mais_dois','colorida_poder', False)
            for _ in range(1):
                aux.append(face_compre_dois)
            
            face_compre_dois_flex = Face(f'card_{pos_flex[i]+9}',cores[i],'mais_dois_flex','colorida_poder', False)
            for _ in range(1):
                aux.append(face_compre_dois_flex)

            face_pular_vez = Face(f'card_{pos[i]+10}',cores[i],'pular_vez','colorida_poder', False)
            for _ in range(1):
                aux.append(face_pular_vez)
            
            face_pular_vez_flex = Face(f'card_{pos_flex[i]+10}',cores[i],'pular_vez_flex','colorida_poder', False)
            for _ in range(1):
                aux.append(face_pular_vez_flex)
            
            face_inverter_ordem = Face(f'card_{pos[i]+11}',cores[i],'inverter_ordem','colorida_poder', False)
            for _ in range(1):
                aux.append(face_inverter_ordem)

            face_coringa_flex = Face(f'card_3',cores[i],'troca_cor','coringa', True)
            for _ in range(4):
                aux.append(face_coringa_flex)

            face_mais_quatro = Face(f'card_8',cores[i],'mais_quatro','coringa', True)
            for _ in range(4):
                aux.append(face_mais_quatro)
            
            face_proximo_mais_dois = Face(f'card_13',cores[i],'proximo_mais_dois','coringa', True)
            for _ in range(4):
                aux.append(face_proximo_mais_dois)
            
            face_todos_mais_dois = Face(f'card_18',cores[i],'todos_mais_dois','coringa', True)
            for _ in range(4):
                aux.append(face_todos_mais_dois)
            
        
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
