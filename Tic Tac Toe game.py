#!/usr/bin/env python
# coding: utf-8

# In[20]:


#Empty board
board=['-','-','-','-','-','-','-','-','-']

#Initializing the variables
game_ongoing=True
option=''
position=0
count=0
win=''

#Printing display board
def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")
    
#Changing player turn
def flip_player():
    global current_player
    
    if current_player=='X':
        current_player='O'
    elif current_player=='O':
        current_player='X'

#Main function        
def game():
    global current_player
    current_player=input("Choose an option:X or O")
    game_continue()

#Checking conditions for winner    
def winner():
    if board[0]==board[1]==board[2]!='-':  
        return board[0]
    elif board[3]==board[4]==board[5]!='-':
        return board[3]
    elif board[6]==board[7]==board[8]!='-':
        return board[6]
    elif board[0]==board[3]==board[6]!='-':  
        return board[0]
    elif board[1]==board[4]==board[7]!='-':
        return board[1]
    elif board[2]==board[5]==board[8]!='-':
        return board[2]
    elif board[0]==board[4]==board[8]!='-': 
        return board[0]
    elif board[2]==board[4]==board[6]!='-':
        return board[2]
    else:
        return game_continue()
              
#Game ongoing        
def game_continue():
    
    global current_player
    global position
    global count
    global game_ongoing
    global win
    
    while game_ongoing:
            print(current_player,"'s turn")
            position=int(input("Choose a position from 1-9:"))
            position=position-1
            if board[position]=='-':
                board[position]=current_player
            else:
                print("Space is already filled. Choose again:")
                flip_player()
                
            display_board()
            flip_player()
            count=count+1
            if count>=5 and count<=7:
                win=winner()
                if win==None:
                    continue
                else:
                    print(win,"won the game") 
                    game_ongoing=False
            elif count==9 and board[position]!='-':
                print("Its a tie")
                game_ongoing=False
            else:
                game_ongoing=True
                            
    
display_board()
game()

#To continue playing the game
z=int(input("Press 1 to continue"))
while z==1:
    board=['-','-','-','-','-','-','-','-','-']
    game_ongoing=True
    option=''
    position=0
    count=0
    win=''
    display_board()
    game()
    z=int(input("Press 1 to continue"))

    



# In[ ]:





# In[ ]:




