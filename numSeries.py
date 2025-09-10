# incr=7

# for i in range(7,incr):
#     print(i," ")
#     # print("incr: ",incr)
#     incr=incr+1
#     print("incr: ",incr)

# a=0
# for i in range(7,14):
#     a=a+i
#     print(a)

# 1. take list from user 
# 2. find odd numbers and in that those numbers fully divided by 5 print hello otherwise print odd numbers

# num=int(input("Enter the number of elements in the list: "))
# list=[]
# for i in range(num):
#     list.append(int(input()))
# print("List elements: ",list)

# for i in list:
#     if i%2!=0:
#         if i%5==0:
#             print("Hello")
#         else:
#             print(i)
    
# # find occurrence of each element in the list 
# for i in list:
#     print(f"{i}: {list.count(i)}")

# # find occurrence of each element in the list with index even
# for i in range(len(list)):
#     if i % 2 == 0:
#         print(f"index {i}: {list[i]} - {list.count(list[i])}")

# print square list
# newList=[2,4,5,6,7]
# for i in newList:
#     print(i**i,end=" ")

# function to check palindrome
def isPalindrome(s):
    if s==s[::-1]:
        print("Palindrome")
    else:
        print("Not Palindrome")

# print(isPalindrome("madam"))
# print(isPalindrome("hello"))

# using list comprehension

def is_palindrome(n):
    return n == n[::-1]

# print(is_palindrome("madam"))
# print(is_palindrome("hello"))

# zero divison error handling
# a=int(input("enter numerator: "))
# b=int(input("enter denominator: "))
# try:
#     print(a/b)
# except ZeroDivisionError:
#     print("zero can be in denominator")

# count vowel set
# text=input("enter text: ")
# vow=set("aeiouAEIOU")
# count=sum([1 for ch in text if ch in vow])
# print("vowel count: ",count)

# fibonaci series
n=10
fib=[0,1]
for _ in range(n-2):
    fib.append(fib[-1]+fib[-2])
print(fib)

for i in range(5):
    print(i,end=" ")