"""this function take the player bind and show what he will have to pay for it"""
def cost_bind(price, alpha, cost):
    return cost + (alpha/(price + 1))

"""this function look at whole game a give the seller revenue"""
def seller_revenue(data, alpha, cost):
    revenue = 0
    for i in data:
        revenue += cost + (alpha/(i[1]+1))
    return revenue

"""same as the last one but will a game with sleeve"""
def seller_revenue_sleeves(data, alpha, cost):
    revenue = 0
    for i in data:
        revenue += cost + (alpha/(i[2]+1))
    return revenue
