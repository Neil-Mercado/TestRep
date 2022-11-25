def median(num):
    num.sort()
    n=len(num)
    med=int(n/2);
    if(n%2==1):
        return num[med]
    else:
        return (num[med]+num[med+1])/2

def mean(num):
    n=len(num)
    mn=0
    for i in num:
        mn=mn+i;
    return mn/n

def mode(num):
    mod = max(set(num), key = num.count)
    return mod

num=[6,5,8,9,18,20]

print("mean=",mean(num))
print("median=",median(num))
print("mode=",mode(num))
