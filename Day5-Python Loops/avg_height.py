n = int(input("Number of records: "))
height = (input("Enter the student heights seperated by a space: ")).split()
print(height)
sum = 0
for i in range(0, n):
    height[i] = int(height[i])
    sum = sum + height[i]
avg = sum/n
print(avg)