# from dataclasses import dataclass
# from datetime import datetime

# imie = input('Podaj swoje imie: ')
# rok = int(input('Podaj rok urodzenia: '))

# print(type(datetime.now().date()))

# data = datetime.now().date()

# wiek = datetime.now().year - rok

# print('Cześć, ' + imie + '!')
# print('Obecnie masz '+ str(wiek) +' lat, 100 lat osiągniesz w ' + str(rok + 100) + ' roku.')

# input_number = int(input("Podaj dowolną liczbę: "))

# if(input_number == 0):
#     print('Podałeś 0')
#     pass

# if(input_number % 2 == 0):
#     print('Podana liczba jest parzysta.')
# else:
#     print('Podana liczba jest nie parzysta.')


# if (input_number == 0):
#     print('Podałeś 0')
# elif (input_number % 2 == 0):
#     print('Podana liczba jest parzysta.')
# else:
#     print('Podana liczba jest nie parzysta.')


def wartość_bezwzgledna(liczba):
    if (liczba < 0):
        print('Wartość bezwzględna liczby: '+ str(liczba) + " to: " + str(-liczba))
    else:
        print('Wartość bezwzględna liczby: '+ str(liczba) + " to: " + str(liczba))

def multiply (a, b):
    print('Wartość mnożenie liczb ' + str(a) + " oraz liczby " + str(b) + " to " + str(a * b)  )

def compare (a, b):
    if (a == b):
        print('Obie liczby są takie same.')
    elif (a > b):
        print('Pierwsza liczba (' + str(a) + ') jest większa od drugiej liczby (' +str(b) + ')')
    else:
        print('Druga liczba ' + str(b) + ' jest większa od pierwszej liczby ' +str(a) + ')')

    

# wartość_bezwzgledna(input_number)

input_number1 = int(input("Podaj pierwszą liczbę: "))
input_number2 = int(input("Podaj drugą liczbę: "))
input_action_number = int(input("""
############## Co chcesz zrobic  ##############
## 1 - porównaj liczby                       ##
## 2 - zwróć wartość bezwzględną             ##
## 3 - pomnóż                                ##
###############################################
"""))

if(input_action_number == 1):
    compare(input_number1, input_number2)
elif (input_action_number == 2):
    wartość_bezwzgledna(input_number1)
    wartość_bezwzgledna(input_number1)
elif (input_action_number == 3):
    multiply(input_number1, input_number2)
else:
    print("Nie właściwy wybór")
