a = "sanjayansa"
b= "ans"
i=0
j=0
while(i<len(a) and j<len(b)):
    if(a[i] == b[j]):
        i+=1
        j+=1
    else:
        i+=1
        j=0
    if(j==len(b)):
        out_text = "b is substring of a"
        print "b is substring of a"
    elif(i==len(a)):
        print "b is not a substring of a"

assert out_text == "b is substring of a"