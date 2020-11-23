jogadas = input()
jogador = 0  # 0 - esquerda; 1 - direita
game = [0, 0]
pontos = [0, 0]

for each in jogadas:
    if each == "S":
        if jogador == 0:
            pontos[0] += 1
        else:
            pontos[1] += 1
    elif each == "R":
        if jogador == 0:
            pontos[1] += 1
            jogador = 1
        else:
            pontos[0] += 1
            jogador = 0
    else:
        if game[0] == 2:
            print("{} (winner) - {}".format(game[0], game[1]))
        elif game[1] == 2:
            print("{} - {} (winner)".format(game[0], game[1]))
        elif jogador == 0:
            print("{} ({}*) - {} ({})".format(game[0], pontos[0], game[1], pontos[1]))
        else:
            print("{} ({}) - {} ({}*)".format(game[0], pontos[0], game[1], pontos[1]))
            
    if pontos[1] >= 5 or pontos[0] >= 5:
        if (pontos[0]-2) >= pontos[1]:
            game[0] += 1
            pontos[0] = 0
            pontos[1] = 0
        elif (pontos[1]-2) >= pontos[0]:
            game[1] += 1
            pontos[0] = 0
            pontos[1] = 0
        else:
            continue
