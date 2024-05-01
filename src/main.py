#
# Actividad Adicional, Estructura de Datos Tipo Colas
#
# Alumno: José Fernando Usui
#

import os
import random

# Tarea: Limpiar consola
clear = lambda: os.system('cls')

class Cliente:
    def __init__(self, DNI, nombre, apellido, estado):
        self.DNI = DNI
        self.nombre = nombre
        self.apellido = apellido
        self.estado = estado

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Queue:
    def __init__(self):
        self.final = None
        self.principio = None
    def comparar(self, operacion):
        if self.principio == None:
            return False
        else:
            aux = self.final
            while not self.esta_vacio(aux):
                if operacion(aux):
                    return True
                aux = aux.siguiente
            return False
    def obtener_el_nodo_anterior(self, puntero):
        if self.esta_vacio(puntero):
            return None
        else:
            anterior = None
            while not self.esta_vacio(puntero.siguiente):
                    anterior = puntero
                    puntero = puntero.siguiente
            return [anterior, puntero]
    # Tarea: Introducir a la fila
    def encolar(self, nodo):
        if self.final == None:
            self.final = nodo
            self.principio = nodo
        else:
            self.principio.siguiente = nodo
            self.principio = nodo
    # Tarea: Ir sacando los nodos de la fila
    def desencolar(self):
        if self.principio == None:
            return None
        else:
            aux = self.final
            if self.esta_vacio(aux.siguiente):
                self.principio = None
                self.final = None
                return aux
            else:
                resultado = self.obtener_el_nodo_anterior(aux)
                anterior = resultado[0]
                aux = resultado[1]
                if aux == self.principio:
                    self.principio = anterior
                    self.principio.siguiente = None
                    return aux
                return None
    def desencolar_por_condicion(self, operacion):
        if self.principio == None:
            return None
        else:
            aux = self.final
            if self.esta_vacio(aux.siguiente):
                if operacion(aux):
                    self.principio = None
                    self.final = None
                    return aux
                else:
                    return None
            else:
                anterior = None
                while not self.esta_vacio(aux):
                    if operacion(aux):
                        self.principio = anterior
                        if self.esta_vacio(self.principio):
                            self.principio = aux.siguiente
                        else:
                            self.principio.siguiente = aux.siguiente
                        aux.siguiente = None
                        return aux
                    anterior = aux
                    aux = aux.siguiente
                return None
    # Tarea: Devuelve la cantidad nodos existente en la cola
    def cantidad_nodos(self):
        if self.principio == None:
            return 0
        else:
            contador = 0
            aux = self.final
            while not self.esta_vacio(aux):
                contador += 1
                aux = aux.siguiente
            return contador
    # Tarea: Comprobar que la cola este vacía
    def esta_vacio(self, puntero):
        if puntero == None:
            return True
        else:
            return False

class Caja:
    # Tarea: Caja[0] = {x|prioridad clientes embarazadas y ancianos}
    # Tarea: Caja[1] = {x|solo clientes discapacitados}
    # Tarea: Caja[2] = {x|solo clientes normales} 
    def __init__(self):
        self.cajas_del_supermercado = [Queue(), Queue(), Queue()]
    # Tarea: (0 > x > 1)
    def esta_dentro_del_intervalo(self, nro_caja):
        if nro_caja < 1 or nro_caja > 3:
            print("ER-0001: El nro de caja no se encuentra dentro del intervalo [1,3]")
            return True
        else:
            return False
    def agregar_a_la_cola(self, nro_caja, nodo):
        if not self.esta_dentro_del_intervalo(nro_caja):
            self.cajas_del_supermercado[nro_caja - 1].encolar(nodo)
    def sacar_de_la_cola(self, nro_caja):
        if not self.esta_dentro_del_intervalo(nro_caja):
            return self.cajas_del_supermercado[nro_caja - 1].desencolar()
        else:
            return None
    # Tarea: Comprobar la cantidad de clientes en cola de la caja
    def cantidad_de_clientes(self, nro_caja):
        if not self.esta_dentro_del_intervalo(nro_caja):
            return self.cajas_del_supermercado[nro_caja - 1].cantidad_nodos()
        else:
            return 0
    def comparar_datos(self, nro_caja, operacion):
        if not self.esta_dentro_del_intervalo(nro_caja):
            return self.cajas_del_supermercado[nro_caja - 1].comparar(operacion)
        else:
            return None

class Carrito:
    def __init__(self):
        self.carritos = [0, 0, 0, 0, 0, 0]
    # Tarea: Cargar DNI al conjunto
    def asignar_carrito(self, DNI, index):
        self.carritos[index] = DNI
    def liberar_carrito(self, DNI):
        for x in self.carritos:
            if x == DNI:
                self.carritos[self.carritos.index(x)] = 0
                return True
        return False
    # Tarea: Comprobar que haya un carrito disponible
    def hay_un_carrito_disponible(self):
        for x in self.carritos:
            if x == 0:
                return self.carritos.index(x)
        return -1
    # Tarea: Obtener la cantidad de carritos disponibles
    def cantidad_de_carrito_disponible(self):
        contador = 0
        for x in self.carritos:
            if x == 0:
                contador += 1
        return contador

def controlar_opcion(opcion, conjunto):
    for x in conjunto:
        if opcion == x:
            return True
    return False

def main():
    carrito_de_compra = Carrito()
    cola_de_espera_de_carritos = Queue()
    cola_de_la_caja = Caja()
    while True:
        print('------------------------------------------------')
        print('Caja Nro 1: prioridad clientes embarazadas y ancianos')
        print('Caja Nro 2: solo clientes discapacitados')
        print('Caja Nro 3: solo clientes normales')
        print('Informacion General:')
        cantidad_de_carritos_de_compra = carrito_de_compra.cantidad_de_carrito_disponible()
        # Caja[0] = {x|prioridad clientes embarazadas y ancianos}
        cantidad_de_cliente_en_caja_nro1 = cola_de_la_caja.cantidad_de_clientes(1)
        # Caja[1] = {x|solo clientes discapacitados}
        cantidad_de_cliente_en_caja_nro2 = cola_de_la_caja.cantidad_de_clientes(2)
        # Caja[2] = {x|clientes normales}
        cantidad_de_cliente_en_caja_nro3 = cola_de_la_caja.cantidad_de_clientes(3)
        # Esperando Carrito Disponibles:
        cantidad_de_cliente_esperando_carrito = cola_de_espera_de_carritos.cantidad_nodos()
        print('\tCarritos: ', end='')
        for x in range(cantidad_de_carritos_de_compra):
            print(f'\U0001F6D2', end='')
        print('\n\tCaja Nro 1: ', end='')
        for x in range(cantidad_de_cliente_en_caja_nro1):
            print(f'\U0001F9CD', end='')
        print('\n\tCaja Nro 2: ', end='')
        for x in range(cantidad_de_cliente_en_caja_nro2):
            print(f'\U0001F9BD', end='')
        print('\n\tCaja Nro 3: ', end='')
        for x in range(cantidad_de_cliente_en_caja_nro3):
            print(f'\U0001F9CD', end='')
        print('\n\tEsperando Carrito Disponibles: ', end='')
        for x in range(cantidad_de_cliente_esperando_carrito):
            print(f'\U0001F9CD', end='')
        print('\n------------------------------------------------')
        print('Menu:')
        print('1> Ingresar un cliente al SuperMercado')
        print('2> Finalizar compra de un cliente (x)')
        print('3> Salir')
        print()
        opcion = int(input('Ingrese una opcion: '))
        print()
        if controlar_opcion(opcion, [1, 2, 3]):
            if opcion == 1:
                clear()
                print('Agregar cliente:')
                print()
                nombre = input('Ingresar el nombre del cliente: ')
                apellido = input('Ingresar el apellido del cliente: ')
                DNI = int(input('Ingresar el DNI del cliente: '))
                print()
                print('Estado del cliente:')
                print('\t1> \U0001F930 Embarazada')
                print('\t2> \U0001F474 Anciano')
                print('\t3> \U0001F9BD Discapacitados')
                print('\t4> \U0001F9CD Perfectamente normal')
                print()
                estado = int(input('Ingrese una opcion: '))
                while True:
                    if controlar_opcion(estado, [1, 2, 3, 4]):
                        break
                    else:
                        print('-- El estado ingresado no se encuentra dentro del conjunto definido [1, 2, 3, 4] --')
                        estado = int(input('Ingrese una opcion: '))
                index = carrito_de_compra.hay_un_carrito_disponible()
                # Mostrar el estado general de la operación
                if index != -1:
                    # DNI mayor a 0 y DNI menor a 70.000.000
                    if DNI > 0 and DNI < 70000000:
                        if (cola_de_la_caja.comparar_datos(1, lambda aux : aux.dato.DNI == DNI) or 
                            cola_de_la_caja.comparar_datos(2, lambda aux : aux.dato.DNI == DNI)):
                            print(f'\tEl cliente con DNI {DNI} ya se encuentra en la cola de la Caja')
                        else:
                            # Asignar carrito
                            carrito_de_compra.asignar_carrito(DNI, index)
                            if estado == 1 or estado == 2:
                                cola_de_la_caja.agregar_a_la_cola(1, Nodo(Cliente(DNI, nombre, apellido, estado)))
                                print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 1')
                            elif estado == 3:
                                cola_de_la_caja.agregar_a_la_cola(2, Nodo(Cliente(DNI, nombre, apellido, estado)))
                                print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 2')
                            elif estado == 4:
                                cola_de_la_caja.agregar_a_la_cola(3, Nodo(Cliente(DNI, nombre, apellido, estado)))
                                print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 3')
                    else:
                        print(f'\tEl DNI {DNI} ingresado no cumple la condición (0 < x < 70.000.000)')
                else:
                    if (cola_de_espera_de_carritos.comparar(lambda aux : aux.dato.DNI == DNI) or 
                        cola_de_la_caja.comparar_datos(1, lambda aux : aux.dato.DNI == DNI) or 
                        cola_de_la_caja.comparar_datos(2, lambda aux : aux.dato.DNI == DNI)):
                        print(f'\tEl DNI {DNI} ya se encuentra en la cola de la Caja/ESPERA DE CARRITOS DISPONIBLES')
                    else:
                        print(f'\t{nombre} {apellido} de DNI {DNI} entro a la COLA DE ESPERA DE CARRITOS DISPONIBLES')
                        cola_de_espera_de_carritos.encolar(Nodo(Cliente(DNI, nombre, apellido, estado)))
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 2:
                clear()
                print('---------------------------------------------------------------')
                nro_caja = random.randint(1, 3)
                cliente = cola_de_la_caja.sacar_de_la_cola(nro_caja)
                if cliente != None:
                    print(f'El cliente {cliente.dato.nombre} {cliente.dato.apellido} de DNI {cliente.dato.DNI} dejo la Caja Nro {nro_caja}')
                    if carrito_de_compra.liberar_carrito(cliente.dato.DNI):
                        print('\tUn carrito liberado')
                    cliente = None
                    index = carrito_de_compra.hay_un_carrito_disponible()
                    if index != -1:
                        # Tarea: Buscar en la COLA DE ESPERA DE CARRITOS DISPONIBLES, personas con prioridad definida y asignar un carrito.
                        if cola_de_espera_de_carritos.comparar(lambda aux : aux.dato.estado == 1 or aux.dato.estado == 2 or aux.dato.estado == 3):
                            print('Hay un cliente de condiciones "ESPECIALES" en la COLA DE ESPERA DE CARRITOS DISPONIBLES')
                            cliente = cola_de_espera_de_carritos.desencolar_por_condicion(lambda aux : aux.dato.estado == 1 or aux.dato.estado == 2 or aux.dato.estado == 3)
                            if cliente != None:
                                print('El cliente de la COLA DE ESPERA DE CARRITOS DISPONIBLES:')
                                carrito_de_compra.asignar_carrito(cliente.dato.DNI, index)
                                if cliente.dato.estado == 1 or cliente.dato.estado == 2:
                                    cola_de_la_caja.agregar_a_la_cola(1, cliente)
                                    print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 1')
                                elif cliente.dato.estado == 3:
                                    cola_de_la_caja.agregar_a_la_cola(2, cliente)
                                    print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 2')
                                elif cliente.dato.estado == 4:
                                    cola_de_la_caja.agregar_a_la_cola(3, cliente)
                                    print(f'\t{nombre} {apellido} de DNI {DNI} entro a la cola de espera Caja Nro 3')
                            else:
                                print('No hay ningún cliente en la COLA DE ESPERA DE CARRITOS DISPONIBLES')
                        else:
                            cliente = cola_de_espera_de_carritos.desencolar()
                            if cliente != None:
                                print('El cliente de la COLA DE ESPERA DE CARRITOS DISPONIBLES:')
                                carrito_de_compra.asignar_carrito(cliente.dato.DNI, index)
                                if cola_de_la_caja.cantidad_de_clientes(1) == 0:
                                    cola_de_la_caja.agregar_a_la_cola(1, cliente)
                                    print('\tLa Caja Nro 1 se encuentra vacia, el cliente normal identificado como:')
                                    print(f'\t\t{cliente.dato.nombre} {cliente.dato.apellido} de DNI {cliente.dato.DNI} entro a la cola de espera Caja Nro 1')
                                elif cola_de_la_caja.cantidad_de_clientes(2) == 0:
                                    cola_de_la_caja.agregar_a_la_cola(2, cliente)
                                    print('\tLa Caja Nro 1 se encuentra vacia, el cliente normal identificado como:')
                                    print(f'\t\t{cliente.dato.nombre} {cliente.dato.apellido} de DNI {cliente.dato.DNI} entro a la cola de espera Caja Nro 2')
                                else:
                                    cola_de_la_caja.agregar_a_la_cola(3, cliente)
                                    print(f'\t{cliente.dato.nombre} {cliente.dato.apellido} de DNI {cliente.dato.DNI} entro a la cola de espera Caja Nro 3')
                            else:
                                print('No hay ningún cliente en la COLA DE ESPERA DE CARRITOS DISPONIBLES')
                    else:
                        print(f'\tNo hay carritos disponibles')    
                else:
                    print(f'No hay ningún cliente en la Caja Nro {nro_caja}')
                print('---------------------------------------------------------------')
                input('Presione cualquier tecla para continuar...')
                clear()
            elif opcion == 3:
                break
        else:
            print('La opcion ingresada no existe')
            input('Presione cualquier tecla para continuar...')
if __name__ == '__main__':
    main()