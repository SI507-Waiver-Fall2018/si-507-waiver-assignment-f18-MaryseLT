# these should be the only imports you need

import requests
from bs4 import BeautifulSoup


# /////////////////////////////////////////
# ////////// README Instructions //////////
# /////////////////////////////////////////

# Part 3: Scrape the Michigan Daily
# FILENAME: part3.py

    # In part 3, you will use Beautiful Soup to scrape the Most Read stories from the Michigan Daily site (http://michigandaily.com), and will crawl one level deeper to find the author of each Most Read story.


# ////////////////////////////////////////////
# /////////////// Start Coding ///////////////
# ////////////////////////////////////////////

# write your code here
# usage should be python3 part3.py

# ////////////////////////////////////////////
# ////////// Scraping the Home Page //////////
# ////////////////////////////////////////////

baseurl = 'https://www.michigandaily.com'
html = requests.get('https://www.michigandaily.com/').text
soup = BeautifulSoup(html, 'html.parser')
#print(soup.prettify())

searching_div = soup.find(id='mini-panel-right_sidebar_standard')
#print(searching_div)

most_read = searching_div.find_all('li') # Most Read Headlines & Urls

headlines = []
for h in most_read:
    headlines.append(h.text)
#    #print(h.text) # Just Headline Text

most_read_urls = []
for y in most_read:
    most_read_urls.append(baseurl + y.a['href']) # Url to each headline

#print(most_read_urls)

# ////////////////////////////////////////////////
# ////////// Searching Individual Pages //////////
# ////////////////////////////////////////////////

headline_authors = {} # Healines: Authors Dict; Keep Above Loop
author_list = [] # Keep Above loop

for abc in most_read_urls:
    url = '{}'.format(abc)
    #print(url)
    each_story = requests.get(url).text # Making Each Page Request
    story_soup = BeautifulSoup(each_story, 'html.parser')


    # ///////////////////////////////////
    # ////////// Headline Text //////////
    # ///////////////////////////////////

    #headline_section = story_soup.find(class_='tmdleft') # Overall

    #headline_text = headline_section.find('h2') # Specific Section
    ##print(headline_text)

    #if len(headline_text) == 0: # In case of old HTML
    #    headline = "The Most Read headline html format has changed dramatically over the years, and in this case my scraping code can't find it.\n"

    #else:
    #    element in headline_text: # If current HTML
        ##headline = element.text
    #    print(element)

    ##print(headline)


    # /////////////////////////////////
    # ////////// Author Text //////////
    # /////////////////////////////////


    author_section = story_soup.find(class_='byline')

    if author_section is not None: # If current HTML
        author_text = author_section.find('a')
        author = author_text.text
        author_list.append(author)

    else:
        if author_section is None: # If old HTML
            author = "The Michigan Daily HTML format has changed dramatically over the years, and in this case my scraping code can't find an author."
            author_list.append(author)


    #print(author)

for x in range(len(headlines)):
    headline_authors[headlines[x]] = author_list[x]

print("Michigan Daily -- MOST READ\n")

for x,y in headline_authors.items():
   print(x)
   print("     by " + y +"\n")
