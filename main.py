# Question 1: Write a Python program to check if a string is a palindrome.
# def is_palindrome(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
#
#
# word = "madam"
# if is_palindrome(word):
#     print(f"{word} is a palindrome")
# else:
#     print(f"{word} is not a palindrome")


# Question 2: Write a Python program to find the factorial of a number.


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)


# def factorial(n):
#     num = 1
#     for j in range(2, n+1):
#         num *= j
#     return num
# # Test the function
# number = 5
# result = factorial(number)
# print(f"The factorial of {number} is {result}")


# Question 3: Write a Python program to find the largest element in a list.

# def find_largest(n):
#     largest = 0
#     for j in n:
#         if j > largest:
#             largest = j
#     return largest
#
# # Test the function
# nums = [10, 5, 50, 8, 20, 3]
# largest_num = find_largest(nums)
# print(f"The largest number is {largest_num}")


# Question 4: Write a Python program to reverse a string.

# def reverse_string(text):
#     return text[::-1]
#
# # Test the function
# text = "Hello, World!"
# reversed_text = reverse_string(text)
# print(reversed_text)


# Question 5: Write a Python program to count the frequency of each element in a list.
# Test the function

# def count_frequency(nums):
#     frequency = {}
#     for el in nums:
#         if el in frequency:
#             frequency[el] += 1
#         else:
#             frequency[el] = 1
#     return frequency
#
# nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# frequency_count = count_frequency(nums)
# print(frequency_count)


# Question 6: Write a Python program to check if a number is prime.

# def is_prime(num):
#     if num < 2:
#         return False
#     else:
#         for n in range(2, num):
#             if num % 2 == 0:
#                 return False
#         return True
#
#
#
# # Test the function
# num = 8
# if is_prime(num):
#     print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")


# Question 7: Write a Python program to find the common elements between two lists.

# def find_common_elements(list_a, list_b):
#     most_common_elements = []
#     for k in list_b:
#         if k in list_a:
#             most_common_elements.append(k)
#     return most_common_elements
#
#
# # Test the function
# list_a = [1, 2, 3, 4, 5]
# list_b = [4, 5, 6, 7, 8]
# common = find_common_elements(list_a, list_b)
# print(common)


# Question 9: Write a Python program to find the second largest number in a list.

# def find_second_largest(n):
#     largest = 0
#     second_largest = 0
#     for k in n:
#         if k > largest:
#             second_largest = largest
#             largest = k
#         elif k > second_largest and k != largest:
#             second_largest = k
#     return second_largest
#
# # Test the function
# nums = [10, 5, 8, 20, 3]
# second_largest_num = find_second_largest(nums)
# print(f"The second largest number is {second_largest_num}")


# Question 10: Write a Python program to find the third largest number in a list.

# def find_third_largest(nums):
#     largest = 0
#     second_largest = 0
#     third_largest = 0
#     for k in nums:
#         if k > largest:
#             third_largest = second_largest
#             second_largest = largest
#             largest = k
#         elif k > second_largest and k != largest:
#             third_largest = second_largest
#             second_largest = k
#         elif k > third_largest and k != second_largest:
#             third_largest = k
#
#     return third_largest
#
# # Test the function
# nums = [10, 5, 8, 20, 3]
# third_largest_num = find_third_largest(nums)
# print(f"The third largest number is {third_largest_num}")


# Question 11: Write a Python program to remove duplicates from a list.

# def remove_duplicates(nums):
#     unique_nums = []
#     for n in nums:
#         if n not in unique_nums:
#             unique_nums.append(n)
#     return unique_nums
#
# # Test the function
# nums = [1, 2, 3, 2, 1, 3, 2, 4, 5, 4]
# unique_nums = remove_duplicates(nums)
# print(unique_nums)


# Question 12 Write python program to group words that are anagrams from given list
# from collections import defaultdict
#
# def group_anagrams(word_list):
#     anagram = defaultdict(list)
#     for word in word_list:
#         sorted_words = "".join(sorted(word))
#         anagram[sorted_words].append(word)
#     return list(anagram.values())
#
#
# # Test the function
# word_list = ["listen", "silent", "enlist", "rat", "tar", "god", "dog", "evil", "vile", "veil"]
# grouped_anagrams = group_anagrams(word_list)
# print(grouped_anagrams)


# Question 13 Writing Fibonacci Series from given range


# Test the function

# def fib_series(n):
#     fib = [0,1]
#     for i in range(n):
#         fib.append(fib[-2] + fib[-1])
#     return fib
#
# num = 5
# result = fib_series(num)
# print(result)



# Question 14  Finding the Middle Element in a List
# def find_middle_element(n):
#     middle_index = int(len(n)/ 2)
#     return n[middle_index]
#
#
# numList = [1, 2, 3, 4, 5]
# result = find_middle_element(numList)
# print(result)



 # Question 15 Adding Two List Elements Together

# def add_two_list_elements(lst1, lst2):
#     result = []
#     for j in range(len(lst2)):
#         result.append(lst1[j] + lst2[j])
#     return result
#
# lst1 = [1, 2, 3]
# lst2 = [4, 5, 6]
# result = add_two_list_elements(lst1, lst2)
# print(result)



# Question 16 Comparing Two Strings for Anagrams

# def find_anagrams(str1, str2):
#     str1_or = sorted(str1.lower())
#     str2_pr = sorted(str2.lower())
#     if str1_or == str2_pr:
#         return True
#     else:
#         return False
#
# str1 = "Listen"
# str2 = "Silent"
#
# result = find_anagrams(str1, str2)
# if result:
#     print("True")
# else:
#     print("False")



# Question 17 Write a function to group a list of dictionaries by a specific key.

# def group_by_key(dicts_list, key):
#     grouped = {}
#
#     # Iterate through each dictionary in the list
#     for dictionary in dicts_list:
#         # Get the value of the specified key
#         key_value = dictionary.get(key)
#
#         # If the key value is not in the grouped dictionary, create a new list for it
#         if key_value not in grouped:
#             grouped[key_value] = []
#
#         # Add the dictionary to the list of the corresponding key value
#         grouped[key_value].append(dictionary)
#
#     return grouped


# Test the function with the provided input
# dicts_list = [{'name': 'John', 'city': 'New York'}, {'name': 'Jane', 'city': 'Los Angeles'}, {'name': 'Doe', 'city': 'New York'}]
# result = group_by_key(dicts_list, 'city')
# print(result)


# Question 18 Python function to find the longest common substring between two strings

# def longest_common_substring(str1, str2):
#     longest = ""
#     for i in range(len(str1)):
#         for j in range(i + 1, len(str1) + 1):
#             substring = str1[i:j]
#             if substring in str2 and len(substring) > len(longest):
#                  longest = substring
#     return longest
#
# # Example usage
# str1 = "abcdxyz"
# str2 = "xyzabcd"
# result = longest_common_substring(str1, str2)
# print(f"Longest common substring: '{result}'")


# 
# def longest_common_substring(str1, str2):
#     log_com_str = ""
#     for i in range(len(str1)):
#         for j in  range(len(str1)+1):
#             substring = str1[i:j]
#             if substring in str2:
#                 if len(substring) > len(log_com_str):
#                     log_com_str = substring
#     return log_com_str
#
#
#
# str1 = "abcdvwxyz"
# str2 = "vwxyzabcd"
# result = longest_common_substring(str1, str2)
# print(f"Longest common substring: '{result}'")



# Question 19 Count substring occurance in given string

# def count_substring(string, substring):
#     count = 0
#     for i in range(len(string) - len(substring) + 1):
#         print(string[i:i + len(substring)])
#         if string[i:i + len(substring)] == substring:
#             count += 1
#     return count
#
#
#
# string = "ABCDCDC"
# substring = "CDC"
# result = count_substring(string, substring)
# print(f"The substring occurs {result} times in the main string.")
