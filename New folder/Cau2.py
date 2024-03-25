import numpy as np
import pandas as pd


# import numpy as np


# 1/ Show the first 5 lines of tsv file
def ex1():
    s = pd.read_table("file/thongtin.tsv")
    print(s.head(5))


# 2/ Find the number of row and column of this file
# pd.shape --> hàm lấy số dòng và cột trong pandas
def ex2():
    s = pd.read_table("file/thongtin.tsv")
    print(s.shape)


# 3/ Print the name of columns
def ex3():
    s = pd.read_table("file/thongtin.tsv")
    print(s.columns)


# 4/ What is the type of the column names ? --> Object
# 5/ Get the country column and it to its own variable. Show the first 5 observations
def ex5():
    s = pd.read_table("file/country.tsv")
    s['country'] = 'country'
    s.to_csv("file/country.tsv", sep=" ", index=False)
    print(s.head(2))


# 6/ Show the last 5 observations of this column
def ex6():
    s = pd.read_table("file/country.tsv")
    print(s.tail(2))


# 7/ Look at continent and year. Show the first 5 observations of these columns, and the last observations
def ex7():
    s = {'continet': pd.Series(['ThaiLand', 'VietNam', 'Cambodia', 'Laos']),
         'year': pd.Series([1., 2., 3., 4.]),
         'country': pd.Series(['country'])}

    df = pd.DataFrame(s)
    print(df[['continet', 'year']])


# 8/ How to get the first row of tsv file? How to get the 100th row
# s.iloc[<tham số đầu là dòng cần in ra>,<số cột muốn in ra]
def ex8():
    s = pd.read_table("file/05_gap-merged-with-china-1952.tsv")
    print(s.iloc[100, :])


# 9/ Try to get the first column by using a interger index. And get the first and last column by pasing the integer
# index
def ex9():
    s = pd.read_table("file/05_gap-merged-with-china-1952.tsv")
    print(s.iloc[0])
    print('------------------------------------------')
    print(s.iloc[-1])


# 10/ How to get the last row with .loc? Try with index -1? Correct?
def ex10():
    s = pd.read_table("file/05_gap-merged-with-china-1952.tsv")
    print(s.loc[-1])
    # Không thực hiện được
    # ==> .loc chỉ thực hiện được khi chỉ số (index) là số nguyên dương
    # ==> .iloc thực hiện được khi chỉ số (index) là số nguyên dương và số nguyên âm


# 11/ How to select the first, 100th, 1000 th rows by two methods?
def ex11():
    s = pd.read_table("file/05_gap-merged-with-china-1952.tsv")
    print(s.loc[0, :])
    print('------------------------------------------')
    print(s.loc[100, :])
    print('------------------------------------------')
    print(s.loc[1000, :])


# 12/ Get the 43rd country in our data using .loc, .iloc?
def ex12():
    s = pd.read_table("file/05_gap-merged-with-china-1952.tsv")
    print("Get by .loc")
    print(s.loc[43, :])
    print('------------------------------------------')
    print("Get by .iloc")
    print(s.iloc[43, :])


# 13/ How to get the first, 100th, 1000th rows from the first, 4th, 6th columns?
def ex13():
    s = pd.read_table("file/05_gap-merged-with-china-1952.tsv")
    print(s.iloc[[0, 100, 100], [0, 2, 5]])


# 14/ Get first 10 row of our data (tsv file)?
def ex14():
    s = pd.read_table("file/05_gap-merged-with-china-1952.tsv")
    print(s.head(10))


# 15/ For each year in our data, what was the average life expectation?
def ex15():
    s = pd.read_table("file/05_gap-merged-with-china-1952.tsv")
    k = s.groupby('year')['lifeExp'].mean()
    print(k)


if __name__ == '__main__':
    # Gọi hàm để thực hiện
    ex15()
