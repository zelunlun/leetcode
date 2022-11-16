    
        # _list = []
        # for slow in prices:
        #     for fast in prices:
        #         _list.append(fast - slow)
        #     prices.remove(slow)
        # return _list
# -----------------------------------------------        
#         temp = prices[0]
#         index = -1
#         dict = {}
#         for list_num in prices:
#             index += 1
#             dict[list_num] = index
#             if list_num < temp:
#                 temp = list_num
#         minmax = [x-temp for x in prices]
#         if max(minmax[dict[temp]:])<=0:return 0
#         else: return max(minmax[dict[temp]:])
# -----------------------------------------------
        
        
#         for i in range(len(prices)):
#             if prices[i] == temp:
#                 for n in range(i,len(prices)):
#                     if prices[n] - temp >= 0: return 0
#                     elif prices[n] - temp < 0: return price[n] - temp

prices = [7,1,5,3,6,4]
left = 0 #Buy
right = 1 #Sell
max_profit = []
while right < len(prices):
    currentProfit = prices[right] - prices[left] #our current Profit
    if prices[left] < prices[right]:
        max_profit.append(currentProfit)
    else:
        left = right
    right += 1
result = max(max_profit, default=0)
print(result)