#!/usr/bin/python
import praw  # for reddit API
import json  # for data format
from os.path import exists as does_file_exist  # for checking if file exist
try:
    import our_secrets
except ImportError:
    print('ha! you are missing the secretsssssss')
    exit(1)  # exit with errrcode 1

# Define data structure
# lists for multiple submissions
list_of_data = []

# make an instance from Reddit class defined in praw module
# username and password is for write access, rest is for read only
reddit = praw.Reddit(client_id=our_secrets.client_id,
                     client_secret=our_secrets.client_secret,
                     user_agent=our_secrets.user_agent,
                     username=our_secrets.username,
                     password=our_secrets.password)

# TODO when no internet connectivity (or train wifi with long timeouts) skip getting the data and quit gracefully
# work with A subreddit
for submission in reddit.subreddit('documentaries').hot(limit=25):
    print(submission.title)
    # dictionary for details
    data = {'title': submission.title,
        'theURL':submission.url, 
	"score" : submission.ups}
    list_of_data.append(data)

# in first run, database.db does not exist, skip reading and appending
if does_file_exist('database.json'):
    # file exists, read the db, and load the data
    with open('database.json', 'r') as iowrap:  # write as bytes
        old_list_of_data = json.load(iowrap)  # load the data from iowrap instance
    print('INFO: Loaded \'databse.json\'')
    # put the old_list_of_data together with the new data
    # TODO don't duplicate the data, tip use sets to filter, based on some unique information in submission
    list_of_data = old_list_of_data + list_of_data
# write the db
with open('database.json', 'w') as iowrap:  # write as bytes
    json.dump(list_of_data, iowrap)  # save the data to iowrap instance
    print('INFO: Saved {0} items \'databse.json\''.format(len(list_of_data)))
