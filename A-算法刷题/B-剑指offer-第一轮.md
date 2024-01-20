# 调整数组顺序使奇数位于偶数前面

[剑指 Offer 21. 调整数组顺序使奇数位于偶数前面](https://leetcode-cn.com/problems/diao-zheng-shu-zu-shun-xu-shi-qi-shu-wei-yu-ou-shu-qian-mian-lcof/)

使用快速排序的思路就好了，一轮快排即完成

# 顺时针打印矩阵

[剑指 Offer 29. 顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/)

要控制好top\bottom\left\right的变化

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        left,right=0,len(matrix[0])-1
        top,bottom=0,len(matrix)-1
        res=[]
        while True:
            for i in range(left,right+1): res.append(matrix[top][i]) #从左往右
            top+=1
            if bottom<top: break
            for i in range(top,bottom+1): res.append(matrix[i][right]) #从上往下
            right-=1
            if right<left: break
            for i in range(right,left-1,-1): res.append(matrix[bottom][i]) #从右往左
            bottom-=1
            if bottom<top: break
            for i in range(bottom,top-1,-1): res.append(matrix[i][left]) #从下往上
            left+=1 
            if right<left: break
        return res
```

# 数值的整数次方

[剑指 Offer 16. 数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x==0: return 0
        res=1.0
        if n<0: 
            n=-n
            x=1/x
        for i in range(32):
            if n%2==1: 
                res*=x
            x*=x
            n>>=1
        return res
```

# 栈的压入、弹出序列

[剑指 Offer 31. 栈的压入、弹出序列](https://leetcode-cn.com/problems/zhan-de-ya-ru-dan-chu-xu-lie-lcof/)

自己写的，没过，思路清晰，但是双指针，挺难设的

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i,j=0,0
        popi=0
        if popped and popped[0] in pushed:
            numIndex=pushed.index(popped[0])
            popped.pop(0)
            pushed.remove(popped[0])
            i=numIndex-1
            j=numIndex
        else: return False
        while pushed and popped:
            if  i>=0 and pushed[i]==popped[0]:
                pushed.remove(popped[0])
                popped.pop(0)
                if i!=0: i=numIndex-1
                j=i        
            elif j<len(pushed) and pushed[j]==popped[0]:
                pushed.remove(popped[0])
                popped.pop(0)
                j=j-1
            else:
                return False
        return True

```

这是大佬的写法

用个栈模拟就好了

```python
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack,i=[],0 #i作为poped数组的索引，免得pop(0)效率不高
        for num in pushed: 
            stack.append(num)
            while stack and stack[-1]==popped[i]:
                stack.pop()
                i+=1
        return not stack
```

# 



```python
class Solution:
    def strToInt(self, str: str) -> int:
        if len(str)==0: return 0
        num=0
        flag=0
        i=0
        while i<len(str) and  str[i]==" ": i+=1 #先跳过空格
        if i<len(str) and str[i]=="+":  #跳过+号
            i+=1
        elif i<len(str) and str[i]=="-":  #验证减号
            flag=1
            i+=1
        # elif i<len(str) and str[i]>="a" and str[i]<="z": return 0 #如果空格后就是字符，err
        if i<len(str) and str[i]>="0" and str[i]<="9": #如果空格、加减号后是数字
            while i<len(str) and str[i]>="0" and str[i]<="9": #遍历所有数字
                num=num*10+int(str[i])
                i+=1
            if flag==0: 
                if num<(2**31-1): return num #验证大小
                else: return (2**31-1)
            else: 
                if -num>(-2**31): return -num #验证大小
                else: return (-2**31)
        return 0
```

# 57.和为s的连续正数序列

[剑指 Offer 57 - II. 和为s的连续正数序列](https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/)

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        if target<3: return []
        res=[]
        for n in range(2,target//2+1):
            if (2*target-n*(n-1))%(2*n)==0:
                listTmp=[]
                a1=int((2*target-n*(n-1))/(2*n))
                if a1<=0: continue
                for i in range(n):
                    listTmp.append(a1)
                    a1+=1
                res.append(listTmp)
        return res[::-1] #因为越往后n越大，即连续的数越多，所以需要逆转
```

# 数据流的中位数 双堆

Python 中 heapq 模块是小顶堆。实现 大顶堆 方法： 小顶堆的插入和弹出操作均将元素 取反 即可。

Java 使用 PriorityQueue<>((x, y) -> (y - x)) 可方便实现大顶堆。

```python
from heapq import *
class MedianFinder:
    
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A=[] #小顶堆，存右边的部分
        self.B=[] #大顶堆，存左边的部分。Python 中 heapq 模块是小顶堆
                  #实现大顶堆方法：小顶堆的插入和弹出操作均将元素取反即可。

    def addNum(self, num: int) -> None:
        if len(self.A)!=len(self.B): #如果len相等，再存一个就是奇个数了，我们优先存到A中
            heappush(self.B,-heappushpop(self.A,num))
        else:
            heappush(self.A,-heappushpop(self.B,-num))

    def findMedian(self) -> float:
        #根据len是否相等，判断要怎么返回
        return self.A[0] if len(self.A)!=len(self.B) else (self.A[0]-self.B[0])/2.0



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
```

# 66. 构建乘积数组 左右分开算

[剑指 Offer 66. 构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/)

```python
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        #DP
        B=[1 for i in range(len(a))]
        tmp=1
        for i in range(len(a)): #先算左边
            B[i]=tmp
            tmp*=a[i]
        tmp=1
        for i in range(len(a)-1,-1,-1): #再算右边
            B[i]*=tmp
            tmp*=a[i]
        return B
```

# 63. 股票的最大利润

[剑指 Offer 63. 股票的最大利润](https://leetcode-cn.com/problems/gu-piao-de-zui-da-li-run-lcof/)

单序列动态规划

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #好思路，48ms
        maxV=0
        for i in range(1,len(prices)):
            maxV=max(prices[i]-prices[i-1],maxV)
            prices[i]=min(prices[i],prices[i-1])
        return maxV
        
        #暴力，80ms
        maxV=0
        right=len(prices)-1
        while right>0 and prices[right]<=prices[right-1]:
            right-=1
            continue
        for i in range(len(prices)):
            if i<=len(prices)-2 and prices[i]>=prices[i+1]:
                continue
            for j in range(i,right+1):
                if prices[i]<prices[j]:
                    maxV=max(maxV,prices[j]-prices[i])
        return maxV
```

# 62. 圆圈中最后剩下的数字 模拟法

[剑指 Offer 62. 圆圈中最后剩下的数字](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/)

模拟法

约瑟夫环

```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n<1: return n
        res=[i for i in range(n)]
        idx=0 #删除下标的基数
        while n>1:
            idx=(idx+m-1)%n #计算要下标的下标，也是下一次的基数
            del res[idx]
            n-=1
        return res[0]
```

[好的题解，讲了两种解法](https://leetcode-cn.com/problems/yuan-quan-zhong-zui-hou-sheng-xia-de-shu-zi-lcof/solution/javajie-jue-yue-se-fu-huan-wen-ti-gao-su-ni-wei-sh/)

![image-20200822202726658](B-剑指offer-第一轮/image-20200822202726658.png)

```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        #约瑟夫环
        res=0
        for i in range(2,n+1):
            res=((res+m)%i)
        return res
```

# 64. 求1+2+…+n  在不给用乘除法的时候想起移位 不给用IF、FOR时想起递归

[剑指 Offer 64. 求1+2+…+n](https://leetcode-cn.com/problems/qiu-12n-lcof/)

```python
class Solution:
    def sumNums(self, n: int) -> int:
        # return n and (n+self.sumNums(n-1)) #递归
        a=pow(n,2)+n #pow用函数
        return a>>1 #移位

```

递归可以通过短路定理来进行

python和c++的逻辑与的运行方式不一样，python的 a and b 是a为真返回b，否则返回a；c++的 a and b 无论如何都返回bool值，相当于python的bool(a and b)。目前我只发现python和javascript的逻辑运算符有这种特性

# 60. n个骰子的点数

[剑指 Offer 60. n个骰子的点数](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/)

[【n个骰子的点数】：详解动态规划及其优化方式](https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/nge-tou-zi-de-dian-shu-dong-tai-gui-hua-ji-qi-yo-3/)

这里使用了矩阵型动态规划，并且优化成了1行数组空间

主要是将轮数、点数进行遍历

```python
class Solution:
    def twoSum(self, n: int) -> List[float]:
        dp=[0 for i in range(n*6+1)]
        for i in range(1,7): 
            dp[i]=1
        for i in range(2,n+1): #轮数遍历
            for j in range(i*6,i-1,-1): #从这轮的最大值遍历到最小值
                dp[j]=0
                kbase=1
                #kbase=1 if j<=(i-1)*6 else j-(i-1)*6 #主要是跳过大于上一轮最大值的空白不遍历 
                									  #优化2
                for k in range(kbase,7): #遍历6个点数，并且试探加入
                    #if j-k>(i-1)*6: continue #如果是大于上一轮的最大值，妥妥为0，所以不管 优化1
                    if j-k>=i-1: #如果减去点数之后，坐标值大于上一轮的最小值，就计算
                        dp[j]+=dp[j-k] #2-1>=2-1
                    else: break
                    
                    
        #print(dp)

        b=float(6**n)
        for i in range(n,n*6+1):
            dp[i]=(dp[i]*1.0)/b
        #print(dp)
        return dp[n:n*6+1]
```

# 16 快速幂迭代 DNA题

[剑指 Offer 16. 数值的整数次方](https://leetcode-cn.com/problems/shu-zhi-de-zheng-shu-ci-fang-lcof/)

![image-20200824195351738](B-剑指offer-第一轮/image-20200824195351738.png)

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 迭代 快速幂
        #if x==0: return 0
        res=1
        if n<0:
            x,n=1/x,-n
        while n:
            if n&1: res*=x
            x*=x
            n>>=1
        return res

        # # 递归 快速幂
        # if n==0: return 1
        # if n==1: return x
        # if n==-1: return 1/x
        # half=self.myPow(x,n//2)
        # mod=self.myPow(x,n%2)
        # return half*half*mod
```

# 20. 表示数值的字符串

[剑指 Offer 20. 表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        state=[
            {' ':0,'s':1,'d':2,'.':4}, #0
            {'d':2,'.':4}, #1
            {' ':8,'d':2,'.':3,'e':5}, #2
            {' ':8,'d':3,'e':5}, #3
            {'d':3}, #4
            {'s':6,'d':7}, #5
            {'d':7},  #6
            {' ':8,'d':7}, #7
            {' ':8} #8
        ]
        p=0
        for c in s:
            if '0'<=c<='9': t='d'
            elif c in '+-': t='s'
            elif c in 'eE': t='e'
            elif c=='.': t='.'
            elif c==' ': t=' '
            else: t='?'
            if t not in state[p]: return False #如果不在意料中的状态就错了
            p=state[p][t]
        return p in [2,3,7,8]
```

# 43.1～n整数中1出现的次数

[剑指 Offer 43. 1～n整数中1出现的次数](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/)

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        if n<=0: return 0
        s=str(n)
        high=s[0]
        # if len
        if len(s)>1:
            last=int(s[1:])
        else:
            last=0
        pwn=10**(len(s)-1)
        # 分类
        # 当high=1时，有三部分要计算，0~999，1XXX, XXX的1
        # 当high>1时，有三部分要计算，0~999*high，pwn(10..0->19..9), XXX的1
        if high=="1":
            return self.countDigitOne(pwn-1)+1+int(last)+self.countDigitOne(last)
        else:
            return self.countDigitOne(pwn-1)*int(high)+pwn+self.countDigitOne(last)
```







# 🚗最长上升子序列

[300. 最长递增子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/)

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0: return 0
        dp=[1 for i in range(len(nums))]
        for j in range(len(nums)):
            for i in range(j):
                if nums[i]<nums[j]:
                    dp[j]=max(dp[j],dp[i]+1)
        return max(dp)
```



# 11. 盛最多水的容器 双指针

[11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/)

在左边比右边矮时，左边+1

在右边比左边矮时，右边-1

基于这个事实：矮才是原罪，不管距离有多长！

```python
class Solution:
    def maxArea(self, height: List[int]) -> int:
        if len(height)<=1: return -1
        i=0
        j=len(height)-1
        res=0
        while i<j:
            h=min(height[i],height[j])
            res=max(res,h*(j-i))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return res
```

# [15. 三数之和](https://leetcode-cn.com/problems/3sum/)

三指针问题

```python
#写的不好呀
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<=2: return []
        nums.sort()
        res=[]
        #print(nums)
        for k in range(len(nums)-2): #指针k
            if nums[k]>0: break
            elif k>0 and nums[k]==nums[k-1]: continue
            else:
                #这里出bug的原因是因为range()的k不能被我们改，这是一个迭代器的输出！！！
                # while k<len(nums) and k>0 and nums[k]==nums[k-1]: k+=1 #跳过重复的k开头计算
                i,j=k+1,len(nums)-1 #指针i、j
                while i<j:
                    tmp=nums[k]+nums[i]+nums[j]
                    #print([nums[k],nums[i],nums[j]],tmp,i,j)
                    if tmp>0 : 
                        j-=1
                        # while j>0 and nums[j]==nums[j+1]: #j>0改为i<j
                        while i<j and nums[j]==nums[j+1]: #j>0改为i<j
                            j-=1
                            #print("j-1")
                    elif tmp<0 :
                        i+=1
                        while i<j and nums[i]==nums[i-1]:
                            #print("i+1")
                            i+=1
                    else:
                        #print("=")
                        res.append([nums[k],nums[i],nums[j]])
                        i+=1
                        j-=1
                        while i<j and nums[i]==nums[i-1] : i+=1
                        while i<j and nums[j]==nums[j+1] : j-=1
        return res
                
```



# 岛屿的面积三种bfs

```python
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res=0
        dr=[[1,0],[-1,0],[0,1],[0,-1]]
        def calc(i,j): #全加入队列，出队列判断
            queue=deque()
            queue.append([i,j])
            cnt=0
            while queue:
                p=queue.popleft()
                #print(queue)
                if p[0]>-1 and p[0]<len(grid) \
                    and p[1]>-1 and p[1]<len(grid[0]) and grid[p[0]][p[1]]==1:
                    cnt+=1
                    grid[p[0]][p[1]]=0
                # Pi=p[0]
                # Pj=p[1]
                # cnt+=1
                # grid[Pi][Pj]=0
                    for i in range(4):
                        tmp=dr[i]
                        tmpi=p[0]+tmp[0]
                        tmpj=p[1]+tmp[1]
                        queue.append([tmpi,tmpj])
                    # if tmpi>=0 and tmpj>=0  and tmpi<len(grid) and tmpj<len(grid[0])  and grid[tmpi][tmpj]==1:
                    #     if [tmpi,tmpj] not in queue:
                    #         queue.append([tmpi,tmpj])
            return cnt 
            

    
    
    
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        res=0
        dr=[[1,0],[-1,0],[0,1],[0,-1]]
        def calc(i,j): #进队列时判断
            queue=deque()
            queue.append([i,j])
            cnt=0
            while queue:
                p=queue.popleft()
                Pi=p[0]
                Pj=p[1]
                cnt+=1
                grid[Pi][Pj]=0
                for i in range(4):
                    tmp=dr[i]
                    tmpi=p[0]+tmp[0]
                    tmpj=p[1]+tmp[1]
                    if tmpi>=0 and tmpj>=0  and tmpi<len(grid) and tmpj<len(grid[0])  and grid[tmpi][tmpj]==1:
                        if [tmpi,tmpj] not in queue:
                            queue.append([tmpi,tmpj])
            return cnt
 
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res=max(res,calc(i,j))
        return res

    
from collections import deque
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: #
        res=0
        def calc(i,j):
            if i<0 or i>len(grid)-1 or j<0 or j>len(grid[0])-1 or grid[i][j]!=1: return 0    
            else: 
                grid[i][j]=0
                return 1+calc(i+1,j)+calc(i-1,j)+calc(i,j+1)+calc(i,j-1)    
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    res=max(res,calc(i,j))
        return res
```



# 分类

## 动态规划

### [剑指 Offer 47. 礼物的最大价值](https://leetcode-cn.com/problems/li-wu-de-zui-da-jie-zhi-lcof/) 矩形

### [剑指 Offer 46. 把数字翻译成字符串](https://leetcode-cn.com/problems/ba-shu-zi-fan-yi-cheng-zi-fu-chuan-lcof/) 单序列

## 找规律

### [剑指 Offer 44. 数字序列中某一位的数字](https://leetcode-cn.com/problems/shu-zi-xu-lie-zhong-mou-yi-wei-de-shu-zi-lcof/)

```python
/* 数字范围    数量  位数    占多少位
    1-9        9      1       9
    10-99      90     2       180
    100-999    900    3       2700
    1000-9999  9000   4       36000  ...

    例如 2901 = 9 + 180 + 2700 + 12 即一定是4位数,第12位   n = 12;
    数据为 = 1000 + (12 -1)/ 4  = 1000 + 2 = 1002
    定位1002中的位置 = (n - 1) %  4 = 3    s.charAt(3) = 2;
*/
class Solution:
    def findNthDigit(self, n: int) -> int:
        if n<10: return n
        cnt=1
        base=9 #当前位数的字符数量
        prevnum=0 #已经跳过的数
        while n>0:
            if n-base*cnt<0:
                break
            prevnum+=base
            n=n-base*cnt
            base*=10
            cnt+=1
        prevnum+=(n-1)//cnt+1 #首先把多余的n先减一再除以cnt当前位数，再+1，其实是向上取整
        #print(prevnum,n)
        #print((n-1)%cnt)
        return int(str(prevnum)[(n-1)%cnt])
```

