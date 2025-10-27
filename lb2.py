'''#zad12
list1=[]
n=int(input())#number of elements in array\
product = 1
for i in range(n):
    number1 = int(input())
    list1.append(number1)
for j in range(0,len(list1)-1,2) :
    if list1[j]+list1[j+1]<=120:
        product*=list1[j]*list1[j+1]

#zad13 - number of lines of same elements
countPl = 0
i=0
while i<len(list1)-1:
    if list1[i]==list1[i+1]:
        countPl+=1
        while i<len(list1)-1 and list1[i] == list1[i + 1]:
            i+=1#skipping every similar
    i+=1

#zad14
rows=int(input())#rows
columns=int(input())#columns
matrix=[]
for i in range(rows):
    for j in range(columns):
        matrix[i][j]=int(input())
print("Elements of two-dimensional array:")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j],end=" ")
    print()

#zad15
s= 0
for i in range(rows):
    for j in range(columns):
        if i==0 or i==rows-1 or j==0 or j==columns-1:
            s+=matrix[i][j]
            '''
#zad16

rows=int(input())#rows
columns=int(input())#columns
matrix=[]
for i in range(rows):
    row=[]
    for j in range(columns):
        row.append(int(input()))
    matrix.append(row)

sums = []
diagonal=0
rowsSum=0
for j in range(rows):
    for k in range(columns):
        rowsSum+=matrix[j][k]
    sums.append(rowsSum)
limit = rows if rows < columns else columns
for i in range(0,limit,1):
    diagonal+=matrix[i][i]
sums.append(diagonal)
count = 0
for i in range(1, rows):      # i > j
    for j in range(i):
        if matrix[i][j] < i + j:
            count += 1
sums.append(count)
print("1D array:", sums)

#zad17
N = 2
M = 3

# Input 2D array
arr1 = []
for i in range(N):
    row = []
    for j in range(M):
        val = int(input(f"arr1[{i}][{j}] = "))
        row.append(val)
    arr1.append(row)

# Input x and y
x = int(input("x = "))
y = int(input("y = "))

# Count elements within [x, y]
k = 0
for i in range(N):
    for j in range(M):
        if x <= arr1[i][j] <= y:
            k += 1

# Create 1D array with elements within [x, y]
arr2 = []
for i in range(N):
    for j in range(M):
        if x <= arr1[i][j] <= y:
            arr2.append(arr1[i][j])

# Print 1D array
for i in range(len(arr2)):
    print(f"arr2[{i}] = {arr2[i]}")

#zad18
N = 2
M = 2

# Input 2D array
arr = []
for i in range(N):
    row = []
    for j in range(M):
        val = int(input(f"arr[{i}][{j}] = "))
        row.append(val)
    arr.append(row)

# Process elements
for i in range(N):
    for j in range(M):
        if j > i and arr[i][j] % 2 != 0:  # above diagonal and odd
            arr[i][j] += 1
            arr[i][i] += 1
        if i > j and arr[i][j] % 2 == 0:  # below diagonal and even
            arr[i][j] -= 1
            arr[i][i] += 1

# Print the resulting array
for i in range(N):
    for j in range(M):
        print(arr[i][j], end=" ")
    print()


#zad20
N = 2
M = 2

# Input 2D array
arr = []
for i in range(N):
    row = []
    for j in range(M):
        val = int(input(f"arr[{i}][{j}] = "))
        row.append(val)
    arr.append(row)

# Flatten 2D array to simulate pointer arithmetic
flat_arr = []
for i in range(N):
    for j in range(M):
        flat_arr.append(arr[i][j])

# Input n and access element
n = int(input("n: "))
# Accessing the (n-1)-th element in the flattened array
print(f"arr[{n}] = {flat_arr[n-1]}")

