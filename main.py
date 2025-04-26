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
from menus import Menus
# Instancia de la clase Utils
menu = Menus()
# Llamada al método get_menu de la clase Utils
menu.get_menu()
