# list is collection of heterogeneous collection of data type 
# list is immutable but using <- assign operator u can change a list element 
# index start with 1 
# list() using to create a list 

my_list <- list("John", 25, TRUE, c(85, 90, 78))


# Print the list
print(my_list)

is.list(my_list)  # Check is list or not 


# create a list in another way 
my_list2  <- list(1:6)
is.list(my_list2)

my_list3 <- list (range(5))  # using range function create number list 
class(my_list3)

# change the item in list 
my_list[1] <- "Rohit"
print(my_list)

# add item 
#c() function to concatenate a new item to the end of an existing list.
my_list <- c(my_list , "Navneet")  # add item in last index 
my_list

#The append() function allows you to add an element to a list at a specified position.
my_list <- append(my_list,"Rahul")
my_list

my_list <- append(my_list, 'Rocky' , after =0  )  # using 'after' add item in  specific position 
length(my_list)

# remove list item 

my_list = my_list[-2]

my_list[3] <- 'ram'

my_list[3] <- 'shyam'

append(my_list, 343)


