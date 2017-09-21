
#这个函数用于获得一个数除了自身的因子
def getDivisor(num):
    list=[]
    for x in range(1,num):
        if num%x==0:
            list.append(x)
    return list
