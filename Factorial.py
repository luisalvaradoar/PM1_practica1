try:
    T = int(input())
    numeros = input().split(" ")
    for numero in numeros:
        n = 0
        for j in range(1, 14):
            n += int(numero) // (5 ** j)
        print(n)
except EOFError:
    pass