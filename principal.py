__author__ = 'Jerson Isaac'

from memoria_dinamica import *
productos = ['Manzanas','E-pura', 'Coca-Cola', 'Bolillo', 'Pastel', 'Salsa Chamoy']
precios = [12, 34, 45, 47, 20]

lista = memDinamica(productos) #Se llama a la clase de memDinamica y  se especifica la lista
lista.imprimirLista()
lista2 = memDinamica(precios)
lista2.imprimirLista()

#Agregando elementos a las listas de "productos" y ""precios".
lista.agregarelementoarray('cerveza')
lista.agregarelementoarray('Chicles')
lista.agregarelementoarray('Sabritas')
lista.agregarelementoarray('Jamon')
lista.agregarelementoarray('Helado')
lista.agregarelementoarray('Sandia')
lista.agregarelementoarray('Mayonesa')
lista.agregarelementoarray('Queso')
lista.agregarelementoarray('Tostadas')

lista.imprimirLista() #En esta linea se imprime los datos capturados que se encuentran en la variable "lista"

lista2.agregarelementoarray(19)
lista2.agregarelementoarray(20)
lista2.agregarelementoarray(80)
lista2.agregarelementoarray(40)
lista2.agregarelementoarray(100)
lista2.agregarelementoarray(30)
lista2.agregarelementoarray(16)
lista2.agregarelementoarray(50)
lista2.agregarelementoarray(25)

lista2.imprimirLista()
