# # # lst=[1,2,3,4,5]
# # # lst1=[10,20,30,40,50]
# # # multiply=list(map(lambda x, y:x*y,lst,lst1))
# # # print(multiply)


# # # lst=[1,2,4,6,6,2,1,7,2,3]

# # # def duplicates_remove(lst):
# # #     uniq_lst=[]
# # #     for i in lst:
# # #         if i not in uniq_lst:
# # #             uniq_lst.append(i)

# # #     print(uniq_lst)
    

# # # duplicates_remove(lst)


# # #=============================================Lambda=================================

# # # s=lambda a,b:a+b
# # # print(s(2,8))


# # # big=lambda a,b,c:a if a>b and a>c else b if b>c else c
# # # print(big(19,8,76))

# # # #+++++++++++++++++++filter()+++++++++++++++++++++
# # # lst=[1,2,3,4,5,6,7,8,9]
# # # result=list(filter(lambda a: a%2==0, lst))
# # # print(result)

# # # lst=["str",12,445,True,68,'a',None]
# # # result=list(filter(lambda x: type(x) is int, lst))
# # # print(result)
# # # #++++++++++++++++++++map()+++++++++++++++++++++++
# # # lst=[2,4,6,8,10,12]
# # # result=list(map(lambda x: 10+x, lst))
# # # print(result)

# # # lst=[1,2,3,4,56,7,8,9]
# # # result=list(map(lambda x:8*x,lst))
# # # print(result)
# # # #+++++++++++++++++++++++reduce()++++++++++++++++++++++
# # from functools import reduce
# # # lst=[1,2,3,4,5,6,6,7]
# # # result=reduce(lambda x,y:x+y, lst)
# # # print(result)


# # lst=[232,4563,365,35,612,12457,4898,4,345,13,4513,463,6,6,62,34,134]
#  # print(reduce(lambda x,y:x if x>y else y, lst))

# # print(reduce(lambda x,y:x if x>y else y, lst))


# # #==================sorting list without sort() function=================


# # # n=len(lst)
# # # for i in range(n):
# # #     for j in range(i+1,n):
# # #        if  lst[i] > lst[j]:         #increasing order
# # #            lst[i],lst[j]=lst[j],lst[i]
# # # print(lst)

# # # for i in range(n):
# # #     for j in range(i+1, n):
# # #         if lst[i]  < lst[j]:       # decreasing Order
# # #             lst[i],lst[j]=lst[j],lst[i]

# # # print(lst)

# # #==================sorting list with sort() and sorted()  function=================

# # sort() : Sort() method sorts list in place meaning it modifies the original list
# #       Takes 2 arguments 
# #            key: A function that serves as a key for the sort comparison.
# #            reverse: A boolean value. If True, the list elements are sorted as if each comparison were reversed


# lst=[3,5,9,9,2,5,2,1,6]
# lst.sort()
# print(lst)       #[1, 2, 2, 3, 5, 5, 6, 9, 9]


# lst_str=['apple','bye','banana','graphes','fruit']
# lst_str.sort(key=len)
# print(lst_str)     #['bye', 'apple', 'fruit', 'banana', 'graphes']



# #sorted():The sorted() function returns a new sorted list and leaves the original list unchanged.
# #       key: A function that serves as a key for the sort comparison.
# #        reverse: A boolean value. If True, the list elements are sorted as if each comparison were reversed.


# lst=[2,4,6,8,7,6,5,4,3]
# sorted_lst=sorted(lst)  
# print(sorted_lst)       # [2, 3, 4, 4, 5, 6, 6, 7, 8]    
# print(lst)              # [2, 4, 6, 8, 7, 6, 5, 4, 3]


# numbers = [4, 2, 9, 1, 5, 6]
# sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)  # Output: [9, 6, 5, 4, 2, 1]


# # #=================Sort a dictonary===================

# # # dict={10:"Apple",11:"banana",9:"guva",5:"Jamun",3:"Graphes"}
# # # dict1={}
# # # d=sorted(dict.keys())
# # # print(d)    #[3,5,9,10,11]
# # # for i in d:
# # #     dict1[i]=dict[i]
# # # print(dict1)




# # #=====================Reverse string without inbuilt functions=================

# # # s='rumina'
# # # first=0
# # # last=len(str)-1

# # # str_lst=list(s)
# # # while first<last:
# # #     str_lst[first],str_lst[last]=str_lst[last],str_lst[first]
# # #     first +=1
# # #     last -=1

# # # str=(''.join(str_lst))
# # # print(str)


# # # str='rumina'
# # # print(str[::-1])



# # #=====================Check Palindrome or not========================

# # # def palindrome(str):    #using While Loop
# # #     first=0
# # #     last=len(str)-1
# # #     while(first<last):
# # #         if str[first]==str[last]:
# # #             first +=1
# # #             last -=1
# # #         else:
# # #             return "It's not a Palindrome...."
# # #         return "It's a Palindrome...."
    
# # # print(palindrome("madam"))


# # # def palindrome(str):
# # #     n=len(str)
# # #     for i in range(n):        #Using for loop and else
# # #         if str[i] != str[n-i-1]:
# # #             print("It's not a Palindrome")
# # #     else:
# # #         print("It's a Palindrome......")
# # # palindrome("madam")
            
# # #=============================Palindrome of Number=============================

# # # def palindrome(n):
# # #     rev_n=0
# # #     temp=n
# # #     while(temp>0):
# # #         digit=temp%10
# # #         rev_n=rev_n*10+digit
# # #         temp=temp//10

# # #     if rev_n==n:
# # #         return True
# # #     else:
# # #         return False

# # # n=1234321
# # # print(palindrome(n))
            

# # #=====================Compresssssssssssssss Stringgggggggggggggg===================
# # # input=aaabbbbbcccceeffffff
# # # output=a3b5c4e2f6

# # # def compress_str(s):
# # #     new_str=""
# # #     n=len(s)
# # #     count=1
# # #     for i in range(n-1):
# # #         if s[i] == s[i+1]:
# # #             count +=1
# # #         else:
# # #             new_str=new_str+s[i]+str(count)
# # #             count=1

# # #     new_str=new_str+s[-1]+str(count)        #To add the last Character


# # #     return new_str

# # # s="aaabbbbbcccceeffffff"

# # # print(compress_str(s))


   



# # #================================Inheritance and Matrix=========================

# # # class Student_Ninth():
# # #     def __init__(self, name, s_id):
# # #         self.name=name
# # #         self.s_id=s_id
# # #     def details(self):

# # #         return f"{self.name}-{self.s_id}"
    
# # # class Student_Tenth(Student_Ninth):
# # #     def __init__(self,name,s_id,practical):
# # #         super().__init__(name,s_id)
# # #         self.practical=practical

# # #     def details(self):
# # #         return f"{self.name}-{self.s_id}--{self.practical}"

# # # s_9=Student_Ninth("RAm",1001)
# # # print(s_9.details())

# # # s_10=Student_Tenth("raam",1002,True)
# # # print(s_10.details())



# # #===========Prit a Matrix and its Elements===========


# # matrix=[
# #     [1,0],
# #     [0,1],
# #     [1,0]
# # ]

# # for row in matrix:
# #     for ele in row:
# #         print(ele, end=" ")
# #     print()


# # import numpy as np

# # matrix=np.array([
# #     [1,3],
# #     [4,5],
# #     [0,1]
# #     ])

# # matrix_list=matrix.tolist()
# # print(matrix_list)

# # matrix_list1=matrix.flatten().tolist()
# # print(matrix_list1)

# # # print(matrix)
# # # for row in matrix:
# # #     for elem in row:
# # #         print(row, end=" ")

# # #     print()




# # # lst=[]
# # # for row in matrix:
# # #     for elem in row:
# # #         lst.append(elem)

# # # print(lst)

# #===========================================Decorators=======================

# def main_func(func):
#     def wrapper(name):
#         print("Before the Function Runs........")
#         func(name)
#         print("After the Function Runs..............")
#     return wrapper

# name="Sara"

# @main_func
# def say_hello(name):
#     print("Hellooooo.....", name)

# say_hello(name)

# #==================================Generators and Iterators==========================

# #GENERATOR
# def sqr(n):
#     for i in range(1,n+1):
#         yield i*i
# a=sqr(7)
# print(next(a))
# print(next(a))
# print(next(a))

# #ITERATOR
# iter_list=iter(['A','B','C','D'])
# print(next(iter_list))
# print(next(iter_list))
# print(next(iter_list))









# # Task Details:
# # Write a Python script that:
# # Makes an HTTP request to a weather website (e.g., Weather.com or BBC Weather).
# # Parses the HTML content to find the current temperature for a specified city.
# # Prints the current temperature in a readable format.
# # Constraints:
# # Use the requests library for making HTTP requests.
# # Use BeautifulSoup from the bs4 library for parsing HTML.
# # The city can be hardcoded for simplicity (e.g., "London").
# # Example:
# # If you choose BBC Weather (https://www.bbc.com/weather), the output should be similar to:
# # The current temperature in London is 15°C.



# # import requests
# # from bs4 import BeautifulSoup
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.common.keys import Keys
# # driver=webdriver.Chrome()

# # driver.get("https://www.bbc.com/weather")

# # input=driver.find_element(By.ID, "ls-c-search__input-label")

# # input.clear()
# # input.send_keys("London")
# # # input.send_keys(keys.RETURN)


# # temperature=driver.find_element(By.CLASS_NAME, "wr-day-temperature ").text.strip()
# # print(temperature)
# # print(driver.page_source)





# # nums = [0,0,1,1,1,2,2,3,3,4]
# # # num=list(set(nums))
# # # print(num)
# # # print(len(num)) 

# # nums1=[]
# # for i in nums:
# #     if i not in nums1:
# #         nums1.append(i)
# # print(nums1)
# # print(len(nums1))







# For example, given the list [[1, [2, [3, 4], 5], 6], [7, 8]],
# the expected output is [1, 2, 3, 4, 5, 6, 7, 8]


lst=[[1, [2, [3, 4], 5], 6], [7, 8]]
def flatten_list(lst):
    flatn_list=[]
    def flatten( sub_list):
        for i in sub_list:
