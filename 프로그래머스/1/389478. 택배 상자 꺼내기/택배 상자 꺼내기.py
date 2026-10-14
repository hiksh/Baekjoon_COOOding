def solution(n, w, num):

    index = (n-1)%w
    height = n//w
    
    if index != w-1:
        height += 1
    
    num_height = num//w
    num_index = (num-1)%w
    
    if num_index != w-1:
        num_height += 1

    if num_height%2 == 0:
        num_index = w - 1 - num_index

    if height%2 == 0:
        index = w - (index + 1)
        # print(index, num_index)
        if index > num_index:
            return height - num_height
        return height - num_height + 1
    
    # print(index,height,num_height,num_index)

    if index >= num_index:
        return height - num_height + 1
    return height - num_height
