# Project 2
Team 7
 
 <ul>
    <li>Matthew Coker</li>
    <li>Matthew Sredojevic</li>
    <li>Guillermo Rodriguez</li>
</ul>
All Team members were active in creating a visualization for this project

This project is built with Bokek, and can be run by using the html file to open a web page or run python3 vis_start.py to build the first visualization. The other two are runnable and explained in 'How to Run'.

<h2>How to Run</h2>
This visualization was built with Python3.
<ol>
  <li>Install Python 3</li>
  <li>Download Python Module - bokeh using pip</li>
  <li>To run the Enrollments and Graduation Visualization: In command line run python vis_start.py</li>
  <li>To run Major Decleration Visualization: In command line run python TypicalDeclerationPY.py</li>
  <li>To run Racial Comparisons Visualization: In command line run python racial.csv</li>
  <li>This will generate all the required html files (these should already be included in the repository)</li>
</ol>

<h2>Visualizations</h2>
<h3>Time Visualization - Guillermo</h3>
In this visualization, we examined the total number of inital enrollments and total graduating female students within all institutions that provided this information. In our script, we discarded any results that did not provide this data when charting our data.

<h3>Major Declecartion Visualization with Time - Matthew Coker</h3>
I used Bekoh to visualize how many students declare their major during their four years at college. I cleaned the data that I needed into a new csv file titled "TypicalDecleration.csv". In order to run the file, enter "TypicalDeclerationPY.py". Inside this python file, the code creates an html file in order to output the scripts encoded visualization. In the script, it reads in the "When do students typically declare their major?" and counts specific instances of diferrent results in the column. In this case there are only four. It then uses the number of instances for the bar graph and compares them next to each other to see when exactly students typically declare their major.

<h3>Racial Comparisions Across Institutions Visualization - Matthew Sredojevic</h3>
I used the Behok bar charts to represent the number of students of a given racial status (or multiple is specified) with 1 graph for each racial field (excluding Hawaiian Native). Each gragh shows the number of students at each Institution where there is data for that Institution. The data that is used here is the racial.csv that has removed the leading number on female students and focus on the Total number of FemaleSstudents (per each race). This data does not worry about the year and focus on the span from when a given Institution started and stopped giving data to NCWIT. (there is also a garbage variable apended to the racial.csv to allow the code to execute properly in a case where there WOULD be data in the last Institude, but here there is not).