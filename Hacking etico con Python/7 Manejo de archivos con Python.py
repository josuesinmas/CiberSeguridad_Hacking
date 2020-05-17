
archivo = open('archivo1.txt','w')
nombre=input("nombre: ")
edad=input("edad: ")

archivo.write(nombre)
archivo.write("\n")
archivo.write(edad)

print(" hemos escrito los datos")
archivo.close()

archivo2 = open('archivo2.txt','r')
#print(archivo2.readline())
#for l in archivo2.read():
#for l in archivo2.readline():
#for l in archivo2.read().split('\n'):
#    print(l)

lista = archivo2.read().split('\n')