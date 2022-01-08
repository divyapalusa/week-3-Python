#negative indexing using lists.
my_string = "giraffe"
print(my_string[-1])
print(my_string[2:4])
print(my_string[:6])
print(my_string[:])



# list negative indexing
my_list = [1,2.5,"python",True,3+4j]
print(my_list[:])
print(my_list[-1])
print(my_list[-5:-2])
print(my_list[-8:])# will print whole list
print(my_list[-2:-4])# will print empty list


# Tuple indexinf
my_tuple = ("apples","cookies","candys","icecremes")
print(my_tuple[-5:])#will print whole tuple
print(my_tuple[-3:-1])
print(my_tuple[-2:-4])# will print empty tuple