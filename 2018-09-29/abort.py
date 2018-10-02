import pandas as pd
import numpy as np
import matplotlib.pylab as plt
plt.ion()
plt.grid( True )

import seaborn as sns
sns.set_style( 'darkgrid' )
sns.set_context( 'talk' )

import datetime

uspop = pd.read_csv('dat/nst-est2017-popchg2010_2017.csv')

# get ohio population numbers for 2010-2017
popest = []
dtlist = []
years = range(2010,2018)
for _y in years:
    yearname = 'POPESTIMATE' + str(_y)
    dtlist.append( datetime.datetime( _y, 1, 1) )
    popest.append(yearname)

ohpop = uspop[ uspop['NAME']=='Ohio' ][ popest ]
ohpop = ohpop.T.set_index( pd.DatetimeIndex( dtlist )) 
ohpop.columns = [ 'Ohio Population' ]

# load the abortion statistics
ohabt = pd.read_csv('dat/ddn.csv')
ohabt.set_index( pd.to_datetime( ohabt['year'] , format='%Y'), inplace = True)

ohabt = pd.read_csv('dat/ohio_doh.csv', delimiter= ' ', header = None, thousands = ',')
abt = ohabt.T
abt.columns = abt.iloc[0]
abt = abt.reindex(abt.index.drop(0))
abt.set_index( pd.to_datetime( abt['YEAR'], format='%Y'), inplace = True )
abt['TOTAL']=abt['TOTAL'].astype(float)
abt['RESIDENT']=abt['RESIDENT'].astype(float)
abt = abt.sort_values(by='YEAR')
abt['TOTDIFF'] = abt['TOTAL'].diff() 

# plot the totals
plt.figure()
sns.lineplot(data=abt[['TOTAL','RESIDENT']], markers = True)
plt.xlabel('Year')
plt.ylabel('Total induced abortions')
plt.title('Total induced abortions in Ohio')

# join the two dataframes together
ohjoin = ohpop.join(abt)
ohjoin['Total abortions'] = ohjoin['TOTAL']/ohjoin['OH population']
ohjoin['Ohio resident abortions'] = ohjoin['RESIDENT']/ohjoin['OH population']

# generate plots
plt.figure()
sns.lineplot(data=ohjoin[[ 'Total abortions',  'Ohio resident abortions']]*100e3, markers=True)
plt.xlabel('Year')
plt.ylabel('Abortions per 100k residents')
plt.title('Ohio abortions per 100k people')

