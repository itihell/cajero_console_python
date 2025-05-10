
from opcion_menu import OpcionMenu
from cajero import Cajero
from colorama import Fore, Style,Back, init
from utils import Utils
class Menus:

    def __init__(self):
       init()
       self.tools=Utils()
       self.cajero=Cajero()

    def pintar_pausa(self):
        self.tools.mensaje_continuar()
        self.get_menu()

    def imprimir_menu(self):
        print(Fore.BLUE + Style.BRIGHT)
        print("###############################")
        print("###### Cajero Automatico ######")
        print("###### Opciones:         ######")
        for opcion in OpcionMenu:
            print(f"###### {opcion.value}. {opcion.name}")
        print("###############################")

    def validar_opcion_menu(self):
        print(Fore.YELLOW + Style.BRIGHT)
        opcion=input("\nSeleccione una opción: ")
        # validar si opcion esta vacia        
        opcion=int(self.es_opcion_valida(opcion))
        self.validar_opcion(opcion)
    
    def validar_opcion(self,opcion:int):
        print(Fore.GREEN + Style.BRIGHT)
        if opcion == OpcionMenu.CONSULTA.value:
            self.tools.limpiar_pantalla()
            self.cajero.estado_cajero()
            self.pintar_pausa()
        elif opcion == OpcionMenu.RETIRO.value:
            self.tools.limpiar_pantalla()
            self.cajero.crear_retiro()            
            self.get_menu()
        elif opcion == OpcionMenu.ESTADO.value:
            self.tools.limpiar_pantalla()
            self.cajero.mostro_disponibilidad() 
            self.pintar_pausa()
        elif opcion == OpcionMenu.SALIR.value:  
            print("Gracias por usar el cajero automatico")
            exit()
        else:
            self.tools.limpiar_pantalla()
            print("Opción no válida. Intente de nuevo.")
            self.pintar_pausa()
            
           
    
    def get_menu(self): 
        self.tools.limpiar_pantalla()       
        self.imprimir_menu()
        self.validar_opcion_menu()

    def es_opcion_valida(self, opcion:str):
        if not opcion:
            self.tools.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("No tecleo una opción del menú. Intente de nuevo.")
            self.mensaje_continuar()
            return 0

        if len(opcion)==0:
            self.tools.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("No selecciono una opción. Intente de nuevo.")
            self.mensaje_continuar()
            return 0
        
        # validar si option no es un número
        if not opcion.isdigit():
            self.tools.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("Debe seleccionar una opción válida. Intente de nuevo.")
            self.mensaje_continuar()
            return 0

        return opcion
        
