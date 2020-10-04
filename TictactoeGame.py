import random

def toss():
    '''This funtion is use for toss'''
    tosschoice =input(f"{pler1} & {pler2} choose Head and Tale respectively: ").split(" ")
    while not('head' in tosschoice and 'tale' in tosschoice):
        tosschoice = input("Re-enter Head and Tale by giving single space: ").lower().split(" ")
    coin_f = random.choice(tosschoice)
    if coin_f == tosschoice[0]:
        print(f"\nit's {coin_f},\n{pler1}, You Won the toss.")
        return pler1, pler2
    else:
        print(f"\nit's {coin_f},\n{pler2}, You Won the toss.")
        return pler2, pler1

def matchReplay():
    return input("Wanna play again(Y/N)?").upper().startswith('Y')
        
def plyMarkChoice(tosswinner):   
    markers=''
    while not(markers=='X' or markers=='O'):
        ply1 = input("\nChoose 'X' or 'O': ").upper()
        if not(ply1 == 'X' or ply1 == 'O'):
            plyMarkChoice(tosswinner)
        else:
            if ply1 == 'X':
                print(f"\n{tosswinner} have 'X'.\nSo, {tosslooser} will have 'O'.")
                return ('X','O')
            else :
                print(f"\n{tosswinner} have 'O',\nSo, {tosslooser} will have 'X'.")
                return ('O','X')

def creat_Tble(mark_position,markers):
    num_ls[mark_position] = markers
    print(num_ls[7]+' | '+num_ls[8]+' | '+num_ls[9])
    print('--|---|--')
    print(num_ls[4]+' | '+num_ls[5]+' | '+num_ls[6])
    print('--|---|--')
    print(num_ls[1]+' | '+num_ls[2]+' | '+num_ls[3])

def player1_choice():
    mark_p = int (input(f"\n{tosswinner},\nyou wanna mark on(1-9):\n "))
    if mark_p not in range(1,10):
        player1_choice()
    if num_ls[mark_p] != " ":
        print("This place is already taken.\n")
        player1_choice()
    return mark_p

def player2_choice():
    mark_p = int (input(f"\n{tosslooser},\nyou wanna mark on:\n "))
    if mark_p not in range(1,10):
        player2_choice()
    if num_ls[mark_p] != " ":
        print("This place is already taken.\n")
        player2_choice()
    return mark_p

def check_Space():
    if " " in num_ls:
        return True
    else:
        print("Just kidding!\nMatch Draw!")
        
def winnercheck():
    if((num_ls[1]== 'X'and num_ls[2]== 'X' and num_ls[3]== 'X') or 
       (num_ls[4]== 'X'and num_ls[5]== 'X' and num_ls[6]== 'X') or
       (num_ls[7]== 'X'and num_ls[8]== 'X' and num_ls[9]== 'X') or
       (num_ls[1]== 'X'and num_ls[4]== 'X' and num_ls[7]== 'X') or
       (num_ls[2]== 'X'and num_ls[5]== 'X' and num_ls[8]== 'X') or
       (num_ls[3]== 'X'and num_ls[6]== 'X' and num_ls[9]== 'X') or
       (num_ls[1]== 'X'and num_ls[5]== 'X' and num_ls[9]== 'X') or
       (num_ls[3]== 'X'and num_ls[5]== 'X' and num_ls[7]== 'X') or
       (num_ls[1]== 'O'and num_ls[2]== 'O' and num_ls[3]== 'O') or 
       (num_ls[4]== 'O'and num_ls[5]== 'O' and num_ls[6]== 'O') or
       (num_ls[7]== 'O'and num_ls[8]== 'O' and num_ls[9]== 'O') or
       (num_ls[1]== 'O'and num_ls[4]== 'O' and num_ls[7]== 'O') or
       (num_ls[2]== 'O'and num_ls[5]== 'O' and num_ls[8]== 'O') or
       (num_ls[3]== 'O'and num_ls[6]== 'O' and num_ls[9]== 'O') or
       (num_ls[1]== 'O'and num_ls[5]== 'O' and num_ls[9]== 'O') or
       (num_ls[3]== 'O'and num_ls[5]== 'O' and num_ls[7]== 'O')):
       return True

while True:   
    num_ls = ['1'," "," "," "," "," "," "," "," "," "]
    print('Welcome To Tic Tac Toe Game!\n')
    pler1 = input("1st player name: ")
    pler2 = input("2st player name: ")
    print("\nToss First\n")
    

    tosswinner, tosslooser =toss()
    ply1,ply2 = plyMarkChoice(tosswinner)
    
    while check_Space() == True:
        
        mark_positionforply1 = player1_choice()
        creat_Tble(mark_positionforply1, ply1)
        if winnercheck() == True:
            print(" You Won!")
            break
            
        mark_positionforply2 = player2_choice()
        creat_Tble(mark_positionforply2, ply2)
        if winnercheck() == True:
            print(" You Won!")
            break
    
    if not matchReplay():
        break