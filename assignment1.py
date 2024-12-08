# a. Given two variable x = 15 and y = 20, use conditional statement to print which variable is larger or if they are equal
# x = 21
# y = 20

# if x>y:
#     print("x is greater")
# elif x==y :
#     print("both are equal")
# else :
#     print("y is greater")


# b. Given a variable num = 7, use a conditional statement to check if the number is even or odd and print the result. 
# num = 8
# if num % 2 == 0:
#     print("{num} is even")
# else:
#     print("{num} is odd")


# c.Write a Python Program to Check weather a candidate Eligible for Vote or not.
# age = int(input(f"Please enter your age :"))
# print(age)
# if age>=18:
#     print("Congralations you eligible for vote")
# else:
#     print("You can't to eligible for vote")


# d.Write a Python program to check weather Given Number is Divisible by 7 or Not.
# number = int(input("Enter a number :"))
# if number//7==0:
#     print("{number} is divisible by 7")
# else:
#     print("{number}can't be divisible by 7")


# e. Write a program to accept percentage from the user and display the grade according to the following ** ** 
# criteria: ** Marks Grade marks > 80: A+ grade marks > 70 : A grade marks > 60: B grade ** marks > 50: C grade** else Failed

marks = float(input("Enter your marks :"))
to_marks = int(input("Enter your total marks :"))
grade = int(marks/to_marks*100)
print(grade)
if grade > 80:
    print("Your {grade} A+")

elif grade >=70:
    print(f"Your {grade} is A")

elif grade >=60:
    print("Your {grade} is B")

elif grade >=50:
    print("Your {grade} is C")

else:
    print("Your failed")