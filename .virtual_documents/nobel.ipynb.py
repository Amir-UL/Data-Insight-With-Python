# Loading in required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Reading in the Nobel Prize data
nobel = pd.read_csv('datasets/nobel.csv', index_col=False)

# Taking a look at the first several winners
display(nobel.head(n=6))
# print(nobel.columns)


# Display the number of (possibly shared) Nobel Prizes handed
# out between 1901 and 2016
print(len(nobel),'\n')

# Display the number of prizes won by male and female recipients.
print(nobel['sex'].value_counts(), '\n')

# Display the number of prizes won by the top 10 nationalities.
print(nobel['birth_country'].value_counts().head(10))



# Calculating the proportion of USA born winners per decade
nobel['usa_born_winner'] = nobel['birth_country'] == 'United States of America'

nobel['decade'] = np.floor(nobel['year']/10 * 10).astype(int)
prop_usa_winners = nobel.groupby(by='decade', as_index=False)['usa_born_winner'].mean()

# Display the proportions of USA born winners per decade
print(prop_usa_winners)


# Setting the plotting theme
sns.set()

# and setting the size of all plots.
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners 
ax = sns.lineplot(x=prop_usa_winners['decade'], y=prop_usa_winners['usa_born_winner'])

# Adding get_ipython().run_line_magic("-formatting", " to the y-axis")
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter(1.0))


# Calculating the proportion of female laureates per decade
nobel['female_winner'] = nobel['sex'] == 'Female'
prop_female_winners = nobel.groupby(by=['decade', 'category'], as_index=False)['female_winner'].mean()
# display(prop_female_winners)
# Plotting USA born winners with % winners on the y-axis
# Setting the plotting theme
sns.set()
# and setting the size of all plots.
plt.rcParams['figure.figsize'] = [11, 7]

# Plotting USA born winners 
ax = sns.lineplot(x='decade', y='female_winner', hue='category', data=prop_female_winners)

# Adding get_ipython().run_line_magic("-formatting", " to the y-axis")
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter(1.0))
plt.savefig("fig1.png")
plt.show()



# Picking out the first woman to win a Nobel Prize
print('The name of the first women got nobel prize: ',nobel[nobel.sex== 'Female'].nsmallest(1, 'year')['full_name'])
nobel[nobel.sex== 'Female'].nsmallest(1, 'year')


# Selecting the laureates that have received 2 or more prizes.
print('The Magnificents Who Received The Nobel Prize Twice', '\n')
print(nobel[nobel['laureate_type'] == 'Individual']['full_name'].value_counts().sort_values(ascending=False).head(4))



# Converting birth_date from String to datetime
nobel['birth_date'] =  pd.to_datetime(nobel.birth_date)
# nobel['year'] = pd.to_datetime(nobel.year, format='get_ipython().run_line_magic("Y-%m-%d').dt.year", "")

# Calculating the age of Nobel Prize winners
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year

# Plotting the age of Nobel Prize winners
sns.lmplot(x='year', y='age', data=nobel, lowess=True, aspect=2, line_kws={'color':'black'})
sns.lmplot(x='year', y='age', data=nobel, hue='category', lowess=True, aspect=2, line_kws={'color':'black'})
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter(1.0))
plt.savefig("fig2.png")
plt.show()



# Same plot as above, but separate plots for each type of Nobel Prize
sns.lmplot(x='year', y='age', data=nobel, col='category', height=7, aspect=.4, x_jitter=.1 )
from matplotlib.ticker import PercentFormatter
ax.yaxis.set_major_formatter(PercentFormatter(1.0))
plt.savefig("fig3.png")
plt.show()



