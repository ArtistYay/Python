sales_w1 = [7,3,42,19,15,35,9] #sales w1 and w2 is how much lemonade was sold each day
sales_w2 = [12,4,26,10,7,28]
sales = [] #Made an empty list to put both week sales in
new_day = input('Enter # of lemonades for new day: ') #asking the user how much lemnade was sold today
sales_w2.append(int(new_day))  #added the # of sales to week one and turned it into and int
sales = sales_w1 + sales_w2 #added both list to one variable
sales.sort() #sorted both list from least to greatest; if you use the max and min method you don't need sort()
worst_day_pro = sales[0] * 1.5 #multiplied the least number of sales with the price of $1.5
#worst_day_pro = (min(sales)) * 1.5
best_day_pro = sales[-1] * 1.5 #multiplied the best number of sales with the price of $1.5
#best_day_pro = (max(sales)) * 1.5
print(f'Worst day: {worst_day_pro}')
print(f'Best day: {best_day_pro}')
print(f'Combined profit: {worst_day_pro + best_day_pro}')