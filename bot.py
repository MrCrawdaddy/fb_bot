from db_fetchers import UserFetcher, PreferencesFetcher
from content_fetchers import RedditFetcher
from content_posters import FacebookPoster
from datetime import datetime, timedelta
import pickle
import os.path


user_fetcher = UserFetcher("db.sqlite3")
preferences_fetcher = PreferencesFetcher("db.sqlite3")
id_list = user_fetcher.fetch_auth_users()
post_tracker = {}
time_tracker = {}
if(os.path.isfile("save.p")):
    post_tracker = pickle.load(open("save.p", "rb"))
    time_tracker = pickle.load(open("save.p", "rb"))
else:
    for id in id_list:
        post_tracker[id] = []
        time_tracker[id] = datetime.now()
for id in id_list:
    if time_tracker[id] < datetime.now():
        subreddit_list = preferences_fetcher.fetch_sub_preference(id)
        reddit_fetcher = RedditFetcher(
            subreddit_list=subreddit_list, previous_posts=post_tracker[id])
        content = reddit_fetcher.fetch_content()
        auth_token = user_fetcher.fetch_auth_token(id)
        facebook_poster = FacebookPoster(auth_token)
        facebook_poster.post(content)
        time_to_add = preferences_fetcher.fetch_time_preference(id)
        time_tracker[id] = datetime.now(
        ) + timedelta(hours=time_to_add)
pickle.dump(post_tracker, open("save.p", "wb"))
pickle.dump(time_tracker, open("save.p", "wb"))
