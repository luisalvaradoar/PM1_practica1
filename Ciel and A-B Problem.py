try:
    numeros = input().split(" ")
    N = str(int(numeros[0]) - int(numeros[1]))
    if int(N[-1] < 9):
        print(int(N) + 1)
    else:
        print(int(N) - 1)
except EOFError:
    pass
