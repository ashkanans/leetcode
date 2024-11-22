from typing import Optional

from utils import *

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = self.listNodeToNumber(l1)
        num2 = self.listNodeToNumber(l2)

        listNode_target = self.numberToListNode(num1 + num2)
        return listNode_target

    def listNodeToNumber(self, listNode: Optional[ListNode]) -> int:

        number = ""

        while listNode:
            number += str(listNode.val)
            listNode = listNode.next


        return int(number[::-1])

    def numberToListNode(self, number: int) -> Optional[ListNode]:

        new_list_node = None
        list_node_previous = None
        number_str = str(number)
        # number_str = number_str[::-1]

        for num in number_str:
            new_list_node = ListNode(int(num), list_node_previous)
            list_node_previous = new_list_node

        return new_list_node


if __name__ == "__main__":
    # Test cases
    test_cases = [
        {"l1": [2, 4, 3], "l2": [5, 6, 4], "expected_output": [7, 0, 8]},
        {"l1": [0], "l2": [0], "expected_output": [0]},
        {"l1": [9, 9, 9, 9, 9, 9, 9], "l2": [9, 9, 9, 9], "expected_output": [8, 9, 9, 9, 0, 0, 0, 1]},
        {"l1": [1], "l2": [9, 9, 9, 9], "expected_output": [0, 0, 0, 0, 1]},
        {"l1": [9], "l2": [1], "expected_output": [0, 1]},
        {"l1": [1, 8], "l2": [0], "expected_output": [1, 8]},
        {"l1": [0], "l2": [1, 8], "expected_output": [1, 8]},
        {"l1": [9, 9, 9], "l2": [1], "expected_output": [0, 0, 0, 1]},
        {"l1": [0, 0, 1], "l2": [9, 9, 9], "expected_output": [9, 9, 0, 1]},
        {"l1": [5, 5], "l2": [5, 5], "expected_output": [0, 1, 1]},
        {"l1": [1, 0, 0, 0, 0], "l2": [9, 9, 9, 9], "expected_output": [0, 0, 0, 0, 1]},
        {"l1": [2, 4, 9], "l2": [5, 6, 4, 9], "expected_output": [7, 0, 4, 0, 1]},
        {"l1": [1, 0], "l2": [9, 9], "expected_output": [0, 0, 1]},
        {"l1": [0, 0, 0], "l2": [0, 0, 0], "expected_output": [0]},
        {"l1": [7, 8, 9], "l2": [3, 2, 1], "expected_output": [0, 1, 1, 1]}
    ]

    for i, test_case in enumerate(test_cases):
        l1 = list_to_linked_list(test_case["l1"])
        l2 = list_to_linked_list(test_case["l2"])

        solution = Solution()
        result = solution.addTwoNumbers(l1, l2)

        result_list = linked_list_to_list(result)
        assert result_list == test_case["expected_output"], (
            f"Test case {i + 1} failed: expected {test_case['expected_output']}, got {result_list}"
        )

    print("All test cases passed!")
