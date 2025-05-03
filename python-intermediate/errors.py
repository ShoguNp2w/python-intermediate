def snake_case(text):
    try:
        clean_text = text.replace(" ", "_")
        clean_text = clean_text.lower()
        #run this if error occurs
    except:
        print("snake case wants a string . pls provide the correct data type")
snake_case("use name 187")

def snake_cases(text):
    if type(text) == str:
        clean_text = text.replace(" ", '_')
        clean_text = clean_text.lower()
    else:
        raise TypeError("snake case only accepts strings. pls provide correct data type")
    snake_cases("user name 187")


