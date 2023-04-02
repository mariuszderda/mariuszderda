# liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 13, 14, 17, 19, 23, 29]

# for n in liczby:
#     if n % 2 == 0:
#         print(f'Liczba {n} jest liczbą parzystą.')
#     else:
#         continue

# i = 1

# while i < 10:
#     print(i)
#     i+=1 


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

def suma (a, b):
    print(f'Suma liczb {a} oraz {b} to {a + b}')

def power_number_2 (a):
    val = range(a)
    for num in val:
        print(f'2 do potęgi {num + 1} to: {2**(num+1)}') 

def sum_of_number(liczba):
    sum = 0

    for n in liczba:
        sum += int(n)
    
    print(f'Suma cufr liczby {liczba} to: {sum}')

def element_of_number(number):
    i = 1
    while True:
        if i * i == number:
            print(f'Pierwiastkiem liczby {number} jest {i}.')
            break
        elif i * i > number:
            print(f'Pierwiastkiem liczby {number} nie jest liczba całkowita.')
            break
        else:
            i += 1
            continue


# wartość_bezwzgledna(input_number)

while True:
    input_action_number = input("""
    ############## Co chcesz zrobic  ##############
    ## 1 - porównaj liczby                       ##
    ## 2 - zwróć wartość bezwzględną             ##
    ## 3 - pomnóż                                ##
    ## 4 - dodaj                                 ##
    ## 5 - 2 do potęgi n (podaj n)               ##
    ## 6 - suma cyfr                             ##
    ## 7 - pierwiastek liczby                    ##
    ## X - zakończ program                       ##
    ###############################################
    """)

    if(str(input_action_number) == 'x'):
        print('Zapraszam ponownie.')
        break
    elif int(input_action_number) == 5:
        power2 = input("Podaj liczbę do spotengowania: ")
        power_number_2(int(power2))
        continue
    elif int(input_action_number) == 6:
        number_to_sum = input("Podaj liczbę do zsumowania: ")
        sum_of_number(number_to_sum)
        continue
    elif int(input_action_number) == 7:
        number = input("Podaj liczbę do obliczenia pierwiastka: ")
        element_of_number(int(number))
        continue

    input_number1 = int(input("Podaj pierwszą liczbę: "))
    input_number2 = int(input("Podaj drugą liczbę: "))

    # if(str(input_action_number) == 'x'):
    #     print('Zapraszam ponownie.')
    #     break
    if (int(input_action_number) == 1):
        compare(input_number1, input_number2)
        continue  
    elif (int(input_action_number) == 2):
        wartość_bezwzgledna(input_number1)
        wartość_bezwzgledna(input_number1)
        continue
    elif (int(input_action_number) == 3):
        multiply(input_number1, input_number2)
        continue
    elif (int(input_action_number) == 4):
        suma(input_number1, input_number2)
        continue
    else:
        print("Nie właściwy wybór")
