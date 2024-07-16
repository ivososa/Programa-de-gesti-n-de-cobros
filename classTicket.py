'''
Por cada ticket cobrado se tienen los siguientes datos:
- número de ticket (un entero),
- nombre de puesto de peaje (una cadena de caracteres
- un número entre 1 y 10 para indicar la ventanilla o carril que hizo el cobro en ese puest
- una cadena para la patente del automóvil al que se le hizo el cobro
- número entero para indicar el monto que se cobró.
'''


class Ticket():
    def __init__(self, num, nombre, ventanilla, patente, monto):
        self.num = num
        self.nombre = nombre
        self.ventanilla = ventanilla
        self.patente = patente
        self.monto = monto

    def __str__(self):
        xd = f' Numero de ticket: {self.num} ' \
             f'   Nombre de puesto: {self.nombre} ' \
             f'   Ventanilla: {self.ventanilla} ' \
             f'   Patente: {self.patente} ' \
             f'   Monto cobrado: {self.monto}'
        return xd