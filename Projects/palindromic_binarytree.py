# @start-editable@

from collections import deque


# @end-editable@

class BinaryTree:
    class node:
        def __init__(self):
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None

    def __init__(self):
        self.sz = 0
        self.root = self.node()
        self.ht = 0

    def preorderTraverse(self, v):

        if v != None:
            print(v.element, end=" ")
            self.preorderTraverse(v.leftchild)
            self.preorderTraverse(v.rightchild)


    def postorderTraverse(self, v):
        # @start-editable@

        if v != None:
            self.postorderTraverse(v.leftchild)
            self.postorderTraverse(v.rightchild)
            print(v.element, end=" ")

    # create a tree that is a mirror image of the original tree and print its levelorder
    def mirror(self, v):
        # @start-editable@

        if v is None:
            return

        self.mirror(v.leftchild)
        self.mirror(v.rightchild)

        temp = v.leftchild
        v.leftchild = v.rightchild
        v.rightchild = temp

        # @end-editable@

    def buildTree(self, eltlist):
        nodelist = []
        nodelist.append(None)
        for i in range(len(eltlist)):
            if (i != 0):
                if (eltlist[i] != -1):
                    tempnode = self.node()
                    tempnode.element = eltlist[i]
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]
                        if (i % 2 == 0):
                            nodelist[i // 2].leftchild = tempnode
                        else:
                            nodelist[i // 2].rightchild = tempnode
                    nodelist.append(tempnode)
                else:
                    nodelist.append(None)

        self.root = nodelist[1]
        self.sz = len(nodelist)
        return nodelist

    # write a function to visualize the tree

    def printTree(self, nlist):
        for i in range(len(nlist)):
            if (nlist[i] != None):
                print(nlist[i].element, end=" ")
            else:
                print(None)

    def isEmpty(self):
        return (self.sz == 0)

    def size(self):
        return self.sz

    def IterativeInorder(self,root):
        current = root

        stack = []
        stack2 = []

        while True:
            if current is not None:
                stack.append(current)
                current = current.leftchild

            elif stack:
                current = stack.pop()
                stack2.append(current.element)

                current = current.rightchild
            else:
                break
        return stack2


    def isPalindrome(self, tree_root,tree_root2):
        self.mirror(tree_root)

        result1 = self.IterativeInorder(tree_root)
        result2 = self.IterativeInorder(tree_root2)

        self.postorderTraverse(tree_root2)
        print()
        self.preorderTraverse(tree_root)
        print()

        if len(result1) == len(result2):
            for i in range(len(result1)):
                if result1[i] != result2[i]:
                    return False

        return True



def main():
    tree = BinaryTree()
    arraySize = int(input())
    arr = list(map(int, input().split()))
    if arr[0] != -1:
        arr.insert(0,-1)
    arr2 = arr
    nlist = tree.buildTree(arr)

    nlist1 = tree.buildTree(arr2)
    output = tree.isPalindrome(nlist[1],nlist1[1])
    if output == True:
        print("Is a Palindromic Tree")
    else:
        print("Is Not a Palindromic Tree")


if __name__ == '__main__':
    main()

    #testcases:
    #[1, 2, 2, 3, -1, 3, 3]
