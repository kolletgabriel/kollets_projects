brd = [str(i) for i in range(9)] 

def print_board(): #PRINTA O TABULEIRO; CHECA O ARRANJO DA LISTA 'brd', ITERA SOBRE ELA E A PRINTA FORMATADA TAL QUAL UM TABULEIRO DE VERDADE
    s = '' #CONTADOR
    for i in brd:
        i = str(i)
        s += i #CONTADOR
    print('') #ESPAÇAMENTO
    print(s[0],' ',s[1],' ',s[2],'\n')
    print(s[3],' ',s[4],' ',s[5],'\n')
    print(s[6],' ',s[7],' ',s[8],'\n')
    print(50*'-') #LINHAS PRA SEPARAR

def player_X():
    while True: 
        try: 
            p1 = str(input("Player 'X': ")) 
            while True:
                if brd[int(p1)] == 'X' or brd[int(p1)] == 'O':
                    print(brd)
                    print("erro")
                    p1 = str(input("Player 'X': "))
                else:
                    brd[int(p1)] = 'X'
                    break
        except:
            print("You must reference a valid index!\n")
        else: 
            print_board()
            player_O() 
            break 

def player_O(): 
    while True:
        try:
            p2 = str(input("Player 'O': "))
            while True:
                if brd[int(p2)] == 'X' or brd[int(p2)] == 'O':
                    print(brd)
                    print('erro')
                    p2 = str(input("Player 'O': "))
                else:
                    brd[int(p2)] = 'O'
                    break
        except:
            print("You must reference a valid index!\n")
        else:
            print_board()
            player_X()
            break

#COMEÇANDO O JOGO:
print_board()
player_X()