mylist = [10, 9, 30, 31, 7, 18, 3, 1, 99, 15, 0]
len_list = len(mylist)

def sort_elements(numlist, lenArry):
    if(lenArry == 1):
        return
    
    for i in range(lenArry-1):
        if(numlist[i]>numlist[i+1]):
            temp = numlist[i]
            numlist[i] = numlist[i+1]
            numlist[i+1] = temp
    sort_elements(numlist, lenArry-1)
    return numlist
    
print sort_elements(mylist, len_list)
