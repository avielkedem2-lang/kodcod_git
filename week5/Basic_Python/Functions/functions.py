# 1
# def is_even(n):
#     return n % 2 == 0
# print(is_even(9))


# 2
# def factorial(n):
#     count = 1
#     sum = 1
#     while count <= n:
#         sum = sum * count
#         count += 1
#     return sum

# print(factorial(7))



# 4
# def is_palindrome(word: str):
#     reversed_word = word[:: -1]
#     return reversed_word == word
# print(is_palindrome("asasa"))



# 5
# def sum_digits(n):
#     if n < 10:
#         return n
#     str_n = str(n)
#     numbers = []
#     for num in str_n:
#         numbers.append(int(num))

#     sum_numbers = 0
#     for num in numbers:
#         sum_numbers += num
#     return sum_digits(n=sum_numbers)

# print(sum_digits(984764786575))




# 6
# def num_digits(n):
#     count = 0
#     while n:
#         n = n // 10
#         count += 1
#     return count
# print(num_digits(6))




# 7
# def reverse_digits(n):
#     new_num = 0
#     x = 10 ** (len(str(n)) -1)
#     while n:
#         new_num += (n % 10) * x 
#         n = n // 10
#         x = x // 10
#     return new_num
# print(reverse_digits(1765))




# 8
# def zero_order(arr:list):
#     for i, num in enumerate(arr):
#         if num == 0:
#             x = arr.pop(i)
#             arr.append(x)
#     return arr

# nums = [1, 2, 0, 4, 0, 6, 0, 4, 7, 0, 12]
# print(zero_order(nums))




# 9
# def sum_digits(arr):
#     sum_nums = 0
#     for num in arr:
#         sum_nums += num
#     return sum_nums


# def average_digits(arr):
#     sum_nums = sum_digits(arr)
#     count = len(arr) 
#     average = sum_nums / count 
#     return average


# def minimum_digits(arr):
#     num_min = None
#     for i, num in enumerate(arr):
#         if i == 0:
#             num_min = num
#             continue
#         if num < num_min:
#             num_min = num
#     return num_min


# def maximum_digits(arr):
#     max_num = None
#     for i, num in enumerate(arr):
#         if i == 0:
#             max_num = num
#         if num > max_num:
#             max_num = num
#     return max_num

# nums = [3, 6, 4, 8, 77, 44, 67, 2, 90, 3]
# print(sum_digits(nums))
# print(average_digits(nums))
# print(minimum_digits(nums))
# print(maximum_digits(nums))




# 10
# def reverse_list(arr):
#     new_arr = []
#     while arr:
#         num = arr.pop(-1)
#         new_arr.append(num) 
#     return new_arr

# nums = [1, 2, 3, 4, 5]
# print(reverse_list(nums))



# 11
# def clean_list(arr):
#     new_list = []
#     for num in arr:
#         if num not in new_list:
#             new_list.append(num)
#     return new_list

# nums = [4, 5, 9, 9, 3, 5, 2, 4, 8, 9]
# print(clean_list(nums))





# def func1(name,/, lastname, age):
#     print(f"name: {name} {lastname}, age: {age}")

# func1("avi", lastname="kedem", age=21)


# def func2(*nums):
#     for num in nums:
#         print(num)

# func2(1, 2, 3, 4, 6)


def func3(name,/,*, lastname, age):
    print(f"name: {name} {lastname}, age: {age}")

func3("avi", lastname="kdem", age=55)