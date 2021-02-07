import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 1024        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    while True :
        message = input("InputTopic (today, daily, province) : ") 
        if "today" == message :
            s.send(message.encode())  # send message
            data = s.recv(1024).decode()  # receive response
            data = data.split('\n')
            for i in data:
                print(i)

        elif "daily" == message :
            s.send(message.encode())  # send message
            day = input("InputDate : ")
            month = input("InputMonth : ")
            year = input("InputYear : ")
            day = '0' + day if len(day) == 1 else day
            month = '0' + month if len(month) == 1 else month
            date = month + "/" + day + "/" + year

            s.send(date.encode())
            data = s.recv(1024).decode()  # receive response
            data = data.split('\n')
            print()
            for i in data:
                print(i)

        elif "province" == message :
            s.send(message.encode())  # send message
            province = input("InputProvince : ")
            province = province.title()
            s.send(province.encode())
            data = s.recv(1024).decode()  # receive response
            data = data.split('\n')
            for i in data:
                print(i)
        elif "exit" == message :
            break
        else :
            print("Invalid Input.")