# for num in range(10):
#     if num % 2 == 0:
#         continue
#     if num == 7:
#         break
#     print(num)


# CODE = 1234
# while True:
#     code_user = int(input("Enter a code "))
#     if code_user == CODE:
#         print("Welcome")
#         break
#     else:
#         print("Try again")


# list_products = []
# while True:
#     product = input("Input a product ")
#     if product == "done":
#         print(list_products)
#         break
#     list_products.append(product)


# for num in range(1, 4):
#     for num1 in range(1, 4):
#         if num1 == 2:
#             break
#         print(f"row:{num} col:{num1}")



# count = 0
# words = input("Enter words ")
# for char in words:
#     if char in "aeoiuAEOIU":
#         count += 1
# print(count)


# for num in range(1,6):
#     for num1 in range(1,6):
#         print(num * num1, end=" ")
#     print("\n")


# word = input("input word ")
# accumulator = ""
# n = -1
# for char in word:
#     accumulator = char + accumulator
# print(accumulator)



# count = 0
# num = int(input("Enter a number "))
# while num:
#     if int(num) % 2 == 0:
#         count += 1
#     num = str(num)[:-1]

# print(count)


# word = input("input word ")
# new_word = ""
# for char in word:
#     new_word += char * 2
# print(new_word)


# x = None
# num_highest = 0
# while x != 0:
#     x = int(input("Enter a number "))
#     if x > num_highest:
#         num_highest = x 

# print(num_highest)


# word = input("input word ")
# flag = True
# for char in word:
#     if char.lower() not in "1234567890abcdefghijklnopkrstuvwxyz":
#         flag = False
# print(flag)    



# num = int(input("Enter a number "))
# new_num = 0
# x = 100

# while num:
#     new_num += (num % 10) * x 
#     num = num // 10
#     x = x // 10

# print(new_num)

x = 1
print(x // 10)

