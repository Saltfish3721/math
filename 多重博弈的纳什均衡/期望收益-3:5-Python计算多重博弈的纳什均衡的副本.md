### 获取纳什均衡下，玩家的策略
如果你在之前的代码中尝试

```
print(eps)
print(type(eps))
```

你会得到这样的结果

```
<generator object support_enumeration.<locals>.<genexpr> at 0x103ab0410>
<class 'generator'>
```

你会发现我们无法直接使用eps中储存的结果，这就需要我们额外转化一下。


```
import nash
import numpy as np

A = np.array([[3,-2],[ -2, 1]])
rps = nash.Game(A)

eps=rps.support_enumeration()

for ep in eps:
    tu=ep
    print(tu)
    print(type(tu))

print('-----')

print(tu[1])

print(tu[1][1])
```

Output:

```
(array([ 0.375,  0.625]), array([ 0.375,  0.625]))
<class 'tuple'>
-----
[ 0.375  0.625]
0.625
```

这样，我们就可以调用eps中存储的策略了。

### 计算收益的期望值
1. 在上述问题中，如果我们想计算A的收益，我们可以这样计算：<br>
计算A以p1（p1就是tu[0][0])的概率出策略一（也就是正面，同时自然语言中的策略一是Python中的策略零），再加上A以p2的概率使用策略二。。。。（如果还有跟多的策略，直接继续相加就行了）<br>

2. 而A在计算每一个策略的收益时，还要考虑到B会以多打的概率使用B的策略一，B的策略二。。。。

到了这里。我们的思路就非常明确了。

+ 这个函数应该有三个输入
A的收益表，即上面代码中的

```
A = np.array([[3,-2],[ -2, 1]])
```

+ 依次实现上面的两段思路，返回一个数字（即收益）


最终函数如下：

```
def payoff(A,tupleA,tupleB):
    shape=A.shape
    #为了适应不同维度的博弈，我们需要使用矩阵的秩来判断每位玩家各有几种策略

    payoff_all=0
    #储存A的收益
    
    for x in range(0,shape[0]):
        payoff_colum = 0
        
        for y in range(0,shape[1]):
            payoff_colum=payoff_colum+A[x][y]*tupleB[y]
            #实现上文中的思路2

        payoff_all=payoff_all+payoff_colum*tupleA[x]
        #实现上文中的思路1
        
    return payoff_all
```

OK，我们来完整的实现计算一场博弈中，A玩家的期望收入。

```
import nash
import numpy as np

A = np.array([[-3,2],[ 2,-1]])

rps = nash.Game(A)

eps=rps.support_enumeration()

for ep in eps:
    tu=ep

def payoff(A,tupleA,tupleB):
    shape=A.shape

    payoff_all=0
    for x in range(0,shape[0]):
        payoff_colum = 0
        for y in range(0,shape[1]):
            payoff_colum=payoff_colum+A[x][y]*tupleB[y]

        payoff_all=payoff_all+payoff_colum*tupleA[x]
    return payoff_all

payoff_all=payoff(A,tu[0],tu[1])

print(payoff_all)

print('done')
```
Output

```
0.125
done
```