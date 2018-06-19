# these should be the only imports you need
import tweepy
import nltk
import json
import sys



# /////////////////////////////////////////
# ////////// README Instructions //////////
# /////////////////////////////////////////

# Part 1: Create a program to analyze the twitter timeline of a selected user.
    # FILENAME: part1.py

    # ARGUMENTS: the program takes two arguments--a twitter username and the number of tweets to analyze.

    # OUTPUT: the program outputs the following:

        # the user name
        # the number of tweets analyzed
        # the five most frequent verbs that appear in the analyzed tweets
        # the five most frequent nouns that appear in the analyzed tweets
        # the five most frequent adjectives that appear in the analyzed tweets
        # the number of original tweets (i.e., not retweets)
        # the number of times that the original tweets in the analyzed set were favorited
        # the number of times that the original tweets in the analyzed set were retweeted by others
        # To determine the five most frequent, ties should be broken alphabetically, capitals before lowercase. (Check out Python stable sorting for a relatively easy way to handle this.)

    # The program should also save a CSV file of the 5 most frequent nouns in the analyzed tweets, called noun_data.csv. You'll use this in Part 4!

    # NOTES:

        # use tweepy for accessing the Twitter API
        # Use NLTK for analyzing parts of speech. Use NLTK's default POS tagger and tagset (this will use the UPenn treebank tagset)--you do NOT need to install any taggers or tagsets into NLTK.
        # "stop words": ignore any words that do not start with an alphabetic character [a-zA-Z], and also ignore 'http', 'https', and 'RT' (these show up a lot in Twitter)
        # a "verb" is anything that is tagged VB*
        # a "noun" is anything that is tagged NN*
        # an "adjective" is anything that is tagged JJ*

    # SAMPLE OUTPUT:

        # mwnewman$ python3 get_tweets.py umsi 12
        # USER: umsi
        # TWEETS ANALYZED: 12
        # VERBS: are(4) being(3) is(3) improve(2) Join(2)
        # NOUNS: umsi(8) UMSI(8) students(5) Join(5) amp(5)
        # ADJECTIVES more(5) umsi(4) doctoral(2) new(2) social(2)
        # ORIGINAL TWEETS: 8
        # TIMES FAVORITED (ORIGINAL TWEETS ONLY): 26
        # TIMES RETWEETED (ORIGINAL TWEETS ONLY): 18

    # SAMPLE CSV FILE OUTPUT inside a .csv file

        # Noun,Number
        # umsi,8
        # UMSI,8
        # students,5
        # Join,5
        # amp,5


# Part 2: Create a Simple Database application

    # For part 2, you will create a program to access information in the Northwind database (included in the repository)


# ////////////////////////////////////////////
# /////////////// Start Coding ///////////////
# ////////////////////////////////////////////

# write your code here
# usage should be python3 part1.py <username> <num_tweets>
