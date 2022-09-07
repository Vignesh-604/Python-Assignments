# Reverse the order of the number. For ex.: 546 --> 645

num = int(input("Enter a valid int number: "))

# Method 1 : Converting into str then int.
nums = str(num)
print(int(nums[::-1]))

# Method 2 : Using loop.
rev = 0

while num != 0:
    n = num % 10
    num = num // 10
    rev = rev * 10 + n
print(rev)
