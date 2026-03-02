def calc_order_cost(*args,coupon = 0,score = 0,express = 0):
    all_price =[goods[1] * goods[2] for goods in args]
    sum_price = sum(all_price)

    # 扣减优惠券
    if sum_price >= 5000 and coupon < sum_price:
        sum_price -= coupon

    # 扣减积分
    if sum_price >= 5000 and score // 100 < sum_price:
        sum_price -= score // 100

    # 添加运费
    sum_price += express
    return sum_price


print(calc_order_cost(("张润", 188, 2), ("林忆宁", 200, 3), coupon=5, score=1000, express=9.9))