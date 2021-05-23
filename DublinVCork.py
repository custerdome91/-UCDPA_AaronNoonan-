import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#--------------------------------#
# Import CSV and merge DataFrames
#--------------------------------#

cork = pd.read_csv("CorkLEA.csv")
dublin = pd.read_csv("DublinLEA.csv")

LEA_100K = pd.concat([cork, dublin])

#print(LEA_100K)

#----------------------------------------------------------------------------#
# Create variables containing information from Cork City and Dublin City LEAs
#----------------------------------------------------------------------------#

cork_NE = LEA_100K.loc[LEA_100K['ENGLISH'] == "CORK CITY NORTH EAST LEA-6"]
cork_NW = LEA_100K.loc[LEA_100K['ENGLISH'] == "CORK CITY NORTH WEST LEA-6"]
cork_SC = LEA_100K.loc[LEA_100K['ENGLISH'] == "CORK CITY SOUTH CENTRAL LEA-6"]
cork_SE = LEA_100K.loc[LEA_100K['ENGLISH'] == "CORK CITY SOUTH EAST LEA-6"]
cork_SW = LEA_100K.loc[LEA_100K['ENGLISH'] == "CORK CITY SOUTH WEST LEA-7"]

cabra = LEA_100K.loc[LEA_100K['ENGLISH'] == "CABRA-GLASNEVIN LEA-7"]
clontarf = LEA_100K.loc[LEA_100K['ENGLISH'] == "CLONTARF LEA-6"]
north = LEA_100K.loc[LEA_100K['ENGLISH'] == "NORTH INNER CITY LEA-7"]
dublin_SE = LEA_100K.loc[LEA_100K['ENGLISH'] == "SOUTH EAST INNER CITY LEA-5"]
dublin_SW = LEA_100K.loc[LEA_100K['ENGLISH'] == "SOUTH WEST INNER CITY LEA-5"]

#Only use data between December and March for Cork City and Dublin City LEAs

dec_feb_NE = cork_NE.loc[258:438,:]
dec_feb_NW = cork_NW.loc[262:442,:]
dec_feb_SC = cork_SC.loc[268:448,:]
dec_feb_SE = cork_SE.loc[259:439,:]
dec_feb_SW = cork_SW.loc[257:437,:]


dec_feb_cabra = cabra.loc[543:915,:]
dec_feb_clontarf = clontarf.loc[549:921,:]
dec_feb_north = north.loc[536:908,:]
dec_feb_dublin_SE = dublin_SE.loc[535:907,:]
dec_feb_dublin_SW = dublin_SW.loc[537:909,:]

#Concatonate DataFrames

cork_dublin = pd.concat([dec_feb_NE, dec_feb_NW, dec_feb_SC,dec_feb_SE,dec_feb_SW, dec_feb_cabra, dec_feb_clontarf,dec_feb_north, dec_feb_dublin_SE, dec_feb_dublin_SW])

cork_dublin.sort_values(['P14_100k'], inplace=True, ascending=False)

print(cork_dublin)

cork_dublin.to_csv('CorkVDublin.csv')


#------------------------------------------------------------#
# Plot graph in Matplotlib
#------------------------------------------------------------#

plt.bar(cork_dublin.ENGLISH, cork_dublin.P14_100k)

plt.xlabel('Date')
plt.ylabel('Cases Per 100K')

plt.title('Comparison of Highest Spike in Cases Between Cork and Dublin LEAs')


plt.xticks(np.arange(10),['Cork South East', 'Cork South West', 'Cabra', 'Cork South Central', 'Cork North East', 'Cork North West', 'South East Inner City', 'North Inner City', 'South West Inner City', 'Clontarf'], rotation=35)
plt.yticks([0,250,500,750,1000,1250,1500,1750,2000,2250, 2500])

#Annotate each bar with number of cases per 100,000 over 14 days

plt.annotate('2452', xy=(0, 0), xytext=(0,2450), ha='center', va='bottom')
plt.annotate('1745', xy=(0, 0), xytext=(1,1760), ha='center', va='bottom')
plt.annotate('1736', xy=(0, 0), xytext=(2,1750), ha='center', va='bottom')
plt.annotate('1715', xy=(0, 0), xytext=(3,1720), ha='center', va='bottom')
plt.annotate('1677', xy=(0, 0), xytext=(4,1680), ha='center', va='bottom')
plt.annotate('1670', xy=(0, 0), xytext=(5,1665), ha='center', va='bottom')
plt.annotate('1606', xy=(0, 0), xytext=(6,1615), ha='center', va='bottom')
plt.annotate('1547', xy=(0, 0), xytext=(7,1560), ha='center', va='bottom')
plt.annotate('1311', xy=(0, 0), xytext=(8,1310), ha='center', va='bottom')
plt.annotate('1266', xy=(0, 0), xytext=(9,1260), ha='center', va='bottom')


plt.show()

