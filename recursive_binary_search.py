
items_list  = [10, 20, 5, 12, 9, 7, 14, 8, 3]

def recursive_binary_search(items_list, target):
    
    items_list.sort()
    
    if len(items_list) == 0:
        
        return False
    
    else:
        
        mid_point = len(items_list) // 2
        
        if items_list[mid_point] == target:
            
            return True
        
        else:
            
            if items_list[mid_point] > target:
                
                
                return recursive_binary_search(items_list[: mid_point], target)
                
            else:
                
                return recursive_binary_search(items_list[mid_point + 1 :], target)
                



def verify_result(item_status):
    if item_status:
        print(f"Item was found!")
    else:
        print(f"Item was not found!")


target = 100
item_status = recursive_binary_search(items_list, target)
verify_result(item_status)