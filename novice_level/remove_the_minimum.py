def remove_smallest(numbers):
    
    mutable_list = numbers.copy()
    if len(mutable_list) == 0:
        return mutable_list
    else:
        smallest = min(mutable_list)
    
    indices_smallest = []
    
    for i in mutable_list:
        if i == smallest:
            indices_smallest.append(mutable_list.index(i))
            break
        else:
            continue
    
    mutable_list.pop(indices_smallest[0])
    return mutable_list