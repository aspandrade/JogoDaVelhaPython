import os
from colorama import Fore

jogarNovamente = 's'
jogadas = 0
maxJogadas = 9
quemJoga = 1
vit = 'n'

# Matriz pra confecção do tabuleiro:
tabuleiro = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "]
]

def tela():
    global tabuleiro
    global jogadas
    os.system("cls") # Função para limpar o terminal sempre que uma jogada for feita
    print("    0   1   2")
    print("0  " + tabuleiro[0][0] + " | " + tabuleiro[0][1] + " | " + tabuleiro[0][2])
    print("   -----------")
    print("1  " + tabuleiro[1][0] + " | " + tabuleiro[1][1] + " | " + tabuleiro[1][2])
    print("   -----------")
    print("2  " + tabuleiro[2][0] + " | " + tabuleiro[2][1] + " | " + tabuleiro[2][2])
    print("")
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)

def jogador1():
    global jogadas
    global quemJoga
    if quemJoga == 1 and jogadas < maxJogadas:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
        except:
            print("Linha e ou coluna inválida.")
            os.system("pause")
            return

            # Marcar o espaço em branco com X

        if tabuleiro[l][c] == " ":
            tabuleiro[l][c] = Fore.RED + 'X' + Fore.RESET
            quemJoga = 2 # Passando a vez pro jogador 2
            jogadas += 1 # Contador de Jogadas
        else:
            print("Local já preenchido ou inválido, vamos tentar novamente...")
            jogador1()

def jogador2():
    global jogadas
    global quemJoga
    if quemJoga == 2 and jogadas < maxJogadas:
        try:
            l = int(input("Linha: "))
            c = int(input("Coluna: "))
        except:
            print("Linha e ou coluna inválida.")
            os.system("pause")
            return

            # Marcar o espaço em branco com O

        if tabuleiro[l][c] == " ":
            tabuleiro[l][c] = Fore.CYAN + 'O' + Fore.RESET
            quemJoga = 1 # Passando a vez pro Jogador 1
            jogadas += 1 # Contador de Jogadas
        else:
            print("Local já preenchido ou inválido, vamos tentar novamente...")
            jogador2()

def verificarVitoria():
    global vit

    # estrutura de repetição For para verificar o vencedor (Se os três espaços são preenchidos por X ou O)

    for c in range(0, 3):
        if tabuleiro[c][0] == tabuleiro[c][1] == tabuleiro[c][2] != " ":
            vit = tabuleiro[c][0]
            return True
        if tabuleiro[0][c] == tabuleiro[1][c] == tabuleiro[2][c] != " ":
            vit = tabuleiro[0][c]
            return True
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != " ":
        vit = tabuleiro[0][0]
        return True
    if tabuleiro[2][0] == tabuleiro[1][1] == tabuleiro[0][2] != " ":
        vit = tabuleiro[2][0]
        return True
    if jogadas == maxJogadas: # condição para empate
        vit = 'E'
        return True
    return False

def redefinir():
    global jogadas
    global quemJoga
    global vit
    global tabuleiro
    jogadas = 0
    quemJoga = 1 
    vit = 'n'
    tabuleiro = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
    ]

while jogarNovamente == 's':
    while True:
        tela()
        jogador1()
        if verificarVitoria():
            break
        tela()
        jogador2()
        if verificarVitoria():
            break

    tela()  # exibir a tela atual antes de mostrar o resultado

    if vit == 'E':
        print(Fore.RED + "Deu velha!" + Fore.RESET)
    else:
        print(Fore.YELLOW + "Vitória do Jogador" + Fore.RESET + f" {vit}" + Fore.YELLOW + "!" + Fore.RESET)

    jogarNovamente = input(Fore.YELLOW + "Deseja jogar novamente? (s/n): " + Fore.RESET).lower()
    if jogarNovamente == 's':
        redefinir()