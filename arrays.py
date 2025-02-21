list1 = [[1,2,3],[4,5,6],[7,8,9]]

# diagonal print in matrix
def print_matrix(list1):
    for i in range (len(list1)):
        for j in range(len(list1[i])):
              if i ==j or i + j == len(list1) - 1:
               print(list1[i][j],end=" ")
              else:
                print(" ",end=" ")
        print()
        

print_matrix(list1)


# print of outer range
def print_matrix(list1):
    for i in range (len(list1)):
        for j in range(len(list1[i])):
            if(i == 0 or i == len(list1) - 1) or (j == 0 or j == (len(list1[i]) - 1)):
               print(list1[i][j],end=" ")
            else:
                print("",end="")
        
        

(print_matrix(list1))


# print of daigonals
def print_matrix(list1):
    for i in range (len(list1)):
        for j in range(len(list1[i])):
              if i ==j or i + j == len(list1) - 1:
                print(list1[i][j],end=" ") 
                if i ==j and i + j == len(list1) - 1:
                 print(list1[i][j],end=" ")
      
             
print_matrix(list1)