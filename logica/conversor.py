import numpy as np

class ConversorAngulos:
    def __init__(self,angulo,op):
        self.angulo = angulo
        self.op = op

    def menuOpciones(self):
        print("""
        CONVERSOR DE GRADOS\n
        1. GRADOS A RADIANDES
        2. RADIANES A GRADOS\n
        """)

        self.op = int(input("Ingrese una opción: "))

    def conversion(self):

        if self.op == 1:
            self.angulo = float(input("Ingrese el angulo en grados: "))
            resultado = self.angulo * 180 / (2 * np.pi)
        elif self.op == 2:
            self.angulo = float(input("Ingrese el angulo en radianes: "))
            resultado = self.angulo * 2 * np.pi / 180
        else:
            print("Opción incorrecta, intentelo nuevamente.")

        return resultado

    def imprimirResultado(self, resultado):
        if self.op == 1:
            print(f'El resultado de la conversión es: {resultado} radianes')
        elif self.op == 2:
            print(f'El resultado de la conversión es: {resultado} grados')
