num=int(input("Enter a number:10"))
num1=0
num2=1
sum=0
if num<=0:
    print("pleas enter greater than 0")
else:
    for i in range(0,num):
        print(sum, end=" ")
        num1=num2
        num2=sum
        sum=num1+num2    
