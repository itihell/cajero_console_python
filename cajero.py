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

    def crear_retiro(self):
        monto:str = input("Ingrese el monto a retirar: ")
        monto=int(self.tools.es_monto_valido(monto))
        if monto < 100:
            print("El monto mínimo a retirar es de 100 córdobas")
            return
        
        self.retirar(monto)
    
    def retirar(self, monto:int):
        if monto > self.disponibilidad_fondos_cajero():
            print("No hay suficiente dinero en el cajero")
            return
