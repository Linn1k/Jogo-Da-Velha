import os

Lista1 = ["-", "-", "-"]
Lista2 = ["-", "-", "-"]
Lista3 = ["-", "-", "-"]
Player = 0


def Mensagens_Ocupado():
    print("POSIÇÃO OCUPADA, ESCOLHA OUTRA!!!\n")


def Limpa_Tela():
    if os.name == "nt":  # Windows
        os.system("cls")
    else:  # Linux e macOS
        os.system("clear")


def Jogo_Tela():
    print("    JOGO DA VELHA")
    print("   Feito por Línnek\n")
    print("    C1 | C2 | C3 ")
    print("   -------------")
    print(f"L1 | {Lista1[0]} | {Lista1[1]} | {Lista1[2]} |")
    print("   -------------")
    print(f"L2 | {Lista2[0]} | {Lista2[1]} | {Lista2[2]} |")
    print("   -------------")
    print(f"L3 | {Lista3[0]} | {Lista3[1]} | {Lista3[2]} |")
    print("   -------------")
    print("\n")


def Ocupado(Linha, Coluna):
    if Linha == 1:
        if Lista1[Coluna - 1] == "-":
            return False
        else:
            return True
    if Linha == 2:
        if Lista2[Coluna - 1] == "-":
            return False
        else:
            return True
    if Linha == 3:
        if Lista3[Coluna - 1] == "-":
            return False
        else:
            return True


def Jogando(Linha, Coluna, Player):
    if not Ocupado(Linha, Coluna):
        if Linha == 1:
            if Player == 0:
                Lista1[Coluna - 1] = "X"
            else:
                Lista1[Coluna - 1] = "O"
        if Linha == 2:
            if Player == 0:
                Lista2[Coluna - 1] = "X"
            else:
                Lista2[Coluna - 1] = "O"
        if Linha == 3:
            if Player == 0:
                Lista3[Coluna - 1] = "X"
            else:
                Lista3[Coluna - 1] = "O"
    else:
        return True


def Vencedor():

    if Lista1[0] == Lista1[1] == Lista1[2] and Lista1[0] != "-":
        return True
    if Lista2[0] == Lista2[1] == Lista2[2] and Lista2[0] != "-":
        return True
    if Lista3[0] == Lista3[1] == Lista3[2] and Lista3[0] != "-":
        return True
    for i in range(3):
        if Lista1[i] == Lista2[i] == Lista3[i] and Lista1[i] != "-":
            return True
    if Lista1[0] == Lista2[1] == Lista3[2] and Lista1[0] != "-":
        return True
    if Lista1[2] == Lista2[1] == Lista3[0] and Lista1[2] != "-":
        return True


def Empate():
    Cont1 = 0
    Cont2 = 0
    Cont3 = 0
    for i in range(0, 3):
        if Lista1[i] != "-":
            Cont1 += 1
        if Lista2[i] != "-":
            Cont2 += 1
        if Lista3[i] != "-":
            Cont3 += 1
    if Cont1 + Cont2 + Cont3 == 9:
        return True
    else:
        return False


def Valor_Certo(Linha, Jogador):
    while Linha not in [1, 2, 3]:
        Limpa_Tela()
        Jogo_Tela()
        if Jogador == 0:
            print("|xxxxx JOGADOR 1 xxxxx|\n")
        else:
            print("|ooooo JOGADOR 2 ooooo|\n")
        print("OPÇÕES VALIDAS 1 | 2 | 3\n")
        Linha = int(input("Digite o certo: "))
    return Linha


Limpa_Tela()

while True:
    Jogo_Tela()
    if Empate() is False:
        if Player == 0:
            print("|xxxxx JOGADOR 1 xxxxx|\n")
        if Player == 1:
            print("|ooooo JOGADOR 2 ooooo|\n")
        Linha = int(input("DIGITE A LINHA (L): "))
        if Linha not in [1, 2, 3]:
            Linha = Valor_Certo(Linha, Player)

        Coluna = int(input("DIGITE A COLUNA (C): "))
        if Coluna not in [1, 2, 3]:
            Coluna = Valor_Certo(Coluna, Player)
        Limpa_Tela()
        if Jogando(Linha, Coluna, Player) is True:
            if Player == 0:
                Player = 0
                Mensagens_Ocupado()
            else:
                Player = 1
                Mensagens_Ocupado()
        else:
            if Player == 0:
                Player = 1
            else:
                Player = 0

        if Vencedor() is True:
            if Player == 1:
                print("Parabéns! Jogador 1 venceu!\n")
            else:
                print("Parabéns! Jogador 2 venceu!\n")
            break
    else:
        print("EMPATOU")
        break
