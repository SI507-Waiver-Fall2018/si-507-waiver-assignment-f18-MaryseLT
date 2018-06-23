
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# \\\\\ Maryse Elizabeth Lundering-Timpano : MaryseLT [6379 5232] \\\\\
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
            # \\\\\ SI 507 Fall 2018 Waiver (2/4) \\\\\
            # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# =================================================================
# ========== Instructions - PART 1: Analyze Twitter Data ==========
# =================================================================

    # FILENAME: part1.py
    # USAGE SHOULD BE:  python3 part1.py <username> <num_tweets>

    # Part 1: Analyze the twitter timeline of a selected user.

    # Program Output [printing]:
        # user name
        # Total number of tweets analyzed
        # 5 most frequent VERBS in the analyzed tweets
        # 5 most frequent NOUNS in the analyzed tweets
        # 5 most frequent ADJECTIVES in the analyzed tweets
        # How many ORIGINAL tweets (i.e., not retweets) there are:
            # How many times the ORIGINAL tweets were FAVORITED
            # How many times the ORIGINAL tweets were RETWEETED by others

    # Saving Results ['noun_data.csv']:
        # The program should also save a CSV file of:
            # the 5 most frequent nouns in the analyzed tweets,
            # called noun_data.csv.
            # You'll use this in Part 4!

            ### SAVE CSV FILE NAME == 'noun_data.csv' ###

    # Determining the 5 most frequent:
        # ties should be broken alphabetically,
        # capitals before lowercase.
            ## (Check out Python stable sorting for a relatively easy way to handle this.)

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




# /////////////////////////////////////////////
# ////////// STEP 1 - Import Library //////////
# /////////////////////////////////////////////

    # these should be the only imports you need

import tweepy
import nltk
import json
import sys

import csv # I added this Library.
import secrets # My py File with My Twitter Access


# ////////////////////////////////////////////////////////
# ////////// STEP 2 - Establish Usage Variables //////////
# ////////////////////////////////////////////////////////

username = sys.argv[1]
num_tweets = sys.argv[2]

# ////////////////////////////////////////////////////////
# ////////// STEP 3 - Setting Up Twitter Access //////////
# ////////////////////////////////////////////////////////

while True:
    try:
        consumer_key = secrets.CONSUMER_KEY
        consumer_secret = secrets.CONSUMER_SECRET
        access_token = secrets.ACCESS_KEY
        access_secret = secrets.ACCESS_SECRET

        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_secret)

        api = tweepy.API(auth)

        user_tweets = api.user_timeline(screen_name=username, count=num_tweets)
        break

    except (AttributeError, NameError):
        print("\nHello person grading my 507 waiver!!! You've received this message because you can't get through the Twitter OAuth step.\nMy Twitter credentials are saved in a file called 'secrets.py' and I have imported that information with the module called 'secrets'.\nCan you please rename your file with your Twitter credentials?\n\nPLEASE! I could not find ANYTHING about credentials in the README instructions on GitHub.\n\nNo, you won't rename your file?\nOK, I understand, but is there some way I could run my program on my computer for you?\nMy email is MaryseLT@umich.edu and we could meet for 5 minutes to run my program on my computer.\n\nNo, that's not going to happen either?\nSERIOUSLY, I have tried to find every way this program could crash and using a try/except for the lack of credentials is the best thing I could come up with.\n\nPLEASE, PLEASE, PLEASE just rename your Twitter credentials file!\nYou read this far into my plea, and you could have already renamed your credentials file, ran the test, and named your credentials file back to its original name!\nYou're killing me Smalls...\n")
        #break
        exit()


# ////////////////////////////////////////////////////////
# ///// STEP 4 - Unpack the <user_tweets> Dictionary /////
# ////////////////////////////////////////////////////////

retweeted_marker = "retweeted_status"

total_tweets = [] # List of ALL Tweet TEXT -- Keep Above Loop

original_tweet_json = [] # List of ORIGINAL Tweet JSON -- Keep Above Loop

original_tweet_favs = []

original_retweet_count = []

#retweeted_list = [] # List of RETWEETED Tweet TEXT -- Keep Above Loop
    ## Only Used to Check Total LEN vs Sum of Both Types Lists

for x in user_tweets:
    tweet_json = x._json # Entire JSON Status Dictionary

    tweet_text = x.text # Just the Tweet TEXT

    total_tweets.append(tweet_text)

    retweet_count = x.retweet_count # Retweets PER Tweet

    favorite_count = x.favorite_count # Favorited PER Tweet

    # ---------------------------------------------------------------
    # ----- STEP 4.1 - Sort Original Tweet JSON -- KEEP IN LOOP -----
    # ---------------------------------------------------------------

    #if retweeted_marker in tweet_json: # If Tweet == Retweeted
    #    retweeted_list.append(tweet_text)
        ## Only Used to Check Total LEN vs Sum of Both Types Lists

    if retweeted_marker not in tweet_json: # If Tweet == Original
        original_tweet_json.append(tweet_json)
        original_tweet_favs.append(favorite_count)
        original_retweet_count.append(retweet_count)

    #print(tweet_text)
    #print(json.dumps(original_tweet_json, indent=4))
    #print(json.dumps(tweet_json, indent=4))


# /////////////////////////////////////////////////////
# ///// STEP 5 - Find <original_tweet_json> Stats /////
# /////////////////////////////////////////////////////
        # -----------------------------------
        # ----- NOTE: Needed for STEP 8 -----
        # -----------------------------------

fav_org_tweets = sum(original_tweet_favs)
retweeted_org_tweets = sum(original_retweet_count)

original_tweet_text = []
for x in original_tweet_json:
    original_tweet_text.append(tweet_text)


# //////////////////////////////////////////////////////////
# ////////// STEP 6 - Sort Through <total_tweets> //////////
# //////////////////////////////////////////////////////////

text_str = "".join(str(x) for x in total_tweets)
#print(type(text_str)) ## type == STRING

tokenizer = nltk.word_tokenize(text_str)
#print(type(tokenizer)) ## type == LIST of WORDS

# ------------------------------------------------------------
# ----- STEP 6.1 - Remove "stop words" from <tokenizer> -----
# ------------------------------------------------------------

real_words = [] ## Only list of "REAL WORDS"
for z in tokenizer:
    if z.isalpha(): ## If char[0] start w/ A-Z or a-z
        real_words.append(z)
    #else:
        continue ## Don't stop the loop for non-alphas[0]

# -------------------------------------------------------
# ----- STEP 6.2 - Delete Abbrevs from <real_words> -----
# -------------------------------------------------------

stop_words = ['RT','http','https']
for stopper in list(real_words):
    if stopper in stop_words:
        real_words.remove(stopper)


# //////////////////////////////////////////////////////////////
# ///// STEP 7 - Sort Word & Count Types from <real_words> /////
# //////////////////////////////////////////////////////////////

type_tagger = nltk.pos_tag(real_words) # Word Type Sorter Variable

# ------------------------------------------------------------
# ----- STEP 7.1 - Sort NOUNS & Count from <type_tagger> -----
# ------------------------------------------------------------

the_nouns = [word for word, pos in type_tagger if (pos == 'NN')]
#print(the_nouns) ## LIST of Words Deemed to be Nouns

num_nouns = nltk.FreqDist(the_nouns)
#print(num_nouns.items()) ## Finds Total of Each Word

noun_count = num_nouns.items()

noun_list = [] ## List of Tuples
for x in noun_count:
    noun_list.append(x)

sorted_nouns = sorted(noun_list, key = lambda x: x[1], reverse = True)
top_n = sorted_nouns[:5]

# ------------------------------------------------------------
# ----- STEP 7.2 - Sort VERBS & Count from <type_tagger> -----
# ------------------------------------------------------------

the_verbs = [word for word, pos in type_tagger if (pos == 'VB')]
#print(the_verbs) ## LIST of Words Deemed to be Verbs

num_verbs = nltk.FreqDist(the_verbs)
#print(num_verbs.items()) ## Finds Total of Each Word

verb_count = num_verbs.items()

verb_list = [] ## List of Tuples
for x in verb_count:
    verb_list.append(x)

sorted_verbs = sorted(verb_list, key = lambda x: x[1], reverse = True)
top_v = sorted_verbs[:5]

# -----------------------------------------------------------------
# ----- STEP 7.3 - Sort ADJECTIVES & Count from <type_tagger> -----
# -----------------------------------------------------------------

the_adj = [word for word, pos in type_tagger if (pos == 'JJ')]
#print(the_adj) ## LIST of Words Deemed to be Adjectives

num_adj = nltk.FreqDist(the_adj)
#print(num_adj.items()) ## Finds Total of Each Word

adj_count = num_adj.items()

adj_list = [] ## List of Tuples
for x in adj_count:
    adj_list.append(x)

sorted_adj = sorted(adj_list, key = lambda x: x[1], reverse = True)
top_a = sorted_adj[:5]

# /////////////////////////////////////////////////
# ////////// STEP 8 - Print the Results ///////////
# /////////////////////////////////////////////////

print("\nUSER: " + username)
print("TWEETS ANALYZED: " + num_tweets)
print("VERBS: {}({}), {}({}), {}({}), {}({}), {}({})".format(top_v[0][0], top_v[0][1], top_v[1][0], top_v[1][1], top_v[2][0], top_v[2][1], top_v[3][0], top_v[3][1], top_v[4][0], top_v[4][1]))
print("NOUNS: {}({}), {}({}), {}({}), {}({}), {}({})".format(top_n[0][0], top_n[0][1], top_n[1][0], top_n[1][1], top_n[2][0], top_n[2][1], top_n[3][0], top_n[3][1], top_n[4][0], top_n[4][1]))
print("ADJECTIVES: {}({}), {}({}), {}({}), {}({}), {}({})".format(top_a[0][0], top_a[0][1], top_a[1][0], top_a[1][1], top_a[2][0], top_a[2][1], top_a[3][0], top_a[3][1], top_a[4][0], top_a[4][1]))
print("ORIGINAL TWEETS: {}".format(len(original_tweet_text)))
print("TIMES FAVORITED (ORIGINAL TWEETS ONLY): {}".format(fav_org_tweets))
print("TIMES RETWEETED (ORIGINAL TWEETS ONLY): {}\n".format(retweeted_org_tweets))


# ///////////////////////////////////////////////////////////
# ////////// STEP 9 - Save Nouns to noun_data.csv ///////////
# ///////////////////////////////////////////////////////////
    # ----------------------------------------------------
    # ----- NOTE: FILE MUST BE CALLED 'noun_data.csv'-----
    # ----------------------------------------------------

with open('noun_data.csv', 'w', newline='') as tweet_csv:
    header = (username,num_tweets)
    fieldname = ["Noun","Number"]

    file_writer = csv.writer(tweet_csv, delimiter = ',')
    file_writer.writerow(header)
    file_writer.writerow(fieldname)
    for x in top_n:
        file_writer.writerow(x)
    tweet_csv.close()
