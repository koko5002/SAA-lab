"""#heron triangle-zad1
import math

a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
p=a+b+c
S=math.sqrt(p*(p-a)*(p-b)*(p-c))
print(f"s={S:.2f}")

#three digit number sum-zad2
num= int(input("Number betweeen 100-999: "))
sumOfDigits = (num//100) + ((num//10)%10) + (num%10)
print(f"Sum of digits: {sumOfDigits}")

#changing number values using multiplication-zad3
a=int(input("a="))
b=int(input("b="))
a=a*b
b=a/b
a=a/b
print(f"a={a:.0f}")
print(f"b={b:.0f}")


#changing values using addition-zad4
a=int(input("a="))
b=int(input("b="))
a=a+b
b=a-b
a=a-b
print(f"a={a:.0f}")
print(f"b={b:.0f}")


#perimeter using sin-zad5
import math

angle_a = float(input("A = "))
angle_b = float(input("B = "))
side_c = float(input("c = "))

C = 180 - angle_a - angle_b

side_b = side_c * math.sin(math.radians(angle_b)) / math.sin(math.radians(C))
side_a = side_c * math.sin(math.radians(angle_a)) / math.sin(math.radians(C))

p = side_a + side_b + side_c

print(f"Perimeter p = {p:.2f}")

#max between 3 numbers(obviously not built-in functions allowed-6
a=int(input("a="))
b=int(input("b="))
c=int(input("c="))
maxNum=0
if a>b and a>c:
    maxNum=a
elif b>c:
    maxNum=b
else:
    maxNum=c
print(maxNum)

#if a year is leap year-7
year = int(input("year="))
if (year%4==0 and year%100!=0) or year%400==0:
    print("YES")
else:
    print("NO")

#calculating factorial-8
n=int(input("n="))
fact = 1.0
for i in range(1,n+1):
    fact=fact*i
print(f'fact={fact:.2f}')


#zad9
n=0
xN=2
while xN<=100:
    xN=2*xN+10
    n+=1
print(xN)
print(n)

#zad10-max element of array, average sum of all elements, count of odd elements and if n is in negative numbers
arrayNum = [1,-5,10,-23,15]
n=int(input("n="))
sumOfElements = 0
maxNum=0
oddCount = 0
found=False
for i in arrayNum:
    sumOfElements+=i
    if i>maxNum:
        maxNum=i#max element
    if i%2!=0 and i!=0:
        oddCount+=1
    if i<0:
        if n==i:
           found=True

averageSum = sumOfElements/len(arrayNum)#average sum of all elements
print(f"Average sum of elements: {averageSum}")
print(f"Max element: {maxNum}")
print(f"Count of odd elements: {oddCount}")
if found:
    print("Yes")
else:
    print("NO")

"""

arr = [3, -2, 4, -5, 6,7]
count = 0
for i in range(0,len(arr)-1,2):#to not have out of bounds issue
    if arr[i]*arr[i+1]<0:#if product is negative, знаците са различни
        count+=1
print(count)