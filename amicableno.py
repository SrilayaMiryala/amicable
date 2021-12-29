import math
def sum_of_factors(num):
    if num<=1:
        return 0
    sum=1
    sq=int(math.sqrt(num))
    for i in range(2,sq):
        if num%i==0:
            sum+=i
            if num!=(num//i):
                sum+=num//i
    return sum
n=219 #since first amicable pair is (220,284)
count=0
n1=int(input("enter no.of amicable pairs"))
while True:
    n+=1
    sof1=sum_of_factors(n)
    if sof1==n:
        continue
    elif sof1>n:
        sof2=sum_of_factors(sof1)
        if sof2==n:
            print(n,end=" ")
            print(sof1)
            count=count+1
    if count==n1:
        break

           