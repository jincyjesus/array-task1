a=[10,13,15,18,20]
inp=int(input('enter digit:'))
c=0
for i in a:
    if (i==inp):
        print(c)
        break
    else:
        if(i!=inp):
            a.append(inp)
    c=c+1
