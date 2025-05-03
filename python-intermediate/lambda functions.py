lambda x : sum(x) / len(x)

#average using lambda
print((lambda x : sum(x) / len(x))([3,6,9]))

#storing as a variable

average = lambda x : sum(x) / len(x)
print(average([3,6,9]))

#lambda with 2 arguments
print((lambda x, y : x**y)(2,3))

names = ["john", "sally", "leah"]

#apply lambda function inside map
capitalize = map(lambda x:x.capitalize(), names)


#convert to list
print(list(capitalize))

print(capitalize)




sale_price = 29.99
add_tax = lambda x : x*1.2
print(add_tax(sale_price))

print((lambda x :x*1.2)(sale_price))


sales_prices = [29.99, 9.95, 14.50, 39.75, 60.00]
add_tax = map(lambda x:x*1.2, sales_prices)
print(list(add_tax))