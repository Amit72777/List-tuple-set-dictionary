# we count the word in a string in dictionary 
def word_counter(a):
    arr = {}
    for i in a:
        arr[i] = a.count(i)
    return arr


str = word_counter(input("Enter the  stirng "))

## print the dictionary 
for i,j in str.items():
    print(f'the word is  {i} = {j}')