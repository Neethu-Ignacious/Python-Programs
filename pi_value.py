#!/usr/bin/env python
# coding: utf-8

# In[9]:


import math

def estimate_pi():
    
    """This function will return the pi value"""
    
    #initializing the variables
    result = 0
    k = 0
    condition = True
    
    #calculating the constant value
    constant_value = 2 * math.sqrt(2) / 9801
    
    #finding pi value
    while condition == True:
        
        numerator = math.factorial(4*k) * (1103 + 26390 * k)
        denominator = math.factorial(k)**4 * 396**(4*k)
        iteration_value = constant_value * (numerator/denominator)
        result += iteration_value
        
        #incrementing k value by 1
        k += 1
        
        #checking for while condition
        if iteration_value < 1e-15:
            condition == False
            break
    return 1/result

#calling the function
pi_value=estimate_pi()

#printing the pi value
print(pi_value)


# In[ ]:





# In[ ]:





# In[ ]:




