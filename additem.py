
fruits = ['Apple ','banana','mango']
fruits.append("Pineapple")
print("Append method{}".format(fruits))

# insert method for add item in position 
fruits.insert(0,'Orange')
print("Inert method ",fruits)

# extend method add two list 
fruit2 =  ['Grapps',"Coconut"]
fruits.extend(fruit2)
print( "extend" ,fruits)

fruits+=["Gauva"]
print(fruits)
