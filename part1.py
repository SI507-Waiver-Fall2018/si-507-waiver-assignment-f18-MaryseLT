# these should be the only imports you need
import tweepy
import nltk
import json
import sys

import csv
import secrets # my py file containing my twitter access requirements


# Part 1: Create a program to analyze the twitter timeline of a selected user.
    # FILENAME: part1.py

    # ARGUMENTS: the program takes two arguments--a twitter username and the number of tweets to analyze.

    # OUTPUT: the program outputs the following:

        # the user name  == ##'screen_name'
        # the number of tweets analyzed  == ##'count'
        # the five most frequent verbs that appear in the analyzed tweets
        # the five most frequent nouns that appear in the analyzed tweets
        # the five most frequent adjectives that appear in the analyzed tweets
        # the number of original tweets (i.e., not retweets) ==                ##'include_rts=false'
        # the number of times that the original tweets in the analyzed set were favorited
        # the number of times that the original tweets in the analyzed set were retweeted by others
        # To determine the five most frequent, ties should be broken alphabetically, capitals before lowercase. (Check out Python stable sorting for a relatively easy way to handle this.)

    # The program should also save a CSV file of the 5 most frequent nouns in the analyzed tweets, called noun_data.csv. You'll use this in Part 4!

    # SAVE CSV FILE NAME == 'noun_data.csv'

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
    #,include_rts='false')


# ///////////////////////////////////////////////////
# ////////// STEP 2 - Unpacking the ._json //////////
# ///////////////////////////////////////////////////

# ---------- Total Tweet Text ----------
total_tweets = []
retweeted_list = []
original_tweet_json = []

retweeted_marker = "retweeted_status"

for x in user_tweets:
    tweet_json = x._json # Entire json dict of the status

    retweet_count = x.retweet_count # Yes, the number of times a SINGLE tweet was retweeted
    favorite_count = x.favorite_count # Tells the number of times a SINGLE tweet was retweeted
    retweet_finder = x.retweeted # Tells whether the tweet was retweeted
    tweet_text = x.text # Prints out just the text of the tweet
    total_tweets.append(tweet_text)
    #print(tweet_text)

    if retweeted_marker in tweet_json:
        retweeted_list.append(tweet_text)

    if retweeted_marker not in tweet_json:
        original_tweet_json.append(tweet_json)


    #print(json.dumps(original_tweet_json, indent=4))
    #print(json.dumps(tweet_json, indent=4))

#print(len(retweeted_list))
#print(len(original_tweet_json))



# ////////////////////////////////////////////////////////////
# ////////// STEP 3 - FINDING ORIGINAL TWEET STATS //////////
# //////////////////////////////////////////////////////////

original_tweet_text = []
fav_org_tweets = 0
retweeted_org_tweets = 0


for x in original_tweet_json:
    original_tweet_text.append(tweet_text)
    fav_org_tweets = favorite_count + fav_org_tweets

    retweeted_org_tweets = retweet_count + retweeted_org_tweets

#for x in favorite_count:
#    fav_org_tweets.append(int(x))

#print(fav_org_tweets)


#print(len(original_tweet_text))
#print(fav_org_tweets)
#print(retweeted_org_tweets)


# /////////////////////////////////////////////////////////
# ////////// STEP 4 - Sorting Through All Tweets //////////
# /////////////////////////////////////////////////////////

#print(len(total_tweets))
text_str = "".join(str(x) for x in total_tweets) ## Now it's a string
#print(len(text_str))
#print(type(text_str))
tokenizer = nltk.word_tokenize(text_str) ## List of words, not letters
#print(type(tokenizer))
#dictt = nltk.FreqDist(tokenizer)


    # ///////////////////////////////////////////
    # ////////// Removing "stop words" //////////
    # ///////////////////////////////////////////

real_words = []
for z in tokenizer:
    if z.isalpha():
        real_words.append(z)
    #else:
        continue

    #word_counter = nltk.FreqDist(real_words)

    # //////////////////////////////////////////////////////
    # ////////// Deleting Abbrevs from Words LIST //////////
    # //////////////////////////////////////////////////////

stop_words = ['RT','http','https']
for stopper in list(real_words):
    if stopper in stop_words:
        real_words.remove(stopper)

    #tup_list = nltk.pos_tag(real_words) ## My LIST of unsorted word types

# del word_counter['RT']
# del word_counter['http']
# del word_counter['https']


# ////////////////////////////////////////////
# ////////// Sorting Types of Words //////////
# ////////////////////////////////////////////

# nouns = []
# verbs = []
# adjectives = []
#
#
#
# for word,pos in tup_list:
#     if pos == 'NN':
#         nouns.append(word)
#     if pos == 'VB':
#         verbs.append(word)
#     if pos == 'JJ':
#         adjectives.append(word)

#print(nouns)
#print(verbs)
#print(adjectives)


tagged = nltk.pos_tag(real_words) # tagged variable


# ////////// NOUNS //////////

the_nouns = [word for word, pos in tagged if (pos == 'NN')]
#print(the_nouns)
num_nouns = nltk.FreqDist(the_nouns)
#print(num_nouns.items())

noun_list = []
noun_count = num_nouns.items()
for x in noun_count:
    noun_list.append(x)


# ////////// VERBS //////////

the_verbs = [word for word, pos in tagged if (pos == 'VB')]
#print(the_verbs)

num_verbs = nltk.FreqDist(the_verbs)
#print(num_verbs.items())

verb_list = []
verb_count = num_verbs.items()
for x in verb_count:
    verb_list.append(x)

# ////////// ADJECTIVES //////////

the_adj = [word for word, pos in tagged if (pos == 'JJ')]
#print(the_adj)

num_adj = nltk.FreqDist(the_adj)
#print(num_adj.items())

adj_list = []
adj_count = num_adj.items()
for x in adj_count:
    adj_list.append(x)


# /////////////////////////////////////////
# ////////// Most Frequent Words //////////
# /////////////////////////////////////////

sorted_adj = sorted(adj_list, key = lambda x: x[1], reverse = True)
top_a = sorted_adj[:5]

sorted_nouns = sorted(noun_list, key = lambda x: x[1], reverse = True)
top_n = sorted_nouns[:5]

#common_nouns = {}
#for x,y in top_n:
#    common_nouns[x]=y

#for x,y in common_nouns.items():
#    print(x,y)


sorted_verbs = sorted(verb_list, key = lambda x: x[1], reverse = True)
top_v = sorted_verbs[:5]


# ////////////////////////////////////////////////////
# ////////// STEP 4 - Printing the Results ///////////
# ////////////////////////////////////////////////////

print("USER: " + username)
print("TWEETS ANALYZED: " + num_tweets)
print("VERBS: {}({}), {}({}), {}({}), {}({}), {}({})".format(top_v[0][0], top_v[0][1], top_v[1][0], top_v[1][1], top_v[2][0], top_v[2][1], top_v[3][0], top_v[3][1], top_v[4][0], top_v[4][1]))
print("NOUNS: {}({}), {}({}), {}({}), {}({}), {}({})".format(top_n[0][0], top_n[0][1], top_n[1][0], top_n[1][1], top_n[2][0], top_n[2][1], top_n[3][0], top_n[3][1], top_n[4][0], top_n[4][1]))
print("ADJECTIVES: {}({}), {}({}), {}({}), {}({}), {}({})".format(top_a[0][0], top_a[0][1], top_a[1][0], top_a[1][1], top_a[2][0], top_a[2][1], top_a[3][0], top_a[3][1], top_a[4][0], top_a[4][1]))
print("ORIGINAL TWEETS: {}".format(len(original_tweet_text)))
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): {}".format(fav_org_tweets))
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): {}".format(retweeted_org_tweets))


# ///////////////////////////////////////////////////////
# ////////// STEP 5 - Saving Results in a CSV ///////////
# ///////////////////////////////////////////////////////


with open('noun_data.csv', 'w', newline='') as tweet_csv:
    header = (username,num_tweets)
    fieldname = ["Noun","Number"]

    file_writer = csv.writer(tweet_csv, delimiter = ',')
    file_writer.writerow(header)
    file_writer.writerow(fieldname)
    for x in top_n:
        file_writer.writerow(x)
    tweet_csv.close()
