# these should be the only imports you need

import requests
from bs4 import BeautifulSoup


# /////////////////////////////////////////
# ////////// README Instructions //////////
# /////////////////////////////////////////

# Part 3: Scrape the Michigan Daily
# FILENAME: part3.py

    # In part 3, you will use Beautiful Soup to scrape the Most Read stories from the Michigan Daily site (http://michigandaily.com), and will crawl one level deeper to find the author of each Most Read story.

    # SAMPLE OUTPUT:

        # dhcp3-213:507waiver2 mwnewman$ python3 part3.py

        # Michigan Daily -- MOST READ
        # Darkness and the Occult: A brief history of doom metal
        #   by Selena Aguilera
        # "The white rice was excellent. Followed the directions on the bag perfectly. Way to go."
        #   by Hunter Zhao
        # Schlissel: "I try not to have a personal opinion" on potential C.C. Little renaming, awaiting further review
        #   by Alexa St. John
        # A guide to Michigan's 2018 gubernatorial race
        #   by Colin Beresford

    # NOTES: If there is more than one reporter, you only need to print the first name on the byline.


# ////////////////////////////////////////////
# /////////////// Start Coding ///////////////
# ////////////////////////////////////////////

# write your code here
# usage should be python3 part3.py
