import socket
import json
import requests



host = ''        # Symbolic name meaning all available interfaces
port = 60301     # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
s.listen(1)
conn, addr = s.accept()


def findProvince(input):
    with open('./data.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    for province in data['provinces']:
        if input == province['PROVINCE_NAME']:
            return 1
    return None
    # print(provinces['provinces'])


def weatherToday(province):
    url = 'https://data.tmd.go.th/api/Weather3Hours/V1/'
    querystring = {'uid': 'u64teelak1113','ukey': 'f97efea71db0ec46c6b9750375720891', 'format': 'json'}
    response = requests.request('GET', url, params=querystring)
    response = json.loads(response.text)
    for i in response['Stations']:
        if i['Province'] == province:
            print(i)
            break
    return ("November")


def news():
    return ("December")


print('Connected by', addr)
while True:
    province = conn.recv(1024)
    province = str(province, 'utf-8')
    print(province)
    check = findProvince(province)
    correct = 'correct' if check == 1 else 'wrong'
    if correct == 'correct':
        
    conn.send(correct.encode())
    number = conn.recv(1024)
    number = str(number, 'utf-8')
    if number == "1":
        weatherToday(province)
    if number == "2":
        news()

    if not province:
        break
    # conn.sendall(data)
conn.close()
# print('client disconnected')
