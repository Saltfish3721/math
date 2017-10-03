首先，安装一个Python第三方库[nashpy](https://github.com/drvinceknight/Nashpy)<br>

在命令行输入下列指令，即可安装nashpy库<br>

```
$ pip install nashpy
```
对于前言中出现的赌局，我们可以得到这样的策略表。（数字为A的期望收入）

|  双方卡组    | __B正__ | __B反__ | 
| :---------:|:-------:| :-----: |
| __A正__    |  -3    |  2    | 
| __A反__    |  2    |  -1    | 

```
import nash
import numpy as np

A = np.array([[3,-2],[ -2, 1]])
#如果你只输入一个矩阵，系统默认这是零和博弈,另一位玩家的收益矩阵自动被设定为 B=-A

rps = nash.Game(A)
#rps代表这场博弈
print(rps)
print('-------')

print('玩家的策略为：')
eps=rps.support_enumeration()
#这个方法是nashpy中提供的用于计算双方策略的函数
print(list(eps))
print('-------')

print('done')
```
结果如下：

```
Zero sum game with payoff matrices:

Row player:
[[ 3 -2]
 [-2  1]]

Column player:
[[-3  2]
 [ 2 -1]]
-------
玩家的策略为：
[(array([ 0.375,  0.625]), array([ 0.375,  0.625]))]
-------
done
```
（默认前者为Row player的策略，后者为Column player的策略）<br>
我们可以看到，结果和我们前面手工计算的是一致的。

遗憾的是，nashpy并没有提供计算玩家期望收益的函数（unbelievable），我们在下一节中自己写方法吧。

