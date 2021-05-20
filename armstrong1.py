def arm(num):
    n=num
    s=0
    while num:
        r=num%10
        num=num//10
        s=s+r*r*r
    if s==n:
        print(n,"armstrong number")
    else:
        print(n,"not an armstrong number")


num=int(input())
arm(num)
