"""

    BLOG DE NOTAS DE ()
    --------------------
    v1.0
    --------------------
    *Ejercicio 3 putns  para el examen final del modulo
    *Sin internet
    Solo Evernote
    No SLACK
    *Diseñado para terminal
    *.persar bien las opciones que tendra el blog de notas
    *Diagramacion en www.lucidchart.co (diamgrama flujo)
    Entorno virtual Python 3.7.4
    Git local
    Finalizar el ejercicio a las 16:15. Eviar enlace por gitHub



"""


# IMPORT'S
# import os
import csv

# CLASE CONTENIDO de la NOTA


class contenidoNota():

    def __init__(self, titulo, escritura):

        self.Titulo = titulo
        self.escritura = escritura

# CLASE bloc de notas


class BlocNotas():

    def __init__(self):

        self._listaNota = []

    def Agregar(self, titulo, escritura):

        nuevaNota = contenidoNota(titulo, escritura)

        self._listaNota.append(nuevaNota)

        self._guardar()

    def Abrir(self):

        print('Estos son las notas que tienes: ')

        for nota in self._listaNota:

            print(nota.Titulo)

        print('Escoge cual nota quieres abrir: ')

        inputAbrir = input('Escoge la nota: ')

        for AbrirNota in self._listaNota:

            if AbrirNota.Titulo.lower() == inputAbrir.lower():

                self._imprimir_Nota(AbrirNota)

                break

    def Eliminar(self):

        print('Estos son las notas que tienes: ')

        for nota in self._listaNota:

            print(nota.Titulo)

        print('Escoge cual nota quieres abrir: ')

        inputEliminar = input('Escoge la nota: ')


        for index, nota in enumerate(self._listaNota):

            if nota.Titulo.lower() == inputEliminar.lower():

                del self._listaNota[index]

                self._guardar()

                break
        





    def _guardar(self):

        with open('notas.csv', 'w') as Escribir:
            writer = csv.writer(Escribir)

            # escribir las columnas
            writer.writerow(('Titulo: ', 'Contenido: '))

            # escribir contacto por filas
            for nota in self._listaNota:
                    # writer.writerow(('Titulo: ', nota.Titulo, '\n', 'Contenido: ', nota.escritura))
                writer.writerow((nota.Titulo, nota.escritura))

    def _imprimir_Nota(self, listaNota):

        print('*******************************************')
        print(f'Titulo: {listaNota.Titulo}')
        print('---------------------------------------')
        print(f'Contenido: {listaNota.escritura}')
        print(f'******************************************')

        # RUN


def run():

    blocNotas = BlocNotas()

    # En este metodo nos permitira que cuando se reinicie la consola, lo que teniamos habiamos agregado previamente
    # al archivo csv. lo volvamos a agregar para cuando usemos los demas metodos, tengamos en memoria las notas que hicimos
    # con anterioridad

    # ************************************************************************

    #* Este es el pedazo de codigo para cuando se reinicie la consola , la lista agregue de nuevo
    #*las notas que fueron previamente agregadas, si es que fueron agregadas previamente, la cuestion
    #* la cuestion es que en mis apuntes este pedazo de codigo si funciona, el tema de nombres y todo, estan bien
    #* pero da error

    # with open('notas.csv', 'r') as f:

    #     # READER: es una funcion del csv

    #     leer = csv.reader(f)

    # #

    #     for index, row in enumerate(leer):

    #         if index == 0:

    #             continue

    #         else:

    #             blocNotas.Agregar(row[0], row[1])

    #*****************************************************************************



    while True:

        print('------------------------------------------------')
        print('l    BIENVENIDO A TU BLOC DE NOTAS PREFERIDO   l')
        print('l                                              l')
        print('l    ESCOGE ENTRE LAS OPCIONES                 l')
        print('l    1. Abrir nota                             l')
        print('l    2. Agregar nota                           l')
        print('l    3. Eliminar nota                          l')
        print('l**********************************************l')

        opcion = int(input('Tu opcion es: '))

        if opcion == 1:

            blocNotas.Abrir()

        elif opcion == 2:

            inputTitulo = input('Introduce el titulo: ')

            inputContenido = input('Contenido: ')

            blocNotas.Agregar(inputTitulo, inputContenido)

        elif opcion == 3:

            blocNotas.Eliminar()

        else:

            print('No escogiste ninguna opcion')

 


if __name__ == "__main__":

    run()
