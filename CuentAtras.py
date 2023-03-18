'''
Jesús Rosales Santana
18-03-2023
Cronómetro regresivo en python
'''
import time#Librería de python para controlar el tiempo. 

def cuentaAtras(num_segundos):#Función con un parámetro en segundos. 
    while num_segundos:
        min, seg = divmod(num_segundos, 60)#Divmod en una función en python que se encarga de aceptar dos números y devuelve el producto y el resto de los dos números, respectivamente. 
        minutos_segundos = "{:02d} : {:02d}".format(min, seg)#Se define el formato del tiempo.
        print(minutos_segundos)#Se imprime el formato.
        time.sleep(1)#Que el tiempo espere un segundo.
        num_segundos -= 1 #Le restamos 1 a los segundos.
    print("Cuenta atras finalizada")

tiempo_usuario = int(input("Dime el tiempo en segundos: "))

print(cuentaAtras(tiempo_usuario))

