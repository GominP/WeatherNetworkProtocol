import socket
import json
import requests


url =  'http://data.tmd.go.th/api/Station/v1/'

host = ''        # Symbolic name meaning all available interfaces
port = 60301     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()


def findProvince(data):
    with open('./data.json',encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    for province in data['provinces']:
        print(data)
    # print(provinces['provinces'])



    
print('Connected by', addr)
while True:
    province= conn.recv(1024)
    province = str(province,'utf-8')
    print(province)
    findProvince(province)
    if not province: break
    # conn.sendall(data)
conn.close()
# print('client disconnected') 
# # response เป็น json
# querystring = {'uid': 'u64teelak1113', 'ukey': 'f97efea71db0ec46c6b9750375720891', 'format':'json'}
# # หรือต้องการ response เป็น XML
# # querystring = {'uid': 'demo', 'ukey': 'demokey'}

# response = requests.request('GET', url,params=querystring)
# print (response.text) # print response