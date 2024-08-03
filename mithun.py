print("Enter a number:")
n=int(input())
f1=0
f2=1
i=1
flag=0
if n==0:
 flag=1
else:
 while(i<=n):
 f3=f1+f2
 if n==f3:
 flag=1
 break
 else:
 f1=f2
 f2=f3
 i=f3
if flag==1:
 print("Given number is in Fibonacci Series")
else:
 print("Given number is not in Fibonacci Series")
