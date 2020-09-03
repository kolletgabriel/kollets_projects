brd = [str(i) for i in range(9)]

def print_board():
    s = ''
    for i in brd:
        i = str(i)
        s += i
    print('')
    print(s[0],' ',s[1],' ',s[2],'\n')
    print(s[3],' ',s[4],' ',s[5],'\n')
    print(s[6],' ',s[7],' ',s[8],'\n')
    print(50*'-')

def player_X():
    while True:
        try:
            p1 = str(input("Player 'X': "))
            brd[int(p1)] = 'X'
        except:
            print("You must reference a valid index!\n")
        else:
            print_board()
            win_conditions('X')
            drawn_conditions()
            player_O()
            break

def player_O():
    while True:
        try:
            p2 = str(input("Player 'O': "))
            brd[int(p2)] = 'O'
        except:
            print("You must reference a valid index!\n")
        else:
            print_board()
            win_conditions('O')
            drawn_conditions()
            player_X()
            break

def win_conditions(char):
    win = [char, char, char] #CONSTANTE
    h1, h2, h3 = brd[0:3], brd[3:6], brd[6:9] #LINHAS HORIZONTAIS
    v1, v2, v3 = [brd[0],brd[3],brd[6]], [brd[1],brd[4],brd[7]], [brd[2],brd[5],brd[8]] #LINHAS VERTICAIS
    d1, d2 = [brd[0],brd[4],brd[8]], [brd[2],brd[4],brd[6]] #LINHAS OBLÍQUAS

    if h1 == win or h2 == win or h3 == win or v1 == win or v2 == win or v3 == win or d1 == win or d2 == win: #TESTE DE IGUALDADE
        print("Player '{}' wins!".format(char))
        play_again()
    else:
        pass


def drawn_conditions():
    lst = [] #LISTA VAZIA 
    for i in brd:
        if i == 'X' or i == 'O': #IDENTIFICA OS CARACTERES INPUTADOS
            lst.append(i)
    else:
        if lst == brd: #COMPARAÇÃO ENTRE AS LISTAS
            print("Drawn.")
            play_again()
        else:
            pass

def play_again():
    while True:
        check = input("Do you want to play again? (y/n): ")
        if check == 'y':
            break
        elif check == 'n':
            print("Thank you for playing! :)")
            exit()
        else:
            continue
    global brd
    brd = [str(i) for i in range(9)]
    print_board()
    player_X()

#COMEÇANDO O JOGO:
print_board()
player_X()