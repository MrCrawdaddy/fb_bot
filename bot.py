from db_fetchers import UserFetcher, PreferencesFetcher
from content_fetchers import RedditFetcher
from content_posters import FacebookPoster
from datetime import datetime, timedelta
import pickle, os.path, time


try:
    user_fetcher = UserFetcher("db.sqlite3")
    preferences_fetcher = PreferencesFetcher("db.sqlite3")
    id_list = user_fetcher.fetch_auth_users()
    post_tracker = {}
    time_tracker = {}

    if(os.path.isfile("save.p")):
        with open("save.p", "rb") as f:
            post_tracker = pickle.load(f)
            time_tracker = pickle.load(f)
            f.close()
    else:
        for id in id_list:
            post_tracker[id] = []
            time_tracker[id] = datetime.now()
except Exception as err:
    print(err)

while True:
    try:
        id_list = user_fetcher.fetch_auth_users()
        for id in id_list:
            if id not in post_tracker.keys():
                post_tracker[id] = []
            if id not in time_tracker.keys():
                time_tracker[id] = datetime.now()
            try:
                if time_tracker[id] < datetime.now():
                    subreddit_list = preferences_fetcher.fetch_sub_preference(id)
                    reddit_fetcher = RedditFetcher(
                        subreddit_list=subreddit_list, previous_posts=post_tracker[id])
                    content = reddit_fetcher.fetch_content()
                    auth_token = user_fetcher.fetch_auth_token(id)
                    facebook_poster = FacebookPoster(auth_token)
                    facebook_poster.post(content)
                    post_tracker[id].append(content['id'])
                    time_to_add = preferences_fetcher.fetch_time_preference(id)
                    time_tracker[id] = datetime.now(
                    ) + timedelta(hours=time_to_add)
            except KeyError as err:
                print(str(err))
                pass

        with open("save.p", "wb") as f:
            pickle.dump(post_tracker, f)
            pickle.dump(time_tracker, f)
            f.close()
        time.sleep(5)
    except Exception as err:
        print(err)
        time.sleep(5)
        pass
