help(round)

#access docstring
print(round.__doc__)

def average(values):
    #one line docstring
    """find the mean and round to 2 decimal places
    
    Args:
        values (list): a list of numeric values
    
    returns:
       rounded_average (float): mean , rounded to 2 decimal places
    
    
    
    """
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)
    return rounded_average

print(average.__doc__)

help(average)


def clean_string(text):

    """swap spaces to underscore and convert text to lowercase"""
    no_spaces = text.replace(" ", '_')
    clean_text = no_spaces.lower()
    return clean_text


print(clean_string.__doc__)



def convert_data_structure (data, data_type = "list"):
    """Convert a data structure to a list, tuple, or set.
  
  Args:
  	data (list, tuple, or set): A data structure to be converted.
    data_type (str): String representing the type of structure to convert data to.
    
  Returns:
      data (list, tuple, or set): Converted data structure"""
    
    if data_type == "tuple":
        data = tuple(data)
    elif data_type == "set":
        data = set(data)
    else:
        data = list(data)
    return data

help(convert_data_structure)