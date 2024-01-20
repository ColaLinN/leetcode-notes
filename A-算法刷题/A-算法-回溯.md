https://leetcode-cn.com/problems/subsets/solution/hui-su-suan-fa-by-powcai-5/

上面的题解中，有个题解很有意思，讲了很多回溯的通用类似题

今天：回溯、DP

明天：堆栈、

# 模板

```python
result=[]
listTmp=[] #用于
def backtrace(选择列表，路径):
    if 满足结束条件:
        result.append(路径)
        return
    for i in 选择列表:
        路径.append(i) #做选择
        bcaktree(选择列表，路径) #下一轮回溯
        路径.pop() #撤销选择
```

如果需要全排列，我们需要用visited解决

```python

        visited={} #哈希字典，检测是否visited
    def backtrace(self,nums,result,listTmp,visited):
        if len(listTmp)==len(nums):
            result.append(路径)
            return
        for i in nums:
            ---------------
            if visited.get(i): #可以这样get检测，如果没有就返回None。也可以用 i in dict来判断
            # if i in visited:                
                continue
            ---------------
            listTmp.append(i)
            visited[i]=True
            self.backtrace(nums,result,listTmp,visited)
            ---------------
            visited[i]=False #如果上面用 i in dict来判断，这里就要改成dict.pop(i)
            # visited.pop(i)
            ---------------
            listTmp.pop()
            
```

如果要给的nums有重复元素，要求返回时没有重复的元素

我们需要先sort排列。

然后跳过重复的数；或者直接检测在不在result中（效率可能低）

遇事不决，就用 `in`

```python
        nums.sort() #需要排序
        ------------------
        if listTmp not in result:  #方法1，直接检测在不在result中。
            result.append(copy.copy(listTmp)) #方法1
        ------------------
        for i in range(pos,len(nums)): 
            if i!=pos and nums[i]==nums[i-1]: #方法2，跳过相同的数
                continue   方法2
```



# 求子集——用position、不用字典记录

给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        listTmp=[]
        self.backtrace(nums,0,listTmp,result)
        return result
    def backtrace(self,nums,pos,listTmp,result):
        result.append(copy.copy(listTmp))
        for i in range(pos,len(nums)):
            listTmp.append(nums[i])
            self.backtrace(nums,i+1,listTmp,result)
            listTmp.pop()
        return
```

# 求子集-ii 去重复——用pos、不用字典

重点是在上一个的基础上

- 对nums排序
- 或检测是否存在于result，或跳过相同的数（开销可能小）

```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result=[]
        listTmp=[]
        nums.sort() #需要排序
        self.backtrace(nums,0,result,listTmp)
        return result
    def backtrace(self,nums,pos,result,lista):
        # if listTmp not in result:  #方法1，直接检测在不在result中
        #    result.append(copy.copy(listTmp)) #方法1

        result.append(copy.copy(listTmp))  #方法2
        for i in range(pos,len(nums)):
            if i!=pos and nums[i]==nums[i-1]: #方法2，跳过相同的数
                continue 
            listTmp.append(nums[i])
            self.backtrace(nums,i+1,result,listTmp)
            listTmp.pop()
```

# 



# 求全排列——字典判断、不用pos（forall）

可以用数组就不要用字典了，性能不好

主要是要有一个 `visited` 数组\哈希字典 来保存已经加入的数，然后大胆遍历就好了

```python
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result=[]
        listTmp=[]
        visited={} #哈希字典，检测是否visited
        self.backtrace(nums,result,listTmp,visited)
        return result
        
    def backtrace(self,nums,result,listTmp,visited):
        if len(listTmp)==len(nums): #长度相等就返回
            result.append(copy.copy(listTmp))
            return
        for i in nums:
            if visited.get(i): #可以这样get检测，如果没有就返回None。也可以用 i in dict来判断
            # if i in visited:                
                continue
            listTmp.append(i)
            visited[i]=True
            self.backtrace(nums,result,listTmp,visited)
            visited[i]=False #如果上面用 i in dict来判断，这里就要改成dict.pop(i)
            # visited.pop(i)
            listTmp.pop()
            
```

# 求全排列-ii 去重复——sort()之后判断nums[i-1]==nums[i]，注意判重的手法(只能用重复的一组)

[全排列-ii](https://leetcode-cn.com/problems/permutations-ii/)

给定一个可包含重复数字的序列，返回所有不重复的全排列。

示例:

```
输入: [1,1,2]
输出:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
```

- 方法1，加上 and listTmp not in result
- 方法2，当上一个元素和当前元素相同，而上一个元素未visited，
  - 当上一个元素和当前元素相同，而上一个元素未visited，（剪枝）
    说明上一个元素已经作为当前位置遍历过了
    当前的元素不能选择了，会引发冲突
    因为上个元素已经选了它产生了结果了，现在又选就会产生冲突

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result=[]
        listTmp=[]
        visited=[False for i in range(len(nums))]
        nums.sort() #排序
        self.backtrace(nums,result,listTmp,visited)
        return result

    def backtrace(self,nums,result,listTmp,visited):
        if len(listTmp)==len(nums): #方法1，这里加上 and listTmp not in result
            result.append(copy.copy(listTmp))
            return
        for i in range(len(nums)):
            if visited[i]:
                continue
            if i!=0 and nums[i]==nums[i-1] and visited[i-1]==False:#方法2，当上一个元素和当前元素相同，而上一个元素未visited，说明已经添加过这个元素了，跳过
                continue
            visited[i]=True
            listTmp.append(nums[i])
            self.backtrace(nums,result,listTmp,visited)
            listTmp.pop()
            visited[i]=False
```

# 剑指-全排列字符串

下面是我写的思路比较清晰的 `visited` 回溯写法

由于字符串不能排序，所以只能用 `listTmp not in result` 来判断，明显效率低了很多。

最后 **47 / 52** 个通过测试用例 ，就超时了，所以还是借鉴网上老哥的清爽写法吧。

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        if not s: return []
        result=[]
        listTmp=""
        visited=[False for i in range(len(s))]
        self.backtrace(s,result,listTmp,visited)
        return result
    
    def backtrace(self,s,result,listTmp,visited):
        if len(listTmp)==len(s) and listTmp not in result:
            result.append(copy.copy(listTmp))
            return
        for i in range(len(s)):
            if visited[i]: 
                continue
            visited[i]=True
            listTmp+=s[i]
            self.backtrace(s,result,listTmp,visited)
            listTmp=listTmp[:-1]
            visited[i]=False
```

这个 `DFS` 有剪枝，所以时间复杂度还过的过去

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        result,c=[],list(s)
        def dfs(x): #遍历第x位的固定
            if x==len(c)-1: #如果遍历到倒数第二位，最后一位其实也固定了
                result.append("".join(c)) 
            # setA=set()
            setA=dict()
            for i in range(x,len(c)):
                if c[i] in setA: continue #如果值已经固定过了，剪枝
                setA[c[i]]=1 #添加
                c[i],c[x]=c[x],c[i] #把i的值固定到第x位上
                dfs(x+1) #遍历下一位
                c[i],c[x]=c[x],c[i] #换回
        dfs(0)
        return result
```

# 

# 组合怎么求？

# 组合总和——需要pos、还有余数

[组合总和](https://leetcode-cn.com/problems/combination-sum/)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 

示例 1：

```
输入：candidates = [2,3,6,7], target = 7,
所求解集为：
[
  [7],
  [2,2,3]
]
```


示例 2：

```
输入：candidates = [2,3,5], target = 8,
所求解集为：
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```



代码如下

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        size=len(candidates)
        if size==0: return []        
        # result=listTmp=[] #这是不能的，引用一样了！！！
        result=[]
        listTmp=[]
        candidates.sort()
        def dfs(target,listTmp,begin):
            if target==0:
                result.append(listTmp.copy()) #listTmp[:] == copy.copy(listTmp)
                return
            for index in range(begin, size):
                residue=target-candidates[index] #计算余数
                if residue<0: break # 剪枝，不必递归到下一层，并且后面的分支也不必执行。因为后面的指定会大于当前的值，没必要计算了
                listTmp.append(candidates[index]) 
                dfs(residue,listTmp,index) # 因为下一层不能比上一层还小，起始索引还从 index 开始防止出现重复的答案
                listTmp.pop()
        dfs(target,listTmp,0)
        return result
```





# [剑指 Offer 17. 打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)