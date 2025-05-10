from colorama import Fore, Style,Back, init
import os
class Utils:
   
    def mensaje_continuar(self):
        print(Fore.GREEN + Style.BRIGHT)
        print("\nPresione una tecla para continuar...")
        input()
        self.limpiar_pantalla()


    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')



    