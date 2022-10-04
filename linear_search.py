def linear_search(list, target):
    """
    Returns the index position of the target is foundm else returns None
    """
    
    for i in range(0, len(list)):
        if list [i] == target:
            return i
    return None

def verify(index):
    if index is not None:
        print ("target found: ", index)
    else:
        print ("target not found")
        
number = [1,2,3,4,5,6,7,8,9,10]

result = linear_search(number, 12)
verify(result)

result = linear_search(number, 6)
verify(result)