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
#Codigo correcto.
lista = [] #Lista. 6 Datos por ahora...
num = 0  #Este num va en la funcion. Son los numeros que pedimos y agregamos a la lista.

def pedidoNum(): #Definimos la funcion con la variable pedidoNum para el ingreso de datos.
              i = 0 #Contador
              while i <= 5: #Bucle para que ingrese hasta 6 numeros
                      num = int(input("Ingresar un numero:")) #Ingreso de datos
                      lista.append(num) #Realizamos un agregado de datos a la lista con .append
                      i += 1 #Limitamos el bucle con el contador i += 1.
                                        
def ordenarNums(): #Definimos la funcion ordenarNums para organizar los numeros, ya sean pares o impares.
        lista.sort() #Ordenamos la lista de menor a mayor con .sort
        listaPar = [] #listapar
        listaImpar = [] #listaimpar
        for i in lista:  #Bucle for para derivar la informacion.
            if i % 2 == 0: #Con esta condicion definimos si es par. Si i % 2 es igual a 0. Es par.
                    listaPar.append(i)
            else:   #Si no. Impar.
                    listaImpar.append(i)
        print("Numeros pares:{}".format(listaPar))   #Print de listas ordenadas
        print("Numeros impares: {}".format(listaImpar)) #Print de listas ordenadas

pedidoNum()
ordenarNums()

#Ejemplo de ejecucion.
'''Ingresar un numero:2
Ingresar un numero:3
Ingresar un numero:4
Ingresar un numero:5
Ingresar un numero:6
Ingresar un numero:7
Numeros pares:[2, 4, 6]
Numeros impares: [3, 5, 7]'''

                
                  










        
        
        


