#list comprehension

arr=[]
for i in range(20):
  if i%2==1:
    arr.append(i)

brr=[i for i in range(20) if i%2==1]

[1, 3, 5, 7, 9, 11, 13, 15, 17, 19]



arr=[]
for i in range(1,10):
  arr.append(i*i)

brr=[i*i for i in range(1,10) ]

[1, 4, 9, 16, 25, 36, 49, 64, 81]



# N*M list
n=3
m=4
brr=[[0]*m for _ in range(n)]

[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]