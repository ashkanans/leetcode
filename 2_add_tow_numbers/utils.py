from list_node import ListNode


# Utility functions to assist with testing
def list_to_linked_list(values):
    """Convert a list of integers to a linked list."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(node):
    """Convert a linked list back to a list of integers."""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result
