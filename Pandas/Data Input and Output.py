# we are able to read data and write data to a variety of sources
# These are the 4 main data sources we will be working with
# ---> CSV
# ---> Excel
# ---> HTML
# ---> SQL
import pandas as pd

# head() in data frame is used to return the first row of the table from the data frame

# # Reading CSV files  (reads and displays in data frames)
# print(pd.read_csv('mycsvfile.csv'))
#
# # Writing a CSV  (reads and displays in data frames)
df = pd.read_csv('mycsvfile.csv')
# df.to_csv('My Output', index=False)
# print(pd.read_csv('My Output'))

# Reading from an Excel file
# print(pd.read_excel('myexcelfile.xlsx',sheet_name='Sheet1'))

# Reading from a HTML file
# data = pd.read_html('html file link comes here . html')

# Writing into a HTMl file
# df.to_html('newhtml.html')

# # Reading from a SQL file
# from sqlalchemy import create_engine
# engine = create_engine('sqlite:///:memory:')
# df.to_sql('my_table', engine)
#
# # Writing to a SQL file
# sqldf = pd.read_sql('my_table', con=engine)
# print(sqldf)