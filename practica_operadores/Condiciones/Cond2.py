                                                                   
PASSWORD = "Lmmg"
#Definir_login
def login(pass_user):
    intentos = 3
    while(PASSWORD != pass_user and intentos > 0):
        pass_user = input("Incorrecto, escribe tu password!")
        intentos = intentos -1
        
    if PASSWORD == pass_user:
        print("Estas logeado")
    elif intentos == 0:
        print("Tus intentos se agotaron, Usuario blockeado!")
    
  
password = input("Ingresa tu password:")
login(password)

'''
Escribir una función que reciba una cadena de caracteres contraseña en una variable,
pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y
minúsculas.
'''
#2