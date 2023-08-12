# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 14:43:42 2023

@author: user
"""

class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self,value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
                
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

#Inorder traversal of the Binary Tree => they will be sorted in ascending order in Binary Search Tree
def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        #Iterative solution
        ans = []
        stack = []
        curr = root
        while curr or stack:
            while curr: # go left until reach left leaf
                stack.append(curr)
                curr = curr.left
            curr = stack.pop() # go back to the one above
            ans.append(curr.val)
            curr = curr.right #check its right value append it then check left again
        return ans


my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.right.value)
print(my_tree.contains(27))
print(my_tree.contains(17))

