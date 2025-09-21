from task_1.linked_list import LinkedList, Node

# 1. Reverse list
def reverse_list(head):
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev

# 2. Sorted list Merge Sort
def merge_sort(head):
    if not head or not head.next:
        return head
    
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = merge_sort(head)
    right = merge_sort(mid)
    
    return merge_two_sorted_lists(left, right)


# 3. Merge two sorted list 
def merge_two_sorted_lists(l1, l2):
    dummy = Node(0)
    tail = dummy

    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 if l1 else l2
    return dummy.next    
        
ll = LinkedList()
for x in [4, 2, 1, 3]:
    ll.append(x)

print("Original LIst:")
ll.print_list()

# Reverse
ll.head = reverse_list(ll.head)
print("Reverse List:")
ll.print_list()

# Sorted
ll.head = merge_sort(ll.head)
print("Sorted Lists:")
ll.print_list()

# Merge lists
ll2 = LinkedList()
for x in [0, 5, 6]:
    ll2.append(x)

merged_head = merge_two_sorted_lists(ll.head, ll2.head)
print("Merged Lists")
current = merged_head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")
