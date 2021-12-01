def beeramid(bonus, price):
    Count = bonus//price
    level = 0

    while((level+1)**2 <= Count):
        level += 1
        Count -= level*level

    return level
