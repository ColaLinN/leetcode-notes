# 二叉搜索树的检查

三种方法：

- 递归DFS中序遍历进行
  - 得到结果res，检查 `res.sort()==res and len(set(res))==len(res)` 
  - 保证中序结果是排好序的，并且没有重复值
- 迭代中序DFS遍历进行，在迭代中检测 `pre<current.val`
- 递归中序DFS遍历进行，如下，每次都要带入`maxV,minV` 两个参数往下走

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#用递归法
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.dfs(root,float("inf"),float("-inf"))
    def dfs(self,root,maxV,minV):
        if root==None: return True
        if root.val>=maxV or root.val<=minV:
            return False
        left=self.dfs(root.left,root.val,minV) 
        right=self.dfs(root.right,maxV,root.val)
        return left and right
```

# 二叉搜索树的插入新节点

思路：

总有一个NULL节点放新的val节点

所以只要看val与root.val的大小关系，然后选左右子树递归插入就好了

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if root==None: return TreeNode(val)
        if root.val>val: root.left=self.insertIntoBST(root.left,val)
        else: root.right=self.insertIntoBST(root.right,val)
        return root
```

# 二叉搜索树的删除节点 ⭐ 主要是分类要考虑好

[450. 删除二叉搜索树中的节点](https://leetcode-cn.com/problems/delete-node-in-a-bst/)

主要是各种情况的判断：

- root为空，直接返回root
- root节点值小于key
- root节点值大于key
- root节点值等同key
  - 右子树为空
  - 左子树为空
  - 左右子树都不为空
    - 找到右子树的最小值\最左的节点，把左子树接到右子树上
  - 都为空的情况没有考虑。。。。。。。。（但是测试例子没有这种例子）

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root==None: return root
        if root.val<key:  #root节点值小于key
            root.right=self.deleteNode(root.right,key)
        elif root.val>key: #root节点值大于key
            root.left=self.deleteNode(root.left,key)
        else: #root节点值等同key
            if root.right==None: return root.left
            elif root.left==None: return root.right
            else: #左右子树都不为空。都为空的情况没有考虑。。。。。。。。
                curNode=root.right
                while curNode.left!=None: #找到右子树的最小值
                    curNode=curNode.left
                curNode.left=root.left #把左子树接到右子树上
                root=root.right
        return root
                
```



# 检查平衡二叉树

平衡二叉树（Balanced BinaryTree）又被称为AVL树。 它具有以下性质：它是**一棵空树或它的左右两个子树的高度差的绝对值不超过1，并且左右两个子树都是一棵平衡二叉树**。

```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.compare(root)<0: return False
        else: return True
    def compare(self,root):
        if root==None: return 0
        left=self.compare(root.left)
        right=self.compare(root.right)
        if left>=0 and right>=0 and abs(left-right)<=1: # 高度差不超过1
            return max(left,right)+1
        else: 
            return -1 
```

# 二叉搜索树与双向循环链表

从小到大连起来

需要用中序遍历

```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""
class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root: return root
        stack=[]
        prev=None
        head=None
        while stack or root:
            while root:
                stack.append(root)
                root=root.left
            node=stack.pop()
            root=node.right
            if prev==None:
                head=node
                prev=head
            else:
                prev.right=node
                node.left=prev
                prev=node
        head.left=prev
        prev.right=head
        return head
            
```

