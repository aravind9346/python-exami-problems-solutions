#sum of digits 
#defining the input variable
num = int(input("enter a positive integer number: "))
#defining result variable to store a data
result = 0
#defing loop for number is greater then 0 or not
while num > 0:
    #definig digit with refering by modiles with number
    digit = num % 10
    #storing the variable result to variable
    result = result + digit
    num = num// 10
#print the data variable    
print("sum is :", result)
#by ANUBOLU ARAVIND
