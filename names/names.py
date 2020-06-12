import time
from binary_search_tree import BSTNode

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# O(n^2)

# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# #Create an instance of binary search
# bst = BSTNode("A")
# #Loop through names in name_1.txt

# #O(n)

# for name in names_1:
# # Each time insert name in bst    
#     bst.insert(name)
# #Loop through names in name_2.tst 

# #O(n)

# for name in names_2:
# #Check if bst contains the name
#    if bst.contains(name):
# #Add the name to duplicates
#        duplicates.append(name)


# end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
# print (f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
"""
Python has built-in tools that allow for a very efficient approach to this problem
What's the best time you can accomplish?  Thare are no restrictions on techniques or data
structures, but you may not import any additional libraries that you did not write yourself.


Say your code from names.py is to run on an embedded computer with very limited RAM. Because of this, memory is extremely constrained and you are only allowed to store names in arrays (i.e. Python lists). How would you go about optimizing the code under these conditions? Try it out and compare your solution to the original runtime. (If this solution is less efficient than your original solution, include both and label the strech solution with a comment)
"""
nam1= []
nam2 = []
for name_1 in names_1:
   nam1.append(name_1)
for name_2 in names_2:
   nam2.append(name_2) 
duplicates.extend(list(set(nam1).intersection(set(nam2))))
end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")
# Stretch solution = 0.03220939636230469 seconds and BST solution =  0.5645394325256348 seconds. Stretch solution is more efficient