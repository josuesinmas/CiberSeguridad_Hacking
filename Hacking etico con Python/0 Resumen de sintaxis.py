#el primer programa que se acostumbra a hacer cuand so aprende cualquier lenguaje
print("Hola Mundo")

#Formas de comparar datos
# == igual
# != no igual
# > ayor que
# < menor que
# >= mayor o igual
# <= menor o igual
print(1 >= 1) #imprime un booleano que será verdadero si 1 es mayor o igal a 1


#Tipos de variables, 
entero = 10
print(type(entero))
flotante = 10.5
print(type(flotante))
verdad = False
print(type(verdad))
saludo = "Hola Usuario"
print(type(saludo))

#tipos de operaciones basicas que tenemos en python
# +
# -
# *
# **
# /
# //
# %
saludo = "Hola"
a = " como estas?"
print(saludo + a)

#tipos de logicas
# and y logico
# or o logico
# not no logico
#print(1>0 and 1>1) si las dos condiciones se cumplen se imprime true
#print(1>2 or 2>5) si una de las dos condiciones se cumple da true
print(not True)

#formas de pedir datos y encadenarlos 
nombre = raw_input("Digite su nombre: ")
edad = int(raw_input("Digite la edad:"))
print("Hola {}, su edad es {}, y el doble de su edad es {}".format(nombre,edad,edad*2))

#tipos de condiciones logicas
# if 
# elif
# else
edad = int(raw_input("Digite su edad: "))
#nombre = raw_input("Digite su nombre: ")
if not edad == 19:
	print("Correcto")
else:
	print("Error")


#bucle for 
numero = int(raw_input("Numero: "))
mensaje = raw_input("Mensaje: ")
for m in range(0,numero):
	print("{} : {}".format(m,mensaje))


#bucle while
numero = int(raw_input("Numero: "))
mensaje = raw_input("Mensaje: ")
i = 1
while i <= numero:
	print(mensaje)
	i = i+1


#listas y sus funciones
# pop nos sirve para eliminar el ultimo elemento de una lista
# del para borrar ciertos elementos de determinadas pocisiones
# ''.join(variable) nos ayuda a convertir una variable en una lista
# append nos ayuda a añadir nuevos elementos a una lista
lista = [1,2,3,4,5,6,7,8,"a","b","c",2.1,2.4,0.2,True,False]
lista1 = ['h','o','l','a']
lista1 = ''.join(lista1)
print(lista1)
print(lista[0:10])
lista.pop()
print(lista)
for l in lista:
	print(l)

del lista[1]
print(lista)

for n in range(90,100):
	lista.append(n)
print(lista)
lista.append("z")
print(lista)

#tuplas
a = ("a",1,2,3,1.5,"c")
print(a[:])
for n in a:
	print(n)

#diccionarios
diccionario = dict(nombre="alumno",plataforma="Udemy",edad=18)
# items 
#print(diccionario)
#a = diccionario.items()
#print(a)
#copy
#b = diccionario.copy()
#print(b)
# keys
# keys = diccionario.keys()
#print(keys)
# values
#values = diccionario.values()
#print(values)
for n in diccionario.keys():
	print("{} Su valor es: {}".format(n,diccionario[n]))

# Funciones
def saludo():
	print("Bienvenido")
def despedida():
	print("adios")
def main():
	saludo()
	despedida()

if __name__ == '__main__':
	main()

#funciones con multiples parametros
def saludo2(nombre1,edad1):
	print("Hola {} tienes: {}".format(nombre1,edad1))
def main():
	nombre = raw_input("Nombre: ")
	edad = int(raw_input("Edad: "))
	saludo2(nombre,edad)
if __name__ == '__main__':
	main()

#creando una clase 
class Carro1(object):
	def __init__(self):
		self.llantas = 4
		self.color = "rojo"
		self.puertas = 2

carro1 = Carro1()
print(carro1.color)
print(carro1.puertas)
print(carro1.llantas)

#otra ejemplo de clases con funcione un poco mas complejas
class Carro(object):
	def __init__(self,m):
		self.color = "Rojo"
		self.puertas = 4
		self.tipo = "Deportivo"
		self.m = m
	def movilidad(self):
		if self.m == True:
			print("Acelerar")
		else:
			print("Frenar")

#instanciamos la clase en la funcion main
def main():
	while True:
		print("1 Acelerar")
		print("2 Frenar")
		valor = int(raw_input("> "))
		if valor == 1:
			c = Carro(True)
			c.movilidad()
		else:
			c = Carro(False)
			c.movilidad()
	#print(c.color)
	#print(c.puertas)
	#print(c.tipo)
if __name__ == '__main__':#ejecutamos la funcion main si se cumple la condicion
	main()


#distintos tipos de funciones con metodos de clases
# classmethod
# staticmethod
# property
class prueba1(object):
	def __init__(self,radio):
		self.radio = radio

	@classmethod # Nos ayuda a usar una funcion sin que antes la clase sea atribuida a un objeto
	def saludo(cls,nombre):
		print("Hola {}".format(nombre))

	@staticmethod #Nos yuda a trabajar con funciones sin argumentos
	def saludo_static():
		print("Bienvenido")

	@property #Con property trabajamos con funciones como si fueran variables al usar 'return'
	def area_circulo(self):
		return 3.1416*(self.radio**2)
def main():
	#nombre = raw_input("Nombre: ")
	#prueba1.saludo(nombre)
	c = prueba1(5)
	area = c.area_circulo
	print(area)
if __name__ == '__main__':
	main()

#utilizamos bloques try catght par manejar errores
try:
	raise IOError
except IOError:
	print("Ocurrio un error")

