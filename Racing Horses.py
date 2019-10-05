try:
    T = int(input())

    for i in range(T):
        N = int(input())
        caballos = input().split(" ")
        Si = []
        for caballo in caballos:
            Si.append(int(caballo))
        Si.sort()
        diferencias = []
        for j in range(len(Si) - 1):
            diferencias.append(Si[j + 1] - Si[j])
        print(min(diferencias))
except EOFError:
    pass
