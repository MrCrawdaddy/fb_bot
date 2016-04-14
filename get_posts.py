import facebook
import sys

def main():
    if len(sys.argv) > 0:
        token = sys.argv[1]
        the_id = sys.argv[2]
        graph = facebook.GraphAPI(token)
        profile = graph.get_object(the_id)
        posts = graph.get_connections(profile['id'],'posts')
        the_file = open('post_json.txt','w')
        for post in posts['data']:
            the_file.write(str(post))
        the_file.close()

main()
