def solution(numbers):
    maximum = numbers[0]
    for i in numbers:
        if i > maximum:
            maximum = i
    
    n = len(str(maximum))+1
    
    num_list = []
    
    for i in numbers:
        j = len(str(i))
        k = str(i)*3
        num_list.append([k,str(i)])
      
    num_list.sort(reverse=True)
    
    ret = ""
    for i in num_list:
        ret += i[1]
    
    p = 0
    while True:  
        if ret[p] == "0" and p != len(ret)-1:
            p += 1
        else:
            break
    return ret[p:]