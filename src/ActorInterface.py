from tkinter import *
from Window import Window
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import simpledialog
from dog.dog_interface import DogPlayerInterface
from dog.dog_actor import DogActor
from Jogo import Jogo
import os
from time import sleep


class ActorInterface(DogPlayerInterface):

    def __init__(self, window: Window) -> None:
        self.__window = window.getWindow()
        self.__window.title('UNO Flex')
        self.__dict_of_cards = {}
        self.__slots_local = []
        self.__slots_remote_right = []
        self.__slots_remote_left = []
        self.__inicio_mao = 0
        self.__mensagem = ''
        self.__jogo = Jogo()
        self.loadCardImages()
        self.startMenu()

    def receive_move(self, a_move: dict) -> None:
        if a_move['tipo'] == 'init':
            self.__jogo.transform_dict_to_object(a_move)
            jogadores = self.__jogo.getJogadores()
            for k, jogador in enumerate(jogadores):
                if jogador.getId() == self.__jogo.getLocalId():
                    self.__jogo.setLocalPosition(k)
                    self.__jogo.setRightPosition((k+1) % 3)
                    self.__jogo.setLeftPosition(k-1)
            self.__jogo.setJogadorAtual(self.__jogo.getJogadores()[0])
            self.__jogo.setProximoJogador(self.__jogo.getJogadores()[1])
            self.__mensagem = self.__jogo.getJogadores(
            )[self.__jogo.getLocalPosition()].getNome()
            self.start_table()

        elif a_move['tipo'] == 'comprar':
            self.__jogo.comprarCarta()
            self.atualizarInterface()

        elif a_move['tipo'] == 'jogar':
            index = a_move['index']
            self.__jogo.jogarCarta(index)
            self.atualizarInterface()
            if not self.__jogo.getJogadorAtual().getMao():
                sleep(0.2)
                self.__jogo.setFimJogo(True)
                self.mostrarEndGame()

        elif a_move['tipo'] == 'passar':
            self.__jogo.passarVez()
            if self.__jogo.getJogadorAtual() is self.__jogo.getJogadores()[self.__jogo.getLocalPosition()]:
                self.setMessage("Seu turno!")

        elif a_move['tipo'] == 'muda_cor':
            self.mudaCor(a_move['cor'])

            self.atualizarInterface()

        elif a_move['tipo'] == 'uno':
            self.__jogo.getJogadorAtual().gritarUno()
            self.__jogo.verificarUNO()
            self.setMessage(
                f"{self.__jogo.getJogadorAtual().getNome()} gritou UNO")
            self.atualizarInterface()

    def receive_start(self, start_status) -> None:
        self.__jogo.setLocalId(start_status.get_local_id())

    def receive_withdrawal_notification(self) -> None:
        self.mostrarTelaDesconexao()

    def start_match(self) -> None:
        start_status = self.__dog_server_interface.start_match(3)
        message = start_status.get_message()
        messagebox.showinfo(message=message)

        if message == 'Partida iniciada':
            jogadores = start_status.get_players()
            id_jogador_local = start_status.get_local_id()

            dict_inicial = self.__jogo.comecarPartida(
                jogadores, id_jogador_local)
            self.__dog_server_interface.send_move(dict_inicial)

            self.__jogo.configurarJogadores()
            self.__mensagem = self.__jogo.getJogadores(
            )[self.__jogo.getLocalPosition()].getNome()
            self.start_table()

    def setCanvas(self) -> None:
        self.__canvas = Canvas(
            self.__window, bg="#ffffff", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.__canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

    def createMenuDesign(self) -> None:
        self.__background_img = PhotoImage(
            file=f"src/menu_images/background.png")
        background = self.__canvas.create_image(
            0, 0, image=self.__background_img, anchor="nw")

        self.__button_menu = PhotoImage(
            file=f"src/menu_images/button_jogar.png")
        button_start = self.__canvas.create_image(
            270, 560, image=self.__button_menu)
        self.__canvas.tag_bind(button_start, "<Button-1>",
                               lambda x: self.start_match())

    def startMenu(self) -> None:
        self.setCanvas()
        self.createMenuDesign()
        self.__window.resizable(False, False)
        player_name = simpledialog.askstring(
            title='player indentification', prompt='Qual seu nome?')
        self.__dog_server_interface = DogActor()
        message = self.__dog_server_interface.initialize(player_name, self)
        messagebox.showinfo(message=message)
        self.__window.mainloop()

    def createTableDesign(self) -> None:
        self.__background_img = PhotoImage(
            file=f"src/table_images/background.png")
        background = self.__canvas.create_image(
            0, 0, image=self.__background_img, anchor="nw")

        self.__button_gritar_uno = PhotoImage(
            file=f"src/table_images/button_gritar_uno.png")
        button_start = self.__canvas.create_image(
            640, 80, image=self.__button_gritar_uno)
        self.__canvas.tag_bind(button_start, "<Button-1>",
                               lambda x: self.gritarUno())

        self.__button_passar_vez = PhotoImage(
            file=f"src/table_images/button_passar_vez.png")
        button_passar_vez = self.__canvas.create_image(
            800, 300, image=self.__button_passar_vez)
        self.__canvas.tag_bind(
            button_passar_vez, "<Button-1>", lambda x: self.passarVez())

        self.__button_mover_mao_esq = PhotoImage(
            file=f"src/table_images/seta_esquerda.png")
        button_passar_vez = self.__canvas.create_image(
            340, 670, image=self.__button_mover_mao_esq)
        self.__canvas.tag_bind(
            button_passar_vez, "<Button-1>", lambda x: self.mover_mao(0))

        self.__button_mover_mao_dir = PhotoImage(
            file=f"src/table_images/seta_direita.png")
        button_passar_vez = self.__canvas.create_image(
            940, 670, image=self.__button_mover_mao_dir)
        self.__canvas.tag_bind(
            button_passar_vez, "<Button-1>", lambda x: self.mover_mao(1))

        button_card = self.__canvas.create_image(
            500, 300, image=self.__dict_of_cards['card_0'])
        self.__canvas.tag_bind(button_card, "<Button-1>",
                               lambda x: self.comprar())

        self.__mesage_var = self.__canvas.create_text(
            150, 25, text=self.__mensagem, fill='white', font=('serif', 16, 'bold'))

    def loadCardImages(self) -> None:

        # Obtenha o diretório atual do script
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))

        for i in range(63):
            caminho_imagem_card = os.path.join(
                diretorio_atual, 'UNO_cards_flex', f'card_{i}.png')

            # Carregar imagens de
            image_card = Image.open(caminho_imagem_card)
            img_card = image_card.resize((100, 150))
            self.__dict_of_cards[f"card_{i}"] = ImageTk.PhotoImage(img_card)

            image_card_90 = image_card.resize((80, 130))
            self.__dict_of_cards[f"card_{i}_90"] = ImageTk.PhotoImage(
                image_card_90.rotate(90, expand=True))

            image_card_270 = image_card.resize((80, 130))
            self.__dict_of_cards[f"card_{i}_270"] = ImageTk.PhotoImage(
                image_card_270.rotate(270, expand=True))

    def gritarUno(self):
        self.__jogo.getJogadorAtual().gritarUno()
        self.__jogo.verificarUNO()
        self.atualizarInterface()
        self.setMessage("Gritou UNO")
        self.__dog_server_interface.send_move(self.__jogo.getDictJogada())

    def comprar(self) -> None:
        if self.__jogo.verificarTurno():
            self.__jogo.comprarCarta()
            self.__dog_server_interface.send_move(self.__jogo.getDictJogada())
            self.atualizarInterface()
        else:
            self.setMessage("Não é sua vez")

    def mover_mao(self, direcao: int) -> None:
        self.delete_local()

        if direcao == 1:
            if self.__inicio_mao+6 < len(self.__jogo.getJogadores()[self.__jogo.getLocalPosition()].getMao()):
                self.__inicio_mao += 1

        if direcao == 0:
            if self.__inicio_mao > 0:
                self.__inicio_mao -= 1

        self.atualizarInterface()

    def passarVez(self):
        if self.__jogo.verificarTurno():
            jogador_atual = self.__jogo.getJogadorAtual()
            if jogador_atual.getJogouCarta() or jogador_atual.getComprouCarta():
                self.__jogo.passarVez()

                self.__dog_server_interface.send_move(
                    self.__jogo.getDictJogada())

                self.setMessage("Turno passado!")
            else:
                self.setMessage("Precisa tentar jogar")
        else:
            self.setMessage("Não é sua vez")

    def jogarCarta(self, index) -> None:
        if self.__jogo.verificarTurno():

            valida = self.__jogo.jogarCarta(self.__inicio_mao+index)
            if valida:
                self.__dog_server_interface.send_move(
                    self.__jogo.getDictJogada())
                self.atualizarInterface()

                frente_ultima_carta = self.__jogo.getMesa().getUltimaCarta().getFrente()
                if frente_ultima_carta.getTipo() == 'coringa':
                    self.setMessage("Escolha uma cor")
                    self.escolherCor()

                self.setMessage("Carta jogada")
            else:
                self.setMessage("Não pode jogar essa\ncarta ou já atuou")

            if not self.__jogo.getJogadorAtual().getMao():
                sleep(0.2)
                self.__jogo.setFimJogo(True)
                self.mostrarEndGame()
        else:
            self.setMessage("Não é sua vez")

    def addCard(self) -> None:
        self.__slots_local = []

        def func0(x): return self.jogarCarta(0)
        def func1(x): return self.jogarCarta(1)
        def func2(x): return self.jogarCarta(2)
        def func3(x): return self.jogarCarta(3)
        def func4(x): return self.jogarCarta(4)
        def func5(x): return self.jogarCarta(5)
        funcs = [func0, func1, func2, func3, func4, func5]

        for i in range(6):
            if (i+self.__inicio_mao) < len(self.__jogo.getJogadores()[self.__jogo.getLocalPosition()].getMao()):
                self.__slots_local.append(self.__jogo.getJogadores(
                )[self.__jogo.getLocalPosition()].getMao()[i+self.__inicio_mao])
            if i < len(self.__slots_local):
                button_card = self.__canvas.create_image(
                    340+i*120, 570, image=self.__dict_of_cards[self.__slots_local[i].getFrente().getId()])
                self.__slots_local[i] = (button_card, self.__slots_local[i])
                self.__canvas.tag_bind(button_card, "<Button-1>", funcs[i])

    def addRemoteCardRight(self) -> None:
        self.__slots_remote_right = []

        for i in range(5):
            if i < len(self.__jogo.getJogadores()[self.__jogo.getRightPosition()].getMao()):
                self.__slots_remote_right.append(self.__jogo.getJogadores()[
                                                 self.__jogo.getRightPosition()].getMao()[i])

            if i < len(self.__slots_remote_right):
                identificator = self.__canvas.create_image(
                    1140, 150+(105*i), image=self.__dict_of_cards[f'card_0_270'])
                self.__slots_remote_right[i] = (
                    identificator, self.__slots_remote_right[i])

    def addRemoteCardLeft(self) -> None:
        self.__slots_remote_left = []

        for i in range(5):
            if i < len(self.__jogo.getJogadores()[self.__jogo.getLeftPosition()].getMao()):
                self.__slots_remote_left.append(self.__jogo.getJogadores()[
                                                self.__jogo.getLeftPosition()].getMao()[i])

            if i < len(self.__slots_remote_left):
                identificator = self.__canvas.create_image(
                    140, 150+(105*i), image=self.__dict_of_cards[f'card_0_90'])
                self.__slots_remote_left[i] = (
                    identificator, self.__slots_remote_left[i])

    def addCheap(self):
        try:
            self.__canvas.delete(self.__button_cheap)
        except:
            pass

        carta = self.__jogo.getMesa().getUltimaCarta()

        self.__button_cheap = self.__canvas.create_image(
            640, 300, image=self.__dict_of_cards[carta.getFrente().getId()])

    def delete_local(self) -> None:
        for k, _ in enumerate(self.__slots_local):
            self.__canvas.delete(self.__slots_local[k][0])

    def delete_right(self) -> None:
        for k, _ in enumerate(self.__slots_remote_right):
            self.__canvas.delete(self.__slots_remote_right[k][0])

    def delete_left(self) -> None:
        for k, _ in enumerate(self.__slots_remote_left):
            self.__canvas.delete(self.__slots_remote_left[k][0])

    def mostrarEndGame(self):
        indice_jogador = self.__jogo.getLocalPosition()
        self.setCanvas()
        if len(self.__jogo.getJogadores()[indice_jogador].getMao()):
            imagem = 'perdeu'
        else:
            imagem = 'venceu'

        self.__background_img = PhotoImage(
            file=f"src/menu_images/{imagem}.png")
        background = self.__canvas.create_image(
            0, 0, image=self.__background_img, anchor="nw")

    def mostrarTelaDesconexao(self):
        self.__jogo.setFimJogo(True)
        self.__jogo.setJogoAbandonado(True)
        self.setCanvas()
        self.__background_img = PhotoImage(
            file=f"src/menu_images/desconexao.png")
        background = self.__canvas.create_image(
            0, 0, image=self.__background_img, anchor="nw")
        sleep(3)
        self.__window.destroy()

    def escolherCor(self):
        carta = self.__jogo.getMesa().getUltimaCarta()
        cor = carta.getFrente().getId()[0]

        if cor == "l":
            quadrado1 = 'vermelho'
            quadrado2 = 'azul'
            quadrado3 = 'amarelo'
            quadrado4 = 'verde'

        self.__vermelho = PhotoImage(file=f"src/table_images/{quadrado1}.png")
        self.__button1_id = self.__canvas.create_image(
            745, 255, image=self.__vermelho)
        self.__canvas.tag_bind(
            self.__button1_id, "<Button-1>", lambda x:  self.mudaCor(quadrado1))

        self.__azul = PhotoImage(file=f"src/table_images/{quadrado2}.png")
        self.__button2_id = self.__canvas.create_image(
            535, 255, image=self.__azul)
        self.__canvas.tag_bind(
            self.__button2_id, "<Button-1>", lambda x: self.mudaCor(quadrado2))

        self.__amarelo = PhotoImage(file=f"src/table_images/{quadrado3}.png")
        self.__button3_id = self.__canvas.create_image(
            745, 465, image=self.__amarelo)
        self.__canvas.tag_bind(
            self.__button3_id, "<Button-1>", lambda x: self.mudaCor(quadrado3))

        self.__verde = PhotoImage(file=f"src/table_images/{quadrado4}.png")
        self.__button4_id = self.__canvas.create_image(
            535, 465, image=self.__verde)
        self.__canvas.tag_bind(
            self.__button4_id, "<Button-1>", lambda x: self.mudaCor(quadrado4))

        # jogo.mudarCor

        # atualiza interface e faz envio da jogada, destruindo a tela criada

    def mudaCor(self, cor: str):
        carta = self.__jogo.getMesa().getUltimaCarta()
        carta.getFrente().setCor(cor)

        cores_mais_dois = {
            'amarelo': 'card_1',
            'vermelho': 'card_1',
            'azul': 'card_1',
            'verde': 'card_1'
        }

        cores_coringa = {
            'amarelo': 'card_1',
            'vermelho': 'card_1',
            'azul': 'card_1',
            'verde': 'card_1'
        }

        print(carta.getFrente().getSimbolo())
        if carta.getFrente().getSimbolo() == 'mais_dois':
            carta.getFrente().setId(cores_mais_dois[cor])
            self.__jogo.getMesa().setUltimaCarta(carta)
        elif carta.getFrente().getSimbolo() == 'troca_cor':
            carta.getFrente().setId(cores_coringa[cor])
            self.__jogo.getMesa().setUltimaCarta(carta)
        ################
        # ficar no Actor
        self.atualizarInterface()

        if self.__jogo.getJogadorAtual().getId() == self.__jogo.getJogadores()[self.__jogo.getLocalPosition()].getId():
            sleep(0.2)

            a = self.__rectangle_id
            for i in range(a, a+5):
                self.__canvas.delete(i)

            dict_a = {
                'match_status': 'progress',
                'tipo': 'muda_cor',
                'cor': cor
            }

            self.__dog_server_interface.send_move(dict_a)

    def start_table(self) -> None:
        self.setCanvas()
        self.createTableDesign()
        self.atualizarInterface()

    def setMessage(self, message: str) -> None:
        self.__mensagem = message
        self.__canvas.itemconfig(self.__mesage_var, text=self.__mensagem)

    def update_mesage(self):
        self.__canvas.itemconfig(self.__mesage_var, text=self.__mensagem)

    def atualizarInterface(self):
        self.delete_local()
        self.delete_left()
        self.delete_right()
        self.addCheap()

        self.addCard()

        self.addRemoteCardLeft()
        self.addRemoteCardRight()
        self.update_mesage()
