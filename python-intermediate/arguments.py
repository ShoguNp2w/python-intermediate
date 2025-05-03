print(round(number = 3.14168757, ndigits = 2))
help(round)


def average(values, rounded = False):
    if rounded == True:
        average_value = sum(values) / len(values)
        rounded_average = round(average_value, 2)
        return rounded_average
    else:
        average_value = sum(values) / len(values)
        return average_value
    

sales = [125.97, 85.32, 99.78, 154.21, 78.50, 83.67, 111.13]
print(average(sales, False))

print(average(sales, True))




def convert_data_structure(data, data_type = "list"):
    if data_type == "tuple":
        data = tuple(data)
    elif data_type == "set":
        data = set(data)
    else:
        data = list(data)
    return data

convert_data_structure({"a", 1, "b", 2, "c", 3}, data_type = "set")


