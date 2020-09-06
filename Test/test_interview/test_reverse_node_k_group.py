import pytest

from Interview.ReverseNodeKGroup.reverse_node_k_group import ListNode, Solution


def print_list(item: ListNode):
    result = ""
    while item:
        result += str(item.val) + " -> "
        item = item.next
    result += "None"
    print(result)


@pytest.fixture
def _obj():
    return Solution()


def test_is_successful(_obj):
    head = ListNode(5, None)
    head = ListNode(4, head)
    head = ListNode(3, head)
    head = ListNode(2, head)
    head = ListNode(1, head)
    head = _obj.reverseKGroup(head, 2)
    expected = [2, 1, 4, 3, 5]
    idx = 0
    while head:
        assert expected[idx] == head.val
        idx += 1
        head = head.next

