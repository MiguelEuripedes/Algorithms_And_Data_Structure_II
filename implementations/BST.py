from node import Node

class BST:
    """
    Represents a Binary Search Tree (BST).

    Attributes:
        root (Node or None): The root node of the tree. Initializes to None for an empty tree.
    """

    def __init__(self):
        """Initializes an empty BST."""
        self.root = None

    def add(self, value):
        """
        Inserts a new value into the BST.

        Args:
            value: The value to be added to the tree.

        If the tree is empty, the value becomes the root. Otherwise, the method uses
        a recursive helper function to find the appropriate position to maintain the BST property.
        """
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_recursive(self.root, value)

    def _add_recursive(self, current_node, value):
        """
        Recursively finds the correct position and inserts a value into the BST.

        Args:
            current_node (Node): The node to start the search for the insert position from.
            value: The value to be added to the BST.

        The method determines if the new value should be placed to the left or right of
        the current node. If the target position is empty, the value is inserted.
        Otherwise, the function calls itself recursively with the respective child node.
        """
        if value <= current_node.value:
            if current_node.left_child is None:
                current_node.left_child = Node(value)
            else:
                self._add_recursive(current_node.left_child, value)
        else:
            if current_node.right_child is None:
                current_node.right_child = Node(value)
            else:
                self._add_recursive(current_node.right_child, value)

    def _contains(self, current_node, value):
        """
        Recursively checks if the BST contains the specified value starting from a given node.

        Args:
            current_node (Node): The node to start the search from.
            value: The value to search for in the BST.

        Returns:
            bool: True if the value exists in the subtree rooted at current_node, otherwise False.
        """
        if current_node is None:
            return False
        if current_node.value == value:
            return True
        if value < current_node.value:
            return self._contains(current_node.left_child, value)
        return self._contains(current_node.right_child, value)

    def contains(self, value):
        """
        Checks if the BST contains the specified value.

        Args:
            value: The value to search for in the BST.

        Returns:
            bool: True if the BST contains the value, otherwise False.
        """
        return self._contains(self.root, value)
    
    def seach_prefix_word(self, prefix):
        """
        Search for a word that starts with a given prefix.

        Args:
            prefix: The prefix to be searched.

        Output:
            list of words in the corpus that starts with the given prefix.
        """
        return self._search_prefix_word(self.root, prefix)
    
    def _search_prefix_word(self, current_node, prefix):
        """
        Search for a word that starts with a given prefix.

        Args:
            current_node (Node): The node to start the search from.
            prefix: The prefix to be searched.

        Output:
            list of words in the corpus that starts with the given prefix.
        """
        if current_node is None:
            return []
        if current_node.value.startswith(prefix):
            return [current_node.value] + self._search_prefix_word(current_node.left_child, prefix) + self._search_prefix_word(current_node.right_child, prefix)
        if prefix < current_node.value:
            return self._search_prefix_word(current_node.left_child, prefix)
        return self._search_prefix_word(current_node.right_child, prefix)
    
    def get_height(self):
        """
        Get the height of the BST.

        Returns:
            int: The height of the BST, -1 for an empty tree.
        """
        return self._get_height_recursive(self.root)

    def _get_height_recursive(self, current_node):
        """
        Recursively calculates the height of the BST.

        Args:
            current_node (Node): The current node being processed.

        Returns:
            int: The height of the subtree rooted at the current node.
        """
        if current_node is None:
            return -1  # Height of an empty tree is -1
        left_height = self._get_height_recursive(current_node.left_child)
        right_height = self._get_height_recursive(current_node.right_child)
        return max(left_height, right_height) + 1







