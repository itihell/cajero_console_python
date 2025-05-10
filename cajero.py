from colorama import Fore, Style,Back, init
from dotenv import load_dotenv
import os
from typing import List
from billete import Billete
from denominacion import Denominacion
from utils import Utils 
class Cajero:

    def __init__(self):  
        load_dotenv()   
        self.tools = Utils()   
        self.billetes: List[Billete]=[]
        self.billetes_retiados: List[Billete]=[]
        self.billetes.append(
            Billete(Denominacion.CIEN.value, 
                    int( os.getenv(Denominacion.CIEN.name))))
        self.billetes.append(
            Billete(Denominacion.DOCIENTOS.value, 
                    int(os.getenv(Denominacion.DOCIENTOS.name))))
        self.billetes.append(
            Billete(Denominacion.QUINIENTOS.value, 
                    int(os.getenv(Denominacion.QUINIENTOS.name))))
        self.billetes.append(
            Billete(Denominacion.MIL.value, 
                    int(os.getenv(Denominacion.MIL.name))))
    
    def estado_denominacion(self,denominacion:int):
        for billete in self.billetes:
            if billete.valor == denominacion:
                return billete
        return None

    def estado_cajero(self):
        total=self.disponibilidad_fondos_cajero()
        print(f"El cajero tiene un total de {total} córdobas")
        for denominacion in Denominacion:
            billete:Billete =self.estado_denominacion(denominacion.value)
            print(f"Billetes de {denominacion.name} tiene: {billete.cantidad}")



    def disponibilidad_fondos_cajero(self):
        total=0
        for billete in self.billetes:
            total+=billete.valor*billete.cantidad
        return total
    
    
    
    def mostro_disponibilidad(self):
        total =self.disponibilidad_fondos_cajero()
        print(f"El cajero tiene un total de {total} córdobas")

    def es_monto_valido(self, monto:str):
        if not monto.isdigit():
            self.tools.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("No es un monto válido. Intente de nuevo.")
            self.tools.mensaje_continuar()
            return 0
        
        disponible =self.disponibilidad_fondos_cajero()
        monto=int(monto)

        if monto <= 0:
            self.tools.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("Debe ser un monto positivo. Intente de nuevo.")
            self.tools.mensaje_continuar()
            return 0
        
        if monto > disponible:
            self.tools.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("No hay suficiente dinero en el cajero.")
            self.tools.mensaje_continuar()
            return 0
        
        if monto % 100 != 0:
            self.tools.limpiar_pantalla()
            print(Fore.RED + Style.BRIGHT)
            print("El monto debe ser múltiplo de 100. Intente de nuevo.")
            self.tools.mensaje_continuar()
            return 0
        
        return monto
     

    def crear_retiro(self):
        monto:str = input("Ingrese el monto a retirar: ")
        """Validar el monto ingresado"""
        monto=int(self.es_monto_valido(monto))
        if monto == 0:            
            return
        
        self.retirar(monto)
    
    def retirar(self, monto:int):
        billetes_a_entregar: List[Billete] = []
        billetes_disponibles = sorted(self.billetes, key=lambda b: b.valor, reverse=True) 

        monto_restante = monto

        for billete in billetes_disponibles:
            if monto_restante == 0:
                break
            # Calcula cuántos billetes de esta denominación se pueden usar
            cantidad_a_entregar = min(monto_restante // billete.valor, billete.cantidad)
            if cantidad_a_entregar > 0:
                billetes_a_entregar.append(Billete(billete.valor, cantidad_a_entregar))
                monto_restante -= cantidad_a_entregar * billete.valor
                billete.cantidad -= cantidad_a_entregar  # Actualiza la cantidad de billetes disponibles

        if monto_restante == 0:
            self.billetes_retirados = billetes_a_entregar
            for billete in billetes_a_entregar:
                print(f"Billetes de {billete.valor} córdobas: {billete.cantidad}")
            self.tools.mensaje_continuar()
            return billetes_a_entregar
        else:
            print("No se puede entregar la cantidad solicitada con los billetes disponibles.")
            self.tools.mensaje_continuar()
            return []  # Retorna una lista vacía para indicar fallo en el retiro
        
       
