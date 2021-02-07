import socket
import json
import requests
import os
from covid19openapi import ThaiCovid19

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 1024        # Port to listen on (non-privileged ports are > 1023)

def SEND_COVIDDATA(send_data):
    temp= ""
    for key in send_data:
         temp += key + " : " + str(send_data[key]) +"\n"
    conn.send(temp.encode())
       
def COVID_TODAY():
    data = requests.get('https://covid19.th-stat.com/api/open/today')
    json_data = json.loads(data.text)
    return json_data

def COVID_DAILY(date):
    data = requests.get('https://covid19.th-stat.com/api/open/timeline')
    json_data = json.loads(data.text)
    for i in json_data['Data'] :
        if i['Date'] == date :
            return i
    print('data not found.')
    return {
        'error' : 'data not found.'
    }

def COVID_PROVINCE(province):
    data = requests.get('https://covid19.th-stat.com/api/open/cases/sum')
    json_data = json.loads(data.text)
    for i in json_data['Province'] :
        if i == province : 
            return {
                i : json_data['Province'][i]
            }
    print('data not found.')
    return {
        'error' : 'data not found.'
    }
    


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            data = str(data,'utf-8')
            print(addr,': ',end="")
            print(data,end="")

            if data == "today":
                print()
                send_data = COVID_TODAY()
                SEND_COVIDDATA(send_data)

            elif data == "daily":
                date = conn.recv(1024)
                date = str(date,'utf-8')
                print(' - ' + date)

                send_data = COVID_DAILY(date)
                SEND_COVIDDATA(send_data)

            elif data == "province":
                province = conn.recv(1024)
                province = str(province,'utf-8')
                print(' - ' + province)

                send_data = COVID_PROVINCE(province)
                SEND_COVIDDATA(send_data)

            if not data:
                break
           
            