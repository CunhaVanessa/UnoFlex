from Window import Window
from ActorInterface import ActorInterface
import os

def main() -> None:
    window = Window()
    ActorInterface(window)
    
    
if __name__ == '__main__':
    print("Diretório de Trabalho:", os.getcwd())
    main()
    