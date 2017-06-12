# n
parent_child_pairs = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (21,23)]

def parents(parent_child_pairs):    
    children = {}
    
    # n
    for pair in parent_child_pairs:
        if pair[0] not in children:
            children[pair[0]] = [] 
        if pair[1] in children:
            children[pair[1]].append(pair[0])
        else:
            children[pair[1]] = [pair[0]]
    
    zerorent = []
    onerent = []
    # n
    for kids in children:
        if len(children[kids]) == 1:
            onerent.append(kids)
        if len(children[kids]) == 0:
            zerorent.append(kids)
            
    return(onerent, zerorent)
        
print(parents(parent_child_pairs))
                 
# original_list = dictionary.get('C1')
# new_list = []
# for item in original_list:
#   new_list.append(item+10)
# dictionary['C1'] = new_list
                 
                 
# 
# Your previous Plain Text content is preserved below:
# 
# Suppose we have some input data describing relationships between parents and children over multiple generations. The data is formatted as a list of (parent, child) pairs, where each individual is assigned a unique integer identifier.
# 
# parentChildPairs = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7],
#      [4, 5], [4, 8], [8, 9]];
# 
# For example, in this diagram, 3 is a child of 1 and 2, and 5 is a child of 4:
#             
# 1   2     4
#  \ /     / \
#   3     5   8
#    \   / \   \
#     \ /   \   \
#      6     7   9
# 
# 
# 
# Write a function that takes this data as input and returns two collections: one containing all individuals with zero known parents, and one containing all individuals with exactly one known parent.
# 
# Sample answer (Format does not matter):
# Zero parents: 1, 2, 4
# One parent: 5, 7, 8, 9
# 
Write a function that, for two given individuals in our dataset, returns true if and only if they share at least one known ancestor.

Sample input and output:
[5, 9] => true
[3, 8] => false
[4, 9] => false
