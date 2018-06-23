
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\ Maryse Elizabeth Lundering-Timpano : MaryseLT [6379 5232] \\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            # \\\\\ SI 507 Fall 2018 Waiver (3/4) \\\\\
            # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# ======================================================================
# ========== Instructions - PART 3: Scrape the Michigan Daily ==========
# ======================================================================

    # FILENAME: part3.py
    # USAGE SHOULD BE: python3 part3.py

    # In part 3, you will:

        # 1. use Beautiful Soup to scrape the MOST READ stories from the Michigan Daily site (http://michigandaily.com),

        # 2. and will crawl ONE LEVEL DEEPER to find the AUTHOR of each Most Read story.


# /////////////////////////////////////////////
# ////////// STEP 1 - Import Library //////////
# /////////////////////////////////////////////

    # these should be the only imports you need

import requests
from bs4 import BeautifulSoup

# /////////////////////////////////////////////////////
# ////////// STEP 2 - Scraping the Home Page //////////
# /////////////////////////////////////////////////////

baseurl = 'https://www.michigandaily.com'
html = requests.get('https://www.michigandaily.com/').text
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

searching_div = soup.find(id='mini-panel-right_sidebar_standard')
#print(searching_div)

most_read = searching_div.find_all('li') # Most Read HTML Headlines & Urls

headlines = [] # List of Home Page Most Read Headlines -- Keep Above Loop
for h in most_read:
    # print(h.text) # Just Headline Text
    headlines.append(h.text)

most_read_urls = [] # List of Individual Page URLS -- Keep Above Loop
for y in most_read:
    most_read_urls.append(baseurl + y.a['href']) # URL to each headline

#print(most_read_urls)

# //////////////////////////////////////////////////////
# ////////// STEP 3 - Scrape Individual Pages //////////
# //////////////////////////////////////////////////////

author_list = [] # List of Individual Page Authors -- Keep Above loop

for abc in most_read_urls:
    url = '{}'.format(abc) # Variable that Holds a URL Each Loop
    #print(url)
    each_story = requests.get(url).text # Making A Page Request
    story_soup = BeautifulSoup(each_story, 'html.parser')

    # ----------------------------------------------------------
    # ----- Finding the Author : STAY INSIDE  REQUEST LOOP -----
    # ----------------------------------------------------------

    author_section = story_soup.find(class_='byline')

    if author_section is not None: # If Up-to-Date HTML
        author_text = author_section.find('a') # Author HTML
        author = author_text.text # Author Text
        author_list.append(author)

    else:
        if author_section is None: # If Out-Dated HTML
            author = "The Michigan Daily HTML format has changed dramatically over the years, and in this case my scraping code can't find an author."
            author_list.append(author)

    #print(author)

# /////////////////////////////////////////////
# ////////// STEP 4 - Format & Print //////////
# /////////////////////////////////////////////

headline_authors = {} # Dict of [Headlines:Authors] -- Keep Above Loop

for x in range(len(headlines)):
    headline_authors[headlines[x]] = author_list[x]

print("Michigan Daily -- MOST READ\n")

for x,y in headline_authors.items():
   print(x)
   print("     by " + y +"\n")
