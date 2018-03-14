import csv
from collections import defaultdict
from bokeh.plotting import figure, output_file, show
from bokeh.models import ColumnDataSource

# Establishing Dictionaries to store the sums of each school year, using school year as the key 
years_enrollment = {'2003-2004':0,'2004-2005':0,'2005-2006':0,'2006-2007':0,'2007-2008':0,'2008-2009':0,'2009-2010':0,'2010-2011':0,'2011-2012':0 ,'2012-2013':0,'2013-2014':0,'2014-2015':0,'2015-2016':0,'2016-2017':0}
years_graduate = {'2003-2004':0,'2004-2005':0,'2005-2006':0,'2006-2007':0,'2007-2008':0,'2008-2009':0,'2009-2010':0,'2010-2011':0,'2011-2012':0,'2012-2013':0,'2013-2014':0,'2014-2015':0,'2015-2016':0,'2016-2017':0}

# Using a cleaned up csv with only the columns we want, we read it in as a dictionary format
with open('timeline.csv') as f:
    reader = csv.DictReader(f) # read rows into a dictionary format
    for row in reader: # read a row as {column1: value1, column2: value2,...}
        # With each row, we determine if the data we are looking for exists, if it does increment the sum by the value of the row
        try:
            if row['female_new_enrollment']:
                years_enrollment[row['school_year']] = int(years_enrollment[row['school_year']])+int(row['female_new_enrollment'])
            if row['female_total_graduated']:
                years_graduate[row['school_year']] = int(years_graduate[row['school_year']])+int(row['female_total_graduated'])
        except KeyError as name: # This captures any csv errors when the key cannot be found in the dictionary
            pass

# Y Axis for Bokeh
years = ['2003-2004','2004-2005','2005-2006','2006-2007','2007-2008','2008-2009','2009-2010','2010-2011','2011-2012' ,'2012-2013','2013-2014','2014-2015','2015-2016','2016-2017']
# Create two empty lists which will be used to graph the summed values
enrollment_totals = []
graduate_totals = []

# We use this to correctly sort the sum dictionaries to a column format that Bokeh can understand (basically lists)
for year in years:
    enrollment_totals.append(years_enrollment[year])
    graduate_totals.append(years_graduate[year])


# Create an HTML file
output_file("timeline.html")

# Create Plot with Title, Size, and the X Axis
p = figure(title="Examining Enrollment and Graduation Totals of Female Students", x_axis_label='School Year', y_axis_label='Total Students', x_range=years,plot_width=940,plot_height=500)

# Add Lines of our data
p.line(years, enrollment_totals, legend="Female: New Enrollments", line_width=2)
p.line(years, graduate_totals, legend="Female: Graduated", color='red', line_width=2)

# Show the Visualization
show(p)