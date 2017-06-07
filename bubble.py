mylist = [10, 9, 30, 31, 7, 18, 3, 1, 99, 15]

def sort_elements(numlist):
    len_list = len(numlist)
    for maxnum in range(len_list-1, 0, -1):
        for i in range(maxnum):
            if(numlist[i]>numlist[i+1]):
                temp = numlist[i]
                numlist[i] = numlist[i+1]
                numlist[i+1] = temp
    return numlist
    
print sort_elements(mylist)