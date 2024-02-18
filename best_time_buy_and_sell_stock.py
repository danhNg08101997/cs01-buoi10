'''
Best time to buy and sell stock
mô tả: cho một mảng prices, mỗi phần tử của nó đại diện cho giá cổ phiếu trong một ngày. Bạn chỉ được mua cổ phiếu một lần và bán
ví dụ:
input: prices=[7,1,5,3,6,4]
output: 5
giải thích: bạn mua vào ngày thứ 2(giá 1) và bán vào ngày thứ 5 (giá 6), lãi là 6-1=5
'''
# Cách 1: 2 vòng lặp lồng nhau độ phức tạp thuật toán n^2 (n^2 là 2 vòng lặp có n phần tử chạy n^2 bước)
# def buy_and_sell_stock(lst_price):
#     max_profit = 0
#     for index_buy, price_buy in enumerate(lst_price):
#         # print(index_buy, price_buy)
#         for index_sell in range (index_buy + 1, len(lst_price)):
#             price_sell = lst_price[index_sell]
#             profit = price_sell - price_buy
#             if profit > max_profit:
#                 max_profit = profit
#     return max_profit

# Cách 2:
def buy_and_sell_stock_best_time(lst_prices):
    min_price = lst_prices[0]
    max_profit = 0
    # process
    for price in lst_prices:
        # min price
        if(price < min_price):
            min_price = price
        # lợi nhuận
        profit = price - min_price
        # lợi nhuận tối đa
        if profit > max_profit:
            max_profit = profit
    return max_profit


prices = [7,1,2,5,3,6,4]
print(buy_and_sell_stock_best_time(prices))