import socket
import json
import requests
url =  'http://data.tmd.go.th/api/Station/v1/'

# response เป็น json
querystring = {'uid': 'u64teelak1113', 'ukey': 'f97efea71db0ec46c6b9750375720891', 'format':'json'}
# หรือต้องการ response เป็น XML
# querystring = {'uid': 'demo', 'ukey': 'demokey'}

response = requests.request('GET', url,params=querystring)
print (response.text) # print response