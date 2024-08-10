非常好的题解

https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/dong-tai-gui-hua-she-ji-fang-fa-zhi-pai-you-xi-jia/



# 三角形入门

[三角形最小路径和](https://leetcode-cn.com/problems/triangle/)

给定一个三角形，找出自顶向下的最小路径和。每一步只能移动到下一行中相邻的结点上。

相邻的结点 在这里指的是 下标 与 上一层结点下标 相同或者等于 上一层结点下标 + 1 的两个结点	。

```python
'''方法1=深搜'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle==None: return None
        minmum=0
        l=len(triangle)-1
        def dfs(i,j,suma):
            if i==l and suma<minmum:
                minmum=suma
                return
            dfs(i+1,j,suma+triangle[i][j])
            dfs(i+1,j+1,suma+triangle[i][j])
        dfs(0,0,0)
        return minmum
'''方法2=分治法'''
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle==None: return None
        l=len(triangle)
        def dfs(i,j):
            if i==l: return 0
            return min(dfs(i+1,j),dfs(i+1,j+1))+triangle[i][j]
        return dfs(0,0)
```

动态规划，自底向上

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle==None: return None
        for i in range(len(triangle)-2,-1,-1):
            for j in range(len(triangle[i])):
                triangle[i][j]=min(triangle[i+1][j],triangle[i+1][j+1])+triangle[i][j]
        # print(triangle)
        return triangle[0][0]
```

动态规划，自顶向下（不比自底向上优雅）

- 从上往下走，算到最后一层
- 由于下面一层比上面一层大，所以需要考虑左右的边界情况
- 然后遍历最后一层，找最小值返回

```python
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if triangle==None: return None
        for i in range(1,len(triangle)):
            for j in range(len(triangle[i])):
                if j-1<0:
                    triangle[i][j]=triangle[i-1][j]+triangle[i][j]
                elif j+1>=len(triangle[i]):
                    triangle[i][j]=triangle[i-1][j-1]+triangle[i][j]
                else:
                    triangle[i][j]=min(triangle[i-1][j],triangle[i-1][j-1])+triangle[i][j]
        len_trangle=len(triangle)
        len_trangle2=len(triangle[len_trangle-1])
        res=triangle[len_trangle-1][0]
        for i in range(len_trangle2):
            res=min(res,triangle[len_trangle-1][i])
        return res
```

# 使用场景

满足两个条件

- 满足以下条件之一
  - 求最大/最小值（Maximum/Minimum ）
  - 求是否可行（Yes/No ）
  - 求可行个数（Count(*) ）
- 满足不能排序或者交换（Can not sort / swap ）

# 四个要素

- 状态：存储小规模问题的结果
- 方程：状态之间的转移计算
- 初始化：开始的状态，可以把能算的先算了
- 答案：最后的状态在哪里？

# 常见四种类型

1. Matrix DP (10%)
2. Sequence (40%)
3. Two Sequences DP (40%)
4. Backpack (10%)

# 编写时注意事项

- 可以先创建 dp[n+1] [m+1] 然后，将 dp[0] [i]  dp[i] [0]先设初值了
- 在算的时候，要做好条件
- 要注意看是什么类型的dp：矩阵、单序列、双序列、零花钱和背包？

# 1、矩阵类型（10%）

## 最小路径和

[最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/)

给定一个包含非负整数的 m x n 网格，请找出一条从左上角到右下角的路径，使得路径上的数字总和为最小。

说明：每次只能向下或者向右移动一步。

示例:

```
输入:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
输出: 7
解释: 因为路径 1→3→1→1→1 的总和最小。
```

使用动态规划

- 由于每次只能向下或者向右移动一步，所以先初始化边缘值
- 然后从第二行开始，一行行往下刷新
- 也可以从第二列开始，一行行往下刷新（都能保证某点值依赖的点都备算过）

```python
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        if n==0 or m==0: return None
        for i in range(1,n): #初始化边缘值
            grid[i][0]=grid[i][0]+grid[i-1][0]
        for j in range(1,m): #初始化边缘值
            grid[0][j]=grid[0][j]+grid[0][j-1]
        for i in range(1,n):
            for j in range(1,m):
                grid[i][j]=grid[i][j]+min(grid[i-1][j],grid[i][j-1])
        # print(grid)
        return grid[n-1][m-1]
```

## 不同路径

[不同路径](https://leetcode-cn.com/problems/unique-paths/)

一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为“Start” ）。

机器人**每次只能向下或者向右**移动一步。机器人试图达到网格的右下角（在下图中标记为“Finish”）。

问总共有多少条不同的路径？

![image-20200731163955686](A-算法-动态规划/image-20200731163955686.png)

例如，上图是一个7 x 3 的网格。有多少可能的路径？

**解题思路：**

- 初始化第一行、第一列为1，因为走到他们都只有一种走法
- 然后从第二行第二行开始遍历，每个走到这些方块的走法，由前两个方块的走法加起来

```python
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1 for j in range(m)] for i in range(n)]
        for i in range(1,n):
            for j in range(1,m):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
```

## 不同路径-ii

在上一题基础上，增加了障碍

网格中的障碍物和空位置分别用 `1` 和 `0` 来表示。

```python
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        dp=[[0 for j in range(m)] for i in range(n)]
        for i in range(0,n): #从零开始，防止[0][0]位置的1，直接堵住
            if obstacleGrid[i][0]==1: break
            dp[i][0]=1
        for j in range(0,m): #从零开始，防止[0][0]位置的1，直接堵
            if obstacleGrid[0][j]==1: break
            dp[0][j]=1
        for i in range(1,n):
            for j in range(1,m):
                if obstacleGrid[i][j]==1: dp[i][j]=0
                else: dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[n-1][m-1]
```

# 2、单序列类型（40%）

## 跳台阶

[70. 爬楼梯](https://leetcode-cn.com/problems/climbing-stairs/)

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

**注意：**给定 *n* 是一个正整数。

解：从前到后遍历计算

要注意的初值：0、1、2

```python
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2: return n
        dp=[i for i in range(n+1)]
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
```

## 跳跃游戏

[55. 跳跃游戏](https://leetcode-cn.com/problems/jump-game/)

给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个位置。

示例 1:

```python
输入: [2,3,1,1,4]
输出: true
解释: 我们可以先跳 1 步，从位置 0 到达 位置 1, 然后再从位置 1 跳 3 步到达最后一个位置。
```

解：

- 遍历每个元素
- 对于一个元素，要遍历其前面所有元素才能判断

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==0: return None
        dp=[False for i in range(n)]
        dp[0]=True
        for i in range(n):
            for j in range(0,i):
                if dp[j]==True and nums[j]+j==i:
                    dp[i]=True
        return dp[n-1]
```

但是这样这道题会超时

我们更推荐下面的做法

```python
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k=0 #能抵达的最远的距离
        for i in range(len(nums)):
            if i>k: return False #i>k就是判断k是否可以到达i
            k=max(k,nums[i]+i) #不断地找最远的距离
        return k
```

## 跳跃游戏-ii ⭐

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

```
输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
```


说明:

假设你总是可以到达数组的最后一个位置。

解法：还是用动态规划，超时了

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        lenL=len(nums)
        if lenL==0: return 1
        dp=[0 for i in range(lenL)]
        for i in range(lenL):
            dp[i]=i
            for j in range(0,i):
                if nums[j]+j>=i: #nums[j]+j越过了i坐标位置
                    dp[i]=min(dp[i],dp[j]+1) #这里要判断的是，找最小的
        # print(dp)
        return dp[lenL-1]
```

于是我们挨着跳，这叫DP？

```python
class Solution:
    def jump(self, nums: List[int]) -> int:
        ans=0
        end=0
        maxPos=0
        for i in range(len(nums)-1): #遍历
            print(i)
            maxPos=max(nums[i]+i,maxPos)#找最大的区间
            if i==end: #如果i等于end，即遍历到了小窗口区间最右边，ans加1
                end=maxPos
                ans+=1
        return ans
```

动态规划加贪心算法

```go
// v2 动态规划+贪心优化
func jump(nums []int) int {
    n:=len(nums)
    f := make([]int, n)
    f[0] = 0
    for i := 1; i < n; i++ {
        // 取第一个能跳到当前位置的点即可
        // 因为跳跃次数的结果集是单调递增的，所以贪心思路是正确的
        idx:=0
        for idx<n&&idx+nums[idx]<i{
            idx++
        }
        f[i]=f[idx]+1
    }
    return f[n-1]
}
```

## 分割回文串-ii

[分割回文串-ii](https://leetcode-cn.com/problems/word-break)

给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：

拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

```
输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
```

思路：

- 首选做初值，dp[0]=True，这样保证之后的可以好好遍历
- 最重要的是要有 `dp[j] and s[j:i] in wordDict` 这个条件的设置能力
- 然后要会计算 `maxLen` ，这个是wordDict中最长字符的长度，所以要遍历也要从 `i-maxLen` 开始（如果i-maxLen不小于零的话）

```python
class Solution: 
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s==None: return True
        dp=[False for i in range(len(s)+1)]
        dp[0]=True
        maxLen=0
        for word in wordDict:
            if len(word)>maxLen: maxLen=len(word)
        for i in range(len(s)+1):
            for j in range(max(0,i-maxLen),i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
        return dp[len(s)]
```

## 最长上升子序列

[最长上升子序列](https://leetcode-cn.com/problems/longest-increasing-subsequence/comments/)

序列类型，大同小异

要注意是这里的上升是严格上升，相同的不算上升

```python
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if nums==[]: return 0
        lenN=len(nums)
        dp=[1 for i in range(lenN)]
        for i in range(lenN):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    dp[i]=max(dp[i],dp[j]+1)
        # print()
        return max(dp)
```

# 3、应是双字符串类型（矩阵） ~双序列类型~（40%）

主要用于两个字符串的比较

两个字符串组成矩阵

## 最长公共子序列

[1143. 最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/)

和背包问题差不多，但是有些难想到

需要有动态规划的思维

```python
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        lenA=len(text1)
        lenB=len(text2)
        dp=[[0 for j in range(lenB+1)] for i in range(lenA+1)]
        for i in range(1,lenA+1):
            for j in range(1,lenB+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return dp[lenA][lenB]
```

## 编辑距离

[编辑距离](https://leetcode-cn.com/problems/edit-distance/)

给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。

你可以对一个单词进行如下三种操作：

- 插入一个字符
- 删除一个字符
- 替换一个字符

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[j for j in range(len(word2)+1)] for i in range(len(word1)+1)]
        for i in range(len(word1)+1): dp[i][0]=i
        for i in range(1,len(word1)+1):
            for j in range(1,len(word2)+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:			#word1插入   word1删除      word1替换
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                    # print(dp[i][j])
        return dp[len(word1)][len(word2)]
```

# 4、零钱与背包

## 零钱兑换 ⭐（虽说可用贪心，但要懂DP思路）

给定不同面额的硬币 coins 和一个总金额 amount。编写一个函数来计算可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回 -1。

**示例 1:**

```
输入: coins = [1, 2, 5], amount = 11
输出: 3 
解释: 11 = 5 + 5 + 1
```

主要是用一个长度为amount的dp数组来做

```python
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[amount+1 for i in range(amount+1)]
        dp[0]=0
        for i in range(amount+1):
            for j in range(len(coins)):
                if i-coins[j]>=0: #如果可以用coins[j]
                    dp[i]=min(dp[i],dp[i-coins[j]]+1)#找到满足dp[i]最少的硬币数
        if dp[amount]>amount: return -1
        return dp[amount]
```

其实直接贪心就好了，何必动态规划

- 从大到小遍历coins，能装就装，装一个ans+1
- 最后判断target等不等于0

## 0-1背包问题（能装多少） ⭐

> 在 n 个物品中挑选若干物品装入背包，最多能装多满？假设背包的大小为 m，每个物品的大小为 A[i]

主要是要做一个矩阵，n个物品作为i , 背包大小m作为j

```go
func backPack (m int, A []int) int {
    // write your code here
    // f[i][j] 前i个物品，是否能装j
    // f[i][j] =f[i-1][j] f[i-1][j-a[i] j>a[i]
    // f[0][0]=true f[...][0]=true
    // f[n][X]
    f:=make([][]bool,len(A)+1)
    for i:=0;i<=len(A);i++{
        f[i]=make([]bool,m+1)
    }
    f[0][0]=true
    for i:=1;i<=len(A);i++{
        for j:=0;j<=m;j++{
            f[i][j]=f[i-1][j]
            // 首先是判断了背包大小j是否大于当前物品大小，然后判断了减去这个物品之后的背包下一个物品是否为真
            if j-A[i-1]>=0 && f[i-1][j-A[i-1]]{ 《--重点，
                f[i][j]=true 《--重点
            }
        }
    }
    for i:=m;i>=0;i--{
        if f[len(A)][i] { //最后在最后一行可以看到最多能装多满？
            return i
        }
    }
    return 0
}
```

## 0-1背包-ii 最大价值

> 有 `n` 个物品和一个大小为 `m` 的背包. 给定数组 `A` 表示每个物品的大小和数组 `V` 表示每个物品的价值. 问最多能装入背包的总价值是多大?

思路：f[i] [j] 前 i 个物品，装入 j 背包 最大价值

做一个矩形的DP，然后

```python
def backPackII(m,A,V):
    dp=[[0 for j in range(m+1)] for i in range(len(A)+1)]    
    for i in range(1,len(A)+1):
        for j in range(1,m+1):
            dp[i][j]=dp[i-1][j]
            if j-A[i-1]>=0: 《--重点
            	dp[i][j]=max(dp[i-1][j-A[i-1]]+V[A[i-1]],dp[i-1][j]) 《--重点
    return dp[len(A)][m]
```

go的版本

```go
func backPackII (m int, A []int, V []int) int {
    // write your code here
    // f[i][j] 前i个物品，装入j背包 最大价值
    // f[i][j] =max(f[i-1][j] ,f[i-1][j-A[i]]+V[i]) 是否加入A[i]物品
    // f[0][0]=0 f[0][...]=0 f[...][0]=0
    f:=make([][]int,len(A)+1)
    for i:=0;i<len(A)+1;i++{
        f[i]=make([]int,m+1)
    }
    for i:=1;i<=len(A);i++{
        for j:=0;j<=m;j++{
            f[i][j]=f[i-1][j]
            if j-A[i-1] >= 0{
                f[i][j]=max(f[i-1][j],f[i-1][j-A[i-1]]+V[i-1])
            }
        }
    }
    return f[len(A)][m]
}
func max(a,b int)int{
    if a>b{
        return a
    }
    return b
}
```



# 5、多序列类型

## 5.1 双序列类型

```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums==None: return None
        res=float("-inf")
        maxl=nums[0]
        minl=nums[0]
        for i in range(1,len(nums)):
            if nums[i]<0:
                maxl,minl=minl,maxl
            maxl=max(maxl*nums[i],nums[i]) #不能是max(maxl*nums[i],maxl,nums[i])
            minl=min(minl*nums[i],nums[i])
            res=max(maxl,res)
        return res
```



# 6.最长回文子串

[动态规划推荐掌握](https://pic.leetcode-cn.com/1f95da43d1bdeebdd1213bb804034ddc5f906dc61451cd63f2b5ab5d0eb33b33-%E3%80%8C%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92%E3%80%8D%E9%97%AE%E9%A2%98%E6%80%9D%E8%80%83%E6%96%B9%E5%90%91.png)

```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2:return s
        maxStart=0
        maxEnd=0
        maxLen=1
        dp=[[False for j in range(len(s))] for j in range(len(s))]
        for right in range(1,len(s)):
            for left in range(right):
                if s[left]==s[right] and (left+2>=right or dp[left+1][right-1]):
                    dp[left][right]=True
                    if maxLen<right-left+1:
                        maxLen=right-left+1
                        maxStart=left
                        maxEnd=right
        return s[maxStart:maxEnd+1]
```

# 

## 剪绳子-1

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        res=[0 for i in range(n+1)]
        res[1]=1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                res[i]=max(res[i],max(j,res[j])*max(i-j,res[i-j]))
        print(res)
        return res[n]
```

## 剪绳子-2

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        opt=[0 for i in range(n+1)]
        opt[1]=1
        for i in range(2,n+1):
            for j in range(1,i//2+1):
                opt[i]=max(opt[i],max(opt[j],j)*max(opt[i-j],i-j))
        return opt[n]%1000000007
```

