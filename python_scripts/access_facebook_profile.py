import facebook
import sys

token = sys.argv[1]
usr_id = sys.argv[2]
graph = facebook.GraphAPI(token)
profile = graph.get_object(usr_id)
print(str(profile))
picture = graph.get_connections(id=profile['id'],connection_name='picture')
file = open('profile_pic.jpeg','w')
file.write(str(picture))
file.close()
