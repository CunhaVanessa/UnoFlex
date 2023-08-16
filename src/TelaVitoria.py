import tkinter as tk
from PIL import Image, ImageTk

class TelaVitoria():
    # Crie a janela principal
    root = tk.Tk()
    root.title("UNO Flex")
    root.geometry("1280x720")
    # Carregue a imagem usando o PIL (Python Imaging Library)
    image = Image.open("src/game_images/BackgroundVitoria.png")
    photo = ImageTk.PhotoImage(image)

    # Crie um widget de rótulo para exibir a imagem
    label = tk.Label(root, image=photo)
    label.pack()

    # Inicie o loop principal da GUI
    root.mainloop()
