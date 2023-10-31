#Question 1:

print("##### Question 1 #####")
print()

result_a = 10*(90+2)-5
print("result of 10*(90+2)-5 is: ",result_a)

result_b = 10*90+2-5
print("result of 10*90+2-5 is: ",result_b)

result_c = 10*90+(2-5)
print("result of 10*90+(2-5) is: ",result_c)

result_d = 10.0*(90+2)-5
print("result of 10.0*(90+2)-5 is: ",result_d)

result_e = 120/(20+40)-(6-2)/4
print("result of 120/(20+40)-(6-2)/4 is: ",result_e)

result_f = 5.0/2
print("result of 5.0/2 is: ",result_f)

result_g = 5/2
print("result of 5/2 is: ",result_g)

result_h = 5.0/2.0
print("result of 5.0/2.0 is: ",result_h)

result_i = 5/2.0
print("result of 5/2.0 is: ",result_i)

result_j = 678%3*(8-(9/4))
print("result of 678%3*(8-(9/4)) is: ",result_j)


#Question 2
print()
print("##### Question 2 #####")
print()

id = input("Please enter your ID: ")
name = input("Please enter your name: ")
date_of_birth = input("Please enter your date of birth in this format 'DD/MM/YYYY': ")
address= input("Please enter your address: ")

formatted_id = "0" + id
formatted_name = name.upper()
formatted_address =  address.lower().strip()

print("Your profile - ID: [",formatted_id,"], name: [",formatted_name,"], DOB: [",date_of_birth,"], Address: [", address )


#Question 3
print()
print("##### Question 3 #####")
print()

number = int(input("Enter a number: "))
number_length = len(str(number))

print(number, "has", number_length, "digits")



#Question 4
print()
print("##### Question 4 #####")
print()

grade = int(input("Enter a grade: "))

if grade <= 60:
  letter_grade = "F"
elif grade >= 60 and grade < 63:
  letter_grade = "D-"
elif grade >= 63 and grade < 67:
  letter_grade = "D"
elif grade >= 67 and grade < 70:
  letter_grade = "D+"
elif grade >= 70 and grade < 73:
  letter_grade = "C-"
elif grade >= 73 and grade < 77:
  letter_grade = "C"
elif grade >= 77 and grade < 80:
  letter_grade = "C+"
elif grade >= 80 and grade < 83:
  letter_grade = "B-"
elif grade >= 83 and grade < 87:
  letter_grade = "B"
elif grade >= 87 and grade < 90:
  letter_grade = "B+"
elif grade >= 90 and grade < 93:
  letter_grade = "A-"
elif grade >= 93 and grade < 97:
  letter_grade = "A"
else:
  letter_grade = "A+"
  
print(grade, "is equivalent to a", letter_grade)


#Question 5
print()
print("##### Question 5 #####")
print()

n = int(input("Enter a number to draw the pattern: "))

for i in range(1, n + 1):
    print('*' * i)

for i in range(n - 1, 0, -1):
    print('*' * i)




#Question 6
print()
print("##### Question 6 #####")
print()

num_1 = int(input("Enter a number: "))
num_2 = int(input("Enter a number greater than the 1st one: "))

while num_2 < num_1:
  num_2 = int(input("Enter a number greater than the 1st one: "))

print("The even numbers between", num_1, "and", num_2, "are:")

for num in range(num_1, num_2 + 1):
  if num % 2 == 0:
    print(num)



