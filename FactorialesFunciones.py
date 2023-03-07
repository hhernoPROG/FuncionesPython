'''Escribir una función que reciba un número entero positivo y devuelva su factorial.

'''
'''
#1 Menos Optima

#Definimos la funcion
def factorial(): 
    num = int(input("Ingresar un numero entero y positivo:")) #Solicitamos el numero
    if num > 0: #Si NUM es menor a 0
        factorial = 1 #Definimos una variable para el factorial
        for i in range(1, num + 1): #i toma el valor de 1.
            #El +1 Sirve para llegar a uno mas, ya que range limita hasta el "ultimo".
            factorial = factorial * i
        print(factorial)     
    else:
        print("El numero es negativo") #Si es menor a 0 es negativo, lo saca.
factorial()
'''

#2 Mas optima.

def factorial(): 
    from math import factorial #CONTEXTO, importamos factorial desde una libreria. Un import de python
    num = int(input("Ingresar un numero entero y positivo:")) #Solicitamos el numero
    if num > 0: #Si NUM es menor a 0
        print(factorial(num))
    else:
        print("El numero es negativo") #Si es menor a 0 es negativo, lo saca.
factorial()
