from array import array
from random import choice


name = input('Podaj swoje imie: ')
print(f'Cześć {name}! Zagramy w zgadywankę. Podaj zakres liczb, ja wylosuję jedną liczbę z zakresu, natomiast Ty będziesz musiał ją odgadnąć.')
step = 0

while True:
    win = 0

    if (win == 1):
        break

    if (step > 1):
        print('Jeśli masz dość, zamiast pierwszej liczby wpisz X')

    first_number = input('Podaj pierwszą liczbę: ')
    second_number = input('Podaj drugą liczbę: ')

    if (first_number == second_number):
        print('Ale śmieszek, ale liczby muszą być różne.')
        continue

    if (first_number == 'x'):
        print(f'Niestety poddałeś się po {step} kroku(ów).')
        break

    numbers = [int(first_number), int(second_number)]
    numbers.sort()

    computer_number = int(choice(range(int(numbers[0]), int(numbers[1]))))
    # print('Computer number: ' + str(computer_number))

    while True:
        user_number = int(input("Jak myślisz jaka to liczba?"))

        if(user_number < int(numbers[0])):
            print('Podałeś liczbę spoza zakresu. Zaczynamy od nowa')
            step +=1
            break
        elif(user_number > int(numbers[1])):
            print('Podałeś liczbę spoza zakresu. Zaczynamy od nowa')
            step +=1
            break
        elif(user_number == computer_number):
            print(f'Gratulacje. Do odgadnięcia potrzebowałeś {step + 1} kroków')
            win = 1
            break
        elif(user_number > computer_number):
            print('Niestety nie trafiłeś, Twoja liczba jest większa od wylosowanej')
            step +=1
            continue
        elif(user_number < computer_number):
            print('Niestety nie trafiłeś, Twoja liczba jest mniejsza od wylosowanej')
            step +=1
            continue

        
