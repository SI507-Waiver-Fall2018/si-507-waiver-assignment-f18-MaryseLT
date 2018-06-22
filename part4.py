# Imports -- you may add others but do not need to
import plotly.plotly as py
import plotly.graph_objs as go

import csv

# /////////////////////////////////////////
# ////////// README Instructions //////////
# /////////////////////////////////////////

# Part 4: Visualize some data
# FILENAME: part4.py

    # Write code that uses plot.ly to create a bar chart representing the data you got in Part 1 about the most common nouns only in the Twitter data. More information about using plot.ly for bar chart creation can be found here: https://plot.ly/python/bar-charts/

    # You should use part4.py to do so.

    # You should create, as a result of part4.py, an image file of the bar chart: part4_viz_image.png.

    # Any bar chart representing your data about nouns is acceptable.

# ////////////////////////////////////////////
# /////////////// Start Coding ///////////////
# ////////////////////////////////////////////

# Code here should involve creation of the bar chart as specified in instructions
# And opening / using the CSV file you created earlier with noun data from tweets


data = [] # List of noun,count Tuples
nouns = [] # nouns
count = [] # count

# /////////////////////////////////////////////////////////
# ////////// Open the CSV and Load to Tuple List //////////
# /////////////////////////////////////////////////////////

with open('noun_data.csv.csv') as f:
    reader = csv.reader(f)
    next(reader) #skip username
    next(reader) #skip header
    for row in reader:
        data.append(row)

#print(data)

# ////////////////////////////////////////////////////////
# ////////// Sort Tuples to Noun & Count Lists  //////////
# ////////////////////////////////////////////////////////

for row in data:
    nouns.append(row[0])
    count.append(row[1])


#print(x)
#print(y)

# ///////////////////////////////////////////////////////
# ////////// Put Variables into Plotly Format  //////////
# ///////////////////////////////////////////////////////

data = [go.Bar(x=nouns,y=count)]

layout = go.Layout(title="Most Common Tweeted Nouns", xaxis=dict(title='NOUNS'), yaxis=dict(title='Count'))


# ////////////////////////////////////////
# ////////// KEEP AT THE BOTTOM //////////
# ////////////////////////////////////////

fig = go.Figure(data=data, layout=layout)
py.iplot(fig, filename='part4_viz_image.png')
