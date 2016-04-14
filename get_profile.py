import urllib.request
import sys

def main():
    access_token = str(sys.argv[1])
    usr_id = str(sys.argv[2])
    url = "https://graph.facebook.com/v2.5/" + usr_id + "/picture?type=large&access_token=" + access_token
    http_response = urllib.request.urlopen(url=url)
    print(http_response.geturl())
    return http_response.geturl()

main()
