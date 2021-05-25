import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

#-----------------------------#
# Import CSV and clean up data
#-----------------------------#

#Import the CSV file, remove index column

LEA_df = pd.read_csv("LEACasesAugustApril.csv", index_col=0)

#Show data

print(LEA_df.head())
print(LEA_df.info())

#Show a list of columns to see which columns are relevant
print(LEA_df.columns)


#Remove columns unrelated to project
LEA_df.drop(['LE_ID', 'GUID'], axis=1)

#Show the remaining columns
print(LEA_df.columns)

#Check to see if there are any missing values/records
print(LEA_df.isna().sum())
#There are no missing values

#Check for duplicate rows
duplicate_rows_df = LEA_df[LEA_df.duplicated()]
print(duplicate_rows_df)
#Empty DataFrame - there are no duplicates


#Create new CSV containing altered data with removed columns
LEA_df.to_csv('modifiedLEA.csv', index=False)

#------------------------------------------------------------#
# Create DataFrame containing just information from Cork LEAs
#------------------------------------------------------------#

#Import CSV file

df = pd.read_csv("modifiedLEA.csv", index_col=0)

#Create new DataFrame with just Cork LEAs - 570 rows
cork_df = df.loc[df['COUNTY'] == "CORK"]

print(cork_df)

#Exporting the Cork DataFrame as a CSV
cork_df.to_csv('CorkLEA.csv')


#------------------------------------------------------------#
# Create DataFrames for each Cork LEA being examined
#------------------------------------------------------------#

#Import CSV file

cork = pd.read_csv("CorkLEA.csv")

#Create DataFrame for each Cork City LEA

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

print(cork_SW_df)
#Only use data between December and March for Cork City LEAs

dec_mar_NE = cork_NE_df.loc[258:438, :]
dec_mar_NW = cork_NW_df.loc[262:442, :]
dec_mar_SC = cork_SC_df.loc[268:448, :]
dec_mar_SE = cork_SE_df.loc[259:439, :]
dec_mar_SW = cork_SW_df.loc[257:437, :]

#Create two variables to plot X and Y on graph

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


#Create DataFrame for each Cork County LEA

cork_bandon = cork.loc[cork['ENGLISH'] == "BANDON - KINSALE LEA-6"]
cork_bantry = cork.loc[cork['ENGLISH'] == "BANTRY-WEST CORK LEA-4"]
cork_carrigaline = cork.loc[cork['ENGLISH'] == "CARRIGALINE LEA-6"]
cork_cobh = cork.loc[cork['ENGLISH'] == "COBH LEA-6"]
cork_fermoy = cork.loc[cork['ENGLISH'] == "FERMOY LEA-6"]
cork_kanturk = cork.loc[cork['ENGLISH'] == "KANTURK LEA-4"]
cork_macroom = cork.loc[cork['ENGLISH'] == "MACROOM LEA-6"]
cork_mallow = cork.loc[cork['ENGLISH'] == "MALLOW LEA-5"]
cork_midleton = cork.loc[cork['ENGLISH'] == "MIDLETON LEA-7"]
cork_skibbereen = cork.loc[cork['ENGLISH'] == "SKIBBEREEN-WEST CORK LEA-5"]

cork_bandon_df = pd.DataFrame(cork_bandon)
cork_bantry_df = pd.DataFrame(cork_bantry)
cork_carrigaline_df = pd.DataFrame(cork_carrigaline)
cork_cobh_df = pd.DataFrame(cork_cobh)
cork_fermoy_df = pd.DataFrame(cork_fermoy)
cork_kanturk_df = pd.DataFrame(cork_kanturk)
cork_macroom_df = pd.DataFrame(cork_macroom)
cork_mallow_df = pd.DataFrame(cork_mallow)
cork_midleton_df = pd.DataFrame(cork_midleton)
cork_skibbereen_df = pd.DataFrame(cork_skibbereen)

#Only use data between December and March for Cork County LEAs

dec_mar_bandon = cork_bandon_df.loc[267:447, :]
dec_mar_bantry = cork_bantry_df.loc[269:449, :]
dec_mar_carrigaline = cork_carrigaline_df.loc[256:436, :]
dec_mar_cobh = cork_cobh_df.loc[264:444, :]
dec_mar_fermoy = cork_fermoy_df.loc[263:443, :]
dec_mar_kanturk = cork_kanturk_df.loc[255:435, :]
dec_mar_macroom = cork_macroom_df.loc[265:445, :]
dec_mar_mallow = cork_mallow_df.loc[266:446, :]
dec_mar_midleton = cork_midleton_df.loc[260:440, :]
dec_mar_skibbereen = cork_skibbereen_df.loc[261:441, :]

#Create two variables to plot X and Y on graph

cork_bandon_df2 = dec_mar_bandon['P14_100k']
cork_bandon_df2_date = dec_mar_bandon['EventDate']

cork_bantry_df2 = dec_mar_bantry['P14_100k']
cork_bantry_df2_date = dec_mar_bantry['EventDate']

cork_carrigaline_df2 = dec_mar_carrigaline['P14_100k']
cork_carrigaline_df2_date = dec_mar_carrigaline['EventDate']

cork_cobh_df2 = dec_mar_cobh['P14_100k']
cork_cobh_df2_date = dec_mar_cobh['EventDate']

cork_fermoy_df2 = dec_mar_fermoy['P14_100k']
cork_fermoy_df2_date = dec_mar_fermoy['EventDate']

cork_kanturk_df2 = dec_mar_kanturk['P14_100k']
cork_kanturk_df2_date = dec_mar_kanturk['EventDate']

cork_macroom_df2 = dec_mar_macroom['P14_100k']
cork_macroom_df2_date = dec_mar_macroom['EventDate']

cork_mallow_df2 = dec_mar_mallow['P14_100k']
cork_mallow_df2_date = dec_mar_mallow['EventDate']

cork_midleton_df2 = dec_mar_midleton['P14_100k']
cork_midleton_df2_date = dec_mar_midleton['EventDate']

cork_skibbereen_df2 = dec_mar_skibbereen['P14_100k']
cork_skibbereen_df2_date = dec_mar_skibbereen['EventDate']



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

#Plot graph 2 - Cork County LEAs

ax2.plot(cork_bandon_df2_date, cork_bandon_df2, color='seagreen', label='Bandon', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(cork_bantry_df2_date, cork_bantry_df2, color='navy', label='Bantry', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(cork_carrigaline_df2_date, cork_carrigaline_df2, color='orchid', label='Carrigaline', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(cork_cobh_df2_date, cork_cobh_df2, color='olive', label='Cobh', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(cork_fermoy_df2_date, cork_fermoy_df2, color='coral', label='Fermoy', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(cork_kanturk_df2_date, cork_kanturk_df2, color='silver', label='Kanturk', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(cork_macroom_df2_date, cork_macroom_df2, color='chocolate', label='Macroom', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(cork_midleton_df2_date, cork_midleton_df2, color='darkkhaki', label='Midleton', linewidth=3, marker='.', markersize=10, linestyle='-')
ax2.plot(cork_skibbereen_df2_date, cork_skibbereen_df2, color='cadetblue', label='Skibbereen', linewidth=3, marker='.', markersize=10, linestyle='-')

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

fig1.savefig('CorkCityVCounty.png')


