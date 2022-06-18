
items_list  = [10, 20, 5, 12, 9, 7, 14, 8, 3]


def linear_search(items_list, target):
    
    # ilterate to the length of the items
    for i in range(0, len(items_list)):
        
        # check if target is at the current index
        if items_list[i] == target:
            
            # return the index of the target item.
            return i
    
    # return none if target is not found on the list.
    return None


def verify_result(index, target):
    if index != None:
        print(f"target is at position {index} and target is {items_list[index]} with total checks of {index + 1}")
    else:
        print(f"target {target} is not in list")

target = 21
index = linear_search(items_list, target)
verify_result(index, target)