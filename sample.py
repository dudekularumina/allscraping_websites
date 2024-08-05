# (1) Palindrome of a Number

def palindrome_num(n):
    temp = n
    rev_n = 0
    while (temp > 0):
        digit = temp % 10
        rev_n = rev_n*10+digit
        temp = temp//10
    if n==rev_n:
        return True
    else:
        False
n=1234321
print(palindrome_num(n))



# (2) Palindrome of String

def palindrome_str(s):
    n=len(s)
    first=0
    last=n-1
    while(first<last):
        if s[first]==s[last]:
            first+=1
            last-=1
        else:
            return "It's not a Palindrome"
    return "It's a Palindrome"

print(palindrome_str("madam"))



# Using for loop

def palindrome_str(s):
    n=len(s)
    for i in range(n):
        if s[i]!=s[n-i-1]:
            print("Its not a palindrome")
    else:
            print("Its a Palindrome")
palindrome_str("madam")


# (3) Copression of String  InPut="aabbbccccddddfff"  OutPut="a2b3c4d4f3"

def compress_str(s):
    n=len(s)
    new_s=''
    count=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            count+=1
        else:
            new_s=new_s+s[i]+str(count)
            count=1
    new_s=new_s+s[n-1]+str(count)
    return new_s
s="aabbbccccddddffffh"
print(compress_str(s))


# (4) Factorial of Num without Recursion


def factorial(n):
    factorial=1

    if n<0:
        print("Factorial for Negative Numbers doesn't exist")
    elif n==0:
        print("Factorial of 0 is 1..")
    else:
        for i in range(1, n+1):
            factorial=factorial*i
        print("Factorial of", n , "is:", factorial)
n=int(input("enter any number:"))

factorial(n)


# (5) Factorial of a Number using Recursion


def fact(n):
    if n==1:
        return 1
    else:
        return n*(fact(n-1))

n=int(input("Enter any num:"))
if n<0:
    print("Factorial for Negative Numbers doesn't exist")
elif n==0:
        print("Factorial of 0 is 1..")

else:
    print("Factorial of", n , "is:", fact(n))


# (6) Prime or not 


def prime(n):
    if n>1:
        for i in range(2, n//2+1):
            if n%i==0:
                print("no not a Prime")
                break
        else:
                print("Its a prime")
    else:
        print("No not a Prime")
prime(11)



# (7) Primes between two numbers

def primes(start, end):
    for n in range(start, end):
        if n>1:
            for i in range(2, n//2+1):
                if n%i==0:
                 break
            else:
                print(n)
primes(1,12)

# OUTPUT: 2,3,5,7,11


# (8) Sort a list without using sort() function

lst=[56,87,4,8,96,78,98,3]
n=len(lst)
for i in range(n):
    for j in range(i+1, n):
        if lst[i]>lst[j]:     #> for increasing order  < for decreasing order
            lst[i], lst[j]=lst[j], lst[i]
print(lst)

# OUTPUT: [3, 4, 8, 56, 78, 87, 96, 98]


# (9) Sort a dictionary

dict1={764:"apple", 86:"Banana", 73:"jugs"}
d=sorted(dict1.keys())   #[73, 86, 764]
dict2={}
for i in d:
    dict2[i]=dict1[i]
print(dict2)


# OUTPUT: {73: 'jugs', 86: 'Banana', 764: 'apple'}



# (10) print all pairs with sum equals to given number


lst=[5,8,7,3,9,4,5,6]
n=len(lst)
k=9
for i in range(n):
    for j in range(i+1, n):
        if (lst[i]+lst[j])==k:
            print(list((lst[i],lst[j])))

# OUTPUT: [5, 4]
#         [3, 6]
#         [4, 5]


# (11) input=" the sky is blue"  output="blue is sky the"

s="the sky is blue"
l=s.split()
l=l[::-1]
l=' '.join(l)
print(l)

# OUTPUT= blue is sky the


# (12) SUM OF DIGITS OF A NUMBER   IP=8128  UP=19

def sum_of_digits(n):
    sum=0
    temp=n
    if n>9:
        while(temp>0):
            digit=temp%10
            sum=sum+digit
            temp=temp//10
    else:
        sum=n
    return sum
print(sum_of_digits(765876))

#   OUTPUT:7+6+5+8+7+6=39

# (13) ARMSTRONG NUMBER OR NOT EG: 153=1*1*1+5*5*5+3*3*==153

def armstrong(n):
    sum=0
    temp=n
    while(temp>0):
        digit=temp%10
        sum=sum+(digit**3)
        temp=temp//10

    if n==sum:
        print("YES")
    else:
        print("no")
armstrong(153)

# OUTPUT: YES

# (14) TO GET A LIST OF ARMSTRONG NUMBERS FROM START TO END 


def armstrong(start, end):
    for n in range(start, end):

        sum=0
        temp=n
        while(temp>0):
            digit=temp%10
            sum=sum+(digit**3)
            temp=temp//10

        if n==sum:
            print(n)
armstrong(0, 500)

# OUTPUT:
# 0
# 1
# 153
# 370
# 371
# 407

# (15) Count No.of occurances of characters

def count_all(s):
    ch={}
    for i in s:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=1
    print(ch)
count_all("aaaabbbablkllklba")

# OUTPUT: {'a': 6, 'b': 5, 'l': 4, 'k': 2}


# (16) To get minimum occorence element from the string 

def count_all(s):
    ch={}
    for i in s:
        if i in ch:
            ch[i]=ch[i]+1
        else:
            ch[i]=1
    print(ch)    #{'a': 6, 'b': 5, 'l': 4, 'k': 2}

    result=min(ch, key=ch.get)

    print(result)    # k

count_all("aaaabbbablkllklba")

# OUTPUT:
# {'a': 6, 'b': 5, 'l': 4, 'k': 2}
#  k

# (17) Fibionacci series

def fibionacci(n):
    a,b = 0,1
    while(b<n):
        print(b)
        a,b=b,a+b
print(fibionacci(150))

# OUTPUT:1,1,2,3,5,8,13,21,34,55,89,144





