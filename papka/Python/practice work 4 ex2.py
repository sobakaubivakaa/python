num = int(input("Write your integer: "))
sum = 0
count=0
while (num != 0):
    sum = sum + num % 10
    num = num // 10
    count=count+1
print("Sum: ", sum)
print("Num:", count)
