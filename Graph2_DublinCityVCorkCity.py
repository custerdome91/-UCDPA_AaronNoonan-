import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#-----------------------------#
# Import CSV and clean up data
#-----------------------------#

#Import the CSV file, remove index column

df = pd.read_csv("modifiedLEA.csv", index_col=0)

#Create new DataFrame with just Dublin
dublin_df = df.loc[df['COUNTY'] == "DUBLIN"]

dublin_df.to_csv('DublinLEA.csv')

dublin = pd.read_csv("DublinLEA.csv")

#------------------------------------------------------------#
# Create DataFrames for each Dublin City LEA being examined
#------------------------------------------------------------#

cabra = dublin.loc[dublin['ENGLISH'] == "CABRA-GLASNEVIN LEA-7"]
clontarf = dublin.loc[dublin['ENGLISH'] == "CLONTARF LEA-6"]
north = dublin.loc[dublin['ENGLISH'] == "NORTH INNER CITY LEA-7"]
dublin_SE = dublin.loc[dublin['ENGLISH'] == "SOUTH EAST INNER CITY LEA-5"]
dublin_SW = dublin.loc[dublin['ENGLISH'] == "SOUTH WEST INNER CITY LEA-5"]

cabra_df = pd.DataFrame(cabra)
clontarf_df = pd.DataFrame(clontarf)
north_df = pd.DataFrame(north)
dublin_SE_df = pd.DataFrame(dublin_SE)
dublin_SW_df = pd.DataFrame(dublin_SW)

#Only use data between December and March for Dublin City LEAs

dec_mar_cabra = cabra_df.loc[543:915, :]
dec_mar_clontarf = clontarf_df.loc[549:921, :]
dec_mar_north = north_df.loc[536:908, :]
dec_mar_dublin_SE = dublin_SE_df.loc[535:907, :]
dec_mar_dublin_SW = dublin_SW_df.loc[537:909, :]

#Create two variables to plot X and Y on graph

cabra_df2 = dec_mar_cabra['P14_100k']
cabra_df2_date = dec_mar_cabra['EventDate']

clontarf_df2 = dec_mar_clontarf['P14_100k']
clontarf_df2_date = dec_mar_clontarf['EventDate']

north_df2 = dec_mar_north['P14_100k']
north_df2_date = dec_mar_north['EventDate']

dublin_SE_df2 = dec_mar_dublin_SE['P14_100k']
dublin_SE_df2_date = dec_mar_dublin_SE['EventDate']

dublin_SW_df2 = dec_mar_dublin_SW['P14_100k']
dublin_SW_df2_date = dec_mar_dublin_SW['EventDate']


#-----------------------------------#
#Bring in Cork City LEAs
#-----------------------------------#

#Import CSV file

cork = pd.read_csv("CorkLEA.csv")

cork_NE = cork.loc[cork['ENGLISH'] == "CORK CITY NORTH EAST LEA-6"]
cork_NW = cork.loc[cork['ENGLISH'] == "CORK CITY NORTH WEST LEA-6"]
cork_SC = cork.loc[cork['ENGLISH'] == "CORK CITY SOUTH CENTRAL LEA-6"]
cork_SE = cork.loc[cork['ENGLISH'] == "CORK CITY SOUTH EAST LEA-6"]
cork_SW = cork.loc[cork['ENGLISH'] == "CORK CITY SOUTH WEST LEA-7"]

cork_NE_df = pd.DataFrame(cork_NE)
cork_NW_df = pd.DataFrame(cork_NW)
cork_SC_df = pd.DataFrame(cork_SC)
cork_SE_df = pd.DataFrame(cork_SE)
cork_SW_df = pd.DataFrame(cork_SW)

dec_mar_NE = cork_NE_df.loc[258:438, :]
dec_mar_NW = cork_NW_df.loc[262:442, :]
dec_mar_SC = cork_SC_df.loc[268:448, :]
dec_mar_SE = cork_SE_df.loc[259:439, :]
dec_mar_SW = cork_SW_df.loc[257:437, :]


cork_NE_df2 = dec_mar_NE['P14_100k']
cork_NE_df2_date = dec_mar_NE['EventDate']

cork_NW_df2 = dec_mar_NW['P14_100k']
cork_NW_df2_date = dec_mar_NW['EventDate']

cork_SC_df2 = dec_mar_SC['P14_100k']
cork_SC_df2_date = dec_mar_SC['EventDate']

cork_SE_df2 = dec_mar_SE['P14_100k']
cork_SE_df2_date = dec_mar_SE['EventDate']

cork_SW_df2 = dec_mar_SW['P14_100k']
cork_SW_df2_date = dec_mar_SW['EventDate']


#------------------------------------------------------------#
# Plot graph in Matplotlib
#------------------------------------------------------------#

#Create subplot graph, sharing both axes

fig, (ax1, ax2) = plt.subplots(2, 1, sharey=True,sharex=True)

#Plot graph 1 - Cork City LEAs

ax1.plot(cork_NE_df2_date, cork_NE_df2, color='cornflowerblue', label='Cork North East', linewidth=3, marker='.', markersize=10, linestyle='-')
ax1.plot(cork_NW_df2_date, cork_NW_df2, color='forestgreen', label='Cork North West', linewidth=3, marker='.', markersize=10, linestyle='-')
ax1.plot(cork_SC_df2_date, cork_SC_df2, color='blueviolet', label='Cork South Central', linewidth=3, marker='.', markersize=10, linestyle='-')
ax1.plot(cork_SE_df2_date, cork_SE_df2, color='gold', label='Cork South East', linewidth=3, marker='.', markersize=10, linestyle='-')
ax1.plot(cork_SW_df2_date, cork_SW_df2, color='grey', label='Cork South West', linewidth=3, marker='.', markersize=10, linestyle='-')

#Set legend, titles, labels, and red line to denote when lockdown began

ax1.legend()
ax1.set_title('Incidence rate per 100,000 population of confirmed COVID-19 cases notified in the previous 14 days')
ax1.set_ylabel('Cases Per 100K')
ax1.axvline(x=3.428571, color='r', linestyle='--')

#Plot graph 2 - Dublin City LEAs

ax2.plot(cabra_df2_date, cabra_df2, color='darkgoldenrod', label='Cabra', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(clontarf_df2_date, clontarf_df2, color='sienna', label='Clontarf', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(north_df2_date, north_df2, color='black', label='North Inner City Dublin', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(dublin_SE_df2_date, dublin_SE_df2, color='steelblue', label='South East Inner City Dublin', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(dublin_SW_df2_date, dublin_SW_df2, color='mediumslateblue', label='South West Inner City Dublin', linewidth=3, marker='.', markersize=10, linestyle='-')

#Set legend, titles, labels, and red line to denote when lockdown began

ax2.legend()
ax2.set_xlabel('Date')
ax2.set_ylabel('Cases Per 100K')
ax2.axvline(x=3.428571, color='r', linestyle='--')

#Insert text box to show when lockdown began for each graph

textstr = 'Broken red lines indicate beginning \nof lockdown on December 24th 2020'
props = dict(boxstyle='round', facecolor='cornflowerblue', alpha=0.5)

ax2.text(0.02, 0.9, textstr, transform=ax2.transAxes, fontsize=10,
        verticalalignment='top', bbox=props)

#Ensure graph starts at 0

ax1.set_xlim(0)

#Set dates at roughly weekly intervals

ax2.set_xticks(dec_mar_NE.EventDate[::1])

#Move dates to 35 degree angle

plt.setp(ax2.xaxis.get_majorticklabels(), rotation=35)


plt.show()

#Save the graph

fig1.savefig('DublinCityVCorkCity.png')


