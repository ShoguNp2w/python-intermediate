
#arbitary argument 
def average(*values):
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

print(average(15, 29, 4, 13, 11, 8))

#calculating across multiple lists
print(average(*[15,30], *[4,14], *[11,8])) 



#arbitary arguments for keywords
def average_keywords(**value):
    average_value = sum(value.values()) / len(value.values())
    rounded_average = round(average_value, 2)
    return rounded_average

print(average_keywords(a=15,b=31,c=4,d=16,e=12,f=9))

print(average_keywords(**{"a":15,"b":35,"c":5,"d":17,"e":13,"f":10}))



def concat(*args):
    result = ""
    for arg in args:
        result += " " +arg
    return result

print(concat("python", "is", "great"))

def concat_key(**kwargs):
    result = ""
    for kwarg in kwargs.values():
        result += " " +kwarg
    return result

print(concat_key(start="python", middle= "is", end="great"))