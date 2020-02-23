num =int(input())
while (not(num>=0 and num<=9)) :
    s=0
    num=3*num +1
    while (not(num>=0 and num<=9)) :
        x2=num%10
        num=num//10
        s=s+x2
    num=s+num
print(num)


