def conversor(tipo_pesos, valor_dolar):
    pesos = input("cuántos pesos" +"tipo_pesos"+" tienes?:" )
    pesos = float(pesos)
    dolares = pesos / valor_dolar
    dolares = round (dolares, 2)
    dolares = str(dolares)
    print("Tienes $ " + dolares + " dólares")



menu = """
Bienvenido camarada 😎

1 - Pesos Colombianos
2 - Pesos Mexicamos
3 - Pesos Bolivianos
Elige una opción: """
opcion = int(input(menu))
if opcion == 1:
    conversor("colombianos", 3875)
elif opcion == 2:
    conversor("Mexicanos", 20)
elif opcion == 3:
    conversor("Bolivianos", 6.97)
else:
    print ("no seas peji, pon una opción")