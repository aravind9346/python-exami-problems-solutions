

# sort array using for loop 

# defing function 
def sort(nums):
    
    #definding an for loop for range of min of 5
    for i in range(5):
        #saving the midterm vale in by defing minpos
        minpos = i
        #then defing value with sequence by range of i to 6
        for j in range(i,9):
            #then comparing value by defing there source by comparing nums and minpos
            if nums[j] < nums[minpos]:
                minpos = j
        #also defing temp variable to store a data
        temp = nums[i]
        nums[i]= nums[minpos]
        nums[minpos] = temp
nums = [5,3,8,6,2]
#calling a function
sort(nums) 
print(nums)             

#by ANUBOLU ARAVIND