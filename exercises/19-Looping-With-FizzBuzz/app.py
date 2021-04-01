def fizz_buzz():
    # your code here
	for i in range(1,101):
        if i% 3 == 0 and i % 5 != 0:
            print(f"{i} es múltiplo de dos")
        elif i % 5 == 0:
            print(f"{i} es múltiplo de cuatro y de dos")
        else:
            print(f"{i} no es múltiplo de dos")
	return i

fizz_buzz()