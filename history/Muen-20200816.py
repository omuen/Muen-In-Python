def menu():
    print('菜单')
    print('----')
    print('1饭')
    print('A汉堡')
    print('B薯条')
    print('C丸子')
    print('D米粥') 
    print('E三明治')
    print('F豆浆')
    print('——————')
    print('2甜点')
    print('----')
    print('A冰激淋')
    print('B可口可乐')
    print('C蛋挞')    

def meow(food):
    menu = ["汉堡","薯条","丸子","米粥","三明治","豆浆","冰激凌","可口可乐","蛋挞"];

    if food in menu:
        print("好的,你的" + food+'在那里')
    else:
        print("你要的不在菜单里哦~~~~")
        

menu()
print("-----------------")
meow("冰激凌")        
meow("冰激淋")        
meow("皮卡丘")
meow('三明治')
