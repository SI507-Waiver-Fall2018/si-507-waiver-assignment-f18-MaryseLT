# these should be the only imports you need
import tweepy
import nltk
import json
import sys

import secrets

# /////////////////////////////////////////
# ////////// README Instructions //////////
# /////////////////////////////////////////

# Part 1: Create a program to analyze the twitter timeline of a selected user.
    # FILENAME: part1.py

    # ARGUMENTS: the program takes two arguments--a twitter username and the number of tweets to analyze.
        #sys.argv[1]
        #sys.argv[2]

    # OUTPUT: the program outputs the following:

        # the user name  == ##'screen_name'
        # the number of tweets analyzed  == ##'count'
        # the five most frequent verbs that appear in the analyzed tweets
        # the five most frequent nouns that appear in the analyzed tweets
        # the five most frequent adjectives that appear in the analyzed tweets
        # the number of original tweets (i.e., not retweets) == ##'include_rts'
        # the number of times that the original tweets in the analyzed set were favorited
        # the number of times that the original tweets in the analyzed set were retweeted by others
        # To determine the five most frequent, ties should be broken alphabetically, capitals before lowercase. (Check out Python stable sorting for a relatively easy way to handle this.)

    # The program should also save a CSV file of the 5 most frequent nouns in the analyzed tweets, called noun_data.csv. You'll use this in Part 4!

    # NOTES:

        # use tweepy for accessing the Twitter API
        # Use NLTK for analyzing parts of speech.
            # Use NLTK's default POS tagger and tagset (this will use the UPenn treebank tagset)--you do NOT need to install any taggers or tagsets into NLTK.
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

username = sys.argv[1]
num_tweets = sys.argv[2]

# ////////////////////////////////////////////////
# ////////// STEP 1 - Setting Up Access //////////
# ////////////////////////////////////////////////

consumer_key = secrets.CONSUMER_KEY
consumer_secret = secrets.CONSUMER_SECRET
access_token = secrets.ACCESS_KEY
access_secret = secrets.ACCESS_SECRET

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

user_tweets = api.user_timeline(screen_name=username, count=num_tweets)


# /////////////////////////////////////////////////////
# ////////// STEP 2 - Sorting Through Tweets //////////
# /////////////////////////////////////////////////////
the_tweets = []
for tweet in user_tweets:
    the_tweets.append(tweet.text.lower())

    #print(tweet.text) ## Non list format (just text)
    #print(the_tweets) ## List format (inside [])
#print(type(the_tweets))




# //////////////////////////////////////////////////////
# ////////// STEP 3 - Sorting Through Cache ///////////
# /////////////////////////////////////////////////////


#text_res = []
#for abc in the_tweets:
#    text_res.append(abc.get('text'))

text_str = "".join(str(x) for x in the_tweets) ## Now it's a string
#print(type(text_str))
tokenizer = nltk.word_tokenize(text_str) ## List of words, not letters
#print(type(tokenizer))
dictt = nltk.FreqDist(tokenizer)


# ///////////////////////////////////////////
# ////////// Removing "stop words" //////////
# ///////////////////////////////////////////

real_words = []
for z in tokenizer:
    if z.isalpha():
        real_words.append(z)
    #else:
        continue

    word_counter = nltk.FreqDist(real_words)
    #dictt = nltk.pos_tag(tokenizer)
sorted_dict = sorted(word_counter.items(), key= lambda x: x[1], reverse = True) # List of tuples

#print(sorted_dict)

# //////////////////////////////////////////////////////
# ////////// Deleting Abbrevs from Words LIST //////////
# //////////////////////////////////////////////////////

stop_words = ['RT','http','https']
for stopper in list(real_words):
    if stopper in stop_words:
        real_words.remove(stopper)


    word_counter = nltk.FreqDist(real_words)
#print(word_counter)

tup_list = nltk.pos_tag(real_words) ## My LIST of unsorted word types

nouns = []

for word,pos in tup_list:
    if pos == 'NN':
        nouns.append(word)
print(nouns)

noun_count = []
for word,freq in sorted_dict:
    if word in nouns:
        #noun_count.append(word)

#print(noun_count)



# /////////////////////////////////////////
# ////////// Most Frequent Words //////////
# /////////////////////////////////////////

sorted_list = sorted(tup_list, key = lambda x: x[1], reverse = False)
#print(sorted_list)


# sorted_dict = sorted(dictt.items(), key= lambda x: x[1], reverse = True)
# final_sort = sorted_dict[:5]

#print("USER: {}\nTWEETS ANALYZED: {}\nThe 5 Most Frequent Words: {}\n".format(username, num_tweets, final_sort))

# ////////////////////////////////////
# ////////// Types of Words //////////
# ////////////////////////////////////


#for word,variations in sorted(word_type):
#    print(word,variations)

        # a "verb" is anything that is tagged VB*
        # a "noun" is anything that is tagged NN*
        # an "adjective" is anything that is tagged JJ*




# ////////////////////////////////////////////////////
# ////////// STEP 4 - Printing the Results ///////////
# ////////////////////////////////////////////////////

#print("USER: " + username)
#print("TWEETS ANALYZED" + num_tweets)
#print("VERBS: {}{()}, {}{()}, {}{()}, {}{()}, {}{()}".format(?))
#print("NOUNS: {}{()}, {}{()}, {}{()}, {}{()}, {}{()}".format(?))
#print("ADJECTIVES: {}{()}, {}{()}, {}{()}, {}{()}, {}{()}".format(?))
#print("ORIGINAL TWEETS: {}".format(?))
#print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): {}".format(?))
#print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): {}".format(?))


# ///////////////////////////////////////////////////////
# ////////// STEP 5 - Saving Results in a CSV ///////////
# ///////////////////////////////////////////////////////


    # SAMPLE CSV FILE OUTPUT inside a .csv file

        # Noun,Number
        # umsi,8
        # UMSI,8
        # students,5
        # Join,5
        # amp,5

#tweet_csv = open('twitter_results.csv', 'w', newline='')
#file_writer = csv.writer(tweet_csv)
#for tweet in #<analyzed list variable>:
#    file_writer.writerow(Noun,Number)
#    file_writer.writerow(username,num_tweets)
#    file_writer.writerow(<var>,<count>)
#tweet_csv.close()

# //////////////////////////////////////////////////////////
# ////////// Part 2 - Simple Database Application //////////
# //////////////////////////////////////////////////////////
