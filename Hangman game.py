#!/usr/bin/env python
# coding: utf-8

# In[1]:


#assigning word
word="sesquipedalianism"
#converting the string to list
word_list=list(word)
#initializing the variable for comparison
word_list1=list(word)
#find the length of the word
new='-'*len(word)
#converting the new string to list
new_list=list(new)
print(new)
print("\n")
print("Its a",len(new),"letter word.")
print("You will have 15 chances to guess the word. Start now")
print("\n")
j=0
z=0
count=15
#function to check for win or lose
def win():
    if new_list==word_list1:
        print("Congrats. You guessed the word correctly.\n")
    else:
        print("No more chances.Sorry you lose the game")   
#loop continues until count reaches 0    
while count>0:
    #guess the alphabet
    guess=input("guess:")
    #if guessed alphabet is not present in word
    if guess not in word_list:
        print("Wrong choice.Try again")
    #if guessed alphabet present in word
    else:
        #loop continues until the guessed alphabet is in word
        while guess in word_list:
            #find the index of the alphabet
            while guess!=word_list[j]:
                j=j+1
            #placing the alphabet in newlist
            new_list[j]=guess
            #replacing the alphabet to null value
            word_list[j]='-'
            #variable to find the number the iterations
            z=z+1
        #converting list to string
        for s in new_list:
            print(s,end=" ")
        print("\n")
        j=0
    
    count=count-1
    #win function will be called if count value reaches 0 or length of the word is reached
    if count==0 or z==len(word):
        win()
        break


# In[ ]:





# In[ ]:




