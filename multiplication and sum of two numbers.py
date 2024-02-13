def ml(num1, num2):
   
    prod = num1 * num2
    if prod >= 1000 :
        return num1 + num2
        
    else :
        return prod
    
#f1
res= ml(20,30)
print ("The res = ", res)

#f2
res = ml(40,30)
print ("The res = ", res)
