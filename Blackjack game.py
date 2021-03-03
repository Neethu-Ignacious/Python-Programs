#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random

suit=['Diamond','Spade','Heart','Club']
rank=['Two','Three','Four','Five','Six','Seven','Eight','Nine','Jack','King','Queen','Ace']
value={'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Jack':10,'King':10,'Queen':10,'Ace':11}
deck=[]
count=100
bet=int(input("Enter the bet amount:"))

def card(s,r):
    suit=s
    rank=r
    d=[suit,rank]
    return d

def shuffle():
    global deck
    global total_dealer
    global total_player
    global dealer_choice
    global player_choice
    dealer_choice=random.choice(deck)
    print("Dealers choice is:",dealer_choice[1],"of",dealer_choice[0])
    deck=remove_card(dealer_choice)
    v5=dealer_choice[1]
    total_dealer=total_dealer+value[v5]
    print("Dealers total",total_dealer)
    player_choice=random.choice(deck)
    print("Players choice is:",player_choice[1],"of",player_choice[0])
    deck=remove_card(player_choice)
    v6=player_choice[1]
    total_player=total_player+value[v6]
    print("Players total:",total_player)
    check_win()
    
def dealer_shuffle():
    global deck
    global total_dealer
    global dealer_choice
    global player_choice
    dealer_choice=random.choice(deck)
    print("Dealers choice is:",dealer_choice[1],"of",dealer_choice[0])
    deck=remove_card(dealer_choice)
    v7=dealer_choice[1]
    total_dealer=total_dealer+value[v7]
    check_win()
    
def repeat():
    con=int(input("Press 1 to continue:"))
    if con==1:
        main()
    else:
        print("Thank you for playing Blackjack")
    
def player_win():
    global count
    global total_player
    global total_dealer
    print("Players total:",total_player)
    print("Dealers total:",total_dealer)
    print("Player won the game")
    count=count+bet
    print("Total amount:",count)
    repeat()
    

def dealer_win():
    global count
    global total_player
    global total_dealer
    print("Players total:",total_player)
    print("Dealers total:",total_dealer)
    print("Dealer won the game")
    count=count-bet
    print("Total amount:",count)
    repeat()


    
def check_win():
    global total_dealer
    global total_player
    global dealer_choice
    global player_choice
    
    if total_dealer==20 and dealer_choice[0]=="Ace":
        total_dealer=21
        dealer_win()

    elif total_player==20 and player_choice[0]=="Ace":
        total_player=21
        player_win()

    elif total_player==21 and total_dealer==21:
        player_win()
    
    elif total_dealer==21 or total_player>21:
        dealer_win()

    elif total_player==21 or (total_dealer>21 and total_player<total_dealer):
        player_win()

    else:
        user_input=input("Do you want to hit or stand:")
        if user_input=="hit":
            shuffle()
        elif user_input=="stand":
            dealer_shuffle()


def remove_card(choice):
    deck.remove(choice)
    return deck


def main():
    global deck
    global total_dealer
    global total_player
    total_player=0
    total_dealer=0
    for i in suit:
        for j in rank:
            deck.append(card(i,j))
    dealer_1st_choice=random.choice(deck)
    deck=remove_card(dealer_1st_choice)
    dealer_2nd_choice=random.choice(deck)
    deck=remove_card(dealer_2nd_choice)
    player_1st_choice=random.choice(deck)
    deck=remove_card(player_1st_choice)
    player_2nd_choice=random.choice(deck)
    deck=remove_card(player_2nd_choice)
    print("Dealers 1st choice is:",dealer_1st_choice[1],"of",dealer_1st_choice[0])
    print("Dealers 2nd choice is:",dealer_2nd_choice[1],"of",dealer_2nd_choice[0])
    print("Players 1st choice is:",player_1st_choice[1],"of",player_1st_choice[0])
    print("Players 2nd choice is:",player_2nd_choice[1],"of",player_2nd_choice[0])
    v1=dealer_1st_choice[1]
    v2=dealer_2nd_choice[1]
    v3=player_1st_choice[1]
    v4=player_2nd_choice[1]
    total_dealer=value[v1]+value[v2]
    total_player=value[v3]+value[v4]
    print("Dealers total:",total_dealer)
    print("Players total:",total_player)
    check_win()

main()

        


# In[ ]:





# In[ ]:




