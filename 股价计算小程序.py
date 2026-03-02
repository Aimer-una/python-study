name = "张润"
stock_price = 19.99
stock_code = "003032"
stock_price_daily_growth_factor = 1.2
growth_day = 7

message = (f"公司:{name},股票代码:{stock_code},当前股价:{stock_price_daily_growth_factor}"
           "\n每日增长系数是:%5.1f,经过%d天的增长后,股价达到了:%5.2f" %(stock_price,growth_day,(stock_price*stock_price_daily_growth_factor**growth_day)))
print(message)