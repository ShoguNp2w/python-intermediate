sales = [125.97, 85.32, 99.78, 154.21, 78.50, 83.67, 111.13]

#find largest sale
print(max(sales))

#find smallest sale
print(min(sales))

#sum of sales
print(sum(sales))

total_sales = sum(sales)
print(round(total_sales), 2)

#no of sales

print(len(sales))

#average sales
average = sum(sales) / len(sales)
print(average)

#length of a string
print(len("introduction to programming for developers"))

#length of a dictionary
print(len({"a":1, "b":2, "c":3}))


#sort sales in ascending order
print(sorted(sales))


#sort string alphabetically
print(sorted("George"))


help(sorted)

#if sum is not used
sales_count = 0
for sale in sales:
    sales_count += sale
    print(sales_count)


course_ratings = {"LLM Concepts": 4.7, 
                  "Introduction to Data Pipelines": 4.75, 
                  "AI Ethics": 4.62, 
                  "Introduction to dbt": 4.81}

num_courses = len(course_ratings)
print(num_courses)

course_completions = [97, 83, 121, 205, 56, 174, 92, 117, 164]

num_completions = len(course_completions)
print(num_completions)

most_popular_course = "Introduction to dbt"

title_length = len(most_popular_course)
print(title_length)

print(sum(course_completions))
print(max(course_completions))
print(sum(course_completions) / len(course_completions))
print(round(sum(course_completions)/ len(course_completions), 1))
