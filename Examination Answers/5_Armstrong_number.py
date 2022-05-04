#Any positive integer of N digits is armstrong number


#define a value by number
num = int(input("Enter your number: "))
#initial variable to store data
sum = 0
#defining temp to store data of a num
temp = num
# convrting integer to string and check length of a string and store in n
n = len(str(num))
#then defining the while loop for temp valu greater than 0
while temp > 0:
    digit = temp % 10
    sum += digit ** n
    temp //= 10
#defining condition valu which give valu is equal to sum of there value
if sum == num:
    print(num, "is a armstrong number")
else:
    print(num,"is not a armstrong number")        
#by ANUBOLU ARAVIND