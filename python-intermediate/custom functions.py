sales = [125.97, 85.32, 99.78, 154.21, 78.50, 83.67, 111.13]
average_sales = sum(sales) / len(sales)

rounded_average_sales = round(average_sales, 2)
print(rounded_average_sales)


def average(values):
    average_value = sum(values) / len(values)
    rounded_average = round(average_value, 2)

    return rounded_average

print(average(sales))

average_sale = average(sales)
print(average_sale)


def clean_string(text):
    #replace space with underscore
    no_spaces = text.replace(" ", "_")
    #make lowercase
    clean_text = no_spaces.lower()
    return clean_text

converted_text = clean_string("I Love DataCAmp")
print(converted_text)


password = "not_very_secure_2023"

def password_checker(submission):
    if password == submission:
        print("correct password")
    else:
        print("incorrect password")

password_checker("not_very_secure_2023")

