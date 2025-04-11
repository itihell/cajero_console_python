""""
Cajero automatico
El cajero solo cuenta con 500 cordobas
dos billeres de 200
un billete de 100

solo Permite las siguientes denominaciones
100
200
500
1000

Validaciones 
1. Si el cajero no tiene el billete solicitado, debe mostrar un mensaje indicando que no hay suficiente dinero.
2. Si el usuario solicita un monto mayor a 500, debe mostrar un mensaje indicando que no se puede retirar esa cantidad.
3. Si el usuario solicita un monto menor a 100, debe mostrar un mensaje indicando que no se puede retirar esa cantidad.
4. Si el usuario solicita un monto que no es múltiplo de 100, debe mostrar un mensaje indicando que no se puede retirar esa cantidad.
5. Si el usuario solicita un monto que no es una de las denominaciones permitidas, debe mostrar un mensaje indicando que no se puede retirar esa cantidad.
6. Si el usuario solicita un monto que no es un número, debe mostrar un mensaje indicando que no se puede retirar esa cantidad.
7. Si el usuario solicita un monto que no es un número entero, debe mostrar un mensaje indicando que no se puede retirar esa cantidad.
8. Si el usuario solicita un monto que no es un número entero positivo, debe mostrar un mensaje indicando que no se puede retirar esa cantidad.
9. Si el usuario solicita un monto que no es un número entero positivo menor o igual a 500, debe mostrar un mensaje indicando que no se puede retirar esa cantidad.
10 Validar la disponibilidad de los billetes
"""
from utils import Utils
from cajero import Cajero
tools = Utils()
cajero =Cajero()


def menu():
    tools.limpiar_pantalla()
    tools.imprimir_menu()
    opcion=tools.validar_opcion_menu()
    print(f"opcion seleccionada {opcion.value}")

    if opcion.value ==4:
        print("Gracias por usar el cajero automatico")
        exit()
    else: 
        menu()

menu()


# if opcion.value ==1:
#     tools.limpiar_pantalla()
#     cajero.retirar()    
# elif opcion.value ==2:
#     tools.limpiar_pantalla()
#     cajero.mostro_disponibilidad()   
# elif opcion.value ==3:
#     tools.limpiar_pantalla()
#     cajero.estado_cajero()
# else: 
#     print("Gracias por usar el cajero automatico")
#     exit()
