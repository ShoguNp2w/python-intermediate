import pandas as pd
sales = {"user_id":["KM37", "PR19", "YU88"], "order_value":[197.75, 208.21, 134.99]}
sales_df = pd.DataFrame(sales)
print(sales_df)


#read in csv file

#sales_df = pd.read_csv("sales.csv")

print(type(sales_df))

#print first 5 rows
print(sales_df.head())

#print mean order value
print(sales_df["order_value"].mean())

#print total value of sales
print(sales_df["order_value"].sum())

