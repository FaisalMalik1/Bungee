import pandas as pd
import numpy as np
df = pd.read_csv('question1.csv')  # reading a csv file to pandas data frame
print(df.dtypes)  # headers or the column names of the csv file
#df['Year'] = pd.to_datetime(df['Year'])
df.set_index('Year')  # setting year to index
df = df.drop(columns='Total')  # deleting the column of total
df_decade = df.groupby(np.floor(df['Year']/10) * 10)['Population','Violent',
                                                     'Property','Murder','Forcible_Rape',
                                                     'Robbery','Aggravated_assault','Burglary',
                                                     'Larceny_Theft', 'Vehicle_Theft'].sum() # applying filter to get the years of decades and only selecting the respective columns
print(df_decade)
df_decade.to_excel("output_of_q1.xlsx",index=True) # exporting our data frame to excel file