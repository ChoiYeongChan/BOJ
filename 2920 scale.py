import sys
a=[]
a=list(sys.stdin.readline().split())
i=0
cnt=0
if int(a[0])==1:
    while 1:
        if int(a[i+1])-int(a[i])==1:
            cnt+=1
            i+=1
        else:
            print('mixed')
            break
        if cnt==7:
            print('ascending')
            break
elif int(a[0])==8:
    while 1:
        if int(a[i])-int(a[i+1])==1:
            cnt+=1
            i+=1
        else:
            print('mixed')
            break
        if cnt==7:
            print('descending')
            break
else:
    print('mixed')