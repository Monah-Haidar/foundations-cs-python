#######
# Ex 1
#######

# s1 = input("Enter a word: ")
# num = int(input("Enter a number: "))

# def printReversed(s, i):
#   if i == 0:
#     return ""
#   else:
#     reversed_string = s[::-1]
#     return reversed_string * i

# print(printReversed(s1, num))


#######
# Ex 2
#######

# s1 = input("Enter a word: ")

# def upperFirst(s):
#   sec1 = ""
#   sec2 = ""
#   for i in s:
#     if i.isupper():
#       sec1 = sec1 + i
#     elif i == " ":
#       continue
#     else:
#       sec2 = sec2 + i

#   return sec1 + sec2
  
# print(upperFirst(s1))


#######
# Ex 3
#######

# s1 = input("Enter a word: ")
# s2 = input("Enter a word: ")

# def isReordered(s1, s2):
#   return sorted(s1) == sorted(s2)

# print(isReordered(s1,s2))




#######
# Ex 4
#######

# list1 = [5,6,3,2,7,2,0,1,6]


# def maxNum(list):
#   max = 0
#   for x in list:
#     if x > max:
#       max = x
#   return max

# def minNum(list):
#   min = list[0]
#   for x in list:
#     if x < min:
#       min = x
#   return min
  

# print("max num:", maxNum(list1))
# print("min num:", minNum(list1))
  


#######
# Ex 5
#######

# num = int(input("Enter a number: ")) # 3 4 8

# def sumOfDigits(n):
#   if n == 0:
#     return 0
#   return n % 10 + sumOfDigits(n // 10)

# print(sumOfDigits(num))



#######
# Ex 6
#######

# s6 = "hhheelloo   wwwoorrrllldd"

# def removeDuplicates(s):
#   if len(s) < 2:
#     return s
#   elif s[0] == s[1]:
#     return removeDuplicates(s[1:])
#   else:
#     return s[0] + removeDuplicates(s[1:])

# print(removeDuplicates(s6))