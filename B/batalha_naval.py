matriz = [[0 for x in range(10)] for y in range(10)]
N = int(input())
resposta = "Y"
for x in range(N):
    D, L, R, C = input().split(' ')
    C = int(C) - 1
    R = int(R) - 1
    D = int(D)
    L = int(L)
    try:
        if D == 0:
            while L != 0:
                if matriz[R][C] == 1:
                    resposta = "N"
                matriz[R][C] = 1
                L -= 1
                C += 1
        else:
            while L != 0:
                if matriz[R][C] == 1:
                    resposta = "N"
                matriz[R][C] = 1
                L -= 1
                R += 1
    except IndexError:
        resposta = "N"
print(resposta)
