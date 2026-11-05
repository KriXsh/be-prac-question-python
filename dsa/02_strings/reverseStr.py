#dont use inbuilt function
str = "krish"
revStr = ""

for ch in str:
    revStr = ch + revStr
print(revStr)


#or

str1 = "krish"
revStr1 = ""
for i in range(len(str1)-1, -1, -1):
    revStr1 += str1[i]
print(revStr1)

#or

print(str1[::-1])