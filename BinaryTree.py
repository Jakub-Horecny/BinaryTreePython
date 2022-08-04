from typing import Any


class Node:

    def __init__(self, data: Any, key: Any, parent: Any) -> None:
        self.data: Any = data
        self.key: Any = key
        self.parent: Node = parent
        self.left_son: Node = None
        self.right_son: Node = None

    def __del__(self) -> None:
        del self.data
        del self.key
        del self.parent
        del self.left_son
        del self.right_son


class BinaryTree:

    def __init__(self) -> None:
        """
        :rtype: None

        """
        self.root: Node = None

    def __is_root(self, node: Node) -> bool:
        """

        :rtype: bool
        :param node:
        :return:
        """
        return node.parent is None

    def __is_leaf(self, node: Node) -> bool:
        """

        :rtype: bool
        :param node:
        :return:
        """
        return (node.left_son is None) and (node.right_son is None)

    def __is_left_son(self, node: Node) -> bool:
        """

        :rtype: bool
        :param node:
        :return:
        """
        return node.parent.left_son == node

    def __is_right_son(self, node: Node) -> bool:
        """

        :rtype: bool
        :param node:
        :return:
        """
        return node.parent.right_son == node

    def __has_left_son(self, node: Node) -> bool:
        """

        :rtype: bool
        :param node:
        :return:
        """
        return node.left_son is not None

    def __has_right_son(self, node: Node) -> bool:
        """

        :rtype: bool
        :param node:
        :return:
        """
        return node.right_son is not None

    def __has_one_son(self, node: Node) -> bool:
        """

        :rtype: bool
        :param node:
        :return:
        """
        return ((self.__has_left_son(node) and not self.__has_right_son(node)) or
                (not self.__has_left_son(node) and self.__has_right_son(node)))

    def __has_two_sons(self, node: Node) -> bool:
        """

        :rtype: bool
        :param node:
        :return:
        """
        return self.__has_left_son(node) and self.__has_right_son(node)

    def is_empty(self) -> bool:
        """

        :rtype: bool
        :return:
        """
        return self.root is None

    def clean_tree(self) -> None:
        """
        :rtype: None

        """
        print()

    def in_order(self) -> list:
        """

        :rtype: list
        :return:
        """
        temp_list: list = []
        if self.root is None:
            return temp_list

        stack: list = []
        temp_node: Node = self.root
        while len(stack) > 0 or temp_node is not None:

            while temp_node is not None:
                stack.append(temp_node)
                temp_node = temp_node.left_son

            temp_node = stack.pop()
            temp_list.append(temp_node.data)
            temp_node = temp_node.right_son

        return temp_list

    def pre_order(self) -> list:
        """

        :return:
        :rtype: list
        """
        temp_list: list = []
        if self.root is None:
            return temp_list

        stack: list = []
        temp_node: Node
        stack.append(self.root)

        while len(stack) > 0:
            temp_node = stack.pop()
            temp_list.append(temp_node.data)

            if temp_node.left_son is not None:
                stack.append(temp_node.left_son)

            if temp_node.right_son is not None:
                stack.append(temp_node.right_son)

        return temp_list

    def post_order(self):
        temp_list: list = []
        if self.root is None:
            return temp_list

        stack: list = []
        temp_node: Node
        head: Node = self.root
        finished: bool

        stack.append(self.root)

        while len(stack) > 0:
            # temp_node = stack.peek()
            print()

    def level_order(self) -> list:
        """

        :rtype: list
        :return:
        """
        temp_list: list = []
        if self.root is None:
            return temp_list

        stack: list = [self.root]
        temp_list.append(self.root.data)

        temp_size: int
        temp_node: Node
        while len(stack) > 0:
            temp_size = len(stack)
            for i in range(temp_size):
                temp_node = stack.pop(len(stack) - 1)
                if temp_node.left_son is not None:
                    stack.append(temp_node.left_son)
                    temp_list.append(temp_node.left_son.data)
                if temp_node.right_son is not None:
                    stack.append(temp_node.right_son)
                    temp_list.append(temp_node.right_son.data)

        return temp_list

    def __find_interval_start(self, min_key: any, max_key: any) -> Any:
        if self.root is None:
            return None

        if min_key > max_key:
            temp: any = max_key
            max_key = min_key
            min_key = temp

        # TO DO

    def interval_search(self, min_key: any, max_key: any) -> list:
        minimal_key: any = self.__find_interval_start(min_key, max_key)
        temp_list: list = []

        if minimal_key is None:
            return temp_list

        temp_node: Node = self.__find_node(min_key)
        while temp_node is not None:
            if max_key >= temp_node.key:
                temp_list.append(temp_node.data)
            else:
                break
            temp_node = self.__find_in_order_successor(temp_node)

        return temp_list

    def __find_node(self, key: any) -> Node:
        """

        :param key:
        :return:
        :rtype: Node
        """
        if self.root is not None:
            temp_node: Node = self.root

            while temp_node is not None:
                if key == temp_node.key:
                    return temp_node
                elif key > temp_node:
                    temp_node = temp_node.right_son
                else:
                    temp_node = temp_node.left_son

        raise KeyError("Binary tree does not contain an item with a key: " + str(key))

    def __find_in_order_successor(self, node: Node) -> Node:
        """

        :rtype: Node
        :param node:
        :return:
        """
        successor: Node = None
        if self.__has_right_son(node):
            successor = node.right_son
            while self.__has_left_son(successor):
                successor = node.left_son
            return successor

        temp_node: Node = self.root
        while temp_node is not None:
            if node.key < temp_node.key:
                successor = temp_node
                temp_node = temp_node.left_son
            elif node.key > temp_node.key:
                temp_node = temp_node.right_son
            else:
                break

        return successor

    def __find_node_successor(self, node: Node) -> Node:
        """

        :rtype: Node
        :param node:
        :return:
        """
        temp_node: Node = node
        if temp_node is not Node:
            temp_node = temp_node.left_son

            while temp_node.right_son is not Node:
                temp_node = temp_node.right_son

        else:
            temp_node = temp_node.right_son
            while temp_node.left_son is not None:
                temp_node = temp_node.left_son

        return temp_node

    def min_key(self) -> Any:
        """

        :rtype: Any
        :return:
        """
        if self.root is not None:
            temp_node: Node = self.root

            while temp_node.left_son is not None:
                temp_node = temp_node.left_son

            return temp_node.key

        raise None

    def max_key(self) -> None:
        """

        :return:
        :rtype: Any
        """
        if self.root is not None:
            temp_node: Node = self.root

            while temp_node.right_son is not None:
                temp_node = temp_node.right_son

            return temp_node.key

        raise None

    def depth(self) -> int:
        """

        :return:
        """
        depth: int = 0
        if self.root is None:
            return depth

        stack: list = [self.root]
        temp_size: int
        temp_node: Node
        while len(stack) > 0:
            temp_size = len(stack)
            for i in range(temp_size):
                temp_node = stack.pop()

                if temp_node.left_son is not None:
                    stack.append(temp_node.left_son)

                if temp_node.right_son is not None:
                    stack.append(temp_node.right_son)
            depth += 1

        return depth
