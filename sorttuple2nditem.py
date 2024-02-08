'''
Sorted a tuple of tuple by 2nd item 
tuple1= ( ('a',23),('b',37),('c',11),('d',29))

Expected Output :-
(('c',11),('a',23),('d',29),('b',37))
'''

tuple1 = ( ('a',23),('b',37),('c',11),('d',29))

print(" Input tuple is :- " ,tuple1)

tuple2 = tuple(sorted(tuple1,key = lambda x:x[1]))  
print("\n Output tuple is :- ",tuple2)
