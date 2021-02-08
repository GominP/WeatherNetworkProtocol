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
    print("ตรวจสอบจังหวัดว่ามีอยู่จริง")
    with open('./data.json', encoding='utf-8') as jsonfile:
        data = json.load(jsonfile)
    for province in data['provinces']:
        if input == province['PROVINCE_NAME']:
            return 'correct'
            print("จังหวัดว่ามีอยู่จริง")

    return 'wrong'
    print("ไม่พบจังหวัดที่กำลังค้นหา")

    # print(provinces['provinces'])


def spiltData(json_data):
    temp = ""
    for key in json_data:
        if key == "Time" or key == "TotolCloud":
            temp += key + " : " + str(json_data[key]) +"\n"
        else:
            temp += key + " : " + str(json_data[key]['Value'])+ " " +str(json_data[key]['Unit']) +"\n"
        
    # print(temp)
    conn.send(temp.encode())
    
def weatherToday(province):
    url = 'https://data.tmd.go.th/api/WeatherToday/V1/'
    querystring = {'uid': 'u64teelak1113','ukey': 'f97efea71db0ec46c6b9750375720891', 'format': 'json'}
    response = requests.request('GET', url, params=querystring)
    response = json.loads(response.text)
    string = ""
    for i in response['Stations']:
        if i['Province'] == province:
            # print(i)
            for j in response['Stations']:
            # string = spiltData(i)
                spiltData(j['Observe'])
                break
            break
    return string


def news():
    return ("December")


print('Connected by', addr)
while True:
    while True:
        print("loop 1")
        province = conn.recv(1024)
        province = str(province, 'utf-8')
        if province == "exit":
            print('client disconnected')
            conn, addr = s.accept()
        check = findProvince(province)
        # correct = 'correct' if check == 1 else 'wrong'
        if check == 'correct':
            conn.send(check.encode())
            break 
        else:
            conn.send(check.encode())
    while True:
        print("loop 2")
        number = conn.recv(1024)
        number = str(number, 'utf-8')
        if number == "1":
            weatherToday(province)  
        elif number == "2":
            news()
        elif number == "3":
            break
        elif number == "exit":
            print('client disconnected')
            conn, addr = s.accept()
            break
conn.close()