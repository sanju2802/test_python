s = "this is my book"
reverse = ""
s_list = s.split()
for word in s_list:
    word = word[::-1]
    reverse = reverse + word + " "
    
print reverse