from turtle import pd

df = pd.read_csv('./data/SampleData.csv', index_col=0)
print(df)

del df['Price'] # Delete Price column
print(df)

# Delete row with index 2
print(df.drop(df.index[2]))

df = pd.read_csv('./data/SampleData.csv', index_col=0)
print(df)

# Add USD price column with exchange rate 1USD = 23,000 VND
df['Usd'] = df['Price']/23
print(df)

df = pd.read_csv('./data/SampleData.csv')
print(df)

# Add line at the end of df
df.loc[df.shape[0]] = ['VCB', 113.6, 23.09]
print(df)

sales_2020 = pd.DataFrame({'sales': [450, 360, 550, 480]}, index=['Mar', 'Jun', 'Feb', 'Apr'])
print(sales_2020)
print(sales_2020.sort_index())

sales_2020 = pd.DataFrame({'sales': [450, 360, 550, 480]}, index=['Mar', 'Jun', 'Feb', 'Apr'])
print(sales_2020)

sales_2021 = pd.DataFrame({'sales': [650, 600, 700, 680]}, index=['Feb', 'Mar', 'Apr', 'Jun'])
print(sales_2020.reindex(sales_2021.index))

df = pd.read_csv('./data/SampleData2.csv')
print(df)
print(df.groupby('Group').mean())

df = pd.read_csv('./data/SampleData2.csv')
df1 = df[['Symbol', 'Price', 'Group']]
df2 = df[['Symbol', 'PE', 'Group']]
print(df1)
print(df2)

df_concat = pd.concat([df1, df2])
print(df_concat)

df_concat = pd.concat([df1, df2], join='inner')
print(df_concat)

df_concat = pd.concat([df1, df2], axis=1)
print(df_concat)

df_append = df1.append(df2)
print(df_append)

df_merge = pd.merge(df1, df2)
print(df_merge)

df = pd.read_csv('./data/SampleData2.csv')
df1 = df[['Symbol', 'Price', 'Group’]]
df1 = df1.drop(df1.index[3])
df2 = df[['Symbol', 'PE', 'Group']]
print(df1)
print(df2)

df_merge = pd.merge(df1, df2)
print(df_merge)
df_merge = pd.merge(df1, df2, how='outer')
print(df_merge)

df = pd.read_csv('./data/SampleData_NaN.csv')
print(df)

df = pd.read_csv('./data/SampleData_NaN.csv')
print(df.isnull())

df = pd.read_csv('./data/SampleData_NaN.csv')
# Check for empty data for each column
print(df.isnull().any())

# Check for empty data for entire DataFrame
print(df.isnull().values.any())

df = pd.read_csv('./data/SampleData_NaN.csv')
# Check the number of empty data for each column
print(df.isnull().sum())

# Check the number of empty data for the entire DataFrame
print(df.isnull().sum().sum())

df = pd.read_csv('./data/SampleData_NaN.csv')
# Delete rows containing empty elements
df_delete_na_by_row = df.dropna(axis=0)
print(df_delete_na_by_row)

df = pd.read_csv('./data/SampleData_NaN.csv')
# Delete columns containing empty elements
df_delete_na_by_col = df.dropna(axis=1)
print(df_delete_na_by_col)

df = pd.read_csv('./data/SampleData_NaN.csv')
# Fill value 100 for empty element
df_fill_na_100 = df.fillna(100)
print(df_fill_na_100)

df = pd.read_csv('./data/SampleData_NaN.csv')
# Fill empty element with adjacent value below
df_fill_na_bfill = df.fillna(method='bfill')
print(df_fill_na_bfill)

df = pd.read_csv('./data/SampleData_NaN.csv')
# Fill empty element with adjacent value above
df_fill_na_ffill = df.fillna(method='ffill')
print(df_fill_na_ffill)

df = pd.read_csv('./data/SampleData_NaN.csv')
# Fill empty elements with interpolated values
df_fill_na_interpolate = df.interpolate()
print(df_fill_na_interpolate)








