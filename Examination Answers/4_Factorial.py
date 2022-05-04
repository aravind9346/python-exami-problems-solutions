


#factorial of a number which 5! = 5*4*3*2*1


#defining the function of facioral
def factorial(n):
    #definting f as varialble 
    f = 1
    #defining the for loop for a range of 1 , n+1
    for i in range(1,n+1):
        #check there value one-by-one of there sequence
        f = f * i
    #return there value with f    
    return f
#defining the valu of x    
x = 4
#storing the date of factioral of x in result
result = factorial(x)
#then printing the results
print(result)

#by ANUBOLU ARAVIND