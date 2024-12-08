# # 1. Given a string s = "Python", use a for loop to print each character of the string.
# s = 'python'
# for i in s:
#     print(i)


# 2. Write a while loop to print the numbers from 10 down to 1.

# a = " ".join(str(i) for i in range(10, 0, -1))
# print (a)

# for i in range(10,0,-1):    # decrementig number (-1)
#     print (i)



# # 3. Write a for loop to print all prime numbers between 1 and 20.
# for i in range(1,20):
#     for j in range (2,i):
#         if (i % j) == 0:
#             print(j)



# # 4.Write a while loop to calculate the factorial of a given number n = 5. 
# n = 5
# fact = 1
# for i in range(n,1,-1):      #line4 #  this line print the range in reverce
#     fact = fact*i
# print(fact)



# 5.Given a list numbers = [10, 20, 4, 45, 99], use a for loop to find the largest element. 
# list = [10,20,4,45,99]
# print(max(list))



# alist=[10,20,4,45,99]
# largest=alist[0]
# for large in alist:
#     if large > largest:
#        largest=large
# print(largest)



# 6.Given a string s = "Python", use a while loop to reverse the string.
# s = 'python'
# i = len(s) - 1
# reverse = ""
# while i >= 0:
#     reverse += s[i]  
#     i  -= 1
# print(reverse)


# ATM machine
balance = 20000
while True:
    print("\Welcome to the ATM!")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check Balance")
    print("4. Exit")

    choice = input("Enter your choice (1/2//3/4):")

    if choice == "1":
        amount = float(input("Enter amount to deposite:"))
        if amount > 0:
            balance += amount
            print(f"{amount} deposit successfully. New balance:{balance}")
        else:
            print("INvalid amont : Please enter a positive value.")

    elif choice == "2":
        amount = float(input("Enter amount to withdraw:"))
        if 0 < amount <= balance:
            balance -= amount
            print(f"{amount} withdraw successfully. Remaining balance: {balance}")
        elif amount > balance:
            print("Insufficient balance:")
        else:
            print("Invalid amount. please enter a positive values.")
    elif choice == "3":
        print(f"Your current balance is : {balance}")
    elif choice == "4":
        print("Thank you for using this ATM.")
        break
    else:
        print("Invalid choice. Please try again")