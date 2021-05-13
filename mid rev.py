num=int(input())
temp=num
s=e=0
nn=0
a=0
b=0
while num:
    r=num%10
    num=num//10
    a+=1
num=temp
a=b=a-1
if num>0:
    s=num//pow(10,a)
    e=num%10
while num:
    r=num%10
    num=num//10
    if a==b:
        r=s
    elif a==0:
        r=e
    nn=nn*10+r
    a=a-1
print(nn)

