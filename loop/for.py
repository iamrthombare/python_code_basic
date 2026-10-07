#for i in range(1,30,2):
   # print(i)
from ftplib import print_line

#print(* range(1,30,2))

print(*range(1, 11,3))  # alternate way to print num

res = sum(range(1, 11, 3))
print(res)

for i in range(1,100):
    if i % 2 == 0:
        print_line(i)

for i in "abscbnfiififi":
    print(i)


while True:
    i = int(input("Enter a number"))
    if(i>0):
        for k in range (1,100):
            if(k %  2== 0 or k % 4 == 0):
                print(k)
            else :
                print(k)
    else:
        break;

sum=0
l = int(input("Enter a number"))
while l > 1:
    for i in range (1,100):
        if(l % 2== 0 or l % 4 == 0):
            sum+=i
    print(sum)

# count digit count
count = 0
num = int(input("Enter a digit"))
while num > 0 :
    count+=1
    num //=10
print(count)