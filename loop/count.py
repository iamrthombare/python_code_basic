# count digit count
count = 0
num = int(input("Enter a digit"))
while num > 0 :
    count+=1
    num //=10
print(count)

# another way
k = 11111
print(len(str(k)))