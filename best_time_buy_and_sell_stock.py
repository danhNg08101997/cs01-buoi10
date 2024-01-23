'''
Best time to buy and sell stock
mô tả: cho một mảng prices, mỗi phần tử của nó đại diện cho giá cổ phiếu trong một ngày. Bạn chỉ được mua cổ phiếu một lần và bán
ví dụ:
input: prices=[7,1,5,3,6,4]
output: 5
giải thích: bạn mua vào ngày thứ 2(giá 1) và bán vào ngày thứ 5 (giá 6), lãi là 6-1=5
'''

def buy_and_sell_stock(lst_price):
    max_profit = 0
    for index_buy, price_buy in enumerate(lst_price):
        print(index_buy, price_buy)
        for index_sell in range (index_buy + 1, len(lst_price)):
            profit = lst_price[index_sell] - price_buy
            if profit>max_profit:
                max_profit = profit
    return max_profit
prices = [7,1,2,5,3,6,4]
print(buy_and_sell_stock(prices))