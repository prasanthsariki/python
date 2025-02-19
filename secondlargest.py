# numbers = [1,1,2,3,4,5,6,6,8,9,12,13,13]

# second_largest = 0

# third_largest = 0

# second_minimum = 0
 
# third_minimum = 0

# uni_num = list(set(numbers))

# # uni_num.sort(reverse= True)

# uni_num.sort()

# second_minimum += uni_num[1]
# third_minimum += uni_num[2]

# second_largest += uni_num[-2]
# third_largest += uni_num[-3]

# print("second largest is:",second_largest)
# print("third largest is:",third_largest)

# print("second minimum is:",second_minimum)
# print("third minimum is:",third_minimum)

def is_decreasing(num):
     num_str = str(num)
     for i in range(len(num_str)- 1):
         if num_str[i] <= num_str[i + 1]:
             return False
     return True

def check_digits(lst):
    return [is_decreasing(num) for num in lst]

numbers = [538,111,200,652]
result = check_digits(numbers)
print(result)
