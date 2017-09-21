from number_modul import getDivisor

m=2
n=99999

checkList=[]

for x in range(m,n):

    if x not in checkList:

        #得到 x 的因子列表
        divisorList=getDivisor(x)
        #print(divisor) ok

        #得到 可能的亲和数
        partner=sum(divisorList)
        #print(partner) ok
        
        #每隔1000输出一次结果，方便观察程序进程
        checkList.append(partner)
        if x%1000==0:
            print ("这是 "+str(x))

        #判断是否是亲和数
        partnerDivisorList=getDivisor(partner)
        mid=sum(partnerDivisorList)
        if mid==x and partner!=x:
            print (str(x)+" 和 "+str(partner)+' 是亲和数')


#程序运行时间较长，习惯性加一行这样的代码
print('done')
