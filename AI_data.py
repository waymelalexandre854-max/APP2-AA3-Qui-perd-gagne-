import random

"""this function take a number of turn played, a list of all the AI that will play those turn and can also have a modified cost and alpha (set at 50 and 5 respectively at default)"""
def AI_data_create (nb_turn, liste_AI, cost = 50, a = 5):
    data = []       #the return data that will also be used for the tree
    svalue = 25     #this value is especially used for the Separate AI
    crvalue = 0     #this value is especially used for the crescedo AI
    for i in range(nb_turn):
        for y in liste_AI:
            if y == "Bozo":
                data = Bozo(data)
            if y == "Cheater":
                data = Cheater(data)
            if y == "Joker":
                data = Joker(data)
            if y == "Separate":
                svalue, data = Separate(data, svalue)
            if y == "Undicided":
                data = Undicided(data)
            if y == "Staline":
                data = Staline(data)
            if y == "Greed":
                data = Greed(data, cost, a)
            if y == "Crescedo":
                crvalue, data = Crescedo(data, crvalue)
            if y == "First":
                data = First(data)
    tree = create_BST(data)
    return data, tree

"""the BST function we used before and the insert that come with"""
def create_BST (liste):
    tree = []
    x = 0
    for i in liste:
        if type(i[1]) == int:
            x = i[1]
            tree = insert(tree, x)
    return tree

def insert (tree, x):
    if tree == []:
        tree.append(x)
        tree.append([])
        tree.append([])
        return tree
    if x < tree[0]:
        tree[1] = insert(tree[1], x)
    if x > tree[0]:
        tree[2] = insert(tree[2], x)
    return tree

"""this AI play randomly between 0 and 70 for every turn it have"""
def Bozo(data):
    data.append(("Bozo", random.randint(0,70)))
    return data
"""this AI try to separate every action it have by at least 10 and at most 20"""
def Separate(data, value):
    signe = random.randint(0,1)
    if signe == 0:
        value -= random.randint(10,20)
    else:
        value += random.randint(10,20)
    if value < 0:
        value += 21
    if value > 70:
        value -= 21
    data.append(("Separate", value))
    return value, data
 
"""this AI choose 5 possibilities and take the lowest one"""           
def Undicided(data):
    liste = []
    x = 100
    for i in range(5):
        liste.append(random.randint(0,70))
    for i in liste:
        if i < x:
            x = i
    data.append(("Undicided", x))
    return data

"""this AI will always take the first 10 numbers for each of his turn no matter what"""
def First(data):
    data.append(("First",random.randint(0,10)))
    return data

"""this AI will look at the cost and try to pay less than a dangerous amount for his action"""
def Greed(data, cost, a):
    verif = 0.0
    good = False
    while good == False:
        x = random.randint(0,70)
        verif = cost + (a/(x+1))
        if verif <= cost+(a/10):
            good = True
    data.append(("Greed",x))
    return data

"""this AI start low and increase his bind every turn"""
def Crescedo (data, value):
    if value == 0:
        value = random.randin(1,10)
    else: 
        value += random.randint(1,5)
    data.append(("Crescedo",value))
    return value, data

"""Those AI are cheating AI that will act by looking at the data list. They aren't fair"""
"""this AI always try tobe where someone isn't and so look between a range of 0 to 70 number to see where there is a place alone"""
def Cheater(data):
    liste = [i for i in range(71)]
    for i in data:
        if i[1] in liste:
            liste.remove(i[1])
    if liste != []:
        data.append(("Cheater", random.choice(liste)))
    else:
        data.append(("Cheater", random.randint(0,70)))
    return data
        
"""this AI don't play to win, it play to make everyone lose"""
def Joker(data):
    liste = []
    for i in data:
        if i[1] not in liste:
            liste.append(i[1])
    if liste == []:
        data.append(("Joker", random.randint(0,70)))
    else:
        data.append(("Joker", random.choice(liste)))
    return data

"""this AI basically delete all other action that have the same number as his number"""
def Staline(data):
    x = random.randint(0,70)
    for i in data:
        if i[1] == x:
            data.remove(i)
    data.append(("Stalin", x))
    return data
