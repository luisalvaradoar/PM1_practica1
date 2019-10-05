try:
    numeros = input().split(" ")
    N = str(int(numeros[0])-int(numeros[1]))
    if int(N[-1]<9):
        N_nuevo = int(numeros[0])-int(numeros[1]) + 1
    else:
        N_nuevo = int(numeros[0])-int(numeros[1]) - 1
    print(N_nuevo)
except EOFError:
    pass
