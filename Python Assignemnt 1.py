Brijendra Assignment 1

#Q1-

s = 'brijendra'
print(s.replace('a', 'k'))

#Q2-

string = 'Brijendra Kumar Yadav'
print('Number of occurrence of a:', string.count('a'))

#Q3-

def check(s1, s2):
	
	if(sorted(s1)== sorted(s2)):
		print("The strings are anagrams.")
	else:
		print("The strings aren't anagrams.")		

s1 ="listen"
s2 ="silent"
check(s1, s2)

#Q4-

def isPalindrome(s):
	return s == s[::-1]
s = "yadav"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")

#Q5-

ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")


#Q6-

x = input("Enter:")
if(x >= '0' and x <= '9'):
    print("It is a Number")
else:
    print("It is Not a Number")


#Q7-

mystr = '12345'
print(mystr.isdigit())

#Q8-

string = "brijendra kumar yadav"
result = '' 
ch = 'B'
for i in string:
        if i == ' ':  
            i = ch  
        result += i  
print(“String after removing space with B = ”,result)

#Q9-

s = 'brijendra kumar yadav'
print(s.replace(' ', 'B'))


#Q10-

str="brijendra"
str1=str.upper() 
print(str1)

#Q11-

st = "brijendra"
new_str = ""
for i in range(len(st)):
    if(st[i] == 'a' or st[i] == 'e' or st[i] == 'i' or st[i] == 'o' or st[i] == 'u' or st[i] == 'A' or st[i] == 'E' or st[i] == 'I' or st[i] == 'O' or st[i] == 'U'):
        new_str = new_str + st[i].upper()
    else:
        new_str = new_str + st[i]
print(new_str)

#Q12-

A = []
for i in range(0,101):
    A.append(i)

A.remove(8)

total = (100)*(101)/2
sum_of_A = sum(A)
print(int(total - sum_of_A))

#Q13-

A = []
for i in range(0,91):
    A.append(i)

for i in range(0,11):
    A.append(i)

dict, new_list = {}, []
 
for i in A:
    if not i in dict:
        dict[i] = 1
    else:
        dict[i] += 1
 
for key, values in dict.items():
    if values > 1:
        new_list.append(key)

print(new_list)

#Q14-

a = []
n = int(input())
for i in range(0,n):
    a.append(int(input()))
num = int(input())
for i in range(0,n):
    c = num-a[i]
    for j in range(i+1, n):
        if(c == a[j]):
            print("Pairs" , a[i] , " and " , a[j])

#Q15-

a = [1,2,3,4,5]

b = [6,7,8,9,10]

if(len(a) == len(b)):
    print("Same size")
else:
    print("Different size")

#Q16-

from cmath import inf
a = [1,2,3,4,5,6,7,8,9]

mn = inf
mx = -inf

for i in range(len(a)):
    mx = max(mx,a[i])
    mn = min(mn,a[i])

print(mx, mn)

#Q17-

l1 = [1,2,3,4,5,6,7,8,9]
l2 = list(set(l1))
l2.sort()
print(l2[-2])

#Q18-

l1 = [1,2,3,4,5,6,7,8,9]
l2 = list(set(l1))
l2.sort()
print(l2[-1],l2[-2])

#Q19-

arr = [1,2,3,4,5,1,2,3,4,5]

st = set(arr)
l1 = list(st)
print(l1)

#Q20-

l1 = [1,2,3,4,5,6,7,8,9]
l2 = list(set(l1))
l2.sort()
print(l2[-1],l2[-2])

#Q21-

arr = [1,2,3,4,5,6,7,8,9]

for i in range(8,-1,-1):
    print(arr[i],end=" ")

#Q22-

print("First Way")

arr=[1,2,3,4,5]
l=[] 
for i in range(4,-1,-1):
    l.append(arr[i])
print(l)

print("Second Way")

brr = [1,2,3,4,5]
brr.reverse()
print(brr)


#Q23-

ar = [1,2,3,4,5]
count = 0
for i in ar:
    count = count + 1
print(count)

#Q24-

arr = [1,2,3,4,5]
num = int(input())
arr.append(num)
print(arr)

s