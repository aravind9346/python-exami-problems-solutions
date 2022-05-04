#fibonacci series

#define the finction
def fibonacci_series(n):
    # defining inital values 0 and 1
    a = 0
    b = 1
# defining conditional statement is there n == 1
    if n == 1:
# if n == 1 then print valu a         
        print(a)
# then if is not satisified then valu return to the else valu its print a , b
    
    else:
        print(a)
        print(b)
# then continue the sequence of valu which defining loop valu from 2 to n th term
        for i in range(2,n):
            # comparing the valu with sequence with change intial value
            c = a + b
            a = b
            b = c
            print(c)

#calling the function            
fibonacci_series(5)

# BY ANUBOLU ARAVIND

