import pandas as pd
import matplotlib.pyplot as plt
import matplotlib

# Read resultant survey file into DataFrame
df = pd.read_csv('ecn_survey.txt',header=None)

# Change column names
df.columns = ['site', 'uses_ecn']

# Getting total number of sites that use ECN and those that don't
df_count = df.groupby(['uses_ecn']).agg('count')

# Plotting pie chart
matplotlib.rcParams['font.size'] = 10.0
plt.gca().axis("equal")
pie = plt.pie(df_count, startangle=0, autopct='%1.0f%%', pctdistance=0.9, radius=1.2)
labels=df.index.unique()
plt.title('ECN Survey', weight='bold', size=14)
plt.legend(pie[0], labels = ["Doesn't Use ECN", "Uses ECN"], bbox_to_anchor=(1,0.5), loc="center right", fontsize=10, 
           bbox_transform=plt.gcf().transFigure)
plt.subplots_adjust(left=0.0, bottom=0.1, right=0.85)

plt.savefig('survey.png')
plt.clf()
plt.close()






