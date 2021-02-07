import socket
import json
import requests
serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)
url =  'http://data.tmd.go.th/api/Station/v1/'

# echo_server.py
import socket

host = ''        # Symbolic name meaning all available interfaces
port = 12345     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()
print('Connected by', addr)
while True:
    data = conn.recv(1024)
    if not data: break
    conn.sendall(data)
conn.close()
# print('client disconnected') 
# # response เป็น json
# querystring = {'uid': 'u64teelak1113', 'ukey': 'f97efea71db0ec46c6b9750375720891', 'format':'json'}
# # หรือต้องการ response เป็น XML
# # querystring = {'uid': 'demo', 'ukey': 'demokey'}

# response = requests.request('GET', url,params=querystring)
# print (response.text) # print response