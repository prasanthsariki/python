# sum of elements in a list
def list_stats(list1):
    total_sum=sum(list1)
    return total_sum

list1=[5,19,10,3,15]
total_sum=list_stats(list1)

print("sum of numbers:",total_sum)

# search element in a list

def search_element(list2,search_num):
    for i in list2:
        if i == search_num:
            return True
    return False

list2=[11,22,33,44,55,66]
search_num=int(input("enter a number"))

if search_element(list2,search_num):
    print("found")
else:
    print("not found")

# 12 largest and smallest in a list
def max_min(list3):
    largest=max(list3)
    smallest=min(list3)
    return largest, smallest

list3=[1,22,45,68,1001]
# maximum=max_min(list3)
largest, smallest =max_min(list3)

print("Smallest number is:",smallest)
print("Largest  numbers is :",largest)

# unique and duplicate

duplicates = set()
unique = set()

list4 = [1,1,1,1,2,2,2,2,3,3,3,3,4,5,6,7,8,9,9,9,9]
for i in list4:
    if i in unique:
        duplicates.add(i)
        unique.remove(i)
    elif i not in duplicates:
        unique.add(i)

print(duplicates)
print(unique)

# 4
def find_duplicates(number):
    list4 = [int(digit) for digit in str(number)] 
    duplicates = set()
    unique = set()

    for i in list4:
        if i in unique:
            duplicates.add(i)
            unique.remove(i)  
        elif i not in duplicates:
            unique.add(i) 

   
    if len(duplicates) == 1:
        print(f"Duplicate is :",duplicates)
    elif len(duplicates) > 1:
        print("Duplicates are:",duplicates)
    else:
        print("No duplicates found")

    print("Unique digits are:",unique)


find_duplicates(1214)

# 5
str1=input("enter the string")

res={}
for k in str1:
    if k in res:
        res[k] +=1
    else:
        res[k] =1

print(res)

# 6
def duplicate_digit_exists(num1):
    curr_list  = []
    while num1 > 0:
        rem  = num1 % 10
        
        if rem in curr_list:
            return True
        curr_list.append(rem)
        num1  = num1 // 10
    return False

list2  = [202,89,112,99]
res  = []
for i in list2:
    # res.append(duplicate_digit_exists(i))
    temp  = duplicate_digit_exists(i)
    res.append(temp)

print(res)

# 7

def sum_of_digits(num1):
    digits_sum = 0
    while num1 > 0:
        rem = num1 % 10
        digits_sum += rem
        num1 = num1 // 10
    return digits_sum

list5 = [202,89,112,88]
res = []

for i in list5:
    temp = sum_of_digits(i)
    res.append(temp)
print(res)

# # 8
# def digits_in_increasing_order(num1):
#     last_digit = -1
#     while num1>0:
#         rem = num1 % 10
#         if rem <= last_digit:
#             return False
#         last_digit = rem
#         num1 = num1 // 10
#     return True

# list6 = [568,89,112,88,571]
# res = []

# for i in list6:
#     temp = digits_in_increasing_order(i)
#     res.append(temp)

# print(res)

# 11 missing numbers
def missing_number(num1):

    remainder = []
    str1 = ""
    while num1 > 0:
        rem = num1 % 10
        remainder.append(rem)
        num1 = num1 // 10

    for i in range(1, max(remainder)):
        if i not in remainder:
            str1 += str(i)
    return str1 + " missing "

# Finding the frequency of elements in an array.
#     arr = [10, 30, 10, 20, 10, 20, 30, 10]  O/p: 10=> 4 30 =>2  20=> 2


arr = [10, 30, 10, 20, 10, 20, 30, 10]

freq = {}

for num in arr:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# Print output
for key, value in freq.items():
    print(f"{key} => {value}")

# 19) check if array is subset of another array or not .if the arr2 contains elements which are there in arr1 then it is a subset of an array.
# arr1=[1,3,4,5,2]
# arr2=[2,4,3,1,7.5.15]

def is_subset(arr1, arr2):
    for element in arr2:
        if element not in arr1:
            return False
    return True

arr1 = [1, 3, 4, 5, 2]
arr2 = [2, 4, 3, 1, 7, 5, 15]

if is_subset(arr1, arr2):
    print("arr2 is a subset of arr1")
else:
    print("arr2 is NOT a subset of arr1")


# Wap to check if the digits of each number in an list are in increasing order, returning true or false for each Increasing order or not
#  Input: [568,89,112,88,571]     Output: [true,true ,false,false ,false]


def is_increasing(num):
    num_str = str(num)  
    for i in range(len(num_str) - 1):
        if num_str[i] > num_str[i + 1]:  
            return False
    return True

def check_numbers(lst):
    return [is_increasing(num) for num in lst]  


numbers = [568, 89, 112, 88, 571]
result = check_numbers(numbers)
print(result)


# wap to check descending order

def is_decreasing(num):
     num_str = str(num)
     for i in range(len(num_str)- 1):
         if num_str[i] <= num_str[i + 1]:
             return False
     return True

def check_digits(lst):
    return [is_decreasing(num) for num in lst]

numbers = []
result = check_digits(numbers)
print(result)