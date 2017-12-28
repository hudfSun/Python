#coding:utf-8

monthly_profit1 = [100,60,40,20,10,0]
list1 = [0.01,0.015,0.03,0.05,0.075,0.1]

monthly_profit = int(input("请输入月利率"))
b = 0
for i in range(len(monthly_profit1)):
    if monthly_profit>=monthly_profit1[i]:
        b1 = (monthly_profit-monthly_profit1[i])*list1[i]
        b = b+b1
        monthly_profit= monthly_profit1[i]
print("应发年终奖%s万元"%b)