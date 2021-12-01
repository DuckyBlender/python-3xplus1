import math, time
print("""
              ┌─────────────────────────┐
              │ Witaj w programie 3x+1! │
┌─────────────┴─────────────────────────┴───────────────────┐ ┌───────────────────────────────────────────────────────────┐ ┌──────────────────────────────┐
│                       ZASADY                              │ │                       UŻYWANIE                            │ │       3x + 1 CALCULATOR      │
│ 1. Jeśli liczba jest parzysta to się dzieje 3x + 1.       │ │ 1. Napisz liczbę, ktora ma być obliczona.                 │ │ Autor: DuckyBlender          │
│ 2. Jeśli liczba jest nieparzysta to się dzieli razy dwa.  │ │ 2. Jeśli wszystkie liczby po kolei sprawdzić, wpisz "ALL" │ │ Wersja: Release 2.0          │
│ Założenie jest takie, że każda liczba dojdzie do 1.       │ │ 3. Po wpiseniu "ALL" napisz ilość liczb, lub napisz "INF" │ │ Data: 18.11.2021             │
└───────────────────────────────────────────────────────────┘ └───────────────────────────────────────────────────────────┘ └──────────────────────────────┘""")
firstInput = input("Podaj liczbę, lub napisz \"ALL\": ")
times = 0
max = 0

if firstInput.isdigit():
    temp = int(firstInput)
    while True:
        if temp % 2 == 0:
            temp = temp / 2
            times = times + 1
            if temp >= max:
                max = temp
            print("Liczba: " + str(int(temp)) + " | Kroki: " + str(int(times)) + " | Max: " + str(int(max)) + " | -")
            if (math.trunc(temp)) == 1:
                break
        if temp % 2 == 1:
            temp = 3 * temp + 1
            times = times + 1
            if temp >= max:
                max = temp
            print("Liczba: " + str(int(temp)) + " | Kroki: " + str(int(times)) + " | Max: " + str(int(max)) + " | +")
            if int(temp) == 1:
                break
else:
    if firstInput.upper() == "ALL":
        secondInput = input("Ile liczb sprawdzić? Napisz \"INF\", aby spradzić naknajwięcej: ")
        if secondInput.isdigit():
            maxNumber = int(secondInput)
            number = int(1)
            temp = number
            while maxNumber >= number:
                if temp % 2 == 0:
                    temp = temp / 2
                    times = times + 1
                    if temp >= max:
                        max = temp
                    if int(temp) == 1:
                        print("Liczba: " + str(int(number)) + " | Kroki: " + str(int(times)) + " | Max: " + str(int(max)))
                        max = 0
                        times = 0
                        number = number + 1
                        temp = number
                if temp % 2 == 1:
                    temp = 3 * temp + 1
                    times = times + 1
                    if temp >= max:
                        max = temp
                    if int(temp) == 1:
                        print("Liczba: " + str(int(number)) + " | Kroki: " + str(int(times)) + " | Max: " + str(int(max)))
                        max = 0
                        times = 0
                        number = number + 1
                        temp = number
        else:
            if secondInput.upper() == "INF":
                number = int(1)
                temp = number
                print("Eksplozja za 3 sekundy...\n")
                time.sleep(3)
                while True:
                    if temp % 2 == 0:
                        temp = temp / 2
                        times = times + 1
                        if temp >= max:
                            max = temp
                        if (int(temp)) == 1:
                            print("Liczba: " + str(int(number)) + " | Kroki: " + str(int(times)) + " | Max: " + str(int(max)))
                            max = 0
                            times = 0
                            number = number + 1
                            temp = number
                    if temp % 2 == 1:
                        temp = 3 * temp + 1
                        times = times + 1
                        if temp >= max:
                            max = temp
                        if (int(temp)) == 1:
                            print("Liczba: " + str(int(number)) + " | Kroki: " + str(int(times)) + " | Max: " + str(int(max)))
                            max = 0
                            times = 0
                            number = number + 1
                            temp = number
                    exit
            else:
                print("ERROR 2: Niewłaściwy input! Przujmuję wartości: Liczba, \"INF\".")
                exit
    else:
        print("ERROR 1: Niewłaściwy input! Przujmuję wartości: Liczba, \"ALL\".")
        exit
print("Pomyślnie zakończono zadanie.")
