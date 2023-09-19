from logica.conversor import ConversorAngulos

if __name__ == '__main__':
    print("===Bienvenido===\n")
    conversor = ConversorAngulos(angulo=0,op=0)
    conversor.menuOpciones()
    result = conversor.conversion()
    conversor.imprimirResultado(result)

