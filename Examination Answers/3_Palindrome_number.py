# palindrome number
# a number or string which is same which its reverse also then its called as palindrom 

# define an input finction to define value
s = input("Enter your value: ")
#by using slicing method for reverse the value and stored in reverse
reverse = s[::-1]

# by using if condition comparing the value of s and reverse 
if s == reverse:
    # while comparing them if  its equal then its is a palindrome
    print('its is a palindrome')
# then else its is not a palindrome
else:
    print("it is not a palindrome")    

# by ANUBOLU ARAVIND    