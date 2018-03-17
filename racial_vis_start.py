import csv
from collections import defaultdict
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot

#
Institution = []
asian = []
black = []
hispanic = []
nativeAmerica = []
mulitCultural = []
white = []

with open('racial.csv') as d:
	reader = csv.DictReader(d)
	currentInst = 0 #out current institute
	prevInst = 0 #the last institute we looked at
	#the total count for each race per institute
	aC = 0
	blC = 0
	hsC = 0
	naC = 0
	mcC = 0
	wC = 0
	for row in reader:
		currentInst = int(row['Institution'])
		if prevInst == 0:
			prevInst = currentInst
		if prevInst != currentInst:
			Institution.append(prevInst)
			asian.append(aC)
			black.append(blC)
			hispanic.append(hsC)
			nativeAmerica.append(naC)
			mulitCultural.append(mcC)
			white.append(wC)
			aC = 0
			blC = 0
			hsC = 0
			naC = 0
			mcC = 0
			wC = 0
			prevInst = currentInst
			
		try:
			if row['Female_Asian']:
				aC += int(row['Female_Asian'])
			if row['Female_Black']:
				blC += int(row['Female_Black'])
			if row['Female_Hispanic']:
				hsC += int(row['Female_Hispanic'])
			if row['Female_American_Indian']:
				naC += int(row['Female_American_Indian'])
			if row['Female_Multi']:
				mcC += int(row['Female_Multi'])
			if row['Female_White']:
				wC += int(row['Female_White'])
		except KeyError as name:
			pass 
	#creating the HTML file
	output_file('racial.html')
	
	# Create Plot with Title, Size, and the X Axis
asianPlt = figure(title="Examining Total Asian Variation between Institutions", x_axis_label='Institution', y_axis_label='Total Female Asian Students',plot_width=600,plot_height=500)

# Add bars of our data
asianPlt.vbar(Institution, 1, asian)

blackPlt = figure(title="Examining Total Black Variation between Institutions", x_axis_label='Institution', y_axis_label='Total Female Black Students',plot_width=600,plot_height=500)

# Add bars of our data
blackPlt.vbar(Institution, 1, black)

hispanicPlt = figure(title="Examining Total Hispanic Variation between Institutions", x_axis_label='Institution', y_axis_label='Total Female Hispanic Students',plot_width=600,plot_height=500)

# Add bars of our data
hispanicPlt.vbar(Institution, .1, hispanic)

nativeAmericaPlt = figure(title="Examining Total Native American Variation between Institutions", x_axis_label='Institution', y_axis_label='Total Female Native American Students',plot_width=600,plot_height=500)

# Add bars of our data
nativeAmericaPlt.vbar(Institution, .1, nativeAmerica)

mulitCulturalPlt = figure(title="Examining Total Multi Cultural Variation between Institutions", x_axis_label='Institution', y_axis_label='Total Female Multi Cultural Students',plot_width=600,plot_height=500)

# Add bars of our data
mulitCulturalPlt.vbar(Institution, .1, mulitCultural)

whitePlt = figure(title="Examining Total White Variation between Institutions", x_axis_label='Institution', y_axis_label='Total Female White Students',plot_width=600,plot_height=500)

# Add bars of our data
whitePlt.vbar(Institution, .1, white)

# Show the Visualization
gridPlt = gridplot([[asianPlt, blackPlt, hispanicPlt], [nativeAmericaPlt, mulitCulturalPlt, whitePlt]])

show(gridPlt)


