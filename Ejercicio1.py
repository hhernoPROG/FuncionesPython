'''Crear un programa que tenga una lista, luego crear una funcion con la 
cual se van a pedir numeros al usuario para agregar a la lista. 
Debes crear una segunda funcion en donde se ordenen los numeros 
pares e impares dentro de dos listas nuevas'''

'''
·Mi codigo·
lista = []
listaImp = []
listaPar = []

def pedidoNum(): #Definimos la funcion con la variable pedidoNum
              
              while len(lista) < 5: #el LEN lo esta utilizando para limitar los datos a ingresar.
               numeros = int(input('Ingresar 5 numeros:')) #Pedimos los numeros
               if numeros == 0: #Si el numero es menor a 0 que haga un break, es decir corta el programa.
                       print("Ingresaste un numero invalido.")
                       break 
               else:
                       lista.append(numeros)   #Si los numeros son validos, se agregan hasta 5 veces en la lista.

print("Los numeros ingresados son:{}".format(lista))#Se imprime los numeros ingresados.              

def ordNums():
        while listaImp.index(lista) % 2:
                listaImp.append(lista)
        else:
                listaPar.index(lista)'''

lista = [] #Lista. 5 Datos por ahora...
num = 0  #Este num va en la funcion. Son los numeros que pedimos y agregamos a la lista.

def pedidoNum(): #Definimos la funcion con la variable pedidoNum
              i = 0 
              while i <= 5:
                      num = int(input("Ingresar un numero:"))
                      lista.append(num)
                      i += 1
                                        
def ordenarNums():
        lista.sort()
        listaPar = []
        listaImpar = []
        for i in lista:
            if i % 2 == 0:
                    listaPar.append(i)
            else:
                    listaImpar.append(i)
        print("Numeros pares:{}".format(listaPar))
        print("Numeros impares: {}".format(listaImpar))

pedidoNum()
ordenarNums()

                
                  










        
        
        


