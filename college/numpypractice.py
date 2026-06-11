import random 
def make_random_ints(num, lower_bound,upper_bound):    
    # rng=random.Random()    
    result=[]    
    for i in range(num):        
        while True:            
            element=random.randrange(lower_bound, upper_bound)             
            if element not in result:                
                break        
        result.append(element)    
    return result 
rd_list=make_random_ints(5,1,13) 
print(rd_list)