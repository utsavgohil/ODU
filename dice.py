"""def inc(x):
    x+=1
    return x  
def dec(y):
    y-=1
    return y""" 




import random
print "start"
p= 0
q= 0
count = 0
while p<=7 or q!=0:
    num=random.randrange(1,7)
    print ("number in the dice is %d " %num)
    count=num
    if p%2==0:
        while count!=0:
            if q==7:
                p+=1
                count-=1
            elif p%2!=0:
                q-=1 
            else: 
                q+=1
                count-=1
            print(p,q)
    elif p==7:
        if num >= q:
            while num> q:
                print ("Roll the dice again")
                num=random.randrange(1,7)
            count=num
            while count!=0:
                q-=1
    elif p%2!=0:
        while count!=0:
            if q==0:
                p+=1
                count-=1
            else:
                q-=1
                count-=1
                print(p,q)
                
    