# 记账程序

records=[]


def search():
    print("\n当前记录：\n")
    for row in records:
        print("------------------------")
        print("  用途：" + row["memo"])
        print("  金额：" + row["cost"])
    print("------------------------")
    print("\n")

def new_record():
    row= {}
    row["memo"] = input("用途：")
    row["cost"] = input("金额：")
    records.append(row)
    print("添加成功！！！\n")

def menu():
    while True:
        a=input(" 记账程序  By Muen \n  1.查询/Search\n  2.新建/New\n  x.退出/Exit\n请选择：")
        if a=="x":
            print("\n欢迎您下次使用\n")
            break
        elif a=="1":
            search()
        elif a=="2":
            new_record()
        else:
            print("\n我不知道你选的是那个\n")
            print("")

menu()
