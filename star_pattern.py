# #  **
# #  **

# n=2
# for i in range(1, n+1):
#     print("*"+"*")

# # * *
# # * *

# n=2
# for i in range(n):
#     for j in range(n):
#         print("*", end=' ')
#     print(end="\n")

# # *
# **


# n=5
# for i in range(1,n+1):
#     for j in range(1, i+1):
#         print("*", end=' ')
#     print(end='\n')

        

# n=5
# for i in range(1,n+1):
#     for j in range(1,(n+2)-i):
#         print("*", end=' ')
#     print(end='\n')

n=5
 

for i in range(1,n+1): 
    for k in range(1,n+1-i):
       print(end=' ') 
    for j in range(1,1+i):
      print("*", end=' ')
    print(end='\n')

# for i in range(1,n+1): 
#     for k in range(1,i):
#        print(end=' ') 
#     for j in range(1,n+2-i):
#       print("*", end=' ')
#     print(end='\n')  