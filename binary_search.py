
items_list  = [10, 20, 5, 12, 9, 7, 14, 8, 3]

def binary_search(items_list, target):
    
    first_item_position = 0
    last_item_position = len(items_list) - 1
    items_list.sort()
    mid_item_position = 0
    
    while first_item_position <= last_item_position:
        
        mid_item_position = (first_item_position + last_item_position) // 2
        
        if items_list[mid_item_position] == target:
            return mid_item_position

        if items_list[mid_item_position] > target:
            last_item_position = mid_item_position - 1
            continue
        else:
            first_item_position = mid_item_position + 1
            continue
    return None  
 
            
def verify_result(index, target):
    if index != None:
        print(f"target is at position {index} and target is {items_list[index]} with total checks of {index + 1}")
    else:
        print(f"target {target} is not in list")

target = 14
index = binary_search(items_list, target)
verify_result(index, target)
    