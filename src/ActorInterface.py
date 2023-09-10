from tkinter import *
from Window import Window
from PIL import Image, ImageTk
from tkinter import simpledialog
import os
from PIL import Image, ImageTk


class ActorInterface():

    def __init__(self, window: Window) -> None:
        self.__window = window.getWindow()
        self.__window.title('UNO Flex')
        print("Diretório de Trabalho:", os.getcwd())
        self.__dict_of_cards = {}  # Movido o dicionário para cá
        self.__button_cards = []  # Inicialize a lista para armazenar as referências dos botões
        self.loadCardImages()  # Carrega as imagens das cartas imediatamente após a inicialização
        self.startMenu()

    def setCanvas(self) -> None:
        self.__canvas = Canvas(
            self.__window, bg="#ffffff", height=720, width=1280, bd=0, highlightthickness=0, relief="ridge")
        self.__canvas.place(relx=0.5, rely=0.5, anchor=CENTER)

    def createMenuDesign(self) -> None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.abspath(
            os.path.join(current_directory, os.pardir))
        game_images_directory = os.path.join(
            parent_directory, "src", "game_images")

        self.__background_img = PhotoImage(file=os.path.join(
            game_images_directory, f'BackgroundUnoFlex.png'))
        background = self.__canvas.create_image(
            0, 0, image=self.__background_img, anchor="nw")

        self.__button_menu = PhotoImage(file=os.path.join(
            game_images_directory, f'ButtonJogar.png'))
        button_start = self.__canvas.create_image(
            250, 600, image=self.__button_menu)
        self.__canvas.tag_bind(button_start, "<Button-1>",
                               lambda x: self.start_match())

    def startMenu(self) -> None:
        self.setCanvas()
        self.createMenuDesign()
        self.__window.resizable(False, False)
        player_name = simpledialog.askstring(
            title='Identificação do Jogador(a)', prompt='Qual seu nome?')
        self.__window.mainloop()

    def createTableDesign(self) -> None:
        self.__background_img = PhotoImage(
            file=f"src/game_images/BackgroundMesa.png")
        background = self.__canvas.create_image(
            0, 0, image=self.__background_img, anchor="nw")

        self.__button_gritar_uno = PhotoImage(
            file=f"src/game_images/ButtonUno.png")
        button_start = self.__canvas.create_image(
            640, 80, image=self.__button_gritar_uno)
        self.__canvas.tag_bind(button_start, "<Button-1>",
                               lambda x: print("Dizer UNO!"))

        self.__button_passar_turno = PhotoImage(
            file=f"src/game_images/ButtonPassarVez.png")
        button_passar_turno = self.__canvas.create_image(
            800, 300, image=self.__button_passar_turno)
        self.__canvas.tag_bind(button_passar_turno,
                               "<Button-1>", lambda x: print("Passar Turno!"))

        self.__button_mover_mao_esq = PhotoImage(
            file=f"src/game_images/ButtonSetaEsquerda.png")
        button_mover_mao_esq = self.__canvas.create_image(
            340, 670, image=self.__button_mover_mao_esq)
        self.__canvas.tag_bind(
            button_mover_mao_esq, "<Button-1>", lambda x: print("Mover mão a esquerda"))

        self.__button_mover_mao_dir = PhotoImage(
            file=f"src/game_images/ButtonSetaDireita.png")
        button_mover_mao_dir = self.__canvas.create_image(
            940, 670, image=self.__button_mover_mao_dir)
        self.__canvas.tag_bind(
            button_mover_mao_dir, "<Button-1>", lambda x: print("Mover mão a direita"))

        button_comprar_carta = self.__canvas.create_image(
            500, 300, image=self.__dict_of_cards['card_0'])
        self.__canvas.tag_bind(button_comprar_carta, "<Button-1>",
                               lambda x: print("Comprar Carta"))

        button_pilha_descarte_card = self.__canvas.create_image(
            645, 300, image=self.__dict_of_cards['card_6'])
        self.__canvas.tag_bind(button_pilha_descarte_card,
                               "<Button-1>", lambda x: print("Pilha de descarte"))

    def createCardButtons(self):
        space_between_cards = 20  # Espaço entre as cartas
        # Largura da carta (pode ser ajustada conforme suas imagens)
        card_width = 80

        # Lista de informações sobre as cartas individuais
        individual_cards = [
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 100, "y_position": 50},
            {"image": self.__dict_of_cards[f"card_1_90"],
                "x_position": 100, "y_position": 50},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 100, "y_position": 150},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 100, "y_position": 250},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 100, "y_position": 350},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 100, "y_position": 450},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 100, "y_position": 550},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 1175, "y_position": 50},
            {"image": self.__dict_of_cards[f"card_1_90"],
                "x_position": 1175, "y_position": 50},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 1175, "y_position": 150},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 1175, "y_position": 250},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 1175, "y_position": 350},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 1175, "y_position": 450},
            {"image": self.__dict_of_cards[f"card_0_90"],
                "x_position": 1175, "y_position": 550},


            {"image": self.__dict_of_cards[f"card_11_360"],
                "x_position": 350, "y_position": 550},
            {"image": self.__dict_of_cards[f"card_2_360"],
                "x_position": 350, "y_position": 550},
            {"image": self.__dict_of_cards[f"card_12_360"],
                "x_position": 450, "y_position": 550},
            {"image": self.__dict_of_cards[f"card_13_360"],
                "x_position": 550, "y_position": 550},
            {"image": self.__dict_of_cards[f"card_21_360"],
                "x_position": 650, "y_position": 550},
            {"image": self.__dict_of_cards[f"card_31_360"],
                "x_position": 750, "y_position": 550},
            {"image": self.__dict_of_cards[f"card_18_360"],
                "x_position": 850, "y_position": 550},
            {"image": self.__dict_of_cards[f"card_10_360"],
                "x_position": 950, "y_position": 550},
        ]

        for card_info in individual_cards:
            x = card_info["x_position"]
            y = card_info["y_position"]
            card_image = card_info["image"]
            button_card = self.__canvas.create_image(x, y, image=card_image)
            self.__canvas.tag_bind(
                button_card, "<Button-1>", lambda event, img=card_image: self.on_card_click(img))
            self.__button_cards.append(button_card)

    def on_card_click(self, index):
        print(f"Carta {index}")

    def loadCardImages(self) -> None:
        current_directory = os.path.dirname(os.path.abspath(__file__))
        parent_directory = os.path.abspath(
            os.path.join(current_directory, os.pardir))
        uno_cards_directory = os.path.join(
            parent_directory, "src", "UNO_cards_flex")

        for i in range(32):
            image = Image.open(os.path.join(
                uno_cards_directory, f'card_{i}.png'))
            img = image.resize((100, 150))
            self.__dict_of_cards[f"card_{i}"] = ImageTk.PhotoImage(img)
            image = Image.open(os.path.join(
                uno_cards_directory, f'card_{i}.png'))
            img = image.resize((80, 130))
            self.__dict_of_cards[f"card_{i}_90"] = ImageTk.PhotoImage(
                img.rotate(90, expand=True))
            image = Image.open(os.path.join(
                uno_cards_directory, f'card_{i}.png'))
            img = image.resize((80, 130))
            self.__dict_of_cards[f"card_{i}_360"] = ImageTk.PhotoImage(
                img.rotate(360, expand=True))

    def start_match(self) -> None:
        self.start_table()

    def start_table(self) -> None:
        self.loadCardImages()
        self.setCanvas()
        self.createTableDesign()
        self.createCardButtons()
