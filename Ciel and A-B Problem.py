try:
    numeros = input().split(" ")
    N = str(int(numeros[0])-int(numeros[1]))
    N_nuevo = N[0:len(N) - 1] + str((int(N[-1]) + 1) % 10)
    print(N_nuevo)
except EOFError:
    pass
