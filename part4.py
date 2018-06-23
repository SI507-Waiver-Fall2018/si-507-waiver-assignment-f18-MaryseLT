
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\ Maryse Elizabeth Lundering-Timpano : MaryseLT [6379 5232] \\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            # \\\\\ SI 507 Fall 2018 Waiver (4/4) \\\\\
            # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ==================================================================
# ========== Instructions - PART 4: Visualize PART 1 Data ==========
# ==================================================================

    # FILENAME: part4.py

    # Write code that uses plot.ly to create:
        # a BAR chart
        # representing the data you got in PART 1
        # about the MOST COMMON NOUNS ONLY
        # in the TWITTER data.
            #More information about using plot.ly for bar chart creation can be found here: https://plot.ly/python/bar-charts/

    # You should create, as a result of part4.py:
        # an image file of the bar chart:

            ### part4_viz_image.png. [<- == filename?]

        # ANY BAR CHART representing your data about nouns is ACCEPTABLE.

        # And opening / using the CSV file you created earlier with noun data from tweets part1.py

            ### part1.py csv file == noun_data.csv


# /////////////////////////////////////////////
# ////////// STEP 1 - Import Library //////////
# /////////////////////////////////////////////

    # Imports -- you may add others but do not need to

import plotly.plotly as py
import plotly.graph_objs as go

import csv # I added this library.

# ////////////////////////////////////////////////////////////////
# ////////// STEP 2 - Open the CSV & Load to Tuple List //////////
# ////////////////////////////////////////////////////////////////

data = [] # List of noun,count Tuples

with open('noun_data.csv') as f:
    reader = csv.reader(f)
    next(reader) #skip username
    next(reader) #skip header
    for row in reader:
        data.append(row)

#print(data)

# /////////////////////////////////////////////////////////////////
# ////////// STEP 3 - Sort Tuples to Noun & Count Lists  //////////
# /////////////////////////////////////////////////////////////////

nouns = [] # List of Only NOUNS
count = [] # List of Only COUNT

for row in data:
    nouns.append(row[0])
    count.append(row[1])

#print(nouns)
#print(count)

# ///////////////////////////////////////////////////////////////
# ////////// STEP 4 - Put Variables into Plotly Format //////////
# ///////////////////////////////////////////////////////////////

# X axis == nouns
# Y axis == count

data = [go.Bar(x=nouns,y=count)]

layout = go.Layout(title="Most Common Tweeted Nouns", xaxis=dict(title='NOUNS'), yaxis=dict(title='Count'))


# ---------------------------------------------
# ---------- KEEP AT THE VERY BOTTOM ----------
# ---------------------------------------------

fig = go.Figure(data=data, layout=layout)
    # First Param - Instructions

py.iplot(fig, filename='part4_viz_image')
    # Only Accepts 2 Params: Instructions Variable & Filename for the Chart
