def bar(drinks,quantity):
    try:
        if quantity<=0:
            print('Not known')
            return
    except :
        print('Not known')
        return

    print("This is your " + str(quantity)  + " cup " + drinks)


bar("apple juice",3)
bar("apple juice",0)
bar("apple juice",-1)
bar("apple juice","xxx")
bar("car",2)