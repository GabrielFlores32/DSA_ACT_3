def create_tuples(list1, list2):
    #Zipping two lists together to form tuples
    return [(list1[i], list2[i]) for i in range(len(list1))]

#Sample lists
list1 = [1, 2, 3]
list2 = ["mark", "alice", "john"]

#Print the result of the list of tuples
print("List of tuples:", create_tuples(list1, list2))