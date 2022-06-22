
def merge_sort(item_list):
    # divide the list into two at the middle of the list
    # sort the items in the list
    # combine the two sorted list
    
    if len(item_list) <= 1:
        return item_list
    
    mid = len(item_list) // 2
    
    left = merge_sort(item_list[:mid])
    right = merge_sort(item_list[mid:])
    
    
    
    sorted_list = []
    i = 0
    j = 0
    
    while i < len(left) and j < len(right):
        
        if left[i] < right[j]:
            
            sorted_list.append(left[i])
            i += 1
            
        else:
            
            sorted_list.append(right[j])
            j += 1
            
    while i < len(left):
        sorted_list.append(left[i])
        i += 1
        
   
    while j < len(right):
        sorted_list.append(right[j])
        j += 1 
    
    
    return sorted_list


print(merge_sort([10, 2, 6, 4, 18, 12, 5, 13, 9]))