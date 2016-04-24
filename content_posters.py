import facebook


class FacebookPoster():

    def __init__(self, auth_token):
        self.graph = facebook.GraphAPI(auth_token)

    def post(self, content):
        attachment = {
            'name': '',
            'link': content['url'],
            'caption': content['title'],
            'description': content['selftext'],
            'picture': ''
        }
        try:
            self.graph.put_wall_post(message='test',attachment=attachment)
        except facebook.GraphAPIError as err:
            print(str(err))
