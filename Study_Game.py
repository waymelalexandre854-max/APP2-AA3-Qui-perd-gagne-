"""this function will study a game given by a file that doesn't have any sleeve and return the winning player or none"""
def study_game (data, tree):
    possibility = []        #list of every possibilities of number and after is used for storing the number of player on a bind
    for i in data:      #we first verify the number of possibilities that we have to verify
        if i[1] not in possibility:
            possibility.append(i[1])
    x = len(possibility)
    for i in range(x):      #this loop will first look at the lowest number possible then see if there is only one winner and show that winner, otherwise will continue. If no winner the programm give the result None
        possibility = []
        lowest_numb = lowest_search(tree)
        for i in data:
            if i[1] == lowest_numb:
                possibility.append(i)
        if len(possibility) == 1:
            return possibility[0][0]
        else:
            tree = remove_tree(tree, lowest_numb)
    return None


"""a simple function that look for the lowest number in the tree"""
def lowest_search(tree):
    if tree[1] == []:
        return tree[0]
    else:
        return lowest_search(tree[1])


"""this first function will delete a value in the BST and us delete_max to modify all the tree in a way that doesn't destroy everything"""
def remove_tree(tree, x):
    if tree == []:
        return []
    if x < tree[0]:
        tree[1] = remove_tree(tree[1], x)
    elif x > tree[0]:
        tree[2] = remove_tree(tree[2], x)
    else: 
        if tree[1] == []: 
            return tree[2]
        elif tree[2] == []: 
            return tree[1]
        else: 
            val, tree[1] = delete_max(tree[1])
            tree[0] = val
    return tree

def delete_max(tree):
    if tree[2] == []:
        return tree[0], tree[1]
    val, tree[2] = delete_max(tree[2])
    return val, tree
