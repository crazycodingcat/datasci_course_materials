import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import dates
import seaborn as sns
sns.set_style('darkgrid')

def load_data(path):
	data = pd.read_csv(path, parse_dates=['Date'])
	return data

def process_data(data):
	# data processing
	df = data[data['Category'] == 'LARCENY/THEFT']
	df.loc[:, 'dow'] = df.Date.apply(lambda x: x.dayofweek)
	df.loc[:, 'HourOfDay'] = df.Time.apply(lambda x: x.split(':')[0])
	return df

def plot_ts(df):
	by_date = df.groupby('Date').size()
	ax = by_date.plot(figsize=(15, 6), legend=False)
	ax.set_ylabel('Total Number of thefts')
	ax.set_xlabel('Date (Weekend is highlighted in red)')
	# ax.xaxis.set_major_locator(plt.MultipleLocator(5))

	for i in by_date.index:
	    if i.dayofweek == 5: 
	        ax.axvspan(i - pd.Timedelta('1days'), i + pd.Timedelta('1days'), 
	                   facecolor='red', edgecolor='none', alpha=.2)

def plot_heatmap(df):
	by_dow = df.pivot_table(values='IncidntNum', index='dow', columns='HourOfDay', aggfunc='count')
	fig, ax = plt.subplots(figsize=(15, 6))
	sns.heatmap(by_dow, ax=ax, annot=True, fmt='d', yticklabels=['Mon', 'Tues', 'Wed', 'Thurs', 'Fri', 'Sat', 'Sun'])
	ax.set_ylabel('Day of Week')
	ax.set_xlabel('Hour of Day')






