import socket
import json
import requests
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
url =  'http://data.tmd.go.th/api/Station/v1/'

# response เป็น json
querystring = {'uid': 'u64teelak1113', 'ukey': 'f97efea71db0ec46c6b9750375720891', 'format':'json'}
# หรือต้องการ response เป็น XML
# querystring = {'uid': 'demo', 'ukey': 'demokey'}

response = requests.request('GET', url,params=querystring)
print (response.text) # print response