class BTNode(object):
    """A node in a binary tree."""

    def __init__(self, value, left=None, right=None):
        """(BTNode, int, BTNode, BTNode) -> NoneType
        Initialize this node to store value and have children left and right,
        as well as depth 0.
        """
        self.value = value
        self.left = left
        self.right = right
        self.d = 0

    def __str__(self):
        return self._str_helper("")

    def _str_helper(self, indentation=""):
        """(BTNode, str) -> str
        Return a "sideways" representation of the subtree rooted at this node,
        with right subtrees above parents above left subtrees and each node on
        its own line, preceded by as many TAB characters as the node's depth.
        """
        ret = ""

        if (self.right is not None):
            ret += self.right._str_helper(indentation + "\t") + "\n"
        ret += indentation + str(self.value) + "\n"
        if (self.left is not None):
            ret += self.left._str_helper(indentation + "\t") + "\n"
        return ret

    def set_depth(self, dep):
        if self.left is None and self.right is None:
            self.d = dep
        else:
            self.d = dep
            dep += 1
            if self.left is not None:
                self.left.set_depth(dep)
            if self.right is not None:
                self.right.set_depth(dep)

    def leaves_and_internals(self, result=None, depth=0):
        if result is None:
            result = (set(), set())
        if self.left is None and self.right is None:
            if depth != 0:
                result[0].add(self.value)
        else:
            if depth != 0:
                result[1].add(self.value)
            depth += 1
            if self.left is not None:
                result = self.left.leaves_and_internals(result, depth)
            if self.right is not None:
                result = self.right.leaves_and_internals(result, depth)
        return result

    def sum_to_deepest(self):
        dic = self.sum_to_deepest_helper(None, 0, 0)
        max_key = max(dic.keys())
        result = dic[max_key]
        return result

    def sum_to_deepest_helper(self, result, depth, total):
        if result is None:
            result = {}
        if self.left is None and self.right is None:
            total = total + self.value
            if depth in result:
                if result[depth] < total:
                    result[depth] = total
            else:
                result[depth] = total
        else:
            depth += 1
            total += self.value
            if self.left is not None:
                result = self.left.sum_to_deepest_helper(result, depth, total)
            if self.right is not None:
                result = self.right.sum_to_deepest_helper(result, depth, total)
        return result
