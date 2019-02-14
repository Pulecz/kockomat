#!/usr/bin/python
import praw  # for reddit API
import sqla  # for sqliteDB
from os.path import exists as does_file_exist  # for checking if file exist
try:
    import our_secrets
except ImportError:
    print('ha! you are missing the secretsssssss')
    exit(1)  # exit with errrcode 1

# make an instance from Reddit class defined in praw module
# username and password is for write access, rest is for read only
reddit = praw.Reddit(client_id=our_secrets.client_id,
                     client_secret=our_secrets.client_secret,
                     user_agent=our_secrets.user_agent,
                     username=our_secrets.username,
                     password=our_secrets.password)

# TODO when no internet connectivity (or train wifi with long timeouts)
# skip getting the data and quit gracefully


# Define data structure
# dict for multiple submissions
# the reddit's submission ID will be the primary key
dict_of_data = {}

# work with A subreddit
for submission in reddit.subreddit('documentaries').new(limit=10):
    # print("Title: {0}\nscore: {1}\n".format(
        # submission.title, submission.ups))
    # dictionary for details
    data = {'id': submission.id,
            'title': submission.title,
            'targetURL': submission.url,
            'redditURL': submission.shortlink,
            "score": submission.ups}
    dict_of_data[data['id']] = data

# TODO print submissions with highest score first

# in first run, database.db does not exist
# skip reading and appending continue at write the db
if does_file_exist('database.db'):
    # file exists, read the db, and load the data
    sqla.metadata.create_all(sqla.engine)
# write the db
conn = sqla.engine.connect()
ins = sqla.prispevky.insert()
for prispevek in dict_of_data:
    conn.execute(ins, id=dict_of_data[prispevek]['id'],
                 title=dict_of_data[prispevek]['title'],
                 targetURL=dict_of_data[prispevek]['targetURL'],
                 redditURL=dict_of_data[prispevek]['redditURL'],
                 score=dict_of_data[prispevek]['score'])
