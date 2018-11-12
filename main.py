#!/usr/bin/python
import praw  # for reddit API
import pickle  # for pickleRICK
import our_secrets
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

# work with A subreddit
for submission in reddit.subreddit('documentaries').hot(limit=25):
    print(submission.title)


# TODO3 (hard) - append to the database:
# OR
# TODO3 (easier) - overwrite the database:
data = {'title': submission.title,
        'theURL':submission.url, 
		"score" : submission.ups}
if does_file_exist('database.db'):
    pass  # file exists, do nothing
    print('WARNING: \'databse.db\' exists, not writing anything')
else:
    with open('database.db', 'wb') as iowrap:  # write as bytes
        pickle.dump(data, iowrap)  # save the data to iowrap instance
