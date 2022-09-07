# Accept marks in 5 subjects out of 100.
# Calculate the average, percentage and display the grade as per the following:
# 80 > O   70 > A   60 > B   50 > C   40 > D   else: F

mat = int(input("Enter your Mathematics marks: "))
phy = int(input("Enter your Phyiscs marks: "))
che = int(input("Enter your Chemistry marks: "))
bio = int(input("Enter your Biology marks: "))
eng = int(input("Enter your English marks: "))

total = mat + phy + che + bio + eng
p = total/5

# Method 1
if p >= 80:
    g = "O"
elif 70 <= p > 80:
    g = "A"
elif 60 <= p > 70:
    g = "B"
elif p >= 50 and p < 60:                 # Could write like the previous ones
    g = "C"
elif p >= 40 and p < 50:                 # Binary comparison of conditions
    g = "D"
else:
    g = "F"
print(f"Percentage = {p}% and Grade = {g}")

# Method 2 : using range func
if p in range(80, 101):
    grd = "O"
elif p in range(70, 80):
    grd = "A"
elif p in range(60, 70):
    grd = "B"
elif p in range(50, 60):
    grd = "C"
elif p in range(40, 50):
    grd = "D"
else:
    grd = "F"
print(f"Percentage = {p}% and Grade = {grd}")
