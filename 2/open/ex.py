with open('sales.txt', 'r', encoding='utf-8') as file:
    sales_sum = 0
    more_sum = 0
    low_sum = 0
    for line in file:
        number = int(line)
        sales_sum += number
        if number >= 0:
            more_sum += number
        else:
            low_sum += number

print("合計:", sales_sum)
print("0以上:", more_sum)
print("0より下:", low_sum)
