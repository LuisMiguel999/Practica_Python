

print("Bienvenido a la pizzeria Bella Napoli.\nTipos de pizza\n\t1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el número correspondiente al tipo de pizza que quieres:")

if tipo == "1" :
    print("Ingredientes de pizzas vegetarianas\n\t 1- Pimiento\n\t2- Tofu\n")
    ingrediente =  input("introduce el ingrediente que desees: ")
    print("pizza vegetariana con mozarella, tomate y ", end = "")
    if ingrediente == "1":
        print("pimiento")
    else:
        print("tofu")
else:
        print("Ingredientes de pizzas no vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
        ingrediente =  input("introduce el ingrdiente que desees ")
        print("Pizza no vegetarina con mozarrella, tomate y ", end="")
        if ingrediente == "1":
             print("peperoni")
        elif ingrediente == "2":
             print ("jamon")
        else:
             print("salmon")
             
             
'''
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.
Ingredientes vegetarianos: Pimiento y tofu.
Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
función de su respuesta le muestre un menú con los ingredientes disponibles para que
elija. Solo se puede elegir un ingrediente además de la mozzarella y el tomate que
están en todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es
vegetariana o no y todos los ingredientes que lleva.
'''
             

#7