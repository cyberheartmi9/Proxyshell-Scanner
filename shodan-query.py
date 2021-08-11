import requests
import shodan
requests.packages.urllib3.disable_warnings()


API_KEY=""
SEARCH_FOR="http.favicon.hash:1768726119"

f=open("url.txt","a")


api = shodan.Shodan(API_KEY)

result = api.search(SEARCH_FOR,limit=1000)


for service in result['matches']:
    IP = service['ip_str']
    url="https://{}".format(IP)
    f.writelines(url+"\n")


