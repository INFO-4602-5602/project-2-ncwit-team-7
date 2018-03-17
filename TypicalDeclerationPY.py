#End of 2nd year: 631
#Upon Enrollment: 1361
#End of 1st year: 389
#Other: 517


from bokeh.io import show, output_file
from bokeh.plotting import figure
import csv
import collections


#Output to html file to display bar graph
output_file("log_lines.html")

#Array of different options in the data
decleration = ['Upon Enrollment', 'End of 1st Year', 'End of 2nd Year', 'Other']

#Setup of graph
p = figure(x_range=decleration, plot_height=350, title="When Do Students Declare Their Major?",
           toolbar_location=None, tools="")



#Count when students declare major
with open('TypicalDecleration.csv') as content_file:
    content = content_file.read()
    uponEnrollment = content.count("Upon Enrollment")

with open('TypicalDecleration.csv') as content_file:
    content = content_file.read()
    firstYear = content.count("End of 1st Year")

with open('TypicalDecleration.csv') as content_file:
    content = content_file.read()
    secondYear = content.count("End of 2nd Year")

with open('TypicalDecleration.csv') as content_file:
    content = content_file.read()
    Other = content.count("Other")


#Design of graph
p.vbar(x=decleration, top=[uponEnrollment, firstYear, secondYear, Other], width=0.9)

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)