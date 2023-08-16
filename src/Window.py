from tkinter import *

class Window():

    def __init__(self) -> None:
        self.__window = Tk()
        self.createWindow()
        
    def getWindow(self) -> Tk:
        return self.__window

    def createWindow(self) -> None:
        self.__window.geometry("1280x720")
        self.__window.configure(bg = "#ffffff")
