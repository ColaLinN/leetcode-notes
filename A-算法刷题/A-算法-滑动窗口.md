# 模板

```go
/* 滑动窗口算法框架 */
void slidingWindow(string s, string t) {
    unordered_map<char, int> need, window;
    for (char c : t) need[c]++;

    int left = 0, right = 0;
    int valid = 0;
    while (right < s.size()) {
        // c 是将移入窗口的字符
        char c = s[right];
        // 右移窗口
        right++;
        // 进行窗口内数据的一系列更新
        ...

        /*** debug 输出的位置 ***/
        printf("window: [%d, %d)\n", left, right);
        /********************/

        // 判断左侧窗口是否要收缩
        while (window needs shrink) {
            // d 是将移出窗口的字符
            char d = s[left];
            // 左移窗口
            left++;
            // 进行窗口内数据的一系列更新
            ...
        }
    }
}
```

需要变化的地方

- 1、右指针右移之后窗口数据更新
- 2、判断窗口是否要收缩
- 3、左指针右移之后窗口数据更新
- 4、根据题意计算结果

# 最小覆盖子串

[最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)

用need收集字符

用win收集窗口内字符

用match==len(need)判断每类字符是否满足t串的需求

用win[c]==need[c]来找最小的满足窗口

用right-left<minLen来更新最小窗口

```python
import sys
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        win={}
        need={}
        for i in t: 
            if i in need: need[i]+=1
            else: need[i]=1
        left=right=0
        start=end=0 #当前匹配成功的窗口范围
        match=0 #字符匹配的次数
        minLen=sys.maxsize #最大值
        c="" #字符串
        while right<len(s):
            c=s[right]
            right+=1
            if c in need: #如果这个字符在need中
                if c in win: win[c]+=1 #win[c]加一
                else: win[c]=1
                if win[c]==need[c]: 
                    match+=1 #如果win中的这个c字符数量与need中一样，
                             #就匹配成功一个字符（超出小于都不加一）
            while match==len(need): #如果match的字符种数等同于need中字符种数
                if right-left<minLen:  #最小长度的更新
                    minLen=right-left
                    start=left
                    end=right
                c=s[left] #这是取left所指的字符
                left+=1
                if c in need: #如果当前字符属于need中，、并且退处
                    if win[c]==need[c]:  #如果当前字符的数量相同，将match减一（关闭匹配）
                        match-=1
                    win[c]-=1 #left移动了，减少当前字符，不管match减不减，这里都要过一个字符
        if minLen==sys.maxsize: return ""
        return s[start:end]
```

