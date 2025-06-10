# MENU CALCULADORA
    # METODOS DEF
    # VALIDACIONES CON TRY EXCEPT
    # MENU ITERATIVO

# CREACION DE FUNCIONES DEF
import time

#METODO DEF QUE RECIBE DOS ARGUMENTOS, NUM1 Y NUM2


def sumar(num1,num2):
    resultado_suma = num1 +num2
    return(resultado_suma)

def restar(num1,num2):
    resultado_resta = num1 - num2
    return(resultado_resta)

def dividir(num1,num2):
    try:
        resultado_division = num1 / num2
        return(resultado_division)
    except ZeroDivisionError:
        print(' error: no se puede dividir por cero.')
        time.sleep(3)

def multiplicar(num1,num2):
    resultado_multiplicacion = num1 * num2
    return(resultado_multiplicacion)

def mostrar_menu():
    print('===========================================')
    print('Menu de claculadora en python')
    print('===========================================')
    print('1.- sumar.')
    print('2.- restar.')
    print('3.- multiplicar.')
    print('4.- dividir.')
    print('5.- salir.')

def obtener_numeros():
    while True:
        try:
          num1 = int(input('Ingrese el primer numero a operar:'))
          num2 = int(input('Ingrese el segundo numero a operar:'))

          return num1, num2
        except ValueError:
           print('Error, por favor ingrese numeros validos.')

def main():
    # ciclo para repatir menu

    while True:
        # llamar a funcion mostrar menu
        mostrar_menu()

        # menu de opciones segun el numero ingresado
        # ingresar una opcion 
        try: 
            op = int(input('Por favor ingrese una opcion de 1 a 5'))
        except ValueError:
            print('Error, ha ingresado un valor no numerico.')
            time.sleep(3)

            # validad que el numero ingresado sea una opcion de 1 a 5
            if op < 1 or op > 5:
                print(' Ha ingresado una opcion no valida.')
                time. sleep(3)

            if op in [1,2,3,4]:
                # en la variable num1 y num2 guardan los datos ingresados
                # en la funcion obtener numeros
                num1, num2 = obtener_numeros()

                if op == 1:
                    resultado = sumar(num1,num2)
                    print(f'Resultado de la suma: {resultado}\n')
                    time. sleep(2)

                if op == 2:
                    resultado = restar(num1,num2)
                    print(f'Resultado de la resta: {resultado}\n')
                    time. sleep(2)

                if op == 3:
                    resultado = multiplicar(num1,num2)
                    print(f'Resultado de la multiplicacion: {resultado}\n')
                    time. sleep(2)

                if op == 4:
                    resultado = dividir(num1,num2)
                    print(f'Resultado de la division: {resultado}\n')
                    time. sleep(2)

            if op == 5: 
                print('Muchas gracias por utilizar el programa. ')
                exit()

        main()


                    

