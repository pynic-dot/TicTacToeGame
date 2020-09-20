import random
import checkall

def toss(toss_choice):
    '''This funtion is use for toss'''

    while not(toss_choice == 'head' or toss_choice == 'tale'):
        toss_choice = input("Please Re-choose Head or Tale: ").lower()
    coin_f = random.randint(0,1)
    print("It's Head, you will start first") if coin_f == 1 else print("It's Tale, start first")

def plyMarkChoice():   
    markers=''
    while not(markers=='X' or markers=='O'):
        ply1 = input("As you won the Toss so Please choose 'X' or 'O': ").upper()
        if not(ply1 == 'X' or ply1 == 'O'):
            plyMarkChoice()
        else:
            if ply1 == 'X':
                return ('X','O')
            else :
                return ('O','X')



def creat_Tble(mark_position,markers):
    num_ls[mark_position]= markers
    print(num_ls[1]+' | '+num_ls[2]+' | '+num_ls[3])
    print('--|---|--')
    print(num_ls[4]+' | '+num_ls[5]+' | '+num_ls[6])
    print('--|---|--')
    print(num_ls[7]+' | '+num_ls[8]+' | '+num_ls[9])


def player1_choice():
    mark_p = int (input('You are Player1, where do you wanna to mark on 1-9: '))
    if mark_p not in range(1,10):
        player1_choice()
    return mark_p

def player2_choice():
    mark_p = int (input('You are Player2, where do you wanna to mark on 1-9: '))
    if mark_p not in range(1,10):
        player2_choice()
    return mark_p

def check_Space():
    for i in num_ls:
        if i==" ":
            return True

        elif i == '1':
            continue
    else:
        return False


def winnercheck():
    if(checkall.allcheck(num_ls[1:4],'X') == True or checkall.allcheck(num_ls[4:7],'X') == True or checkall.allcheck(num_ls[7:10],'X') == True or
    checkall.allcheck(num_ls[1:8:3],'X') == True or checkall.allcheck(num_ls[2:9:3],'X') == True or checkall.allcheck(num_ls[3:10:3],'X') == True or
    checkall.allcheck(num_ls[1:6:4],'X') == True or checkall.allcheck(num_ls[3:8:2],'X') == True or
    checkall.allcheck(num_ls[1:4],'O') == True or checkall.allcheck(num_ls[4:7],'O') == True or checkall.allcheck(num_ls[7:10],'O') == True or 
    checkall.allcheck(num_ls[1:8:3],'O') == True or checkall.allcheck(num_ls[2:9:3],'O') == True or checkall.allcheck(num_ls[3:10:3],'O') == True or 
    checkall.allcheck(num_ls[1:6:4],'O') == True or checkall.allcheck(num_ls[3:8:2],'O') == True ):
        return True
 

print('Lets Play the Tic Tac toe Game\n')
print("First lets have Toss\n")
toss_choice = input("Please enter Head or Tale: ").lower()
toss(toss_choice)
ply1,ply2 = plyMarkChoice()
num_ls = ['1'," "," "," "," "," "," "," "," "," "]
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


    
if check_Space == False:
    print('game Draw')

