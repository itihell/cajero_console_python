import os
from opcion_menu import OpcionMenu
from cajero import Cajero
from colorama import Fore, Style,Back, init
class Utils:

    def __init__(self):
       init()
       self.cajero=Cajero()

    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def pintar_pausa(self):
        print(Fore.GREEN + Style.BRIGHT)
        print("\nPresione una tecla para continuar...")
        input()
        self.limpiar_pantalla()
        self.get_menu()

    def imprimir_menu(self):
        print(Fore.BLUE + Style.BRIGHT)
        print("###############################")
        print("###### Cajero Automatico ######")
        print("###### Opciones:         ######")
        for opcion in OpcionMenu:
            print(f"###### {opcion.value}. {opcion.name}")
        print("###############################")

    def es_opcion_valida(self, opcion:str):
        if not opcion:
            self.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("No tecleo una opción del menú. Intente de nuevo.")
            self.pintar_pausa()

        if len(opcion)==0:
            self.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("No selecciono una opción. Intente de nuevo.")
            self.pintar_pausa()
        
        # validar si option no es un número
        if not opcion.isdigit():
            self.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("Debe seleccionar una opción válida. Intente de nuevo.")
            self.pintar_pausa()

        return opcion


    def validar_opcion_menu(self):
        print(Fore.YELLOW + Style.BRIGHT)
        opcion=input("\nSeleccione una opción: ")
        # validar si opcion esta vacia        
        opcion=int(self.es_opcion_valida(opcion))
        self.validar_opcion(opcion)
    
    def validar_opcion(self,opcion:int):
        print(Fore.GREEN + Style.BRIGHT)
        if opcion == OpcionMenu.CONSULTA.value:
            self.limpiar_pantalla()
            self.cajero.estado_cajero()
            self.pintar_pausa()
        elif opcion == OpcionMenu.RETIRO.value:
            self.limpiar_pantalla()
            self.cajero.crear_retiro()
            self.pintar_pausa()
        elif opcion == OpcionMenu.ESTADO.value:
           self.limpiar_pantalla()
           self.cajero.mostro_disponibilidad() 
           self.pintar_pausa()
        elif opcion == OpcionMenu.SALIR.value:  
            print("Gracias por usar el cajero automatico")
            exit()
        else:
            self.limpiar_pantalla()
            print("Opción no válida. Intente de nuevo.")
            self.pintar_pausa()
            
           
    
    def get_menu(self):        
        self.imprimir_menu()
        self.validar_opcion_menu()
        
