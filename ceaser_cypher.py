#!/usr/bin/env python
# coding: utf-8

# In[9]:


def  ceaser_cypher(my_string,shift_num):
    
    """This function will find the ceaser cypher encrypted value"""
    
    #initializing the string
    cypher = ''
    
    #traversing through the input string
    for string in my_string:
        
        if string == '':
            cypher = cypher + string
            
        #encrypting uppercase characters
        elif string.isupper():
            cypher = cypher + chr((ord(string) + shift_num - 65) % 26 + 65)
            
        #encrypting lowercase characters
        else:
            cypher = cypher + chr((ord(string) + shift_num - 97) % 26 + 97)
    return cypher

#getting input string and shift number
input_string = input("Enter the string:")
input_shift_num = int(input("Enter the shift number:"))

#printing the original string
print("\nOriginal string is:",input_string)

#function call to find the encrypted string
print("\nEncrypted string is:",ceaser_cypher(input_string,input_shift_num))


# In[ ]:




