from ClasePila import Pila
def factorial(numD):
    total= 0
    unaPila= Pila(numD+1)
    guardarNum=numD
    while(numD >= 0):
        unaPila.insertar(numD)
        numD -= 1
    while unaPila.vacia() == False:
        if total != 0:
            total *= unaPila.suprimir()
        else:
            total= unaPila.suprimir() + 1
    print("El factorial de {} es: {}".format(guardarNum,total))
if __name__=='__main__':
    print("-----CALCULAR EL FACTORIAL DE UN NUMERO-----")
    num=int(input("Ingrese el numero para calcular el factorial: "))
    factorial(num)
