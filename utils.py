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

    def es_opcion_valida(self, opcion:str):
        if not opcion:
            self.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("No tecleo una opción del menú. Intente de nuevo.")
            self.mensaje_continuar()
            return 0

        if len(opcion)==0:
            self.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("No selecciono una opción. Intente de nuevo.")
            self.mensaje_continuar()
            return 0
        
        # validar si option no es un número
        if not opcion.isdigit():
            self.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("Debe seleccionar una opción válida. Intente de nuevo.")
            self.mensaje_continuar()
            return 0

        return opcion

