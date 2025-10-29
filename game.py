import random
import time

import io1

def Creat_plger()->dict:
    playr={
    'Steps':None,
    'lis':[]}
    return playr

def creating_a_card_deck(size:int)->list[list]:
    l=[]
    deck=[]
    for i in range((size**2)//2):
        l.append(i)
        l.append(i)
    random.shuffle(l)
    c=0
    for i in range(size):
        deck.append([])
        for j in range(size):
            deck[i].append(l[c])
            c+=1

    return deck



def parallel_matrix(size:int)->list[list]:
    matrix=[]
    for i in range(size):
        matrix.append([])
        for j in range(size):
            matrix[i].append("*")
    return matrix


def Checking_for_proper_input(deck,playr):
    card=io1.input_cards()
    if len(deck)-1>=card[0] and len(deck[card[0]])-1>=card[1]:
        if card[0]>=0 and card[1]>=0:
            if [card[0],card[1]]not in playr['lis']:
                return card
    print('The card was not found')
    card=Checking_for_proper_input(deck,playr)
    return card




def step_move(deck,matr,playr):

    c1=Checking_for_proper_input(deck,playr)
    c2=Checking_for_proper_input(deck,playr)
    if c1==c2:
        print('You cannot choose a ticket twice.')
        c2=Checking_for_proper_input(deck,playr)
    matr[c1[0]][c1[1]],matr[c2[0]][c2[1]]=deck[c1[0]][c1[1]],deck[c2[0]][c2[1]]
    io1.print_metrix(matr)
    if deck[c1[0]][c1[1]] == deck[c2[0]][c2[1]]:
        print(deck[c1[0]][c1[1]] ,deck[c2[0]][c2[1]])
        playr['lis'].append(c1)
        playr['lis'].append(c2)
        return matr
    else:
        matr[c1[0]][c1[1]], matr[c2[0]][c2[1]] ="*","*"
        time.sleep(2)
        io1.print_metrix(matr)
        return matr




def is_won(playr,size):
   if len(playr['lis'])==size**2:
       print('winner')
       return False
   return True




def Steps(playr):
    steps=input('Please enter a step limit.')
    try:
        steps=int(steps)
    except:
        print('not a number')
    playr['Steps']=0
    if type(playr['Steps'])==int:
        playr['Steps']+=1
    if steps==playr['Steps']:
        return False
    return True


