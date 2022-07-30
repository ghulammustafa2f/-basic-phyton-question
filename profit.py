def profit(cost,sell):
    x = sell - cost
    if x>0:
        print("profit=",x)
    elif x<0:
        print("loss=",x*(-1))
    else:
        print("no profit,no loss")


profit(50,50)           