import praw


class RedditFetcher():

    def __init__(self, subreddit_list, previous_posts):
        self.subs = subreddit_list
        self.previous_posts = previous_posts
        self.source = praw.Reddit(user_agent="Reddit Content Fetcher for localhost")

    def fetch_content_list(self):
        content_list = []
        for sub in self.subs:
            submissions = self.source.get_subreddit(sub).get_top(limit=5)
            for submission in submissions:
                submission_content = vars(submission)
                if submission_content['id'] not in self.previous_posts:
                    content_list.append({
                        'title': submission_content['title'],
                        'url': submission_content['url'],
                        'selftext': submission_content['selftext'],
                        'ups': submission_content['ups'],
                        'id':  submission_content['id'],
                    })
        return content_list

    def fetch_content(self):
        content_list = self.fetch_content_list()
        most_ups_tracker = {'ups': 0, 'index': 0}
        for index, content in enumerate(content_list):
            content = content_list[index]
            if content['ups'] > most_ups_tracker['ups']:
                most_ups_tracker['ups'] = content['ups']
                most_ups_tracker['index'] = index
        content = content_list[most_ups_tracker['index']]
        return content
