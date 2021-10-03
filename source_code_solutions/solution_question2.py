import pandas as pd
df = pd.read_csv('question2.csv') # reading the input file
print(df.columns)  # printing column names to get column names
df1 = df.groupby('occupation').age.agg(['min','max'])  # applying filter to occupation and then getting the min and max ages and saving it into new data frame
print(df1)  # printing the data frame
df1.to_excel("output_of_q2.xlsx",index=True)  # exporting our dataframe to new excel file