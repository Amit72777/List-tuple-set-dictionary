'''
Create a list by picking an odd-index items from the first list and even index items from
the second
                                        OR
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list
l1 and even index elements from the list l2.
'''
a  = int(input("Enter the size of  1st list :"))
l1 = [input( )  for i in range(a)]
b = int(input("Enter the size of  1st list :"))
l2 = [ input() for i in range(b)] 

l3  = [ i for i in zip(l1[1::2],l2[0::2])]
print("Final list are ",l3)
