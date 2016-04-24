import pprint
import praw
r = praw.Reddit(user_agent='example')
for submission in r.get_front_page(limit=5):
    pprint.pprint(vars(submission))
