try:
    T = int(input())

    for i in range(T):
        G = int(input())
        for j in range(G):
            parametros = input().split()
            I = parametros[0]
            N = parametros[1]
            Q = parametros[2]
            juego = []
    # H -> 0
    # T -> 1
            if I == "1":
                for n in range(int(N)):
                    juego.append(0)
            else:
                for n in range(int(N)):
                    juego.append(1)
            juego_final = []
            for k in range(int(N)):
                if (int(N) - k) % 2 == 0:
                    juego_final.append(juego[k])
                else:
                    juego_final.append(int(not juego[k]))
            if Q == "1":
                print(juego_final.count(0))
            else:
                print(juego_final.count(1))
except EOFError:
    pass
