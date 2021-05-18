def fib(num):
    if num==0 or num==1:
        return True
    a=0
    b=1
    count=0
    while True:
        c=a+b
        count+=1
        if c==num:
            return count+2
        if c>num:
            return False
        a=b
        b=c
num=int(input())
print(fib(num))
        
    
   
   
    
