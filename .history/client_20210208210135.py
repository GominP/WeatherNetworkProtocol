# echo_client.py
import socket

host = socket.gethostname()
port = 60301                 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
while True:
        if province == 'exit':
            s.send(province.encode())
        break
    province = input("ใส่ชื่อจังหวัด: ")
    if province == 'exit':
        s.send(province.encode())
        break
    s.send(province.encode())
    correct = s.recv(1024).decode()
    
    if correct == 'correct':
        while True:
            print('(1) ภูมิอากาศวันนี้')
            print('(2) ข่าวเตือนภัยสภาพอากาศ')
            number = input("กรุณาใส่เลขที่ต้องการ: ")
            s.send(number.encode())
            if number == "3" :
                break
            elif number == 'exit':
                province = 'exit'
                break
            data = s.recv(1024).decode()
            print(data)
    else:
        print('พิมพ์ชื่อไม่ถูก')
    

s.close()
# print('Received', repr(data))
