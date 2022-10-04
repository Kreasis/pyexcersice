from linked_list import LinkedList

def merge_sort(linked_list):
    """
    sorts a linked lsit in ascending order
    - recursedly divide the linked list into sublists until one remains
    
    returns a sorted linked list
    """
    
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split(linked_list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    
    return merge (left, right)
def split(linked_list):
    """
    divide the unsorted list at midpont inte sublist
    """
    
    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None
        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        
        mid_node = linked_list.node_at_index(mid-1)
        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None
        
        return left_half, right_half
def merge (left, right):
    """
    merges two linked list, sorting by data in nodes
    returns a new mergen list
    """
    #create a new linked list that contains nodes from
    # merging left and right
    merged = LinkedList()
    
    #add a fake head that is discarted later
    merged.add(0)
    
    #set current to the head of the linked list
    current = merged.head
    
    #obtain head node for the left and right linked lists
    left_head = left.head
    right_head = right.head
    
    #iterate over left and right until we reach the tail node
    #of eithe
    while left_head or right_head:
        #if the head node of left is Node we¿re past the tail
        #add the node from right to merged linked list
        if left_head is None:
            current.next_node = right_head
            #call next on rght t setp the loop condition to False
            right_head = right_head.next_node
        #if the head node of right is None we're past the tail
        #add the tail node from left to merged linked list
        elif right_head is None:
            current.next_node = left_head
            #call next on left t setp the loop condition to False
            left_head = left_head.next_node
        else:
            #not at iether tail node
            #obtain node data to peroform comparison operations
            left_data = left_head.data
            right_data = right_head.data
            #if data on left is less than right, set current to left node
            if left_data < right_data:
                current.next_node = left_head
                #move left head to next node
                left_head = left_head.next_node
            #if data on left is greater tha  right, set current to right node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        #move current to next node
        current = current.next_node
    #discar fake head and set first merged node as head
    head = merged.head.next_node
    merged.head = head
    
    return merged
l = LinkedList ()
l.add(10)
l.add(45)
l.add(36)
l.add(78)
l.add(28)
l.add(1059)
print(l)
sorted_linked_list = merge_sort(l)
print (sorted_linked_list)
