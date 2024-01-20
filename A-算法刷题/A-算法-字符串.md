[几道常见的字符串算法题归纳](https://github.com/Snailclimb/JavaGuide/blob/master/docs/dataStructures-algorithms/%E5%87%A0%E9%81%93%E5%B8%B8%E8%A7%81%E7%9A%84%E5%AD%90%E7%AC%A6%E4%B8%B2%E7%AE%97%E6%B3%95%E9%A2%98.md)



# 1.KMP

[字符串的KMP算法](http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html)

[KMP](https://blog.sengxian.com/algorithms/kmp)

```python
# -*- coding: UTF-8 -*-
# KMP
def kmp_match(s, p):
    m = len(s);
    n = len(p)
    cur = 0  # 起始指针cur
    table = partial_table(p)
    while cur <= m - n:
        for i in range(n):
            if s[i + cur] != p[i]:
                cur += max(i - table[i - 1], 1)  # 有了部分匹配表,我们不只是单纯的1位1位往右移,可以一次移动多位
                break
        else:
            return True
    return False


# 部分匹配表
def partial_table(p):
    '''partial_table("ABCDABD") -> [0, 0, 0, 0, 1, 2, 0]'''
    prefix = set()
    postfix = set()
    ret = [0]
    for i in range(1, len(p)):
        prefix.add(p[:i])
        postfix = {p[j:i + 1] for j in range(1, i + 1)}
        print((prefix & postfix or {''}).pop())
        ret.append(len((prefix & postfix or {''}).pop()))
    return ret

#朴素匹配
def naive_match(s, p):
    m = len(s); n = len(p)
    for i in range(m-n+1):#起始指针i
        if s[i:i+n] == p:
            return True
    return False

print(naive_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
print(partial_table("ABCDABD"))
print(kmp_match("BBC ABCDAB ABCDABCDABDE", "ABCDABD"))
```

# 2.替换空格

暴力法

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        sr=""
        for c in s:
            if c==" ": sr+="%20"
            else: sr+=c
        return sr
```

# 3.字符串的最长公共前缀

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==0: return ""
        strs.sort()
        s=""
        for i in range(len(strs[0])):
            if i<len(strs[-1]) and strs[0][i]==strs[-1][i]:
                s+=strs[0][i]
            else: return s
        return s
```

