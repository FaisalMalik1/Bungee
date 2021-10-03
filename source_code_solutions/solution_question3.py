import pandas as pd
df = pd.read_csv('question3.csv')
df = df[['Team','Yellow Cards','Red Cards']]
df1=df.sort_values(ascending=False,by=['Red Cards','Yellow Cards'])
print(df1)
df1.to_excel("output_of_q3.xlsx",index=False)