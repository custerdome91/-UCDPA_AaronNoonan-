import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt
import seaborn as sns
sns.set()

#-----------------------------#
# Import CSV and clean up data
#-----------------------------#

#Import the CSV file, remove index column

df = pd.read_csv("COVID19STATS.csv", index_col=0)

#show data
print(df.head())
print(df.info())

#Show a list of columns to see which columns are relevant
print(df.columns)


#Remove columns unrelated to project
df.drop(['IGEasting', 'IGNorthing', 'Lat', 'Long', 'UGI', 'ConfirmedCovidDeaths', 'ConfirmedCovidRecovered', 'SHAPE_Area', 'SHAPE_Length', 'PopulationProportionCovidCases'], inplace=True, axis=1)


#Show remaining columns
print(df.columns)

#Check to see if there are any missing values/records
print(df.isna().sum())

#Check for duplicate rows
duplicate_rows_df = df[df.duplicated()]
print(duplicate_rows_df)
#There are no duplicates


#Create new CSV showing altered data with removed columns
df.to_csv('COVID19STATS_modified.csv', index=False)

covid_stats = pd.read_csv("COVID19STATS_modified.csv", parse_dates=True, index_col=0)

print(covid_stats.head())

#------------------------------------------------------------#
# Create DataFrames for each Border Counties being examined
#------------------------------------------------------------#

donegal = covid_stats.loc[covid_stats['CountyName'] == "Donegal"]
cavan = covid_stats.loc[covid_stats['CountyName'] == "Cavan"]
leitrim = covid_stats.loc[covid_stats['CountyName'] == "Leitrim"]
monaghan = covid_stats.loc[covid_stats['CountyName'] == "Monaghan"]
louth = covid_stats.loc[covid_stats['CountyName'] == "Louth"]

donegal_df = pd.DataFrame(donegal)
cavan_df = pd.DataFrame(cavan)
leitrim_df = pd.DataFrame(leitrim)
monaghan_df = pd.DataFrame(monaghan)
louth_df = pd.DataFrame(louth)

print(donegal_df)


#----------------------------------------------------------------------------#
# Use boolean mask to create new DataFrame with only dates required for graph
#----------------------------------------------------------------------------#

donegal_df['TimeStamp'] = pd.to_datetime(donegal_df['TimeStamp'])
donegal_mask = (donegal_df['TimeStamp'] > '2020/11/30') & (donegal_df['TimeStamp'] <= '2021/03/01')

cavan_df['TimeStamp'] = pd.to_datetime(cavan_df['TimeStamp'])
cavan_mask = (cavan_df['TimeStamp'] > '2020/11/30') & (cavan_df['TimeStamp'] <= '2021/03/01')

leitrim_df['TimeStamp'] = pd.to_datetime(leitrim_df['TimeStamp'])
leitrim_mask = (leitrim_df['TimeStamp'] > '2020/11/30') & (leitrim_df['TimeStamp'] <= '2021/03/01')

monaghan_df['TimeStamp'] = pd.to_datetime(monaghan_df['TimeStamp'])
monaghan_mask = (monaghan_df['TimeStamp'] > '2020/11/30') & (monaghan_df['TimeStamp'] <= '2021/03/01')

louth_df['TimeStamp'] = pd.to_datetime(louth_df['TimeStamp'])
louth_mask = (louth_df['TimeStamp'] > '2020/11/30') & (louth_df['TimeStamp'] <= '2021/03/01')


donegal_df2 = donegal_df.loc[donegal_mask]
cavan_df2 = cavan_df.loc[cavan_mask]
leitrim_df2 = leitrim_df.loc[leitrim_mask]
monaghan_df2 = monaghan_df.loc[monaghan_mask]
louth_df2 = louth_df.loc[louth_mask]

#Create two variables to plot X and Y on graph

donegal_df3 = donegal_df2['ConfirmedCovidCases']
donegal_df3_date = donegal_df2['TimeStamp']

cavan_df3 = cavan_df2['ConfirmedCovidCases']
cavan_df3_date = cavan_df2['TimeStamp']

leitrim_df3 = leitrim_df2['ConfirmedCovidCases']
leitrim_df3_date = leitrim_df2['TimeStamp']

monaghan_df3 = monaghan_df2['ConfirmedCovidCases']
monaghan_df3_date = monaghan_df2['TimeStamp']

louth_df3 = louth_df2['ConfirmedCovidCases']
louth_df3_date = louth_df2['TimeStamp']


#------------------------------------------------------------------------------------------------------#
#NORTHERN IRELAND
#------------------------------------------------------------------------------------------------------#

#Import CSV file

df = pd.read_csv("UKCOVIDDATA.csv")

#Didn't set the index_col to 0 because areaType wouldn't drop then

#show data
print(df.head())
print(df.info())

#Show a list of columns to see which columns are relevant
print(df.columns)

#Remove columns unrelated to project
df.drop(['areaType','areaCode'], inplace=True, axis=1)

#areaType won't drop for some raisin

#Show remaining columns
print(df.columns)
print(df.head())

#Check to see if there are any missing values/records
print(df.isna().sum())

#Check for duplicate rows
duplicate_rows_df = df[df.duplicated()]
print(duplicate_rows_df)
#There are no duplicates

#Create new CSV showing altered data with removed columns
df.to_csv('NICOVIDDATA_modified.csv', index=False)


#Import new CSV

NI_covid_stats = pd.read_csv("NICOVIDDATA_modified.csv", parse_dates=True)

print(NI_covid_stats.head())

#Isolate Northern Ireland from other three UK countries

northern_ireland = NI_covid_stats.loc[NI_covid_stats['areaName'] == "Northern Ireland"]

print(northern_ireland)

northern_ireland_df = pd.DataFrame(northern_ireland)

#Use boolean mask to create new DataFrame with only dates required for graph

northern_ireland_df['date'] = pd.to_datetime(northern_ireland_df['date'])
northern_ireland_mask = (northern_ireland_df['date'] > '2020/11/30') & (northern_ireland_df['date'] <= '2021/03/01')

northern_ireland_df2 = northern_ireland_df.loc[northern_ireland_mask]

print(northern_ireland_df2)

#Create two variables to plot X and Y on graph

northern_ireland_df3 = northern_ireland_df2['cumCasesByPublishDate']
northern_ireland_df3_date = northern_ireland_df2['date']


#------------------------------------------------------------#
# Plot graph in Matplotlib
#------------------------------------------------------------#

#Create subplot graph, sharing both axes

fig, (ax1, ax2) = plt.subplots(2, 1, sharey=False,sharex=True)

#Plot graph 1 - Border Counties

ax1.plot(donegal_df3_date, donegal_df3, color='cornflowerblue', label='Donegal', linewidth=3, linestyle='-')
ax1.plot(cavan_df3_date, cavan_df3, color='darkorchid', label='Cavan', linewidth=3, linestyle='-')
ax1.plot(leitrim_df3_date, leitrim_df3, color='gold', label='Leitrim', linewidth=3, linestyle='-')
ax1.plot(monaghan_df3_date, monaghan_df3, color='darkslategrey', label='Monaghan', linewidth=3, linestyle='-')
ax1.plot(louth_df3_date, louth_df3, color='dimgray', label='Louth', linewidth=3, linestyle='-')

#Set legend, titles, labels, and red line to denote when lockdown began

ax1.legend()
ax1.set_title('COVID-19 Cumulative Cases From December 2020 through February 2021')
ax1.set_ylabel('Cases')
ax1.axvline(dt.datetime(2020,12,24), color='r', linestyle='--')

#Plot graph 2 - Northern Ireland

ax2.plot(northern_ireland_df3_date, northern_ireland_df3, color='crimson', label='Northern Ireland', linewidth=3, linestyle='-')

#Set legend, titles, labels, and red line to denote when lockdown began

ax2.legend()
ax2.set_xlabel('Date')
ax2.set_ylabel('Cases')
ax2.axvline(dt.datetime(2020,12,26), color='r', linestyle='--')

#Insert text box to show when lockdown began for each graph

textstr = 'Broken red lines indicate beginning \nof Christmas lockdown: \nDecember 24th in Republic of Ireland, \nDecember 26th in Northern Ireland'
props = dict(boxstyle='round', facecolor='cornflowerblue', alpha=0.5)

ax2.text(0.72, 0.06, textstr, transform=ax2.transAxes, fontsize=10,
        verticalalignment='bottom', bbox=props)

#Set dates at roughly ten-day intervals

ax2.set_xticks(donegal_df2.TimeStamp[::10])

plt.setp(ax2.xaxis.get_majorticklabels(), rotation=35)

plt.show()













