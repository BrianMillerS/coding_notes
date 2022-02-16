# general
# [[rows], [columns]]
# 2D = data frame, 1D = series (typically columns)
df.shape
df.head  # display first 10 rows
df.tail
df.set_index('Date', inplace=True)  # set the row names to be a specific column, implace makes the change permanent
df.rename(columns={"A": "a", "B": "c"}) #A>a and B>c

# column selection
df.columns
df[['col1','col2']]

# iloc (uses Integer LOCation)
df.iloc[[0,1]]  # returns the first two rows
df.iloc[[0,1], [1,2]]  # returns the first two rows, and the second column

# loc (uses lables)
df.loc[[0,1]]. # returns the first two rows
df.loc[[0,1], ['col1','col2']]
df.loc[0:1 , 'col1':'col3']  # includes row 1 and column 3

# data frame combining
pd.concat([df1,df2])  # stack dataframes with the same column names


# datetime (dt class)
# https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior (link to datetime custom input symbols)
df['date'] = pd.to_datetime(df['date'])  # tries to convert the 'date' column into a pandas datetime object
df['date'] = pd.to_datetime(df['date'], format = '%Y-%m-%d %I-%p') # convert '2020-03-13 20:00:00' to pd datetime
df[0,'date'].dayname()  # get the day of the week for single value
df['Date'].dt.day_name()  # get the day of the week for a whole column
df['Date'].min()
df['Date'].max()
filt = (df['Date'] >= pd.to_datetime('2019-01-01'))
df.loc[filt]


# dataframe resampleing (aggregation)
df.resample('W').agg({'Close': 'mean', 'High': 'max', 'Low': 'min', 'Volume': 'sum'})
# the index was already set to datetime (df.set_index('Date'))
# returns a new df with the weekly: mean close, max high, min low, and total volume
