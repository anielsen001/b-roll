import pandas as pd
import numpy as np
import matplotlib.pylab as plt
plt.ion()
plt.grid( True )

import seaborn as sns
sns.set_style( 'darkgrid' )
sns.set_context( 'talk' )

import datetime

# read the data
df = pd.read_csv('dat/data.csv')

# set thei index to a datetime object using the year
df.set_index( pd.to_datetime( df['Year'] , format='%Y'), inplace = True)

# create a sum
df['sum'] = df['No Discipline'] + df[ 'Discipline']

plt.figure()
#sns.lineplot(data=df[ ['No Discipline','Discipline' ] ],markers=True)
sns.lineplot(data=df[ ['No Discipline','Discipline', 'Total Cases Opened' ,'sum'] ],markers=True)
plt.title('Teacher conduct cases')
plt.ylabel('Number')

plt.figure()
sns.lineplot(data = df['Total Cases Opened']/df['Applications'], markers=True)
plt.title('Number of cases per application')
plt.xlabel('Year')
plt.ylabel('Cases per application')
