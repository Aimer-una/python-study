

menu = """
#########购物车管理系统##########
#         1.添加购物车         #
#         2.修改购物车         #
#         3.删除购物车         #
#         4.查询购物车         #
#         5.退出购物车         #
##############################
"""
print("欢迎使用购物车管理系统")

shopping_cart = {}
while True:
    print(menu)
    choice_num = input("请选择你要进行的操作1-5:")

    match choice_num:
        case "1":
            shop_name = input("请输入商品名")
            if shop_name in shopping_cart:
                print("商品已经存在")
            else:
                shop_price = float(input("请输入商品价格"))
                shop_goods = int(input("请输入商品数量"))
                shopping_cart[shop_name] = {"商品价格":shop_price,"商品数量":shop_goods}
                print("商品添加完毕")
        case "2":
            shop_name = input("请输入要修改的商品名")
            if shop_name not in shopping_cart:
                print("您输入的商品不存在")
            else:
                shop_price = float(input("请输入要修改的商品价格"))
                shop_goods = int(input("请输入要修改的商品数量"))
                shopping_cart[shop_name] = {"商品价格": shop_price, "商品数量": shop_goods}
                print("商品修改完毕")
        case "3":
            shop_name = input("请输入要删除的商品名")
            if shop_name not in shopping_cart:
                print("要删除的商品不存在")
            else:
                del shopping_cart[shop_name]
        case "4":
            for goods_name in shopping_cart.keys():
                goods_info = shopping_cart[goods_name]
                print(f"商品名称{goods_name},商品价格:{goods_info['商品价格']},商品数量:{goods_info['商品价格']}")
        case "5":
            print("退出成功")
            break
        case _:
            print("非法操作不支持")
