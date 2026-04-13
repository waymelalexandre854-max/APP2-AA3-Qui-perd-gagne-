import random

def AI_data_create (nb_round, liste_AI, cost = 50, a = 5):
    data = []
    lvalue = 25
    for i in range(nb_round):
        for y in liste_AI:
            if y == "Bozo":
                data = Bozo(data)
            if y == "Cheater":
                data = Cheater(data)
            if y == "Joker":
                data = Joker(data)
            if y == "Separate":
                lvalue, data = Separate(data, lvalue)
            if y == "Undicided":
                data = Undicided(data)
            if y == "Staline":
                data = Staline(data)
            if y == "Greed":
                data = Greed(data, cost, a)
    return data
            
def Bozo(data):
    data.append(("Bozo", random.randint(0,250)))
    return data

def Cheater(data):
    liste = [i for i in range(101)]
    for i in data:
        if i[1] in liste:
            liste.remove(i[1])
    if liste != []:
        data.append(("Cheater", random.choice(liste)))
    else:
        data.append(("Cheater", random.randint(0,250)))
        
def Joker(data):
    liste = []
    for i in data:
        if i[1] not in liste:
            liste.append(i[1])
    if liste == []:
        data.append(("Joker", random.randint(0,250)))
    else:
        data.append(("Joker", random.choice(liste)))
    return data

def Separate(data, value):
    signe = random.randint(0,1)
    if signe == 0:
        value -= random.randint(10,20)
    else:
        value += random.randint(10,20)
    if value < 0:
        value += 21
    if value > 250:
        value -= 21
    data.append(("Separate", value))
    return value, data
            
def Undicided(data):
    liste = []
    x = 250
    for i in range(5):
        liste.append(random.randint(0,250))
    for i in liste:
        if i < x:
            x = i
    data.append(("Undicided", x))
    return data

def Staline(data):
    x = random.randint(0,250)
    for i in data:
        if i[1] == x:
            data.remove(i)
    data.append(("Stalin", x))
    return data

def Greed(data, cost, a):
    verif = 0.0
    good = False
    while good == False:
        x = random.randint(0,250)
        verif = cost + (a/(x+1))
        if verif <= cost+(a/10):
            good = True
    data.append(("Greed",x))
    return data