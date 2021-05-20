def perfectno(num):
    s=0
    for i in range(1,num-1):
        if num%i==0:
            s=s+i
    if s==num:
        print(num,"perfect number")
    else:
        print(num,"not perfect number")
num=int(input())
perfectno(num)
