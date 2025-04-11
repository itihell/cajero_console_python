import os
from opcion_menu import OpcionMenu
class Utils:
    def limpiar_pantalla(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def imprimir_menu(self):
        print("###### Cajero Automatico ######")
        print("###### Optiones          ######")
        for opcion in OpcionMenu:
            print(f"######{opcion.value}. {opcion.name}")
        

    def validar_opcion_menu(self):
        opcion=int(input("Seleccione una opción: "))
        return OpcionMenu(opcion) 
