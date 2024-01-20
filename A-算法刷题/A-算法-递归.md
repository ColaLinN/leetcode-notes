# 注意事项

## 递归深度过深出错(超出时间限制)

如果提醒递归深度过深出错

就用如下的代码更改限制

```python
class Solution: 
    @functools.lru_cache(maxsize=512)
```

## PS : 为什么要模1000000007

（跟我念，一，八个零，七）。参考https://www.liuchuo.net/archives/645

1. 大数相乘，大数的排列组合等为什么要取模

- 1000000007是一个质数（素数），对质数取余能最大程度避免结果冲突/重复
- int32位的最大值为2147483647，所以对于int32位来说1000000007足够大。
- int64位的最大值为2^63-1，用最大值模1000000007的结果求平方，不会在int64中溢出。
- 所以在大数相乘问题中，因为(a∗b)%c=((a%c)∗(b%c))%c，所以相乘时两边都对1000000007取模，再保存在int64里面不会溢出。

1. 这道题为什么要取模，取模前后的值不就变了吗？

- 确实：取模前 f(43) = 701408733, f(44) = 1134903170, f(45) = 1836311903, 但是 f(46) > 2147483647结果就溢出了。
- _____，取模后 f(43) = 701408733, f(44) = 134903163 , f(45) = 836311896, f(46) = 971215059没有溢出。
- 取模之后能够计算更多的情况，如 f(46)
- 这道题的测试答案与取模后的结果一致。
- 总结一下，这道题要模1000000007的根本原因是标准答案模了1000000007。不过大数情况下为了防止溢出，模1000000007是通用做法，原因见第一点。

# 反转字符串

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i=0
        j=len(s)-1
        while i<j:
            s[i],s[j]=s[j],s[i]
            i+=1
            j-=1
    #     result=[]
    #     self.reverse(s,result,0)
    #     print(result)
    #     s=result.copy() #这样子是不算改s的
    #     # print(s)
    # def reverse(self,s,result,index):
    #     if index==len(s): return
    #     self.reverse(s,result,index+1)
    #     result.append(s[index])

```

# 斐波那契数列

虽然简单，但是也花了时间调，主要是因为递归的时候，python中递归会超出最大的长度，需要用 `@functools.lru_cache(maxsize=512)` 来关闭限制。

**迭代型**：需要做好初值：res[0] , res[1] ，一般都需要两个初值

```python
from functools import lru_cache
class Solution:
    @functools.lru_cache(maxsize=512)
    def fib(self, n: int) -> int:
        if n<2: return n #递归型
        return (self.fib(n-1) + self.fib(n-2))%1000000007
        
        # res=[i for i in range(n+1)] #迭代型
        # for i in range(2,n+1): res[i]=(res[i-1]+res[i-2])%1000000007
        # return res[n]
```

# 跳台阶-ii

用迭代型，还是要做好两个初值：res[1]、res[2]

PS：当台阶为零时，值为1 `？？` 这个特殊情况，我们不算在两个初值中

```python
class Solution:
    def numWays(self, n: int) -> int:
        if n<=1: return 1
        res=[0 for i in range(n+1)]
        res[1]=1
        res[2]=2
        for i in range(3,n+1):
            res[i]=(res[i-1]+res[i-2])%1000000007
        # print(res)
        return res[n]

class Solution:
    @functools.lru_cache(maxsize=512)
    def numWays(self, n: int) -> int:
        if n==0: return 1
        if n<=2: return n
        return (self.numWays(n-1)+self.numWays(n-2))%1000000007

```

# 两两交换链表中的节点

[两两交换链表中的节点](https://leetcode-cn.com/problems/swap-nodes-in-pairs/submissions/)

主要要用tmp把暂时无关的节点存好

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        tmpnext=head.next.next
        tmp=head.next
        tmp.next=head
        head.next=self.swapPairs(tmpnext)
        return tmp
```



# 不同的二叉搜索树-ii

给定一个整数 *n*，生成所有由 1 ... *n* 为节点所组成的 **二叉搜索树** 。

```
示例：

输入：3
输出：
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
解释：
以上的输出对应以下 5 种不同结构的二叉搜索树：

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
```

主要是

- 遍历选取不同的根节点
- 然后递归获得左子树的根节点数组，右子树的根节点数组
- 然后创建根节点，遍历左右子树两个for循环，连上根节点，添加到list中

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n<=0: return None
        return self.helper(1,n)
    def helper(self,start,end):
        if start>end: return [TreeNode(None)] #这里要注意
        ans=[]
        for i in range(start,end+1): #从零开始遍历
            left=self.helper(start,i-1)
            right=self.helper(i+1,end)
            for leftNode in left: #遍历左节点
                for rightNode in right: #遍历右节点
                    root=TreeNode(i)
                    if leftNode.val!=None:root.left=leftNode
                    if rightNode.val!=None:root.right=rightNode
                    ans.append(root)
        return ans
```

