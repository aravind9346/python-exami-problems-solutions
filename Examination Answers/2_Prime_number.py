#PRIME NUMBER
#Number which divisibal by 1 or its self is called prime number

# define value

num = 11

#define for loop for 
for i in range(2, num):
    # i is a counter variable
    if num % i == 0:
        print("ItS Not a Prime number")
        #break is use to not to continune the sequence
        break
else:
    print("Its is prime number ")         

# BY Anubolu Aravind