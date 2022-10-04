def conversacion(mensaje):
    print("hola")
    print("como estas")
    print(mensaje)
    print("adios")

opcion = int(input("elige una opcion (1,2,3): "))
if opcion == 1:
    conversacion("elegiste la opcion 1")
elif opcion == 2:
    conversacion("elegiste la opcion 2")
elif opcion == 3:
    conversacion("elegiste la opcion 3")
else:
    print("elige un opción pa")

