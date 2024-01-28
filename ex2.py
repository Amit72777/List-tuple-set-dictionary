# pass the string list a
# return the string whoes  capital  of the 1st element in every items 
def cap(  *args, l2 = False):
    
    if l2  == False:
        return  [ i.title() for i  in args]
    

    l2 = [ i[::-1].title() for i  in args]
    
    # l1.reverse()
    return  l2


# print(cap ('amit','sandhya','kushwaha','raju'))
print(cap("amit","sandhys",'ksuhaha','raju',  l2 =  True ))