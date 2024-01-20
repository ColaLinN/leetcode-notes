# -*- coding: UTF-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin:
            return None
        root=TreeNode(pre.pop(0))
        tin_root_index=tin.index(root.val)
        # root.left=self.reConstructBinaryTree(pre[0:tin_root_index],tin[0:tin_root_index]) #方便理解1
        # root.right=self.reConstructBinaryTree(pre[tin_root_index:],tin[tin_root_index+1:]) #方便理解2
        root.left=self.reConstructBinaryTree(pre,tin[0:tin_root_index]) #先左子树，会把左子树的pre消耗完
        root.right=self.reConstructBinaryTree(pre,tin[tin_root_index+1:]) #然后就是右子树的事了
        return root
    def PreOrderTraversal_1(self,root): #前序遍历递归版
        if root==None:
            return
        print(root.val, end=" ") #前序遍历——根左右
        self.PreOrderTraversal_1(root.left)
        # print(root.val, end=" ") #中序遍历——左根右
        self.PreOrderTraversal_1(root.right)
        # print(root.val, end=" ") #后序遍历——左右根
        return
    def PreOrderTraversal_2(self,root):#非递归前序遍历
        if root==None:
            return
        stack=[]
        result=[]
        while root!=None or stack: #stack存在值为真
            while root!=None:
                # print(root.val, end=" ")
                result.append(root.val) #在此处打印
                stack.append(root)
                root=root.left
            root=(stack.pop()).right
        return result
    def InOrderTraversal(self,root): #中序遍历
        if root==None:
            return
        stack=[]
        result=[]
        while root!=None or stack: #stack存在值为真
            while root!=None:
                stack.append(root)
                root=root.left
            x=stack.pop() #在此处打印
            result.append(x.val)
            root=x.right
        return result
    def postOrderTraversal(self,root):#后序遍历 #根节点必须在右节点弹出之后，再弹出
        if root==None:
            return
        stack=[]
        result=[]
        lastVist=TreeNode(None)
        while root!=None or stack:
            while root!=None:
                stack.append(root)
                root=root.left
            node=stack[len(stack)-1]
            if node.right==None or node.right==lastVist: #如果一个节点的右节点为空，或者已访问过，就可以打印该节点
                result.append(stack.pop().val)
                lastVist=node
            else: # 否则往右边努力
                root=node.right
        return result
    def dfs(self,root,result): #深度优先遍历，递归
        if root==None:
            return
        result.append(root.val)
        self.dfs(root.left,result)
        self.dfs(root.right,result)
        return result
    def dfs_divideandconquer(self,root): #深度优先遍历，二分法
        result = []
        if root==None:
            return result
        result.append(root.val)
        result=result+self.dfs_divideandconquer(root.left)
        result=result+self.dfs_divideandconquer(root.right)
        # return +self.dfs(root.left,result)+self.dfs(root.right,result)
        return result
    def bfs(self,root,result): #广度优先
        if root==None:
            return
        queue=[root]
        while queue:
            x=queue.pop(0)
            if x!=None: # 如果不为空则可以打印，进一步添加左右子节点
                result.append(x.val)
                queue.append(x.left) # 如果要进一步优化效率，这里可以添加判断是否为空
                queue.append(x.right) # 如果要进一步优化效率，这里可以添加判断是否为空
        result_new=[] #第k个数
        for x in result:
            result_new.append(x)
        result_new.sort()
        print(result_new)
        print(result_new[2-1])
        return result
    def bfs_2(self,root): #广度优先，每层分开添加,[逆转]
        if root==None:
            return
        result=[]
        queue=[root]
        while queue:
            list_tmp=[]
            len_layer_now=len(queue)
            for i in range(len_layer_now):
                x = queue.pop(0)
                if x!=None: # 如果不为空则可以打印，进一步添加左右子节点
                    list_tmp.append(x.val)
                    queue.append(x.left) # 如果要进一步优化效率，这里可以添加判断是否为空
                    queue.append(x.right) # 如果要进一步优化效率，这里可以添加判断是否为空
            result.append(list_tmp)
        # print(result)
        result=result[-1::-1] # [逆转]，[-1::-1]等同[::-1]
        result_new=[]
        for x in result:
            result_new=result_new+x
        return result_new
    def bfs_z(self,root): #广度优先，z字形打印
        if root==None:
            return
        result=[]
        queue=[root]
        reverse_flag=False
        while queue:
            list_tmp=[]
            len_layer_now=len(queue)
            for i in range(len_layer_now):
                x = queue.pop(0)
                if x!=None: # 如果不为空则可以打印，进一步添加左右子节点
                    list_tmp.append(x.val)
                    queue.append(x.left) # 如果要进一步优化效率，这里可以添加判断是否为空
                    queue.append(x.right) # 如果要进一步优化效率，这里可以添加判断是否为空
            if reverse_flag: #z字形打印的判断
                result.append(list_tmp[-1::-1])# [逆转]，[-1::-1]等同[::-1]
            else:
                result.append(list_tmp)
            reverse_flag=not reverse_flag #每层结束都要改变方向
        # print(result)
        result_new=[]
        for x in result:
            result_new=result_new+x
        return result_new



if __name__=="__main__":
    s=Solution()
    pre=[1,2,4,7,3,5,6,8]
    tin=[4,7,2,1,5,3,8,6]
    # pre=[1,2,3]
    # tin=[2,1,3]
    root=s.reConstructBinaryTree(pre,tin) #使用前序和中序重建二叉树
    # s.PreOrderTraversal_1(root) #前序/中序/后序 遍历递归版
    # print("\n非递归前序遍历",s.PreOrderTraversal_2(root)) #非递归前序遍历
    # print("非递归中序遍历",s.InOrderTraversal(root)) #非递归中序遍历
    # print("非递归后序遍历",s.postOrderTraversal(root)) #非递归后序遍历 #根节点必须在右节点弹出之后，再弹出
    # print("深度优先遍历，递归",s.dfs(root,[])) #深度优先遍历，递归
    # print("深度优先遍历，二分法",s.dfs_divideandconquer(root)) #深度优先遍历，二分法
    print("广度优先",s.bfs(root,[]))  #广度优先
    # print("广度优先，层次遍历，自底向上",s.bfs_2(root))  #广度优先
    # print("广度优先",s.bfs_z(root))  #广度优先