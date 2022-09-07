# Insert 3 numbers and find out the highest and second-highest number among the three.
a = float(input("Enter your first number: "))
b = float(input("Enter your second number: "))
c = float(input("Enter your third number: "))

# First method : using 'max' function
list = [a, b, c]
max1 = max(list)
list.remove(max1)
max2 = max(list)
print(f"The first highest number is {max1} and second highest is {max2}.")

# Second method
if b<a>c:
    print(f"The highest number is {a}.")
    if b>c:
        print(f"The second-highest number is {b}.")
    else:
        print(f"The second-highest number is {c}.")
elif a<b>c:
    print(f"The highest number is {b}.")
    if a>c:
        print(f"The second-highest number is {a}.")
    else:
        print(f"The second-highest number is {c}.")
elif a<c>b:
    print(f"The highest number is {c}.")
    if a>b:
        print(f"The second-highest number is {a}.")
    else:
        print(f"The second-highest number is {b}.")
else:
    print("Please input different numbers.")

# Third method : without elif
if a > b:
    if a > c:
        large=a
        if b > c:
            s_large = b
        else:
            s_large = c
    else:
        large = c
        s_large = a
else:
    if b > c:
        if b > a:
            large = b
            if a > c:
                s_large = a
            else:
                s_large = c
        else:
            large = a
            s_large = b
print(f"The highest number is {large} and second highest number is {s_large}.")
