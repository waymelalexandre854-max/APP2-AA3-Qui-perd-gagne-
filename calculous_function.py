def cost_bind(price, alpha, cost):
    return cost + (alpha/(price + 1))

def seller_revenue(data, alpha, cost):
    revenue = 0
    for i in data:
        revenue += cost + (alpha/(i[1]+1))
    return revenue
