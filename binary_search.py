#!/usr/bin/env python
# coding: utf-8

# In[61]:


def binary_search(array,min_value,max_value,target):
    
    """This function will perform binary search"""
    
    if max_value < min_value:
        return 0
    
    else:
        guess = (max_value + min_value) // 2
        if array[guess] == target:
            return guess
        elif array[guess] < target:
            return binary_search(array,guess+1,max_value,target)
        else:
            return binary_search(array,min_value,guess-1,target)
 

#initializing the list   
my_list=[]

#inputing the number of elements
num=int(input("Enter the number of elements you need in the list:")) 

#inputing and storing the elements in the list
i=0    
while i<num: 
    print(f"Enter the {i+1} element of the list:") 
    my_list.append(int(input()))
    i+=1

#inputing the number to be searched
special_num=int(input("Enter the special number to be searched:"))

#sorting the list elements for binary search
sort_list=sorted(my_list)
  
#function call for binary search
search_result=binary_search(sort_list,0,len(sort_list)-1,special_num)
    
#printing the result
if search_result == 0:
    print("\nFalse")
else:
    print("\nTrue")


# 

# In[ ]:




