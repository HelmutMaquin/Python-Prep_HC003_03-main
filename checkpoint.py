# Importante: No modificar ni el nombre ni los argumetos que reciben las funciones, sólo deben escribir
# código dentro de las funciones ya definidas.

def ListaDivisibles(numero, tope):
    numeros_divi=[]
    t=1
    while (t<=tope/numero):
        numeros_divi.insert((t-1),t*numero)
        t +=1
    return numeros_divi
    
def Exponente(numero, exponente):

    b=numero**exponente
    return b

def ListaDeListas(lista):

    listafinal =[]
    if type(lista) != list:
        return None
    for i in lista:
        if (type(i) != list):
            listafinal.append(i)
        else:
            listafinal.extend(ListaDeListas(i))
    return listafinal

def Factorial(numero):

    if (type(numero) != int):
        return "deber ser un entero"
    if (numero>0):
        numero=numero*Factorial(numero-1)
    if (numero==0):
        numero = 1
    if (numero<0):
        return "nulo"
    return numero

def ListaPrimos(desde, hasta):

    List_pri=[]
    tope=hasta
    n=desde
    primo = True
    if(type(n) != int):
            return None
    if(type(tope)!= int):
            return None
    while (n<=tope):
        for div in range(2,n):
            if(n%div==0):
                primo=False
        if (primo):
            List_pri.insert(n-1,n)
        else:
            primo = True
        n +=1
    return List_pri

def ListaRepetidos(lista):
    
    if(type(lista)!=list):
        return None
    from collections import Counter
    list1 = Counter(lista).keys()
    list2 = Counter(lista).values()
    listf = zip(list1,list2)
    return list(listf)

def ClaseVehiculo(tipo, color):
    
    class Vehiculo:
        def __init__(self,tipo, color,velocidad = 0.0):
            self.tipo = tipo
            self.color = color
            self.velocidad = velocidad
        def Acelerar(self,velinc):
            self.velocidad = self.velocidad + velinc
            if self.velocidad < 0 :
                self.velocidad = 0
                return self.velocidad
            if self.velocidad>=100 :
                self.velocidad = 100
                return self.velocidad
            return self.velocidad
    return Vehiculo(tipo,color)

def OrdenarDiccionario(diccionario_par, clave, descendente=True):
    '''
    Esta función recibe como parámetro un diccionario, cuyas listas de valores tienen el mismo
    tamaño y sus elementos enésimos están asociados. Y otros dos parámetros que indican
    la clave por la cual debe ordenarse y si es descendente o ascendente.
    La función debe devolver el diccionario ordenado, teniendo en cuenta de no perder la
    relación entre los elementos enésimos.
    Recibe tres argumentos:
        diccionario:    Diccionario a ordenar.
        clave:          Clave del diccionario recibido, por la cual ordenar.
        descendente:    Un valor booleano, que al ser verdadero indica ordenamiento ascendente y 
                        descendente si es falso. 
                        Debe tratarse de un parámetro por defecto en True.
    Si el parámetro diccionario no es un tipo de dato diccionario ó el parámetro clave no 
    se encuentra dentro de las claves del diccionario, debe devolver nulo.
    Ej:
        dicc = {'clave1':['c','a','b'],
                'clave2':['casa','auto','barco'],
                'clave3':[1,2,3]}
        OrdenarDiccionario(dicc, 'clave1')          debe retornar {'clave1':['a','b','c'],
                                                                'clave2':['auto','barco','casa'],
                                                                'clave3':[2,3,1]}
        OrdenarDiccionario(dicc, 'clave3', False)   debe retornar {'clave1':['b','a','c'],
                                                                'clave2':['barco','auto','casa'],
                                                                'clave3':[3,2,1]}
    '''
    #Tu código aca:
    if type(diccionario_par) != dict:
        return None
    listet = list(diccionario_par.keys())
    for i in diccionario_par:
        if i == clave:
            for j in diccionario_par:
                diccionario_par[j].sort()
                if descendente == True:
                    diccionario_par[j].reverse()
    
    return diccionario_par
