我们一征服赛制下的炉石传说为例，其他情况能不能使用则要具体分析。


|  双方卡组    | __刘1__ | __刘2__ |  __刘3__ |
| :---------:|:-------:| :-----: |:-----:   |
| __泽1__    |  0.5    |  0.6    |   0.4    | 
| __泽2__    |  0.7    |  0.3    |   0.5    | 
| __泽3__    |  0.3    |  0.6    |   0.5.   |

+ 当阿泽只剩下一个卡组后，它的胜率很好计算：
multiple_payoff=1-(1-pLiu1) * (1-pLiu2) * (1-pLiu3)

+ 假设有一个胜率表A

+ 这场博弈中，rps=nash.Game(pre_payoff),其中，pre_paypff（m * n）是阿泽的预收益矩阵。

+ if m>1 and n>1:<br>
     pre_payoff（ij）=Aij * 阿泽赢得收益 +（1-Aij）* 阿泽输的收益
     
     阿泽赢得收益=pre_payoff((m-1)* n)，减去的行为index为i的行<br>
     阿泽输的收益=pre_payoff(m* (n-1))，减去的列为index为i的列<br>
     
+ if m=1:<br>
     pre_payoff（1 * j)=A1 * A2 * ..... *Aj. 
     
+ if m=1:<br>
     pre_payoff（1 * j)=A1 * A2 * ..... *Aj. 
     
 （注，是否有* 是区分这是矩阵还是矩阵元素的标志。）
 
最终代码如下：

```
import nash
import numpy as np

A = np.array([[0.5,0.5],[ 0.5, 0.5]])
#A=np.array([[0.5],[0.5]])

def payoffw(A):
    rps = nash.Game(A)

    eps = rps.support_enumeration()

    for ep in eps:
        tu = ep

    shape=A.shape

    payoff_all=0
    for x in range(0,shape[0]):
        payoff_colum = 0
        for y in range(0,shape[1]):
            payoff_colum=payoff_colum+A[x][y]*tu[1][y]

        payoff_all=payoff_all+payoff_colum*tu[0][x]
    return payoff_all

payoff_all=payoffw(A)
print(payoff_all)


def multilie_payoff(A):

    shape=A.shape
    pre_payoff=np.zeros((shape[0],shape[1]))

    if shape[0]==1:
        loss_pb=1
        for j in range(0,shape[1]):
            loss_pb=loss_pb*A[0][j]
        payoff_pb=1-loss_pb
        return payoff_pb

    if shape[1] == 1:
        payoff_pb = 1
        for i in range(0, shape[0]):
            payoff_pb = payoff_pb * A[i][0]
        return payoff_pb

    if shape[0]>1 and shape[1]>1:
        pre_payoff = np.zeros((shape[0], shape[1]))

        for i in range(0,shape[0]):
            for j in range(0,shape[1]):
                pre_payoff_win=np.delete(A,i,0)
                pre_payoff_loss=np.delete(A,j,1)
                pre_payoff[i][j]=A[i][j]*multilie_payoff(pre_payoff_win)+(1-A[i][j])*multilie_payoff(pre_payoff_loss)

        return payoffw(pre_payoff)

print(multilie_payoff(A))

print('done')
```

Output:

```
0.5
0.5
done
```