num = int(input("enter a nummber"))
rev = 0
while num > 0:
    rev = rev * 10 + num % 10;
    num //=10

print(rev)

# anoter way

k = 1234
print(str(k)[::-1])