s = input("Enter teh string ")
vowels = 0
con = 0
for i in s:
    if i in "aeiouAEIOU":
        vowels += 1
    else:
        con += 1

print(vowels)
print(con)

s = "python"

print(sum(1 for ch in s if ch in "aeiou"))