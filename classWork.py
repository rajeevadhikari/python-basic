# # 1
# a = int(input("enter first number:"))
# b = int(input("enter second number:"))
# def sum(a,b):
#     return a+b
# print(f"{sum(a,b)}")
    

# 2 factorial
# n = int(input("Enter your number "))
# def fact(n):
#     if n == 1 or n == 0:
#         return 1
#     return n*fact(n-1)
# print(fact(n))

# 3 fbinacci series
# def fibo(l):
#     if l == 0:
#         return 0
#     elif l == 1:
#         return 1
#     return fibo(l-1)+fibo(l-2)
# print(fibo(3))


# 4.Write a function called count_vowels that takes a string as an argument and returns the number of vowels in the string. 
# def count_vowels(string):
#     return sum(ch in 'aeiou' for ch in string.lower())

# print(count_vowels('oboe'))


# 5.Write a function called find_max that takes a list of numbers as an argument and returns the maximum number in the list.
# numbers = [10, 45, 67, 23, 89, 2]
# def find_max(numbers):
#     if not numbers:  # Check if the list is empty
#         return None  # Return None for empty lists
    
#     max_number = numbers[0]  # Assume the first number is the largest
#     for num in numbers:
#         if num > max_number:
#             max_number = num
#     return max_number
# # max_number = find_max(numbers)
# print("The maximum number is:",find_max(numbers))



# 5.Write a function that takes a string as an argument and returns True if the string is a palindrome, and False otherwise.
words = ['level', 'wow', 'maam', 'did', 'hello']
def is_palindrome(word):
    left, right = 0, len(word) - 1  # Initialize two pointers

    while left < right:
        if word[left] != word[right]:  # Compare characters from both ends
            return False  # If mismatch found, it's not a palindrome
        left += 1  # Move left pointer inward
        right -= 1  # Move right pointer inward

    return True  # If the loop completes, the word is a palindrome

# Example usage
for word in words:
    if is_palindrome(word):
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
