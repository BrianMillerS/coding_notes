# general
# [[rows], [columns]]
df.shape
df.head
df.tail

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
