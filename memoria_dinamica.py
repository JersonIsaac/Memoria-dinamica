__author__ = 'Jerson Isaac'

class memDinamica:
    __lista = []

    def __init__(self, list):
    	self.__lista = list

    def agregarelementoarray(self, elemento): #Metodo que permite agregar mas elementos a las listas al final de estas
        self.__lista.append(elemento)

    def imprimirLista(self): #Este metodo puede imprimir si es llamado
    	print (self.__lista)




